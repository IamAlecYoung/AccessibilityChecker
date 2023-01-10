from cgitb import text
import tkinter as tk
import customtkinter as ctk

class TemplatePageTodoList(ctk.CTkFrame):

    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master)
        self.master=master.master.master.master.master.master   # This is just ridiculous

        self.container = ctk.CTkFrame(self)
        self.container.grid_columnconfigure(0, weight=3)        # configure grid of individual tabs
        self.container.grid_columnconfigure(0, weight=1)

        self.descriptor = tk.Label(self,
                                    text="Any templated page to only return a single result for?")
        self.text_widget = tk.Text(self)                        # Holds the text links

        # Text entry and button to add to list
        self.entry = tk.Entry(self)
        self.add_button = tk.Button(self, text='Add', command=lambda:self.add_task(master=self.master))

        # Position elements
        self.descriptor.grid(row=0, column=0, columnspan=2, sticky="w")
        self.entry.grid(row=1, column=0, sticky="nsew")
        self.add_button.grid(row=1, column=1, sticky="nsew")
        self.text_widget.grid(row=2, column=0, columnspan=2)
 
        self.update_list(text_widget=self.text_widget, master=self.master)


    def add_task(self, master):
        """Update the pages list and refresh"""
        master.templated_pages.append(self.entry.get())      
        self.entry.delete(0, 'end')
        self.update_list(text_widget=self.text_widget, master=master)

    def delete_task(self, index, text_widget, master):
        """Delete an item from the pages list"""
        del master.templated_pages[index]
        self.update_list(text_widget=text_widget, master=master)

    def update_list(self, text_widget, master):
        """Refresh the pages list"""
        text_widget.delete('1.0', 'end')
        
        # Insert each task in the list into the text widget
        for i, task in enumerate(master.templated_pages):
            # Create a delete button for each task
            delete_button = tk.Button(text_widget, text='X', command=lambda index=i: self.delete_task(index=index, text_widget=text_widget, master=master))
            
            # Insert the task and delete button into the text widget
            text_widget.window_create('end', window=delete_button)
            text_widget.insert('end', f' {task}\n')


if __name__ == "__main__":
    app = TemplatePageTodoList()
    app.mainloop()