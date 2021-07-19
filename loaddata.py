import os
import cv2
import random
import matplotlib.pyplot  as plt

directory = r'C:\Users\youss\desktop\newdata'
current_directory = r'C:\Users\youss\PycharmProjects\age-extraction\data\\'
new_directory = r'C:\Users\youss\PycharmProjects\age-extraction\newdata\\'


def resize_data():
    data = []
    for folder in os.listdir(current_directory):  # looping on the folders (from 0 to 9)
        for img in os.listdir(current_directory + folder):
            label = int(img.split('_')[2].split('.')[0]) - int(img.split('_')[1].split('-')[0])
            path = os.path.join(current_directory, folder, img)
            path_processed = r'' + str(path)
            img_data = cv2.imread(path_processed)
            img_data = cv2.resize(img_data, (100, 100))
            os.chdir(directory)

            cv2.imwrite(str(label) + '_' + str(img.split('_')[0]) + '.jpg', img_data)


def load_data():
    data = []
    label = []
    for img in os.listdir(new_directory):
        current_img = cv2.imread(os.path.join(new_directory, img))
        data.append(current_img)
        label.append(int(img.split('_')[0]))
    both = list(zip(data, label))  # join both arrays together
    random.shuffle(both)  # shuffle
    b: object
    a, b = zip(*both)  # disconnect them from each other

    return a, b  # return the data and label array.




