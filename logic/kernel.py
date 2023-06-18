import os

import cv2
import numpy as np

IMAGE_FOLDER = 'database'
NUM_EIGENVALUES = 10


class Kernel:

    def __init__(self):
        self.transformed_faces = None
        self.eigenfaces = None
        self.mean_face = None
        self.image_names = []

        if not os.path.exists(IMAGE_FOLDER):
            os.mkdir(IMAGE_FOLDER)

    # TODO dodać po rejestracji przez użytkownika
    def compute_eigenfaces(self):
        if len(os.listdir(IMAGE_FOLDER)) == 0:
            return

        feature_vectors = self.load_from_database()
        feature_vectors = np.transpose(feature_vectors)

        self.mean_face = np.mean(feature_vectors, axis=1)

        feature_vectors_subtracted = feature_vectors - np.expand_dims(self.mean_face, axis=1)
        covariance_matrix = np.dot(feature_vectors_subtracted.T, feature_vectors_subtracted)

        eigenvalues, eigenvectors = np.linalg.eigh(covariance_matrix)

        eig_pairs = sorted(zip(eigenvalues, eigenvectors.T), reverse=True)
        _, eigenvectors_sort = zip(*eig_pairs)
        eigenvectors_sort = np.array(eigenvectors_sort)

        self.eigenfaces = np.dot(eigenvectors_sort[:16], feature_vectors_subtracted.T)
        self.transformed_faces = np.dot(self.eigenfaces, feature_vectors_subtracted).T

    def load_from_database(self):
        feature_vectors = []

        for filename in os.listdir(IMAGE_FOLDER):
            file_path = os.path.join(IMAGE_FOLDER, filename)

            image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            feature_vectors.append(image.flatten() / 255.0)
            self.image_names.append(filename)

        return feature_vectors
