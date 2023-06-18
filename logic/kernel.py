import os

import cv2
import numpy as np

IMAGE_FOLDER = 'database'
NUM_EIGENVALUES = 90


class Kernel:

    def __init__(self):
        self.theta = None
        self.transformed_faces = None
        self.eigenfaces = None
        self.mean_face = None
        self.image_names = []

        if not os.path.exists(IMAGE_FOLDER):
            os.mkdir(IMAGE_FOLDER)

    def compute_eigenfaces(self):
        if len(os.listdir(IMAGE_FOLDER)) == 0:
            return

        feature_vectors = self.load_from_database()

        from sklearn.decomposition import PCA
        pca = PCA(n_components=4)
        pca.fit(feature_vectors)

        print(pca.explained_variance_)


        # feature_vectors = np.transpose(feature_vectors)

        self.mean_face = np.mean(feature_vectors, axis=0)



        feature_vectors_subtracted = feature_vectors - np.expand_dims(self.mean_face, axis=0)

        # print(feature_vectors_subtracted)
        # covariance_matrix = np.dot(feature_vectors_subtracted.T, feature_vectors_subtracted)
        #
        # eigenvalues, eigenvectors = np.linalg.eigh(covariance_matrix)
        # print(eigenvalues)
        #
        # eig_pairs = sorted(zip(eigenvalues, eigenvectors.T), reverse=True)
        # _, eigenvectors_sort = zip(*eig_pairs)
        # eigenvectors_sort = np.array(eigenvectors_sort)
        #
        # self.eigenfaces = np.dot(eigenvectors_sort[:NUM_EIGENVALUES], feature_vectors_subtracted.T)
        # self.transformed_faces = np.dot(self.eigenfaces, feature_vectors_subtracted).T

        self.eigenfaces = pca.components_
        self.transformed_faces = np.dot(self.eigenfaces, feature_vectors_subtracted.T)

        # print(feature_vectors_subtracted.shape)
        # print(self.eigenfaces.shape)
        # print(self.transformed_faces.shape)
        # print(self.transformed_faces)
        #
        # normalized_matrix = cv2.normalize(self.eigenfaces[3].reshape(64, 64), None, 0, 255, cv2.NORM_MINMAX,
        #                                   dtype=cv2.CV_8U)
        # cv2.imwrite('test.png', normalized_matrix)

        temp_norms = []
        for i in self.transformed_faces:
            for j in self.transformed_faces:
                temp_norms.append(np.linalg.norm(i - j))

        self.theta = max(temp_norms) / 2
        print("theta: " + str(self.theta))



        print()


        # print(pca.components_[0])
        # print(self.eigenfaces[0])
        # print()
        # print(pca.components_[1])
        # print(self.eigenfaces[1])
        # print()
        # print(pca.components_[2])
        # print(self.eigenfaces[2])
        # print()
        # print(pca.components_[3])
        # print(self.eigenfaces[3])

        # X_pca = pca.transform(feature_vectors)

    def login(self, image_path):
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        image_vector = image.flatten() / 255.0

        subtracted_vector = image_vector - self.mean_face
        projected_vector = np.dot(self.eigenfaces, subtracted_vector)

        epsilon = []
        for face in self.transformed_faces:
            epsilon.append(np.linalg.norm(projected_vector - face))

        print("epsilon: " + str(min(epsilon)))

        reconstructed_face = np.dot(self.eigenfaces.T, projected_vector)
        ksi = np.linalg.norm(subtracted_vector - reconstructed_face)

        print("ksi: " + str(ksi))

        normalized_matrix = cv2.normalize(reconstructed_face.reshape(64, 64), None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        cv2.imwrite('test.png', normalized_matrix)

        if ksi >= self.theta:
            print("This is not a face")
        else:
            new = False
            for i in epsilon:
                if i >= self.theta:
                    print("Nowa twarz")
                    new = True
                    break

            if not new:
                if min(epsilon) < self.theta:
                    print("Znana twarz")
                else:
                    print("Ani nowe ani stare")


    def load_from_database(self):
        feature_vectors = []

        for filename in os.listdir(IMAGE_FOLDER):
            file_path = os.path.join(IMAGE_FOLDER, filename)

            image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            feature_vectors.append(image.flatten() / 255.0)
            self.image_names.append(filename)

        return feature_vectors
