from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
import easygui
import sys
import subprocess


class MainApp(App):

    def build(self):                                    #Главное окно приложения

        floatlayout = FloatLayout()                                     #Для расположения элементов на экране

        label_login = Label(text="Регистрация для получения отчетов.\nВ поле ввода последний зарегистрированный адрес.",
                            size_hint=(0.48, 0.45),
                            pos_hint={'center_x': 0.5, 'center_y': 0.9},
                            halign="center",
                            color=(0, 0, 0, 1))
        floatlayout.add_widget(label_login)

        label_email = Label(text="Введите email:",
                            size_hint=(0.48, 0.1),
                            pos_hint={'center_x': 0.25, 'center_y': 0.7},
                            color=(0, 0, 0, 1))
        floatlayout.add_widget(label_email)

        email = open("mail.txt").read()                   #####  Путь до файла с почтой!!!!!!!!    ########

        self.email_input = TextInput(text=email,
                                     size_hint=(0.48, 0.1),
                                     pos_hint={'center_x': 0.75, 'center_y': 0.7})
        floatlayout.add_widget(self.email_input)

        label_time = Label(text="Выбор времяни получения отчетов.\nОтчеты отправляются каждый день в выбранное время.\n"
                                "Введите время в формате 'чч:мм' в 24 часовом формате.\nЕсли нужно получать отчеты чаще, введите значения времени через запятую.",
                           size_hint=(0.48, 0.45),
                           pos_hint={'center_x': 0.5, 'center_y': 0.5},
                           halign="center",
                           color=(0, 0, 0, 1))
        floatlayout.add_widget(label_time)

        label_choose_time = Label(text="Введите время:",
                                  size_hint=(0.48, 0.1),
                                  pos_hint={'center_x': 0.25, 'center_y': 0.3},
                                  color=(0, 0, 0, 1))
        floatlayout.add_widget(label_choose_time)

        time = open("time.txt", encoding="utf-8").read()                               ###### Путь до файла с временем!!!!!! ########

        self.time_input = TextInput(text=time,
                                    size_hint=(0.48, 0.1),
                                    pos_hint={'center_x': 0.75, 'center_y': 0.3})
        floatlayout.add_widget(self.time_input)

        button_save = Button(text="Сохранить",
                             size_hint=(0.3, 0.17),
                             pos_hint={'center_x': 0.5, 'center_y': 0.11},
                             background_color=(255/255, 255/255, 51/255, 1))
        button_save.bind(on_press=app.save_email)
        floatlayout.add_widget(button_save)

        Window.clearcolor = (255/255, 255/255, 204/255, 1)

        return floatlayout


    def save_email(self, instance):                              #Сохраняем email в текстовый файл

        global time_input
        new_time = self.time_input.text
        check1 =""

        if (":" in new_time and len(new_time) == 5) or (":" in new_time and "," in new_time and (len(new_time) - new_time.count(",") - new_time.count(" ")) % 5 == 0):
            new_time = new_time.replace(" ", "")
            write_new_time = open("time.txt", "w").write(new_time)          # Путь до файла!!!!!
            subprocess.call(["python3", "change_crontab.py", new_time])              # Путь до проги!!!!!!!!!!!!!
        else:
            easygui.msgbox("Ошибка в значение времени!", "Неправильно введено время")
            check1 = "error"

        global email_input
        new_email = self.email_input.text

        check2 = ""
        rus_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        for i in new_email:                                     #Проверка на наличие русских букв в email
            if i in rus_alphabet:
                check2 = "error"
        if check2 != "error" and check1 != "error":
            if "@" in new_email and new_email[-1] != "@":                   #Проверка, чтобы @ не было последним символом
                write_new_email = open("mail.txt", "w").write(new_email)

                success_save = easygui.msgbox('Изменения сохранены.', 'Изменения сохранены')
                if success_save == "OK":
                    sys.exit()                                                      #Выход из приложения при успешном сохранение email
            else:
                check2 = "error"
        if check2 == "error":                                        #Оповешение об ошибке
            error = easygui.msgbox('Проверте правильность введенного адреса электронной почты!\nНе используйте русский алфавит!', 'Ошибка')



if __name__ == '__main__':
    app = MainApp()
    app.run()


