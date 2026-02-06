from PIL import Image
import numpy as np
from skimage.feature import hog
from sklearn.svm import LinearSVC
import joblib
import os

dataset_dir = "dataset"  # pasta com suas imagens aumentadas

X = []
y = []

for label_name in os.listdir(dataset_dir):
    label_path = os.path.join(dataset_dir, label_name)
    if not os.path.isdir(label_path):
        continue

    label = int(label_name)

    for fname in os.listdir(label_path):
        if not fname.endswith(".jpeg"):
            continue

        img = Image.open(os.path.join(label_path, fname)).convert("L").resize((128, 128))
        arr = np.array(img)

        feat = hog(arr, pixels_per_cell=(16, 16), cells_per_block=(2, 2))
        X.append(feat)
        y.append(label)

model = LinearSVC()
model.fit(X, y)

joblib.dump(model, "number_model.pkl")
print("Modelo salvo: number_model.pkl")
