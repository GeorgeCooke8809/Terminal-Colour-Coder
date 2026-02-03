import customtkinter

class Colours:
    colours = {
        "Header": ['\033[95m', "#FFFFFF"],
        "Blue": ['\033[94m',"#FFFFFF"],
        "Cyan": ['\033[96m',"#FFFFFF"],
        "Green": ['\033[92m',"#FFFFFF"],
        "Yellow": ['\033[93m',"#FFFFFF"],
        "Red": ['\033[91m',"#FFFFFF"],
        "Normal": ['\033[0m',"#FFFFFF"],
        "Bold": ['\033[1m',"#FFFFFF"],
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
        self.colour_select = customtkinter.CTkOptionMenu(self, values=["Header", "Blue", "Cyan", "Green", "Yellow", "Red", "BOLD", "Underline"], command=self.refresh_text, variable=self.colour_variable)

        self.input_entry = customtkinter.CTkTextbox(self) # TODO: bind changing to refresh text

        self.copy_button = customtkinter.CTkButton(self, text="COPY",command=self.copy)

        self.output_box = OutputFrame(self)

        self.draw_widgets()

    def draw_widgets(self):
        self.colour_select.grid(row = 0, column = 0, sticky="NSW")
        self.input_entry.grid(row=1, column=0, sticky="NSEW", pady=10)
        self.copy_button.grid(row=2, column=0, sticky = "NSEW")
        self.output_box.grid(row=3, column=0, sticky = "NSEW", pady=10)

    def refresh_text(self, new_value = None):
        print(f"{new_value = }")

    def copy(self):
        pass


class OutputFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.create_widgets()

    def create_widgets(self):
        self.label = customtkinter.CTkLabel(self, text="", fg_color=Colours.colours["Blue"][1])

        self.draw_widgets()

    def draw_widgets(self):
        self.label.grid(row=0, column=0, sticky="NSEW")

    def change_colour(self, new_colour):
        pass

    def update_text(self, new_text):
        pass

    def copy(self):
        pass


if __name__ == "__main__":
    App()