from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
import easygui
import subprocess



class MainApp(App):

    def build(self):                                            #Главное окно приложения

        floatlayout = FloatLayout()

        remove_text = "Это программа для удаления базы данных.\n" \
                      "Базы данных будет полностью удалена!"

        remove_label = Label(text=remove_text,
                             size_hint=(0.5, 0.5),
                             pos_hint={'center_x': 0.5, 'center_y': 0.6},
                             halign="center",
                             font_size=22,
                             color=(0, 0, 0, 1))
        floatlayout.add_widget(remove_label)

        remove_button = Button(text="Стереть базу данных",
                               size_hint=(0.3, 0.17),
                               pos_hint={'center_x': 0.5, 'center_y': 0.3},
                               background_color=(255/255, 255/255, 51/255, 1))
        remove_button.bind(on_press=app.delete_database)
        floatlayout.add_widget(remove_button)

        Window.clearcolor = (255/255, 255/255, 204/255, 1)                          #Цвет фона

        return floatlayout


    def delete_database(self, instance):

        answer = easygui.ccbox(msg="При нажатиии кнопки 'Continue' база данных будет удалена!", title="Продолжить?", choices=('Continue', 'Cancel'))

        if answer == True:
            subprocess.call(["python3", "create_dataset.py"])                   # Путь до проги!!!!!!!!!!!

            easygui.msgbox("База данных удалена.", "База данных удалена")



if __name__ == '__main__':
    app = MainApp()
    app.run()
