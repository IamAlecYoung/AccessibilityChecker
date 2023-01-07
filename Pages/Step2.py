import customtkinter as ctk

class StepTwo(ctk.CTkFrame):

    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master)
        ctk.CTkLabel(self, text="This is page two").pack(side="top", fill="x", pady=10)
        ctk.CTkButton(self, text="Return to first page", command=lambda: master.master.switch_frame("PageOne")).pack()


if __name__ == "__main__":
    app = StepTwo()
    app.mainloop()