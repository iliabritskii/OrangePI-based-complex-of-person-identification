import face_recognition
import pickle
import cv2
import os
import sys

way_to_directory = sys.argv[1]                              # Получаем на вход путь до директории с фотографиями ОДНОГО человека без последнего \
                                                            # Название директории вида ФИО_дополнительная инфа
name_and_dop = way_to_directory[way_to_directory.rfind("\\") + 1 : ]       # Получаем имя в формате ФИО_дополнительная инфа

new_way_to_directory = way_to_directory.replace(way_to_directory[way_to_directory.rfind("\\") + 1 : ], "work_with_images")
os.rename(way_to_directory, new_way_to_directory)                   # Переименовываем директорию, т.к. imread работает только с английскими символами

way_to_images = os.listdir(new_way_to_directory + "\\")                 # Список всех фото в папке
known_faces = []                                        # Сюда будем добавлять полученные эмбеддинги
known_names = []                                        # Здесь будет повторяться одно и то же имя, полученное из имени директории


for i in range(len(way_to_images)):

    way_to_image = new_way_to_directory + "\\" + way_to_images[i]                   # Путь до фотографи

    image = cv2.imread(way_to_image)                            # Не распознает русский!!!!!!!!
    bgr = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    faces = face_recognition.face_locations(bgr, model='hog')               # Находим лица на фото
    encodings = face_recognition.face_encodings(bgr, faces)                 # Вычисляем эмбеддинги

    for encoding in encodings:
        known_faces.append(encoding)
        known_names.append(name_and_dop)

    os.remove(way_to_image)                                 # Удаляем уже обработанное фото

data = {"faces": known_faces, "names": known_names}                 # Создаем датасет из данных для каждой фотографии


last_data = pickle.loads(open("dataset", "rb").read())      # Путь до файла с датасетом!!!!!!

for i in range(len(data["names"])):                         # Будем добавлять к старому словарю новый
    last_data["names"].append(data["names"][i])                     #Добавляем новые значения
    last_data["faces"].append(data["faces"][i])


file = open("dataset", "wb")          # Путь до файла с датасетом!!!!
file.write(pickle.dumps(last_data))                                 # Записываем данные в датасет
file.close()


os.rmdir(new_way_to_directory)                              # Удаляем директорию

#### Данная программа запускается для добавления нового пользователя ( для нескольких перезапуск циклом из другой проги)
#### Запускается для каждого нового человека отдельно!!!!
