import sys
import face_recognition
import pickle
import cv2
import os
from datetime import date
import subprocess
from PIL import Image, ImageDraw, ImageFont

cascPathface = os.path.dirname(cv2.__file__) + "/data/haarcascade_frontalface_alt2.xml"
faceCascade = cv2.CascadeClassifier(cascPathface)

path_with_embeddings = "dataset"                       # Путь до директории c датасетами!!!!!!!!
data = pickle.loads(open(path_with_embeddings, "rb").read())                  # Загружаем известные нам эмбеддинги

way_to_image = sys.argv[1]                                         # Получаем путь до фотографии, которую обрабатываем

image = cv2.imread(way_to_image)                                # Открываем фото
bgr_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

faces = faceCascade.detectMultiScale(bgr_image,
                                     scaleFactor=1.1,
                                     minNeighbors=5,
                                     minSize=(30, 30),
                                     flags=cv2.CASCADE_SCALE_IMAGE)
    
encodings = face_recognition.face_encodings(bgr_image)              # Находим эмбеддинги для лица с фото
names = []                                                  # Список неопознанных людей на фото
                                                  # Список опознанных людей на фото

for encoding in encodings:                                          # Для каждого найденного лица
    name = "unknown"                                        # Если не будет опознан, то unknown

    matches = face_recognition.compare_faces(data["faces"], encoding)           # Ищем совпадения

    if True in matches:                                                 # Если нашлось совпадение
        matchedIdxs = [i for (i, b) in enumerate(matches) if b]             # Находим с чем конкретно совпало
        counts = {}                                                     # Будем считать количество совпадений по каждому имени

        for i in matchedIdxs:                           # Для каждого совпадения
            name = data["names"][i]                 # Находим имя, с кем совпало
            counts[name] = counts.get(name, 0) + 1      # Записываем совпадение
            name = max(counts, key=counts.get)          # Выбираем имя, с которым было больше всего совпадений

        names.append(name)                          # Добавляем в список людей, которые есть на фото

    if name == "unknown":                               # Если обнаружен неизвестный, то выделяем его лицо на фото
        names.append(name)                                  # Для этого подтвердим, что он unknown

if "unknown" in names:                              # Если были неопознанные люди, то сохраняем фото с ними
    time = way_to_image[ : way_to_image.rfind(".")]             # Получаем время из имени файла, который обрабатываем
    time = time[time.rfind("_") + 1 : ]
    name_for_image = "unknown_people\\" + time + ".jpg"      # Путь сохранения!!!!!!!!

    isWritten = cv2.imwrite(name_for_image, image)              # Сохраняем фото, так как для добавления надписи нужно открыть по-другому

    image_again = Image.open(name_for_image)                    # Открываем это же фото
    image_white = Image.open("white.jpg")               # Открываем белое фото для добавления места для подписи !!!!!Путь!!!!!!

    image_with_white = Image.new('RGB', (image_again.width, (image_again.height + 300)))         # Основа для фото с белым полем
    image_with_white.paste(image_again, (0, 0))                                 # Вставляем фото в основу
    image_with_white.paste(image_white, (0, image_again.height))

    font = ImageFont.truetype("arial.ttf", 15)                          # Задаем шрифт и размер
    drawer = ImageDraw.Draw(image_with_white)

    known_names = ""                                # Будем выводить известные имена
    count_unknown = 0                               # И количество неопознанных людей
    for i in range(len(names)):
        if names[i] != "unknown":
            known_names = known_names + names[i] + "\n"
        else:
            count_unknown += 1

    show_text = "Обнаружено людей: " + str(len(names)) + "\n" + known_names + "\n" + "Неопознанных людей: " + str(count_unknown)
    drawer.text((25, (image_again.height + 25)), show_text, font=font, fill='black')                     # Помещаем текст на картинку

    image_with_white.save(name_for_image)                    # Сохраняем с тем же именем

for i in range(len(names)):                                 # Будем заносить всех известных людей в отчет
    if names[i] != "unknown":
        if "_" in names[i]:                                     # Если есть доп инфа о человеке
            person_name = names[i][ : names[i].find("_")]               # Отделяем имя от доп инфы
            person_dop = names[i][names[i].find("_") + 1 : ]
            time = way_to_image[ : way_to_image.rfind(".")]             # Получаем время из имени файла, который обрабатываем
            time = time[time.rfind("_") + 1 : ]
            time = time.replace(",", ":")
            date_today = str(date.today())                                # Добавляенм дату
            date_time = date_today + "/" + time
        else:                                                   # Если нет доп инфы
            person_name = names[i]
            person_dop = ""
            time = way_to_image[ : way_to_image.rfind(".")]             # Получаем время из имени файла, который обрабатываем
            time = time[time.rfind("_") + 1 : ]
            time = time.replace(",", ":")
            date_today = str(date.today())                                # Добавляенм дату
            date_time = date_today + "/" + time

        subprocess.run(["python3", "writer.py", person_name, person_dop, date_time])            # Запускаем прогу для занесения данных в отчет


os.remove(way_to_image)                         # Удаляем обработанное фото

# cv2.imshow("Frame", image)               # Для вывода картинки на экран
# cv2.waitKey(0)


#### Данна программа получает на вход путь до фотографии, людей на которой нужно опознать
#### После завершения работы с фото, оно будет удалено
#### Если были найдены люди, которых нет в базе, то фото с ними сохраниться




