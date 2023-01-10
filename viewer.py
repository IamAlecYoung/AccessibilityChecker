import tkinter, customtkinter
#from StartPage import StartPage
from Pages.Step1 import StepOne
from Pages.Step2 import StepTwo
from Pages.Step3 import StepThree

# Solution from (modified): https://stackoverflow.com/questions/67992255/switch-between-two-frames-in-tkinter-in-separates-files

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

pages = {
    "PageOne": StepOne, 
    "PageTwo": StepTwo,
    "PageThree": StepThree
}

class MainView(customtkinter.CTk):

    def __init__(self):
        customtkinter.CTk.__init__(self)
        
        self.geometry("1000x700")
        self.title("This is a new window")

        # Global variables persisted across pages
        self.templated_pages = [
            "https://www.fife.ac.uk/news",
            "https://www.fife.ac.uk/courses/search-all-courses/"
        ]           # Pages which are templated, get the start of the url to disregard
        self.export_type = ".json"          # File format to export files to
        self.pages_to_search_against = []   # Pages to search against, pulled from Sitemap or CSV file
        self.actually_selected_pages = []   # Files to actually search against, selected from pages_to_search_against 

        # configure grid layout (4x4)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=6)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=9)

        self.top_bar = customtkinter.CTkFrame(self, width=800, height=20)
        self.top_bar.grid(row=0, column=0, columnspan=2)
        self.top_bar_label = customtkinter.CTkLabel(self.top_bar, text="Localized Live Accessibility and Modification Analyzer")
        self.top_bar_label.grid(row=0, column=0, sticky="w")

        self.side_panel = customtkinter.CTkFrame(self, width=125)
        self.side_panel.grid(row=1, column=0)
        self.side_panel_label = customtkinter.CTkLabel(self.side_panel, text="Left panel")
        self.side_panel_label.grid(row=0, column=0)

        self.main_frame = customtkinter.CTkFrame(self, width=875)
        self.main_frame.grid(row=1, column=1, columnspan=3, sticky="nsew") 

        self._frame = None
        self.switch_frame("PageOne")


    def switch_frame(self, page_name:str):
        """Destroys current frame and replaces it with a new one."""
        current_selection = pages[page_name]
        new_frame = current_selection(master = self.main_frame)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid(row=0, column=0)
        #self._frame.pack()


if __name__ == "__main__":
    app = MainView()
    app.mainloop()