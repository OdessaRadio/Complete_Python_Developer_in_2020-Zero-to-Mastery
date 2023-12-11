from translate import Translator

translator = Translator(to_lang="de")

try:
    with open('./Complete_Python_Developer_in_2020-Zero-to-Mastery/IO/test.txt', mode = 'r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
        with open('./Complete_Python_Developer_in_2020-Zero-to-Mastery/IO/result.txt', mode = 'w') as my_file_2:
            my_file_2.write( translation )
except FileNotFoundError as e:
    print('check your file path')