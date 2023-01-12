import sys
import tkinter as tk
from RunAccessibilityCheck import RunAccessibilityCheck
import customtkinter as ctk
import threading

class StepThree(ctk.CTkFrame):

    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master)
        self.master = master
        
        self.currently_running = ctk.BooleanVar(value=False)
        #self.other_runner = tk.BooleanVar(value=False)
        # self.other_other_thing = tk.StringVar(value="Yes")

        self.step3_inner_container = ctk.CTkFrame(self)
        self.step3_inner_container.pack()

        self.step3_inner_container.grid_columnconfigure(0, weight=3)
        self.step3_inner_container.grid_columnconfigure(1, weight=1)
        
        self.return_button = ctk.CTkButton(self.step3_inner_container, text="Return to previous page", command=lambda: self.clear_and_return(self=self, master=master))
        self.return_button.grid(row=0, column=0)

        # create Text widget
        self.text_widget = ctk.CTkTextbox(self.step3_inner_container, width=600)
        self.text_widget.grid(row=1, column=0, columnspan=2)

        # Redirect the console output to the Text widget
        sys.stdout = TextRedirector(self.text_widget)

        self.file_save_location = ctk.CTkLabel(self.step3_inner_container, text="Saving to "+RunAccessibilityCheck.get_file_type(self=self, file_to_print=self.master.master.export_type))
        self.file_save_location.grid(row=2, column=0, columnspan=2, padx=3, pady=2)

        if self.currently_running.get():
            self.running_currently = ctk.CTkLabel(self.step3_inner_container, text="Currently running...")
            self.running_currently.grid(row=3, column=0)
        else:
            # Create a button to start printing numbers
            self.print_button = ctk.CTkButton(self.step3_inner_container, text="Start checks", 
            command=lambda: [
                self.change_running_status(), 
                threading.Thread(target=self.start_file_download).start()
            ])
            self.print_button.grid(row=3, column=0)

        # Create a quit button
        self.quit_button = ctk.CTkButton(self.step3_inner_container, text="Quit", command=master.quit)
        self.quit_button.grid(row=3, column=1)



    def clear_and_return(event=None, self=None, master=None):
        """Clear the list and return to the previous page"""
        master.master.actually_selected_pages = []  # Clear old list
        master.master.switch_frame("PageTwo")       # Return to old page

    def start_file_download(self):
        """This method will be run on a seperate thread to prevent blockign the ui"""
        #print("File download before",str(self.currently_running.get()))
        self.start_download = RunAccessibilityCheck()
        self.start_download.run(pages_to_check=self.master.master.actually_selected_pages, file_to_print=self.master.master.export_type)
        self.currently_running.set(False)
        # print("File download", str(self.currently_running.get()))

    def change_running_status(self):
        """Simply updates the currently_running var prior to downloading file to update the ui buttons"""
        self.currently_running.set(True)
        # self.other_runner.set(True)
        # self.other_other_thing.set("Non")
        # self.master.update_idletasks()
        # print("Change status", str(self.currently_running.get()))


class TextRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.configure(state=ctk.NORMAL)
        self.text_widget.insert(ctk.END, string)
        self.text_widget.see(ctk.END)
        self.text_widget.configure(state=ctk.DISABLED)


if __name__ == "__main__":
    app = StepThree()
    app.mainloop()