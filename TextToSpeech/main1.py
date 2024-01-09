import os
import subprocess
from datetime import datetime
from gtts import gTTS  # Импорт gTTS из библиотеки gtts

def check_dependencies():
    try:
        import gtts
        return True
    except ImportError:
        return False

def install_dependencies():
    subprocess.check_call(['pip', 'install', 'gtts'])

def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def convert_text_to_audio(file_name):
    text_files = [f for f in os.listdir('Text') if f.endswith('.txt')]

    if file_name not in text_files:
        print("Указанный файл не найден в папке Text.")
        return

    text_file_path = os.path.join('Text', file_name)

    # Чтение текста из файла
    with open(text_file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Создание объекта gTTS
    tts = gTTS(text, lang='ru')

    # Определение имени аудиофайла и пути к папке Audio
    output_audio_file = f"Audio/{os.path.splitext(file_name)[0]}.mp3"

    # Создание папки Audio, если она не существует
    os.makedirs(os.path.dirname(output_audio_file), exist_ok=True)

    # Сохранение аудио в файл
    tts.save(output_audio_file)

    # Воспроизведение аудио
    os.system(f"start {output_audio_file}")
    print(f"Текст из файла {file_name} успешно преобразован в аудио и сохранен в папке Audio.")

if __name__ == "__main__":
    try:
        while True:
            # Проверка наличия зависимостей
            if not check_dependencies():
                install_dependencies()

            # Вывод баннера и другие функции
            banner = """
             _______        _     _______       _____                      _     
            |__   __|      | |   |__   __|     / ____|                    | |    
               | | _____  _| |_     | | ___   | (___  _ __   ___  ___  ___| |__  
               | |/ _ \ \/ / __|    | |/ _ \   \___ \| '_ \ / _ \/ _ \/ __| '_ \ 
               | |  __/>  <| |_     | | (_) |  ____) | |_) |  __/  __/ (__| | | |
               |_|\___/_/\_\\__|     |_|\___/  |_____/| .__/ \___|\___|\___|_| |_|
                                                             | |                         
                                                             |_|
            """

            print(banner)
            print("made by TyOpey")
            print(f"Текущее время: {get_current_time()}")

            text_files = [f for f in os.listdir('Text') if f.endswith('.txt')]
            print("Файлы в папке Text:")
            for file_name in text_files:
                print(file_name)

            chosen_file = input("Введите название файла из папки Text: ")
            convert_text_to_audio(chosen_file)

            answer = input("Хотите провести ещё одну операцию? (Да/Нет): ")
            if answer.lower() != 'да':
                break  # Завершение цикла, если пользователь ввел что-то кроме "да"
    except Exception as e:
        print(f"Ошибка: {e}")
