import sys
import os
import subprocess

file_name_1 = sys.argv[1]                   #Получаем путь до файлов
file_name_2 = sys.argv[2]

os.remove(file_name_1)                      #Удаляем файлы
os.remove(file_name_2)

images_path = "\unknown_people\\"                      # Путь до директории!!!!!!!!!
if len(os.listdir(images_path)):                        # Если есть фото неопознанных людей, их тоже удаляем
    list_of_images = os.listdir(images_path)
    for i in range(len(list_of_images)):
        os.remove(images_path + list_of_images[i])

subprocess.run(["python3", "table_creator.py"])                 #Запускаем программу для создания новых файлов
# Даписать путь до проги

##### Данная программа получает на вход пути до файлов и удаляет их.
##### Данная программа запускается программой отправки email после успешной отправки!!!!!!
##### Данная программа запускает программу, которая создает новые шаблоны отчетов вместо удаленных!!!!



