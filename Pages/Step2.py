from statistics import variance
from tkinter import Variable
import tkinter as tk
import customtkinter as ctk
from tkinter.scrolledtext import ScrolledText

class StepTwo(ctk.CTkFrame):

    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master)

        self.step2_inner_container = ctk.CTkFrame(self)
        self.step2_inner_container.pack()

        self.step2_inner_container.grid_columnconfigure(0, weight=3)
        self.step2_inner_container.grid_columnconfigure(1, weight=1)
        
        self.return_button = ctk.CTkButton(self.step2_inner_container, text="Return to previous page", command=lambda: self.clear_and_return(self=self, master=master))
        self.return_button.grid(row=0, column=0)

        self.url_list = ctk.CTkLabel(self.step2_inner_container,text="Below is a list of URLs obtained")
        self.url_list.grid(row=1,column=0)

        checked = []    # Holds the checkbox values

        self.text = ScrolledText(self.step2_inner_container, width=80, height=30)
        self.text.grid(row=2, column=0)

        # Refresh the frame
        for index, value in enumerate(master.master.pages_to_search_against):
            checked.append(tk.IntVar(value=1)) # Holds whether the checkbox is checked or not
            checkbox = ctk.CTkCheckBox(self.text, text=value + '\n', variable=checked[index], text_color="black")
            self.text.window_create('end', window=checkbox)
            self.text.insert('end', '\n')

        self.total_count = ctk.CTkLabel(self.step2_inner_container, text="Total pages:"+str(len(master.master.pages_to_search_against)))
        self.total_count.grid(row=3, column=0)
        
        self.csv_export_frame = ctk.CTkFrame(self.step2_inner_container)
        self.csv_export_frame.grid(row=4, column=0)
        self.export_csv = ctk.CTkButton(self.csv_export_frame, text="Export to CSV", command=lambda: self.export_to_files(IsChecked=checked,master=master,download_type=".csv"))
        self.export_csv.grid(row=0, column=0)
        self.export_csv_label = ctk.CTkLabel(self.csv_export_frame, text="Simpler output")
        self.export_csv_label.grid(row=1, column=0)

        self.json_export_frame = ctk.CTkFrame(self.step2_inner_container)
        self.json_export_frame.grid(row=4, column=1)
        self.export_json = ctk.CTkButton(self.json_export_frame, text="Export to JSON", command=lambda: self.export_to_files(IsChecked=checked,master=master,download_type=".json"))
        self.export_json.grid(row=0, column=0)
        self.export_json_label = ctk.CTkLabel(self.json_export_frame, text="More detailed output")
        self.export_json_label.grid(row=1, column=0)
    


    def clear_and_return(event=None, self=None, master=None):
        """Clear the list and return to the previous page"""
        master.master.pages_to_search_against = []  # Clear old list
        master.master.switch_frame("PageOne")       # Return to old page

    def show_all_clicked(event=None, IsChecked=None, master=None):
        """Show all checked checkboxes to search against"""
        master.master.actually_selected_pages = [] # Reset list
        for index, value in enumerate(IsChecked):
            if(value.get() == 1):   # If checked
                print("Clicked:", master.master.pages_to_search_against[index])
                master.master.actually_selected_pages.append(master.master.pages_to_search_against[index])
        print("----")

    def export_to_files(event=None, IsChecked=None, master=None, download_type:str=".json"):
        """Begin the download process"""
        master.master.actually_selected_pages = [] # Reset list
        for index, value in enumerate(IsChecked):
            if(value.get() == 1):   # If checked
                master.master.actually_selected_pages.append(master.master.pages_to_search_against[index])
            
        master.master.export_type = download_type
        master.master.switch_frame("PageThree") # Go to next page

if __name__ == "__main__":
    app = StepTwo()
    app.mainloop()