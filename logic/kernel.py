import os

import cv2
import numpy as np
from sklearn import preprocessing

IMAGE_FOLDER = 'database'
NUM_EIGENVALUES = 100


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
            return None

        feature_vectors = self.load_from_database()

        self.mean_face = np.mean(feature_vectors, axis=0)
        feature_vectors_subtracted = feature_vectors - self.mean_face
        covariance_matrix = (
                feature_vectors_subtracted.dot(feature_vectors_subtracted.T) / len(feature_vectors_subtracted))
        eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

        eig_pairs = sorted(zip(eigenvalues, eigenvectors.T), reverse=True)
        _, eigenvectors_sort = zip(*eig_pairs)
        eigenvectors_sort = np.array(eigenvectors_sort)[:NUM_EIGENVALUES]

        matrix_eigenvectors = feature_vectors_subtracted.T @ eigenvectors_sort.T

        self.eigenfaces = preprocessing.normalize(matrix_eigenvectors.T)
        self.transformed_faces = np.dot(self.eigenfaces, feature_vectors_subtracted.T).T

        temp_norms = []
        for i in self.transformed_faces:
            for j in self.transformed_faces:
                temp_norms.append(np.linalg.norm(i - j))

        self.theta = max(temp_norms) / 4

    def login(self, image_path):
        if len(os.listdir(IMAGE_FOLDER)) == 0:
            return

        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        image_vector = image.flatten() / 255.0

        subtracted_vector = image_vector - self.mean_face
        projected_vector = np.dot(self.eigenfaces, subtracted_vector)

        epsilon = []
        for face in self.transformed_faces:
            epsilon.append(np.linalg.norm(projected_vector - face))

        if min(epsilon) < self.theta:
            return self.image_names[np.argmin(epsilon)].replace('_', ' ')
        else:
            return None

    def load_from_database(self):
        feature_vectors = []
        image_names = []

        for filename in os.listdir(IMAGE_FOLDER):
            file_path = os.path.join(IMAGE_FOLDER, filename)

            image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            feature_vectors.append(image.flatten() / 255.0)
            username = filename.split("_")[:-1]
            image_names.append("_".join(username))

        self.image_names = image_names
        return feature_vectors
