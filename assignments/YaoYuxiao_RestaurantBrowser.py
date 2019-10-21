# Assignment 7
# GUI application that allows the user to browse, search, and sort the Restaurants database
import tkinter
import sqlite3
import os


# GUI customizations for color, fonts, and spacing (you may change)
bg_color = 'steelblue'
fg_color = 'white'
label_fg = '#1d3549'
data_font = "Verdana 12 normal"
label_font = "Verdana 12 bold"
pad = 20

db = None    # db object is a global variable, that initially has no value


# GUI object that represents the Restaurant Browser application
class RestaurantBrowser:
    def __init__(self, rows):
        # Main window and Label
        self.main_window = tkinter.Tk()
        self.main_window.title("Restaurant Browser")
        self.main_window.geometry('660x650')
        self.main_window.configure(background=bg_color)
        tkinter.Label(self.main_window, text='Restaurant Browser', fg=label_fg, bg=bg_color, padx=pad, pady=pad, font=label_font).grid(row=0, column=0, sticky=tkinter.constants.W)

        # Search Button and Entry field
        self.search_value = tkinter.StringVar()
        tkinter.Button(self.main_window, text="Search", command=self.search_db, fg=label_fg, bg="#adebad", padx=10, font=label_font, borderwidth=0).grid(row=0, column=2, sticky=tkinter.constants.W)
        self.search_value_entry = tkinter.Entry(self.main_window, width=15, font=data_font, textvariable=self.search_value).grid(row=0, column=3)

        # Column header Buttons -- when a button is clicked, the restaurant data is sorted by the selected column
        try:
            tkinter.Button(self.main_window, text='Name', command=lambda: self.sort_db('Name'), fg=label_fg, bg="#2db92d", anchor="w", padx=pad, font=label_font, borderwidth=0).grid(row=1, column=0, sticky=tkinter.constants.EW)
            tkinter.Button(self.main_window, text='City', command=lambda: self.sort_db('City'), fg=label_fg, bg="#32cd32", anchor="w", padx=pad, font=label_font, borderwidth=0).grid(row=1, column=1, sticky=tkinter.constants.EW)
            tkinter.Button(self.main_window, text='State', command=lambda: self.sort_db('State'), fg=label_fg, bg="#5bd75b", anchor="w", padx=pad, font=label_font, borderwidth=0).grid(row=1, column=2, sticky=tkinter.constants.EW)
            tkinter.Button(self.main_window, text='Cuisine', command=lambda: self.sort_db('Cuisine'), fg=label_fg, bg="#84e184", anchor="w", padx=pad, font=label_font, borderwidth=0).grid(row=1, column=3, sticky=tkinter.constants.EW)

            # Call this function when the GUI is initialized to display all of the restaurant data
            self.display_rows(rows)

            tkinter.mainloop()
        except IndexError as err:
            print('Index error: ', err)
        except Exception as err:
            print('An error occurred: ', err)

    # Display all of the restaurant data in the rows parameter.
    # 'rows' will contain the results of the most recent SQL query
    def display_rows(self, rows):
        # Clear any previous rows of data before displaying results of most recent SQL query
        # For example, if a query that displays all rows is followed by one that displays fewer results
        # (as in a search),then you must first clear the previous results from the window.
        self.clear_rows()

        r = 2
        for row in rows:
            tkinter.Label(self.main_window, text=row[1], fg=fg_color, bg=bg_color, padx=pad, font=data_font).grid(row=r, column=0, sticky=tkinter.constants.W)
            tkinter.Label(self.main_window, text=row[2], fg=fg_color, bg=bg_color, padx=pad, font=data_font).grid(row=r, column=1, sticky=tkinter.constants.W)
            tkinter.Label(self.main_window, text=row[3], fg=fg_color, bg=bg_color, padx=pad, font=data_font).grid(row=r, column=2, sticky=tkinter.constants.W)
            tkinter.Label(self.main_window, text=row[4], fg=fg_color, bg=bg_color, padx=pad, font=data_font).grid(row=r, column=3, sticky=tkinter.constants.W)
            r = r + 1

    def clear_rows(self):
        # Clear any previous rows of data before displaying results of current SQL query
        for label in self.main_window.grid_slaves():
            if int(label.grid_info()['row']) > 1:
                label.grid_forget()

    # Search the database across all columns using a wildcard search with the user-provided search value
    def search_db(self):
        print("search_db function")
        # Define, execute, and fetch the results of the SQL query
        # Call self.display_rows to display the results of the query
        try:
            cursor = db.cursor()          # get the database cursor to we can execute queries
            # add the user-provided search_term to the SQL query
            if self.search_value.get():
                sql = "SELECT * FROM RESTAURANT WHERE Name LIKE '%" + self.search_value.get() + "%'  OR  City LIKE '%" + \
                      self.search_value.get() + "%' OR State LIKE '%" + self.search_value.get() + "%'  OR Cuisine LIKE '%" + \
                      self.search_value.get() + "%' ORDER BY Name"

                cursor.execute(sql)  # execute the query
                records = cursor.fetchall()  # fetch the list of records generated by the query
                # If no restaurants are found with the search value, display a message: 'No results found.'
                if len(records) > 0:
                    self.display_rows(records)
                else:
                    print("No results found.")
            # If no search value is provided, display all of the restaurants in the database
            else:
                sql = "SELECT * FROM RESTAURANT"
                cursor.execute(sql)  # execute the query
                all_records = cursor.fetchall()  # fetch the list of records generated by the query
                self.display_rows(all_records)
        except sqlite3.IntegrityError as err:
            print('Integrity Error:', err)
        except sqlite3.OperationalError as err:
            print('Operational Error:', err)
        except sqlite3.Error as err:
            print('Error:', err)

    # Sort the database on the column selected by the user
    def sort_db(self, column_name):
        print("sort_db function")
        # Define, execute, and fetch the results of the SQL query
        try:
            cursor = db.cursor()          # get the database cursor to we can execute queries
            # Sort restaurants by Name, City, State or Cuisine by clicking the appropriate button
            if column_name == 'Name':
                sql = "SELECT * FROM RESTAURANT  ORDER BY Name"
                cursor.execute(sql)           # execute the query
            elif column_name == 'City':
                sql = "SELECT * FROM RESTAURANT  ORDER BY City"
                cursor.execute(sql)           # execute the query
            elif column_name == 'State':
                sql = "SELECT * FROM RESTAURANT  ORDER BY State"
                cursor.execute(sql)           # execute the query
            elif column_name == 'Cuisine':
                sql = "SELECT * FROM RESTAURANT  ORDER BY Cuisine"
                cursor.execute(sql)           # execute the query
            records = cursor.fetchall()   # fetch the list of records generated by the query
            # Call self.display_rows to display the results of the query
            self.display_rows(records)
        except sqlite3.IntegrityError as err:
            print('Integrity Error:', err)
        except sqlite3.OperationalError as err:
            print('Operational Error:', err)
        except sqlite3.Error as err:
            print('Error:', err)


# Connect to the database
# Define, execute, and fetch the results of the SQL query that retrieves all restaurant data
# Create the GUI object, RestaurantBrowser, and pass it the rows containing the restaurant data


def main():
    global db
    try:
        dbname = 'restaurants.db'
        if os.path.exists(dbname):
            db = sqlite3.connect(dbname)
            cursor = db.cursor()
            sql = 'SELECT * FROM RESTAURANT ORDER BY Name'
            cursor.execute(sql)
            rows = cursor.fetchall()
            RestaurantBrowser(rows)
            db.close()
        else:
            print('Error:', dbname, 'does not exist')
    except sqlite3.IntegrityError as err:
        print('Integrity Error on connect:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error on connect:', err)
    except sqlite3.Error as err:
        print('Error on connect:', err)


main()