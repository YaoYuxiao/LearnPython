# Assignment 5
# This program uses a GUI to prompt the user for an input file and search text,
# and then finds and displays the number of occurrences of the search text in the file.
import tkinter, tkinter.filedialog


class CountOccurrencesGUI:

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Count Occurrences')
        self.main_window.geometry('400x150')
        bg_color = 'lightsteelblue'
        button_color = 'cornflowerblue'
        self.main_window.configure(background=bg_color)

        # Create three frames to group widgets.
        self.top_frame = tkinter.Frame(self.main_window, background=bg_color)
        self.mid_frame = tkinter.Frame(self.main_window, background=bg_color)
        self.bottom_frame = tkinter.Frame(self.main_window, background=bg_color)

        self.file_name = tkinter.StringVar()
        # Create the widgets for the top frame.
        self.select_button = tkinter.Button(self.top_frame, text='Select a file', command=self.select_file,
                                            background=button_color)
        self.display_name = tkinter.Label(self.top_frame, textvariable=self.file_name, width=40, background=bg_color)

        # Pack the top frame's widgets.
        self.select_button.pack(side='left', pady=10)
        self.display_name.pack(side='left', padx=10)

        self.text = tkinter.StringVar()
        # Create the widgets for the middle frame.
        self.text_label = tkinter.Label(self.mid_frame, text='Enter search text: ', background=bg_color)
        self.text_entry = tkinter.Entry(self.mid_frame, width=15, textvariable=self.text)
        self.count_button = tkinter.Button(self.mid_frame, text='Count Occurrences', command=self.count_occurrences,
                                           background=button_color)

        # Pack the middle frame's widgets.
        self.text_label.pack(side='left', pady=10)
        self.text_entry.pack(side='left')
        self.count_button.pack(side='left', padx=10)

        # Create the widgets for the bottom frame.
        self.print = tkinter.StringVar()
        self.print_label = tkinter.Label(self.bottom_frame, textvariable=self.print, background=bg_color)

        # Pack the bottom frame's widgets.
        self.print_label.pack(side='left', pady=10)

        # Pack three frames.
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # Create the widgets and arrange them using either the pack or grid layout manager
        # Widgets include:
        #    2 Buttons: 'Select a file' and 'Count occurrences'
        #    An Entry field where the user enters the search text
        #    Label fields to display the file name and messages

        # Enter the tkinter main loop
        tkinter.mainloop()

    # This is the function that is called when the user clicks the 'Select a file' button
    # Use the tkinter.filedialog.askopenfilename function to open a File Dialog
    def select_file(self):
        filename = ''
        try:
            # Open a File Dialog
            filename = tkinter.filedialog.askopenfilename()
            # Store the filename in the StringVar
            self.file_name.set(filename)

        except FileNotFoundError as err:
            print('Error: cannot find file,', filename)
            print('Error:', err)
        except OSError as err:
            print('Error: cannot access file,', filename)
            print('Error:', err)
        except ValueError as err:
            print('Error: invalid data found in file', filename)
            print('Error:', err)
        except Exception as err:
            print('An unknown error occurred')
            print('Error:', err)

    # This is the function that is called when the user clicks the 'Count occurrences' button
    # Open the file using the filename that the user selected
    # Get the search text value that the user entered
    # Read the file contents into a string variable
    # Use the count function to obtain the number of occurrences of the search text in the file.
    # Display the number of occurrences (if any)
    # If the user did not select a file, or enter search text, display a message
    def count_occurrences(self):
        try:
            # Make sure the file and the text are not empty.
            if self.file_name.get():
                if self.text_entry.get():
                    # Read the file
                    article_file = open(self.file_name.get(), 'r').read()
                    # Normalize the article text
                    article_file = article_file.lower()
                    # Normalize the input text
                    normal_text = self.text_entry.get().strip().lower()
                    occurrence = article_file.count(normal_text)
                    # Display the result.
                    if occurrence != 0:
                        result = normal_text+' occurs '+str(occurrence)+' times.'
                    # Display an appropriate message when the word cannot be found,
                    # or a file has not been selected, or no search text has been entered
                    else: result = self.text_entry.get()+' not found'
                else: result = 'No search text was entered.'
            else: result = 'No file was selected.'
            self.print.set(result)

        except FileNotFoundError as err:
            print('Error: cannot find the file')
            print('Error:', err)
        except OSError as err:
            print('Error: cannot access the file')
            print('Error:', err)
        except ValueError as err:
            print('Error: invalid data found in file')
            print('Error:', err)
        except Exception as err:
            print('An unknown error occurred')
            print('Error:', err)


CountOccurrencesGUI()