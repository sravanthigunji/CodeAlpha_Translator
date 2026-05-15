from deep_translator import GoogleTranslator
import tkinter as tk
from tkinter import ttk, messagebox


def translate_text():
    text = input_text.get("1.0", tk.END).strip()
    target = language_box.get()

    if text == "":
        messagebox.showerror("Error", "Please enter text")
        return

    try:
        translated = GoogleTranslator(
            source="auto",
            target=languages[target]
        ).translate(text)

        output_text.config(state="normal")
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)
        output_text.config(state="disabled")

    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("CodeAlpha Translator")
root.geometry("650x500")
root.config(bg="#f0f4f8")


title = tk.Label(
    root,
    text="🌐 CodeAlpha Translator",
    font=("Arial", 22, "bold"),
    bg="#f0f4f8",
    fg="#1e3a8a"
)
title.pack(pady=15)


input_label = tk.Label(
    root,
    text="Enter Text",
    font=("Arial", 12, "bold"),
    bg="#f0f4f8"
)
input_label.pack()


input_text = tk.Text(
    root,
    height=7,
    width=60,
    font=("Arial", 12),
    relief="solid",
    bd=2
)
input_text.pack(pady=10)


languages = {
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "Kannada": "kn",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja"
}


lang_label = tk.Label(
    root,
    text="Select Language",
    font=("Arial", 12, "bold"),
    bg="#f0f4f8"
)
lang_label.pack()

language_box = ttk.Combobox(
    root,
    values=list(languages.keys()),
    font=("Arial", 11),
    state="readonly",
    width=20
)

language_box.set("Telugu")
language_box.pack(pady=10)


translate_btn = tk.Button(
    root,
    text="Translate",
    command=translate_text,
    font=("Arial", 13, "bold"),
    bg="#2563eb",
    fg="white",
    padx=20,
    pady=5,
    relief="flat",
    cursor="hand2"
)
translate_btn.pack(pady=15)


output_label = tk.Label(
    root,
    text="Translated Text",
    font=("Arial", 12, "bold"),
    bg="#f0f4f8"
)
output_label.pack()


output_text = tk.Text(
    root,
    height=7,
    width=60,
    font=("Arial", 12),
    relief="solid",
    bd=2,
    state="disabled"
)
output_text.pack(pady=10)


footer = tk.Label(
    root,
    text="Built with Python + AI Translation",
    font=("Arial", 10),
    bg="#f0f4f8",
    fg="gray"
)
footer.pack(pady=10)

root.mainloop()