from translate import Translator
try:
    my_file = open(r"C:\Users\USER\Desktop\Hey.txt", mode='r')
    text = my_file.read()

    translator = Translator(to_lang="es")
    translation = translator.translate(text)
    print(translation)

    trans_file = open(r"C:\Users\USER\Desktop\Jap_translate.txt", mode='w')
    trans_file.write(translation)


except FileNotFoundError as err:
    print(err)
