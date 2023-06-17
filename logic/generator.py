import os.path
import shutil

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def generate():
    if not os.path.exists('generated_faces'):
        os.mkdir('generated_faces')

    matplotlib.use('TkAgg')

    data = np.load("olivetti_faces.npy")

    j = 0
    parent_dir = ""
    for i in range(len(data)):
        if j == 0:
            parent_dir = os.path.join("generated_faces", 'person_' + (i // 10).__str__())
            if os.path.exists(parent_dir):
                shutil.rmtree(parent_dir)
            os.mkdir(parent_dir)

        plt.figure(figsize=(0.64, 0.64))
        plt.axis('off')
        plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
        plt.imshow(data[i], cmap='gray')
        file_name = parent_dir + "/face_" + j.__str__() + ".png"
        plt.savefig(file_name, bbox_inches='tight', pad_inches=0)
        plt.close()

        if j == 9:
            j = 0
        else:
            j += 1

    print("Images generated successfully")
