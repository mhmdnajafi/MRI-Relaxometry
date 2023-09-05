
'''
Relaxometry is the measurement of relaxation times from MR images. T1, T2 and T2* can be estimated using the appropriate pulse sequence and parameters.
This app in frist version measure T1-time and calcuate R1.

'''
import tkinter as tk
from tkinter import *
from tkinter import messagebox

class Programe():
    def __init__(self) -> None:
        # Initializer (currently empty)
        pass

    def main(self):
        """Set up and display the main GUI window with three buttons."""

        root_main = tk.Tk()
        self.root_main = root_main
        root_main.title('T1 relaxometry')
        # Configuring rows and columns for the main window
        root_main.rowconfigure([0,1] , minsize=50, weight=10)
        root_main.columnconfigure([0,1] , minsize=50, weight=10)
        
        # Adding the three main buttons to the main window
        bottom_con = tk.Button(master=root_main, text="Input", width=15, command=self.input)
        bottom_con.grid(row=0, column=0)
        bottom_image = tk.Button(master=root_main, text="Images and ROI", width=15, command=None)
        bottom_image.grid(row=0, column=1)
        bottom_analysis = tk.Button(master=root_main, text="Analysis", width=15, command=self.Analysis)
        bottom_analysis.grid(row=0, column=2)
        
        root_main.mainloop()

    def input(self):
        """Display the input window where the user provides different data."""
        # Variables to store user inputs

        count_concentration = tk.StringVar()
        concentration_str = tk.StringVar()
        count_TR = tk.StringVar()
        TR_str = tk.StringVar()
        Image_str = tk.StringVar()

        # Store these variables for later use
        self.count_concentration = count_concentration
        self.concentration_str = concentration_str
        self.count_TR = count_TR
        self.TR_str = TR_str
        self.Image_str = Image_str

        # Setting up the input window
        root_input = tk.Toplevel()
        root_input.title('Input')
        self.root_input = root_input

        # Creating labels and entries for 'Concentration'
        label_con = tk.Label(master=self.root_input, text='Count of Concentration')
        label_con.grid(row=1, column=0)
        label_con_list = tk.Label(master=self.root_input, text='Concentration(separate with",")')
        label_con_list.grid(row=2, column=0)

        enrty_count_con = tk.Entry(master=self.root_input, textvariable=self.count_concentration, width=30, bd=5)
        enrty_count_con.grid(row=1, column=1)
        enrty_Concentration = tk.Entry(master=self.root_input, textvariable=self.concentration_str, width=30, bd=5)
        enrty_Concentration.grid(row=2, column=1)

        # Creating labels and entries for 'TR'
        label_tr = tk.Label(master=self.root_input, text='Count of TR')
        label_tr.grid(row=3, column=0)
        label_image = tk.Label(master=self.root_input, text='TR(separate with ",")')
        label_image.grid(row=4, column=0)


        enrty_TR = tk.Entry(master=self.root_input, textvariable=self.count_TR, width=30, bd=5)
        enrty_TR.grid(row=3, column=1)
        enrty_TR_list = tk.Entry(master=self.root_input, textvariable=self.TR_str, width=30, bd=5)
        enrty_TR_list.grid(row=4, column=1)

        # Creating labels and entries for 'Image'
        label_image = tk.Label(master=self.root_input, text='Image names/Image address(separate with ",")')
        label_image.grid(row=5, column=0)
        enrty_image_list = tk.Entry(master=self.root_input, textvariable=self.Image_str, width=30, bd=5)
        enrty_image_list.grid(row=5, column=1)

        # Data processing methods
        # 'Save All' button that triggers the save_input_data method
        bottom_save = tk.Button(master=self.root_input, text='Save All', width=25, command=self.save_input_data)
        bottom_save.grid(row=1, column=4)


    def Images(self):
        """Display the 'Images and ROI' window."""
        root_image = tk.Toplevel()
        root_image.title('Images and ROI')
        root_image.rowconfigure([0,1], minsize=50, weight=10)
        root_image.columnconfigure([0,1], minsize=50, weight=10)
        self.root_image = root_image




    def Analysis(self):
        """Display the 'Analysis' window (currently empty)."""
        root_main = tk.Toplevel()
        root_main.title('Analysis')
        root_main.rowconfigure([0,1], minsize=50, weight=10)
        root_main.columnconfigure([0,1], minsize=50, weight=10)
        # TODO: Add functionality to the Analysis section
        root_main.mainloop()

    # Utility methods for data processing
    def matching_path_TR(self, paths, TR):
        """Match each path with a TR value."""
        TR_list = TR.split(',')
        paths_list = paths.split(',')
        path = [(paths_list[i], TR_list[i]) for i in range(len(paths_list))]
        self.paths_list = paths_list
        self.TR_list = TR_list
        self.path = path

    def create_dataset(self, concentration, TR):
        """Create dataset using provided concentration and TR values."""
        co_list = concentration.split(',')
        TR_list = TR.split(',')
        data = [{i: (j, None)} for i in co_list for j in TR_list]
        self.co_list = co_list
        self.TR_list = TR_list
        self.data = data



    def input_checker(self, count, co_list, TR_list, paths_list):
        """Validate user inputs."""
        return int(count) == len(co_list) and len(TR_list) == len(paths_list)


    def update_input_save_button(self, checker):
        """Update the 'Save All' button based on input validation."""
        if checker:
            # Successful input processing
            messagebox.showinfo('Great', "Your input is successfully detected")

            image_name = [f'Image TR= {TR}' for TR in self.TR_list]
            self.image_name = image_name
            button_configs = [{'name': name, 'command': None} for name in self.image_name]
            for config in button_configs:
                i = 1
                button = tk.Button(master=self.root_main, width=15,text=config["name"], command=config["command"])
                button.grid(row=1 , column=1)
                i+=1
        else:
            # Input mismatch
            messagebox.showinfo("WARNING", "Can't Match. Check Your Input.")



    def save_input_data(self):
            """Process and validate user input when 'Save All' button is clicked."""
            # Data processing
            self.matching_path_TR(self.Image_str.get(), self.TR_str.get())
            self.create_dataset(self.concentration_str.get(), self.TR_str.get())  # Note: Typo corrected in method name

            # Validate the input
            checker = self.input_checker(self.count_concentration.get(), self.co_list, self.TR_list, self.paths_list)
                
                # Update based on input validation
            self.update_input_save_button(checker)  # Note: Typo corrected in method name















app = Programe()
app.main()
