from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
import easygui
import subprocess
import sys
import os


class MainApp(App):

    def build(self):                                            #Главное окно приложения

        floatlayout = FloatLayout()

        not_one_help_text = "Добавление новых людей в базу данных.\n" \
                            "Выбирете директорию, в которой находятся папки с фотографиями людей.\n" \
                            "Каждая папка должна быть названа в формате ФИО_дополнительная информация\n" \
                            "Не используйте точки в название, это может привести к неправильной работе программы!\n" \
                            "В каждой папке должны находиться фотографии только ОДНОГО человека!\n" \
                            "Для каждого человека необходимо создать отдельную папку!"

        not_one_person_info_label = Label(text=not_one_help_text,
                                          size_hint=(0.5, 0.5),
                                          pos_hint={'center_x': 0.5, 'center_y': 0.7},
                                          halign="center",
                                          font_size=18,
                                          color=(0, 0, 0, 1))
        floatlayout.add_widget(not_one_person_info_label)

        select_way_to_directories = Button(text="Выбрать директорию",
                                           size_hint=(0.3, 0.17),
                                           pos_hint={'center_x': 0.25, 'center_y': 0.35},
                                           background_color=(255/255, 255/255, 51/255, 1))
        select_way_to_directories.bind(on_press=app.select_directory_with_diretories)
        floatlayout.add_widget(select_way_to_directories)

        start_work_button = Button(text="Начать обработку",
                                   size_hint=(0.3, 0.17),
                                   pos_hint={'center_x': 0.75, 'center_y': 0.35},
                                   background_color=(255/255, 255/255, 51/255, 1))
        start_work_button.bind(on_press=app.work_with_images)
        floatlayout.add_widget(start_work_button)

        exit_button = Button(text="Выход",
                             size_hint=(0.3, 0.17),
                             pos_hint={'center_x': 0.5, 'center_y': 0.11},
                             background_color=(255/255, 255/255, 51/255, 1))
        exit_button.bind(on_press=app.exit)
        floatlayout.add_widget(exit_button)

        Window.clearcolor = (255/255, 255/255, 204/255, 1)                          #Цвет фона

        return floatlayout


    def select_directory_with_diretories(self, instance):                       #Выбор директории, в которой лежат другие директории с фото людей!!!

        self.way_to_directory = easygui.diropenbox("Путь до директории с директориями с фото", default="photosofnewpeople")      # Указать дефолтную папку!!!!!!

        try:                                                    #Проверка на выбор директории
            if len(self.way_to_directory):
                self.selected_mode = "selected"
        except:
            self.selected_mode = "notselected"


    def exit(self, instance):                       # Закрытие приложения
        sys.exit()


    def work_with_images(self, instance):                       #Обработка выбранных значений и изображений

        try:                                                    #Проверка на наличие выбранных изображений
            global selected_mode

            if self.selected_mode == "notselected":
                error = easygui.msgbox('Не выбрана директория!', 'Не выбрана директория')

            elif self.selected_mode == "selected":
                global way_to_directory

                list_of_directories = os.listdir(self.way_to_directory)             # Получаем список папок внутри директории

                checker = 0                                 # Для проверки количества добавленных людей

                banner = easygui.msgbox("Нажмите 'ОК' для начала обработки.\nДожитесь сообщения о завершение работы!", "Начало обработки")

                for i in range(len(list_of_directories)):
                    if "." not in list_of_directories[i]:                           # Проверяем, что это точно директории
                        try:
                            way_to_one_directory = self.way_to_directory + "\\" + list_of_directories[i]

                            subprocess.run(["python3", "add_new_people.py", way_to_one_directory])         #### Запускаем другую программу #### Путь до проги!!!!!

                            checker += 1

                        except:                                                             #Если что-то пошло не так, то папка будет пропущено
                            message_error = "Произошла ошибка при обработке папки: " + list_of_directories[i] + ".\nОна будет пропущена!"
                            easygui.msgbox(message_error, 'Ошибка при работе программы')

                if checker != 0:
                    ready = easygui.msgbox('Обработка заверешена.\nЛюди добавлены в базу.', 'Обработка заверешена')
                if checker == 0:                                                        # Если неправильная директория или неправильно расположены файлы
                    alarm = easygui.msgbox("Ни добален ни один человек! Проверте выбранную директорию!")

        except:
            error = easygui.msgbox('Не выбрана директория!', 'Не выбрана директория')



if __name__ == '__main__':
    app = MainApp()
    app.run()


#### В данной программе нужно выбрать путь до директории, в которой лежат папки с фотографиями людей.
#### Она запускает программу обработки лиц и добавления людей в базу!
