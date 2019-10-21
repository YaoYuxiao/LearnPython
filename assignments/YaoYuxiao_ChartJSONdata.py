# Assignment 6
# This program uses a web API to make a request of the HIVE application to generate indexes
# for the Astronomy wiki page, using the UAT vocabulary.
# This request returns the index data in JSON format. This data must be parsed to select the
# information needed to chart each index (concept) and its score with a Google Column Chart.
import urllib.request
import urllib.error
from urllib.error import URLError, HTTPError
import json
import gviz_api
import webbrowser   # optional

# This is a template that defines the HTML for the web page that will contain the chart.
# It contains a substitution variable, 'json_text', that is replaced by the JSON data
# that defines the data for the Google Chart.
# Do NOT change this!! (You can change the title and colors values under options)
column_template = """
<html>
  <head>
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
      google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = new google.visualization.DataTable(%(json_text)s);

        var options = {
          title: 'Unified Astronomy Thesauras (UAT) Concepts in Astronomy Wiki page',
          colors: ['deepskyblue']
        };

        var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
        chart.draw(data, options);
      }
    </script>
  </head>
  <body>
    <div id="chart_div" style="width: 80em; height: 37.5em;"></div>
  </body>
</html>
"""


def main():
    try:
        # This is the URL for requesting the HIVE app to index the Astronomy wiki page with the UAT vocabulary
        url = "http://hive2.cci.drexel.edu:8080/generateIndex?url=https://en.wikipedia.org/wiki/Astronomy&vocs=UAT&parms=3,2,3,20"
        url_content = urllib.request.urlopen(url).read().decode('utf8')

        # NOTE: If you are unable to access the HIVE application, i.e., exceptions occur,
        # then you can uncomment the 3 lines below and use the provided local file.
        # This local file can also be used to test your program, but your final program
        # must work with the url specified above.

        # input_file = open('hive_index.json', 'r', encoding="utf8")
        # url_content = input_file.read()
        # input_file.close()

        # Parse the json data, and select the data needed for the chart.
        # The json contains a list of concepts. For each concept you want
        #    -- the prefLabel which is the name of concept, and
        #    -- the score which is the rank of the concept for this document
        voc_list = json.loads(url_content)

        # This is the list of tuples that will be loaded into the DataTable.
        # Each tuple will contain the prefLabel and score for each concept
        data = []

        # NEW CODE starts here...
        # This is where you loop through the json data to select the prefLabel and score.
        # Create a tuple with the prefLabel and score for each concept, and append to the data list.

        # Your code goes here. HINT: this can be done in less than 10 statements.
        infos = voc_list[0]["concepts"]
        for info in infos:
            score = info["score"]
            tuple = (info["prefLabel"], int(score))
            data.append(tuple)

        # END of NEW CODE...
        # You do not (or rather, should not) change any of the code that follows

        # Create the schema, defining the columns and their types
        description = [("Concept", "string"), ("Score", "number")]

        # Create a DataTable object
        data_table = gviz_api.DataTable(description)
        data_table.LoadData(data)

        # Convert to JSON
        json_text = data_table.ToJSon()

        # Create a file for the HTML and write the chart contents
        filename = 'google_chart.html'
        html_file = open(filename, 'w', encoding='utf8')

        # Write the column_template to the file
        html_file.write(column_template % vars())

        html_file.close()

        webbrowser.open_new_tab(filename)   # Open the HTML file in a browser (optional)

    except ValueError as err:
        print(err)
    except FileNotFoundError as err:
        print(err)
    except HTTPError as err:
        print(err)
    except URLError as err:
        print(err)
    except OSError as err:
        print(err)
    except Exception as err:
        print('An error occurred: ', err)


main()

