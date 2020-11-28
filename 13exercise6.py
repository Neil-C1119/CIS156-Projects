#Import dependencies
import tkinter
import tkinter.messagebox

#Create a GUI class
class GUI:
    def __init__(self):
        #Create a tkinter window
        self.window = tkinter.Tk()

        #Create variables for each of the Checkbuttons
        self.oil_var = tkinter.IntVar()
        self.lube_var = tkinter.IntVar()
        self.radiator_var = tkinter.IntVar()
        self.transmission_var = tkinter.IntVar()
        self.inspection_var = tkinter.IntVar()
        self.muffler_var = tkinter.IntVar()
        self.tire_var = tkinter.IntVar()

        #Set all of the Checkbutton variables to 0 by default
        self.oil_var.set(0)
        self.lube_var.set(0)
        self.radiator_var.set(0)
        self.transmission_var.set(0)
        self.inspection_var.set(0)
        self.muffler_var.set(0)
        self.tire_var.set(0)

        #Top frame and its contents
        self.top_frame = tkinter.Frame(self.window)
        self.name_label = tkinter.Label(self.top_frame, text='Joe\'s Auto')
        self.svc_label = tkinter.Label(self.top_frame, text='Services:')

        #Checkbutton frame and its contents
        self.cb_frame =tkinter.Frame(self.window)
        self.oil_cb = tkinter.Checkbutton(self.cb_frame, text='Oil change', variable=self.oil_var)
        self.lube_cb = tkinter.Checkbutton(self.cb_frame, text='Lube job', variable=self.lube_var)
        self.radiator_cb = tkinter.Checkbutton(self.cb_frame, text='Radiator flush', variable=self.radiator_var)
        self.transmission_cb = tkinter.Checkbutton(self.cb_frame, text='Transmission flush', variable=self.transmission_var)
        self.inspection_cb = tkinter.Checkbutton(self.cb_frame, text='Inspection', variable=self.inspection_var)
        self.muffler_cb = tkinter.Checkbutton(self.cb_frame, text='Muffler replacement', variable=self.muffler_var)
        self.tire_cb = tkinter.Checkbutton(self.cb_frame, text='Tire rotation', variable=self.tire_var)

        #Button frame and its contents
        self.button_frame = tkinter.Frame(self.window)
        self.submit_btn = tkinter.Button(self.button_frame, text='Submit', command=self.show_total)
        self.exit_btn = tkinter.Button(self.button_frame, text='Exit', command=self.window.destroy)

        #Pack the contents of the top frame
        self.name_label.pack(side='top')
        self.svc_label.pack(side='top')

        #Pack the contents of the Checkbutton frame
        self.oil_cb.pack(side='top')
        self.lube_cb.pack(side='top')
        self.radiator_cb.pack(side='top')
        self.transmission_cb.pack(side='top')
        self.inspection_cb.pack(side='top')
        self.muffler_cb.pack(side='top')
        self.tire_cb.pack(side='top')

        #Pack the contents of the Button frame
        self.submit_btn.pack(side='left')
        self.exit_btn.pack(side='left')

        #Pack the frames
        self.top_frame.pack(side='top')
        self.cb_frame.pack(side='top')
        self.button_frame.pack(side='top')

        #Start the tkinter main loop
        tkinter.mainloop()

    #Define a function to show the total cost of the services a user selects
    def show_total(self):
        #Start the message to be shown to the user
        self.message = 'The total cost will be: $'

        #Define a variable to hold the total cost of services selected by the user
        total_amount = 0

        #See which Checkbuttons are checked and add the cost of that service to the total
        if self.oil_var.get() == 1:
            total_amount += 30
        if self.lube_var.get() == 1:
            total_amount += 20
        if self.radiator_var.get() == 1:
            total_amount += 40
        if self.transmission_var.get() == 1:
            total_amount += 100
        if self.inspection_var.get() == 1:
            total_amount += 35
        if self.muffler_var.get() == 1:
            total_amount += 200
        if self.tire_var.get() == 1:
            total_amount += 20

        #Add the final total to the message
        self.message += str(total_amount)

        #Open a message box with the total cost information
        tkinter.messagebox.showinfo('Total Cost', self.message)

#Main function that calls the GUI class
def main():
    myGUI = GUI()

#Call the main function
main()
