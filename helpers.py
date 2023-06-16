import os.path
import shutil
import matplotlib
import numpy as np
import matplotlib.pyplot as plt


class Helper:
    def generate_images(self):
        # utworzenie folderu ze zdjęciami
        if not os.path.exists('faces'):
            os.mkdir('faces')

        matplotlib.use('TkAgg')

        # pobranie danych z pliku
        data = np.load("olivetti_faces.npy")

        j = 0
        parent_dir = ""
        for i in range(len(data)):
            # utworzenie nowego folderu (1 folder = 1 osoba)
            if j == 0:
                parent_dir = os.path.join("faces", 'person_' + (i // 10).__str__())

                # jeśli folder istnieje, zotaje usunięty i stworzony na nowo
                if os.path.exists(parent_dir):
                    shutil.rmtree(parent_dir)
                os.mkdir(parent_dir)

            # dodanie zdjęcia do folderu
            plt.figure()
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

        print("Images generated successfuly")
