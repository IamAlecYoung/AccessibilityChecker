import csv
import tkinter
import customtkinter as ctk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.scrolledtext import ScrolledText
from RetrieveLinks import RetrieveLinks
from TemplatePageTodoList import TemplatePageTodoList

class StepOne(ctk.CTkFrame):

    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master)
        
        self.__text_variable = ctk.StringVar(value="https://www.fife.ac.uk/sitemap/") 
        self.__templated_page = ctk.StringVar(value="https://www.fife.ac.uk/news")
        
        # Tabview container
        self.tabview = ctk.CTkTabview(self, width=800)
        self.tabview.pack(anchor="w")

        self.tabview.add("Sitemap")
        self.tabview.add("Upload")
        self.tabview.add("Starts with")

        self.tabview.tab("Sitemap").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Upload").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Starts with").grid_columnconfigure(0, weight=1)

        # Sitemap Section
        # -----------------------
        # --------------------------------
        
        ctk.CTkLabel(self.tabview.tab("Sitemap"), text="If the site has a Sitemap, obtain random results", anchor="w").pack()
        
        # Sitemap frame container section
        # -------------------------------
        self.sitemap_frame_container = ctk.CTkFrame(self.tabview.tab("Sitemap"))
        self.sitemap_frame_container.pack()

        self.sitemap_frame_container.grid_columnconfigure(0, weight=3)
        self.sitemap_frame_container.grid_columnconfigure(1, weight=1)
 
        # Sitemap text entry
        self.sitemap_text_entry = ctk.CTkEntry(self.sitemap_frame_container, textvariable=self.__text_variable, width=240)
        self.sitemap_text_entry.grid(row=0, column=0, padx=(0, 4), sticky="nesw")

        # Sitemap upload button
        self.sitemap_upload_button = ctk.CTkButton(self.sitemap_frame_container,
                                     width=120, height=32, border_width=0, corner_radius=5, text="Fetch content",
                                     command=lambda:self.fetch_sitemap_content(master=master, sitemap=self.__text_variable.get()))
        self.sitemap_upload_button.grid(row=0, column=1, padx=4)
        
        self.page_manager = TemplatePageTodoList(master=self.sitemap_frame_container)
        self.page_manager.grid(row=1,column=0, columnspan=2, padx=2, pady=2)

        # Upload Section
        # -----------------------
        # --------------------------------

        ctk.CTkLabel(self.tabview.tab("Upload"), text="Upload a CSV of files to check", anchor='w').pack()

        self.download_examle_csv = ctk.CTkLabel(self.tabview.tab("Upload"), text="Download example csv", cursor="hand2", font=ctk.CTkFont(underline=True))
        self.download_examle_csv.pack()
        self.download_examle_csv.bind("<Button-1>", lambda e:self.create_example_file()) #lambda e:callback(e, "tag1"))

        # Upload frame container section
        self.upload_frame_container = ctk.CTkFrame(self.tabview.tab("Upload"))
        self.upload_frame_container.pack()

        self.upload_frame_container.grid_columnconfigure(0, weight=3)
        self.upload_frame_container.grid_columnconfigure(1, weight=1)
 
        # Upload upload button
        self.upload_upload_button = ctk.CTkButton(self.upload_frame_container,
                                     width=120, height=32, border_width=0, corner_radius=5, text="Select file",
                                     command=lambda:self.open_file(self=self,master=master))
        self.upload_upload_button.grid(row=0, column=1, padx=4)

        # Starts with Section
        # -----------------------
        # --------------------------------

        ctk.CTkLabel(self.tabview.tab("Starts with"), text="Check all URLs and children of that URL", anchor='w').pack()

        # Startwith frame container section
        self.startwith_frame_container = ctk.CTkFrame(self.tabview.tab("Starts with"))
        self.startwith_frame_container.pack()

        self.startwith_frame_container.grid_columnconfigure(0, weight=3)
        self.startwith_frame_container.grid_columnconfigure(1, weight=1)
 
        # Startwith text entry
        self.startwith_text_entry = ctk.CTkEntry(self.startwith_frame_container, textvariable=self.__templated_page, width=240)
        self.startwith_text_entry.grid(row=0, column=0, padx=(0, 4), sticky="nesw")

        # Startwith upload button
        self.startwith_upload_button = ctk.CTkButton(self.startwith_frame_container,
                                     width=120, height=32, border_width=0, corner_radius=5, text="Fetch content",
                                     command=lambda:self.pages_that_start_with(master=master, sitemap=self.__text_variable.get(), startswith=self.__templated_page.get()))
        self.startwith_upload_button.grid(row=0, column=1, padx=4)


    def pages_that_start_with(event=None, master=None, sitemap:str=None, startswith:str=None):
        """Find all pages that start with a certain url."""
        retrieve_links = RetrieveLinks()
        master.master.pages_to_search_against = retrieve_links.initial_return_all_pages_starting_with(sitemap=sitemap, starts_with=startswith)
        master.master.switch_frame("PageTwo") # Go to next page

    def open_file(event=None, self=None, master=None):
        """Open a file for editing."""
        filepath = askopenfilename(
            filetypes=[("CSV File", "*.csv"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        filename = open(filepath, 'r')
        reader = csv.DictReader(filename)

        for sites in reader:
            master.master.pages_to_search_against.append(sites['pages'])

        master.master.switch_frame("PageTwo") # Go to next page


    def fetch_sitemap_content(event=None, master=None, sitemap:str=None):
        retrieve_links = RetrieveLinks()
        master.master.pages_to_search_against = retrieve_links.initial_return_all_pages_using_sitemap(sitemap=sitemap, templated_pages=master.master.templated_pages)
        master.master.switch_frame("PageTwo") # Go to next page


    def create_example_file(event=None):
        """Generates an example file to show how the CSV should look"""
        filepath = asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV File", "*.csv"), ("All Files", "*.*")],
        )
        if not filepath:
            return

        example_sites = []
        example_sites.append("https://www.fife.ac.uk")
        example_sites.append("https://www.fife.ac.uk/staff/")
        example_sites.append("https://www.fife.ac.uk/about-us/board-of-governors/our-board-of-governors/")
        
        csv_titles = "pages\n"
        csv_content = ',\n'.join(example_sites)
        
        with open(filepath, mode="w", encoding="utf-8") as output_file:
            output_file.write("{}{}".format(csv_titles,csv_content))


if __name__ == "__main__":
    app = StepOne()
    app.mainloop()