import cv2
import time
from datetime import datetime

face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


cap = cv2.VideoCapture(0)                                                           # Захват видио с камеры

while True:

    success, image = cap.read()                                               # Зачем нужна первая переменная, я не знаю, без нее не работает

    image_bgr = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)                        # Переводим в нужный формат bgr

    faces = face_cascade_db.detectMultiScale(image_bgr,
                                             scaleFactor=1.1,
                                             minNeighbors=5,
                                             minSize=(30, 30),
                                             flags=cv2.CASCADE_SCALE_IMAGE)              ######## Посмотреть параметры и потестить с разными значениями

    # for (x, y, w, h) in faces:
    #     cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)            # Это рисует рамку вокруг лица, нам не нужно

    if len(faces):                                              # Если обнаружено лицо, то ищем ладонь

        date = str(datetime.now().time())                                   # Получаем время для названия файла
        date = date[ : date.rfind(".")]
        date = date.replace(":", ",")
        name_for_image = "\images\image_" + date + ".jpg"      # путь сохранения!!!!!!!!

        isWritten = cv2.imwrite(name_for_image, image)                          # картинка сохраниться, если на ней есть человек

        time.sleep(2)                                           # Чтобы не делать несколько фото одного человека

    # cv2.imshow('detection', image)                            # Это вывод на экран, нам он не нужен

    time.sleep(0.2)                                             # Оставим 5 fps при пустой съемке, чтобы не грузить цп


    if cv2.waitKey(1) & 0xff == 27:                          # Нажать Esc для закрытия
        break

cap.release()
cv2.destroyAllWindows()


##### Данная программа работает постоянно! Должна автоматически запускаться при включение Orange PI!
##### Делает фото человека, который подошел и показал какой-нибудь жест. Должен загораться светодиод при фотографирование!
