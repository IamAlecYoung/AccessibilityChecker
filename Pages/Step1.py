from cgitb import text
import customtkinter as ctk

class StepOne(ctk.CTkFrame):

    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master)
        
        self.__text_variable = ctk.StringVar(value="https://www.fife.ac.uk/sitemap/") 

        # Tabview container
        self.tabview = ctk.CTkTabview(self, width=250)
        self.tabview.pack()

        self.tabview.add("Sitemap")
        self.tabview.add("Upload")

        self.tabview.tab("Sitemap").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Upload").grid_columnconfigure(0, weight=1)

        # Sitemap Section
        # ---------------
        # ---------------
        
        ctk.CTkLabel(self.tabview.tab("Sitemap"), text="If the site has a Sitemap, obtain random results", anchor='w').pack()
        ctk.CTkButton(self.tabview.tab("Sitemap"), text="Go to second page", command=lambda: master.master.switch_frame("PageTwo")).pack()

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
                                     command=lambda:self.button_event(value_to_print=self.__text_variable))
        self.sitemap_upload_button.grid(row=0, column=1, padx=4)


        # Upload Section
        # ---------------
        # ---------------

        ctk.CTkLabel(self.tabview.tab("Upload"), text="Upload a CSV of files to check", anchor='w').pack()
        ctk.CTkButton(self.tabview.tab("Upload"), text="Go to second page", command=lambda: master.master.switch_frame("PageTwo")).pack()

        # Sitemap frame container section
        # -------------------------------
        self.upload_frame_container = ctk.CTkFrame(self.tabview.tab("Upload"))
        self.upload_frame_container.pack()

        self.upload_frame_container.grid_columnconfigure(0, weight=3)
        self.upload_frame_container.grid_columnconfigure(1, weight=1)
 
        # Sitemap text entry
        self.sitemap_text_entry = ctk.CTkEntry(self.upload_frame_container, textvariable=self.__text_variable, width=240)
        self.sitemap_text_entry.grid(row=0, column=0, padx=(0, 4), sticky="nesw")

        # Sitemap upload button
        self.sitemap_upload_button = ctk.CTkButton(self.upload_frame_container,
                                     width=120, height=32, border_width=0, corner_radius=5, text="Fetch content",
                                     command=lambda:self.button_event(value_to_print=self.__text_variable))
        self.sitemap_upload_button.grid(row=0, column=1, padx=4)

        # # self.uploaded_value = customtkinter.CTkLabel(self.tabview.tab("Sitemap"),
        # #                        textvariable=self.__text_variable, width=120, height=25, fg_color=("white", "gray75"), corner_radius=8)
        # # self.uploaded_value.grid(row=2,column=0)

        # # Upload tab content
        # self.upload_label = customtkinter.CTkLabel(self.tabview.tab("Upload"), text="Upload a CSV list of website addresses")
        # self.upload_label.grid(row=1,column=0)
        

        # self.label = customtkinter.CTkLabel(self.main_frame, text="Login System")
        # self.label.place()

    def button_event(event=None, value_to_print=None):
        print(value_to_print.get())


if __name__ == "__main__":
    app = StepOne()
    app.mainloop()