from deep_translator import GoogleTranslator

text = input("Enter text: ")

print("1. Telugu")
print("2. Hindi")

choice = input("Choose language: ")

if choice == "1":
    target_lang = "te"

elif choice == "2":
    target_lang = "hi"

else:
    print("Invalid choice")
    exit()

translated = GoogleTranslator(
    source='auto',
    target=target_lang
).translate(text)

print("Translated Text:", translated)
