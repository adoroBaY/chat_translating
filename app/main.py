from googletrans import Translator


def text_translator(text="May force be with you!", src="en", dest="ru"):
    try:
        translator = Translator()
        translation = translator.translate(text=text, src=src, dest=dest)
        return translation.text
    except Exception as ex:
        return ex


def main():
    print(text_translator(text="May force be with you!", src="en", dest="ru"))


if __name__ == "__main__":
    main()
