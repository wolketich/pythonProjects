from googletrans import Translator, LANGUAGES

def display_languages():
    """Displays all available languages and their codes."""
    print("\nCode : Language")  # Heading of language option menu
    for code, language in LANGUAGES.items():
        print(f"{code} => {language.title()}")
    print()  # adding an empty space

def get_language_selection():
    """Prompts the user for a language code and checks its validity."""
    while True:
        user_code = input("Please input desired language code. To see the language code list enter 'options': ").lower()

        if user_code == "options":
            display_languages()
        elif user_code in LANGUAGES:
            print(f"You have selected {LANGUAGES[user_code].title()}")
            return user_code
        else:
            print("It is not a valid language code!")

def translate_loop(translator, dest_language):
    """Keeps receiving user input and translates until the user decides to exit."""
    while True:
        text_to_translate = input("\nWrite the text you want to translate: \nTo exit the program write 'close':\n")

        if text_to_translate.lower() == "close":
            print("\nHave a nice day!")
            break

        try:
            # Attempting the translation
            translated = translator.translate(text=text_to_translate, dest=dest_language)
            
            print(f"\n{LANGUAGES[dest_language].title()} translation: {translated.text}")
            print(f"Pronunciation: {translated.pronunciation or 'N/A'}")
            print(f"Translated from: {LANGUAGES[translated.src].title()}")
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    translator = Translator()
    selected_language = get_language_selection()
    translate_loop(translator, selected_language)

if __name__ == "__main__":
    main()
