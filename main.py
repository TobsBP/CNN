import cv2
import numpy as np
from skimage.feature import hog
from PIL import Image
import joblib

# carregar modelo HOG+SVM
model = joblib.load("number_model.pkl")

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
ultimo_digit = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    key = cv2.waitKey(1) & 0xFF

    if key == ord(" "):
        ultimo_digit = predict_frame(frame)
        print("Detectado:", ultimo_digit)

        with open("resultado.txt", "w") as f:
            f.write(ultimo_digit)

    if ultimo_digit is not None:
        cv2.putText(frame, f"Num: {ultimo_digit}", (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Cam", frame)

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
