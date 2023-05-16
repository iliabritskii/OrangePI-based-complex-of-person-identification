import pandas as pd
import sys


name = sys.argv[1]                          # Получаем данные на вход программы
dop = sys.argv[2]
enter_time = sys.argv[3]

table_exel = pd.read_excel("report.xlsx")                       # Открываем таблицы для редактирования
table_csv = pd.read_csv("report.csv")

new_line = pd.DataFrame({"ФИО": [name], "Дополнительная информация": [dop], "Время входа": [enter_time]})           # Создаем новую строку для таблицы

table_exel = pd.concat([table_exel, new_line])                  # Добавляем новую строку в таблицы
table_csv = pd.concat([table_csv, new_line])

table_exel.to_excel("report.xlsx", index=False)                          #### Путь до места сохранения!!!!! #####

table_csv.to_csv("report.csv", index=False)                             #### Путь до места сохранения!!!!! #####

###### Данная программа запускается, если вошедщий человек был найден в базе.
###### На вход программа получает значения ФИО, дополнительной информации и время (время сохранения фотографии!!!!!!!)
