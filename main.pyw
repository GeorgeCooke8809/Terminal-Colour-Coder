import customtkinter
import pyperclip

class Colours:
    colours = {
        "Pink": ['\033[95m', "#AF6FBD"],
        "Blue": ['\033[94m',"#5690E2"],
        "Cyan": ['\033[96m',"#67B6D7"],
        "Green": ['\033[92m',"#6FCC92"],
        "Yellow": ['\033[93m',"#F3F26A"],
        "Red": ['\033[91m',"#D85945"],
        "Normal": ['\033[0m',"#FFFFFF"],
        "BOLD": ['\033[1m',"#FFFFFF"],
        "Underline": ['\033[4m',"#FFFFFF"]
    }

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x400")
        self.title("String Colour Coder")

        self.main_frame = MainFrame(self)

        self.mainloop()


class MainFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")

        self.create_widgets()

        self.pack(anchor = "center", expand = True, fill = "both", padx=10, pady=10)

    def create_widgets(self):
        self.columnconfigure(0, weight=1)

        self.rowconfigure((0,2), weight=1)
        self.rowconfigure((1,3), weight=500, minsize=150)

        self.colour_variable = customtkinter.StringVar(value="Blue")
        self.colour_select = customtkinter.CTkOptionMenu(self, values=["Pink", "Blue", "Cyan", "Green", "Yellow", "Red", "BOLD", "Underline"], command=self.refresh_text, variable=self.colour_variable)

        self.input_entry = customtkinter.CTkTextbox(self, wrap="word", font=("Consolas", 20)) # TODO: bind changing to refresh text
        self.input_entry.bind("<KeyRelease>", self.refresh_text)

        self.copy_button = customtkinter.CTkButton(self, text="COPY",command=self.copy)

        self.output_box = OutputFrame(self)

        self.draw_widgets()

    def draw_widgets(self):
        self.colour_select.grid(row = 0, column = 0, sticky="NSW")
        self.input_entry.grid(row=1, column=0, sticky="NSEW", pady=10)
        self.copy_button.grid(row=2, column=0, sticky = "NSEW")
        self.output_box.grid(row=3, column=0, sticky = "NSEW", pady=10)

    def refresh_text(self, new_value=None):
        self.output_box.change_colour(self.colour_variable.get())
        self.output_box.update_text(self.input_entry.get(0.0, "end"))

    def copy(self):
        colour = self.colour_select.get()
        text = Colours.colours[colour][0] + self.input_entry.get("0.0", 'end-1c') + Colours.colours["Normal"][0]

        pyperclip.copy(text)


class OutputFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)

        self.create_widgets()

    def create_widgets(self):
        self.label = customtkinter.CTkLabel(self, text="", text_color=Colours.colours["Blue"][1], font=("Consolas", 20))

        self.draw_widgets()

    def draw_widgets(self):
        self.label.grid(row=0, column=0, sticky="NSEW", padx=10, pady=10)

    def change_colour(self, new_colour):
        if new_colour == "BOLD":
            self.label.configure(font=("Consolas", 20, "bold"))
        elif new_colour == "Underline":
            self.label.configure(font=("Consolas", 20, "underline"))
            
        self.label.configure(text_color=Colours.colours[new_colour][1])

    def update_text(self, new_text):
        self.label.configure(text=new_text)


if __name__ == "__main__":
    App()