import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email import encoders
import os
from datetime import datetime
import subprocess
import time


date = datetime.now().date()                                        # Получаем текущую дату

address_from = "monitoring.posetiteley@ mail.ru"                     # Адрес для отправки
address_to = open("mail.txt", encoding="utf-8").read()              # Указать путь до файла с почтой!!!!!!!!
password = "supersecretpassword!"

message = MIMEMultipart()                                           # Создаем заготовку письма
message["From"] = address_from
message["To"] = address_to
message["Subject"] = "Отчет за " + str(date)

text = "Отчет о посетителях в помещение."                            # Текст в письме
message.attach(MIMEText(text))                                      # Добавляем текст в письмо

way_to_exel = "report.xlsx"                                            # Указать путь до файла, который отправляем!!!!!!!!
basename = os.path.basename(way_to_exel)

part_exel = MIMEBase('application', "octet-stream")
part_exel.set_payload(open(way_to_exel, "rb").read())
encoders.encode_base64(part_exel)
part_exel.add_header('Content-Disposition', 'attachment; filename="%s"' % basename)
message.attach(part_exel)                                                                    # Добавляем файл в письмо

way_to_csv = "report.csv"                                            # Указать путь до файла, который отправляем!!!!!!!!
basename = os.path.basename(way_to_csv)

part_csv = MIMEBase('application', "octet-stream")
part_csv.set_payload(open(way_to_csv, "rb").read())
encoders.encode_base64(part_csv)
part_csv.add_header('Content-Disposition', 'attachment; filename="%s"' % basename)
message.attach(part_csv)                                                                    # Добавляем файл в письмо


# Прикрепляем фото неопознаных людей, если они были
directory_whith_images = "\unknown_people\\"                             # Указать путь до директории!!!!!!!!!!!!!

if len(os.listdir(directory_whith_images)):                                       # Если там есть фотографии!!!!!!!!
    list_images = os.listdir(directory_whith_images)

    text_with_images = "\nСобраны фото неопознанных людей!"                            # Текст в письме, если есть неопознанные люди
    message.attach(MIMEText(text_with_images))                                       # Добавляем текст в письмо

    for i in range(len(list_images)):                                             # Перебирает фото по очереди
        image_name = list_images[i]
        way_to_image = directory_whith_images + image_name
        file_type = image_name[image_name.rfind(".") + 1 : ]                      # Определяем расширение файла
        image = MIMEImage(open(way_to_image, "rb").read(), file_type)
        image.add_header('Content-Disposition', 'attachment', filename=image_name)               # Добавляем заголовки
        message.attach(image)                                                                    # Добавляем фото в письмо


check = ""                                          # Для подтверждения отправки
while check != "ready":

    try:                                                               # На случай отсутствия интернета
        server = smtplib.SMTP_SSL("smtp.mail.ru:465")                                   # Подключаемся к серверу
        server.login(address_from, password)                                            # Логинимся на сервере
        server.sendmail(address_from, address_to, message.as_string())                  # Отправляем письмо
        server.quit()                                                                   # Закрываем подключение к серверу

        # Запускаем программу для удавления отправленных файлов
        subprocess.run(["python3", "remove.py", way_to_exel, way_to_csv])           # Путь до проги дописать!!!!

        check = "ready"                              # Подтверждение отправки

    except:                                          # Если отсутствовал интернет
        time.sleep(300)                              # Повторная попытка отправки через 5 минут


###### Данная программа отправляет email с отчетом и, при успешной отправке, запускает программу, которая удаляет отправленные файлы ######




