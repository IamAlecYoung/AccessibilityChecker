import csv
import tkinter
import customtkinter as ctk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.scrolledtext import ScrolledText
from RetrieveLinks import RetrieveLinks
from TemplatePageTodoList import TemplatePageTodoList

class StartPage(ctk.CTkFrame):

    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master)
        
        self.start_inner_container = ctk.CTkFrame(self)
        self.start_inner_container.pack()

        self.start_inner_container.grid_columnconfigure(0, weight=3)
        self.start_inner_container.grid_columnconfigure(1, weight=1)
        
        self.disclaimer = ctk.CTkTextbox(self.start_inner_container, width=600, height=400, border_spacing=6)
        self.disclaimer.grid(row=0, column=0, columnspan=2)

        full_warranty = """Welcome to this wee accessibility checker.
        
- This is provided 'as is', and is NOT an official Digital project, meaning you will not receive assistance from the Digital Helpdesk.
This was just a fun (subjective) wee hobby project that will hopefully make your jobs easier.

- This makes use of the 'Axe accessibility checker' extension to check against a page (https://www.deque.com/axe/). 
We have noticed some discrepencies between different tools giving different results, such as SiteImprove (https://www.siteimprove.com/platform/accessibility/).
This tool is just a way to quickly check pages without having to do it manually, this does not guarantee 100% compliance so best judgement should still be 
followed. Think of it as a supplementary tool rather than a replacement.

- When using the tool, you MUST announce to everyone else in the room, loudly and clearly, that you are an 'A11Y champion'. Direct eye contact optional.

- To work, you MUST have the Firefox browser installed on your machine, I can set it up to work with Chrome too but have not had the chance.

"""

        self.disclaimer.insert("0.0", full_warranty)

        #self.point_01.grid(row=0, column=0)

        self.start_button = ctk.CTkButton(self.start_inner_container, text="I understand, Lets get started", command=lambda: self.begin_the_fun(self=self, master=master))
        self.start_button.grid(row=1, column=0, sticky="nsew", pady=6)

        
    def begin_the_fun(event=None, self=None, master=None):
        """Just get started"""
        master.master.switch_frame("PageOne")


if __name__ == "__main__":
    app = StartPage()
    app.mainloop()