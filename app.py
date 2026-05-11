from deep_translator import GoogleTranslator
import tkinter as tk
from tkinter import messagebox

# Function to translate text
def translate_text():
    text = input_text.get("1.0", tk.END).strip()
    choice = lang_var.get()

    if text == "":
        messagebox.showerror("Error", "Please enter text")
        return

    if choice == "Telugu":
        target_lang = "te"
    elif choice == "Hindi":
        target_lang = "hi"
    else:
        messagebox.showerror("Error", "Select language")
        return

    translated = GoogleTranslator(
        source='auto',
        target=target_lang
    ).translate(text)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, translated)


# Window setup
root = tk.Tk()
root.title("CodeAlpha Translator")
root.geometry("400x400")

# Input label
tk.Label(root, text="Enter Text:").pack()

# Input box
input_text = tk.Text(root, height=5)
input_text.pack()

# Language selection
tk.Label(root, text="Select Language:").pack()

lang_var = tk.StringVar(value="Telugu")

tk.Radiobutton(root, text="Telugu", variable=lang_var, value="Telugu").pack()
tk.Radiobutton(root, text="Hindi", variable=lang_var, value="Hindi").pack()

# Translate button
tk.Button(root, text="Translate", command=translate_text).pack(pady=10)

# Output label
tk.Label(root, text="Translated Text:").pack()

# Output box
output_text = tk.Text(root, height=5)
output_text.pack()

# Run app
root.mainloop()