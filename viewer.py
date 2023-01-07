from cProfile import label
from doctest import master
import tkinter, customtkinter
from turtle import width
from Pages.Step2 import StepTwo

# Solution from (modified): https://stackoverflow.com/questions/67992255/switch-between-two-frames-in-tkinter-in-separates-files

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#from StartPage import StartPage
from Pages.Step1 import StepOne
from Pages.Step2 import StepTwo

pages = {
    "PageOne": StepOne, 
    "PageTwo": StepTwo
}

class MainView(customtkinter.CTk):

    def __init__(self):
        customtkinter.CTk.__init__(self)
        
        self.geometry("500x350")
        self.title("This is a new window")

        self.templated_pages = []
        self.pages_to_search_against = []

        # configure grid layout (4x4)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0, weight=1)

        self.side_panel = customtkinter.CTkFrame(self, width=125)
        self.side_panel.grid(row=0, column=0)        
        self.side_panel_label = customtkinter.CTkLabel(self.side_panel, text="Left panel")
        self.side_panel_label.grid(row=0, column=0)

        self.main_frame = customtkinter.CTkFrame(self, width=375)
        self.main_frame.grid(row=0, column=1, columnspan=3, sticky="nsew") 

        self.main_frame_label = customtkinter.CTkLabel(self.main_frame, text="Main panel")
        self.main_frame_label.grid(row=1, column=0)

        self._frame = None
        self.switch_frame("PageOne")

    def switch_frame(self, page_name):
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