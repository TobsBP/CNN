import cv2
import numpy as np
from skimage.feature import hog
from PIL import Image
import joblib
import sys
import os

def resource_path(path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, path)
    return path


# carregar modelo HOG+SVM
model_path = resource_path("number_model.pkl")
model = joblib.load(model_path)

def predict_frame(frame):
    # converter para PIL
    img = Image.fromarray(frame).convert("L").resize((128, 128))
    arr = np.array(img)

    # extrair HOG
    feat = hog(arr, pixels_per_cell=(16, 16), cells_per_block=(2, 2))

    # prever classe (1,2,3,4)
    pred = model.predict([feat])[0]

    return str(pred)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    digit = predict_frame(frame)
    print("Detectado:", digit)

    with open("resultado.txt", "w") as f:
        f.write(digit)

    cv2.putText(frame, f"Num: {digit}", (10,40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.imshow("Cam", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
