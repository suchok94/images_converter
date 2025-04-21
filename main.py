from modules.app import App
from modules.converters_creator import ConverterCreatorJpgToPng, ConverterCreatorPngToJpg

def main():

    source_path = input('Введите путь до исходного файла: ')
    destination_path = input('Введите путь до конечного файла: ')
    image_type = source_path[-4:]

    if image_type == '.png':
        app = App(ConverterCreatorPngToJpg())
        app.convert(source_path, destination_path)

    elif image_type == '.jpg' or image_type == 'jpeg':
        app = App(ConverterCreatorJpgToPng())
        app.convert(source_path, destination_path)
    
    else: print("Не правильный путь")


if __name__ == '__main__':
    main()