# Trai Torti Machine learning related words 2023

# Importing libraries
import tkinter as tk
from tkinter import ttk
from gensim.models import Word2Vec

# Load model
mdl = Word2Vec.load('relatedWordsModel')

# Functionality for finding related words.
def Synonyms():
    
    word = txtfield.get()

    result.config(state='normal')
    result.delete(1.0, tk.END)

    # Loop through and find the related words to display.
    try:
        relatedWords = mdl.wv.most_similar(word)
        for relatedWord, similarity in relatedWords:
            result.insert(tk.END, f'found {relatedWord} with {round(similarity, 2)}\n')

        result.config(state='disabled')
    except KeyError:
        result.insert(tk.END, 'The word is not found in this vocabulary set\n Try a different word.')
        result.tag_configure('center', justify='center')
        result.tag_add('center', '1.0', 'end')


# Function to center the frame whenever the window is resized
def centerFrame(self):
    frame.place(relx=0.5, rely=0.5, anchor='c')

# Setup GUI main window
mainWindow = tk.Tk()
mainWindow.geometry('600x400')
mainWindow.resizable(True, True)
mainWindow.title('Related Words')

# Add a frame to insert the rest of the UI
frame = ttk.Frame(mainWindow, padding="10 10 20 20")

# Textfield setup
txtfield = ttk.Entry(frame, width=30, font=('Ariel', 16))
txtfield.grid(column=0, row=0, padx=5, pady=5)

# Search button setup
searchBtn = ttk.Button(frame, text='Search', command=Synonyms)
searchBtn.grid(column=1, row=0, padx=5, pady=5)

# Results setup
result = tk.Text(frame, width=40, height=10, font=('Ariel', 16))
result.grid(column=0, row=1, padx=20, pady=20)
result.config(state='disabled')

# Run it!
mainWindow.bind('<Configure>', centerFrame)
mainWindow.update()
mainWindow.geometry(mainWindow.geometry())
mainWindow.mainloop()