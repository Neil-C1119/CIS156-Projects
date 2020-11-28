#Import dependencies
import tkinter
import tkinter.messagebox

#Create a GUI class
class GUI:
    def __init__(self):
        #Create a tkinter window
        self.window = tkinter.Tk()

        #Variable for all of the radio buttons
        self.radio_var = tkinter.IntVar()

        #Set the variable to 1 by default
        self.radio_var.set(1)

        #Top frame and its contents
        self.top_frame = tkinter.Frame(self.window)
        self.name_label = tkinter.Label(self.top_frame, text='Long-Distance Calls')
        self.select_label = tkinter.Label(self.top_frame, text='Please select one of the following rates: ')

        #Radiobutton frame and its contents
        self.rb_frame = tkinter.Frame(self.window)
        self.day_rb = tkinter.Radiobutton(self.rb_frame, text='Daytime (6:00 am - 5:59 pm)', variable=self.radio_var, value=1)
        self.evening_rb = tkinter.Radiobutton(self.rb_frame, text='Evening (6:00 pm - 11:59 pm)', variable=self.radio_var, value=2)
        self.off_peak_rb = tkinter.Radiobutton(self.rb_frame, text='Off-Peak (midnight - 5:59 am)', variable=self.radio_var, value=3)

        #Entry frame and its contents
        self.entry_frame = tkinter.Frame(self.window)
        self.entry_label = tkinter.Label(self.entry_frame, text='Minutes: ')
        self.minutes_input = tkinter.Entry(self.entry_frame, width=10)

        #Button frame and its contents
        self.button_frame = tkinter.Frame(self.window)
        self.submit_btn = tkinter.Button(self.button_frame, text='Submit', command=self.show_total)
        self.exit_btn = tkinter.Button(self.button_frame, text='Exit', command=self.window.destroy)

        #Pack the contents of the Top frame
        self.name_label.pack(side='top')
        self.select_label.pack(side='top')

        #Pack the contents of the Radiobutton frame
        self.day_rb.pack(side='top')
        self.evening_rb.pack(side='top')
        self.off_peak_rb.pack(side='top')

        #Pack the contents of the Entry frame
        self.entry_label.pack(side='left')
        self.minutes_input.pack(side='left')

        #Pack the contents of the Button frame
        self.submit_btn.pack(side='left')
        self.exit_btn.pack(side='left')

        #Pack the frames
        self.top_frame.pack(side='top')
        self.rb_frame.pack(side='top')
        self.entry_frame.pack(side='top')
        self.button_frame.pack(side='top')

        #Start the tkinter main loop
        tkinter.mainloop()

    #Define a function to show the total cost of the call
    def show_total(self):
        #Start the message to be shown to the user
        self.message = 'The total cost will be: $'

        #Define a variable that gets the user's input on how many minutes the call was
        user_minutes = int(self.minutes_input.get())

        #Define a variable to hold the total cost of the call
        total_amount = 0

        #See which Radiobutton was selected and calculate how much the call will cost, then add that to the total
        if self.radio_var.get() == 1:
            total_amount = round(user_minutes * .07, 2)
        if self.radio_var.get() == 2:
            total_amount = round(user_minutes * .12, 2)
        if self.radio_var.get() == 3:
            total_amount = round(user_minutes * .05, 2)

        #Add the total cost to the message
        self.message += str(total_amount)

        #Open a message box with the total cost information
        tkinter.messagebox.showinfo('Total Cost', self.message)

#Main function that calls the GUI class
def main():
    myGUI = GUI()

#Call the main function
main()
