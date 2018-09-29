import cv2
import sys
import os
import numpy as np

# Получить значения
imagePath = 'images/input_imgs/Z/'
output = 'images/output_imgs/Z/'
cascPath = "haarcascade_frontalface_default.xml" # Были заменены устаревшик классы, так как основному проекту около 4 лет.
# Были изменены способы импорта фото. Василь. За основу были выбраны два проекта и оба не работающие, соединил и решил проблемы. Снова Василь.
counter = 1
num_input_images = 1
# Создание каскада
faceCascade = cv2.CascadeClassifier(cascPath)


for i in range(1, 3): #Тут нужно добавить число загружаемых фоток если 2 то 1:3 3 - 1:4 и т.д.
    img_path = imagePath + '2' +str(i)+ '.jpg'
    img = cv2.imread(img_path)
    # Чтение изображения

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Обнаружение лиц на изображении
    faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE)


    for (x,y,w,h) in faces: #Цикл для разрезки лиц
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        sub_face = img[y:y+h, x:x+w]
        face_file_name = output + "z" + str(counter) + ".JPG"
        counter += 1
        cv2.imwrite(face_file_name, sub_face, [int(cv2.IMWRITE_JPEG_QUALITY), 90])

    counter+=10 #Отделяет загружаемые фото от других фото значением +10





