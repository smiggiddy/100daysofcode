from tkinter import *
from tkinter import font
from turtle import width 
from random import shuffle
import time

from pyparsing import col



class TypingTestGui:
    # Class Initates How Many Words One Can type in a minute

    def __init__(self, words):
        """Function initiates the gui and the typing test"""
        welcome_msg = "Welcome To Typing Test. Press start to begin"
        self.words = words
        self.window = Tk()
        self.window.title("Typing Speed Test")
        self.window.minsize(500, 500)

        # make window sticky for every case (center)
        self.window.grid_rowconfigure(0, weight=0)
        self.window.grid_columnconfigure(0, weight=1)

        self.text = Text(font=("Arial", 20), height=10, width=40)
        self.text.insert('end', welcome_msg)
        self.text.config(state='disabled')
        self.text.grid(row=1, column=0)

        # Place to Enter Text 
        self.word_input = Entry(self.window, width=50)
        self.word_input.grid(row=3, column=0)

        # Labels
        self.title_label = Label(text="Typing Tester 1.0")
        self.title_label.grid(row=0, column=0)

        # Start Button
        self.start_btn = Button(text="Start", command=self.setup_test)
        self.start_btn.grid(row=4, column=0)
        self.test_started = False


        # initializing score elements
        self.words_right = 0
        self.words_total = 0
        self.wpm = 0

        # import typing test class for word calc
        self.typing_test_class = TypingTest()

        self.window.mainloop()


    def setup_test(self):
        if not self.test_started:    
            shuffle(self.words)
            self.text.config(state='normal')
            self.text.delete(1.0, 'end')
            self.text.insert('end', self.words[:30])
            self.text.config(state='disabled')
            self.test_started = True 
            self.end_time = time.time() + 60
            self.typing_test_loop()

    def typing_test_loop(self):
        """Function runs for 60 seconds while user types"""
        if time.time() < self.end_time:
            # loops for 60 seconds
            self.window.bind('<space>', self.clear_typed_word)
            self.window.after(1000, self.typing_test_loop)
        else:
            wpm = self.typing_test_class.calculate_wpm()
            self.text.config(state='normal')
            self.text.delete(1.0, 'end')            
            self.text.insert('end', f'Final Stats WPM: {wpm:.02f}')
            self.text.insert('end', f'\nTyped Words: {self.typing_test_class.words}')
            self.text.insert('end', f'\nIncorrect Words: {self.typing_test_class.incorrect}')

            self.text.config(state='disabled')

            # Remove Window Bind
            self.window.unbind('<space>')
            

    def typing_test(self):
        """Function tests typing speed once user presses start"""
        # check if word is right
        if not self.typing_test_class.spelling_check(self.input.strip(), self.actual_word):
            self.typing_test_class.incorrect += 1
        else:
            self.typing_test_class.words += 1
            self.typing_test_class.characters += len(self.actual_word)



    def clear_typed_word(self, event):
        # command for deleting text after space is pressed. 
        self.input = self.word_input.get()
        self.word_input.delete(0, "end")
        self.next_word()

        return None

    
    def next_word(self):
        # Function changes highlighted word to the next word and deletes first word in list
        self.actual_word = self.words.pop(0)
        
        # evaluate what was typed
        self.typing_test()

        self.text.config(state='normal')
        self.text.delete(1.0, 'end')
        self.text.insert('end', self.words[:30])
        self.text.config(state='disabled')
        
        # self.canvas.itemconfig(self.canvas_words, text=self.words)


class TypingTest:
    # Class for creating typing test game
    def __init__(self):
        self.characters = 0
        self.words = 0
        self.incorrect = 0
        self.wpm = 0 

    def spelling_check(self, typed_word, actual_word):
        # function returns bool if user typed word == actual word
        return typed_word.lower() == actual_word.lower() 

    def calculate_wpm(self):
        # function returns wpm 
        if self.characters != 0 and self.words != 0:
            return (self.characters / (self.words - self.incorrect) ) / 60


if __name__ == "__main__":
    # Read Data From Word List
    try:
        with open("./day-85/words.txt") as f:
            words = f.readline()

        words = words.split()
        tt = TypingTestGui(words)

    except FileNotFoundError:
        error = "Please save a word list in current dir. and try again"
        print(error)
        tt = TypingTestGui("")
        tt.canvas.itemconfig(tt.canvas_words, text=error)
