import os.path
import shutil

import cv2
import numpy as np


def generate():
    if not os.path.exists('generated_faces'):
        os.mkdir('generated_faces')

    data = np.load("olivetti_faces.npy")

    j = 0
    parent_dir = ""
    for i in range(len(data)):
        if j == 0:
            parent_dir = os.path.join("generated_faces", 'person_' + (i // 10).__str__())
            if os.path.exists(parent_dir):
                shutil.rmtree(parent_dir)
            os.mkdir(parent_dir)

        file_name = parent_dir + "/face_" + j.__str__() + ".png"

        normalized_matrix = cv2.normalize(data[i], None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        cv2.imwrite(file_name, normalized_matrix)

        if j == 9:
            j = 0
        else:
            j += 1

    print("Images generated successfully")
