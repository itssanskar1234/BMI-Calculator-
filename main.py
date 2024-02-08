from tkinter import *
from tkinter import messagebox as tsmg

class BMI(Tk):
    def __init__(self):
        super().__init__()
        '''Initialize the BMI Calculator GUI window'''

        # Set the initial geometry of the window
        display_width = 400
        display_height = 260
        x_cordinate = (self.winfo_screenwidth() - display_width)//2
        y_cordinate = ((self.winfo_screenheight() - display_height)//2)-120
        self.geometry(f"{display_width}x{display_height}+{x_cordinate}+{y_cordinate}")

        # Set background color
        self.config(background="#B2DFEE")

        # Disable window resizing
        self.resizable(False,False)

        # Set window title
        self.title("BMI Calculator")

        # # Initialize flag for info frame visibility
        self.info_frame_visible = False
    
        

    def menuBar(self):
        '''Create a themed menu bar allowing users to change the interface color.'''

        # Creating a menu bar
        Menu_bar = Menu()

        # Creating a submenu for theme selection
        Theme = Menu(Menu_bar,tearoff=0,background="#EAEAEA")

        # List of colors and corresponding functions to set the background color
        colors = [["Light Blue (default)", lambda:self.config(background="#B2DFEE")],
                   ["Rose", lambda:self.config(background="#EEB4B4")],
                   ["Light Green", lambda:self.config(background="#BCEE68")]]
        
        # Adding color options to the theme submenu
        for color,function in colors:
            Theme.add_command(label=color,command=function,font="lucida 9 normal") 

        # Adding the theme submenu to the menu bar   
        Menu_bar.add_cascade(label="Theme",menu=Theme,font="lucida 9 normal")

        # Configuring the menu bar for the interface
        self.config(menu=Menu_bar)
    


    def interface(self):
        '''Set up the BMI calculator interface with entry fields, labels, and buttons.'''
        # Initializing StringVar variables for weight, height, and BMI
        self.weight_val = StringVar()
        self.height_val = StringVar()
        self.bmi_val = StringVar()

        # Setting initial values for the Entry fields
        self.weight_val.set("")
        self.height_val.set("")
        self.bmi_val.set("")

        # Creating Entry fields for weight, height, and BMI
        self.height_entry = Entry(textvariable=self.height_val,font="Helvetica 14",width=7,borderwidth=2,justify='center',background="#EAEAEA")
        self.weight_entry = Entry(textvariable=self.weight_val,font="Helvetica 14",width=7,borderwidth=2,justify='center',background="#EAEAEA")    
        self.bmi_entry = Entry(textvariable=self.bmi_val,font="Helvetica 14",width=7,state="readonly",borderwidth=2,justify='center',background="#EAEAEA")       

        # Labels for fields: Height, Weight, BMI
        units = [["Height",0],["Weight",1],["BMI",2],["m",0],["kg",1],["kg/m2",2]]
        for unit,r in units[0:3]:
            labels = Label(text=unit,font="ariel 14",background="#EEEEE0",borderwidth=0)
            labels.grid(row=r,column=0,padx=20,pady=10,ipadx=7,ipady=1)

        # Labels for units: m, kg, kg/m2
        for unit,r in units[3:6]:
            labels = Label(text=unit,font="lucida 13",background="#EEEEE0",borderwidth=0)
            labels.grid(row=r,column=2,ipadx=3,ipady=1)

        # Buttons: Calculate, Clear, Show Info
        button_1= Button(text="Calculate",width=10,font="lucida 10 bold",command=self.calculate_bmi,borderwidth=2,background="#EECBAD")
        button_2= Button(text="Clear",width=7,font="lucida 10 bold",command=self.clear,background="#EEE0E5")
        self.button_3= Button(text="Show info",width=22,font="lucida 8 underline",background="#EEE0E5",command=self.toggle_info,border=0,justify="center")
        
        # Placing Entry fields and buttons in the grid
        self.height_entry.grid(row=0,column=1,ipady=1,ipadx=5)
        self.weight_entry.grid(row=1,column=1,ipady=1,ipadx=5)
        self.bmi_entry.grid(row=2,column=1,ipady=1,ipadx=5)

        button_1.grid(row=3,column=1,pady=5)
        button_2.grid(row=4,column=1,pady=7)
        self.button_3.grid(row=5,column=1,pady=5)
        


    def calculate_bmi(self):
        '''Calculate the BMI based on user input for weight and height.'''

        try:
            # Attempting to calculate BMI based on user-provided weight and height values
            weight = float(self.weight_val.get())
            height = float(self.height_val.get())
            value =weight/(pow(height,2))

        # This set of if-else conditions checks whether the user has entered a zero or negative value in the Entry widgets.
        # If the user enters a negative value, it displays an error message and clears the respective field where the user entered 0 or a negative value.
            if height<=0 or weight<=0:                        
                if weight<=0:
                    tsmg.showerror("Error","Please enter a positive number for weight")
                    self.weight_val.set("")
                
                if height<=0:
                    tsmg.showerror("Error","Please enter a positive number for height")
                    self.height_val.set("")
            else:
                self.bmi_val.set(f"{value:.4}")
                
        except ZeroDivisionError:
        # Handling the case where height is zero (which would cause a ZeroDivisionError)
                
            # Displaying an error message for zero height
                tsmg.showerror('Error',"Please enter a positive number for height.")
                self.height_val.set("")
                if weight<=0:
                    self.weight_val.set("")
                    tsmg.showerror("Error","Please enter a positive number for weight")

        except ValueError:
            # Handling the case where non-numerical values are entered

            # Displaying an error message for non-numerical input
            tsmg.showerror("Error","Please Enter numerical value")

            # Clearing height field if it contains non-numerical input
            if not self.height_val.get().isdigit():
                self.height_val.set("")
                self.bmi_val.set("")
            if not self.weight_val.get().isdigit():
                self.weight_val.set("")
                self.bmi_val.set("")

        except Exception:
            # Handling any other unexpected errors
            tsmg.showerror("Error","an error has occured")
            # Clearing all fields
            self.clear()



    def info(self):
        '''Displays information about BMI categories.'''
        # # Initialize flag for info frame visibility
        self.info_frame_visible = False

        # Creating a frame for displaying information
        self.info_frame = Frame(background="#EEEEE0")

        # List of BMI categories and their descriptions
        info_list = ["BMI Categories:\n",
                     "* Underweight: BMI less than 18.5\n",
                     "* Normal weight: BMI between 18.5 and 24.9\n",
                     "* Overweight: BMI between 25 and 29.9\n",
                     "* Obese: BMI of 30 or greater"]  
        for i in info_list:
            information = Label(self.info_frame,text=i,justify='left',font="Verdana 11" ,background="#EEEEE0")
            information.pack(anchor="nw")   
     


    def toggle_info(self):
        """Toggle the visibility of the information frame and update the button text."""

        if self.info_frame_visible==True:
        # If info frame is currently visible, hide it, reset, and update button text
            self.info_frame.place_forget()
            self.reset_geometry()
            self.button_3.config(text="Show Info")
            self.info_frame_visible = False

        else:
            # If info frame is currently hidden, expand the geometry, show info frame, and update button text
            self.expand_geometry()
            self.info_frame.place(x=25, y=263)
            self.button_3.config(text="Hide Info")
            self.info_frame_visible = True 



    def expand_geometry(self):
        # Define the width and height for expanding the interface
        display_width = 400
        display_height = 500

        # Define the new x and y coordinates for positioning the interface
        x_cordinate = (self.winfo_screenwidth() - display_width)//2
        y_cordinate = (self.winfo_screenheight() - display_height)//2

        # Adjust the geometry of the interface to the new dimensions and position
        self.geometry(f"{display_width}x{display_height}+{x_cordinate}+{y_cordinate}")
    


    def reset_geometry(self):
        # Define the width and height for resetting the interface
        display_width = 400
        display_height = 260

        # Define the width and height for resetting the interface
        x_cordinate = (self.winfo_screenwidth() - display_width)//2
        y_cordinate = ((self.winfo_screenheight() - display_height)//2)-120

        # Reset the geometry of the interface to the default dimensions and position
        self.geometry(f"{display_width}x{display_height}+{x_cordinate}+{y_cordinate}")



    def clear(self):
        '''Clear all entry widgets'''
        self.weight_val.set("")
        self.height_val.set("")
        self.bmi_val.set("")



if __name__ == "__main__":
    window = BMI()
    window.menuBar()
    window.interface()
    window.info()
    window.mainloop()