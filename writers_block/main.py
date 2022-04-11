from settings import Settings
from tkinter import * 

class WritersBlock():
    """Main class to manage writers block app"""

    def __init__(self):
        """Main class to manage writers app behavior and assets"""         
        self.settings = Settings() 

        self.window = Tk() 
        self.window.title(self.settings.title)
        self.window.minsize(self.settings.screen_height, self.settings.screen_width)

        # Initiate typing area and labels
        self.label = Label(text=self.settings.label_text)
        self.label.pack()


        self.text = Text(self.window, font=("Arial", 20))
        self.text.pack()

        # Flag for user typing
        self.is_typing = None 
        self.text.bind('<Key>', self.check_events)


    def run(self):
        """Start the main loop"""

        self.window.mainloop()


    def delete_words(self):
        self.text.delete(1.0, 'end')


    def check_events(self, event):
        """Respond to keypress events"""

        if self.is_typing is not None:
            self.window.after_cancel(self.is_typing)

        # Remove all words due to no typing 
        self.is_typing = self.window.after(self.settings.no_typed_words_time, self.delete_words)


if __name__ == "__main__":
    app = WritersBlock()
    app.run()
