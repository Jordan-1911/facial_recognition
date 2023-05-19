import cv2
import pathlib


# cascade paths should be provided within CV2
cascade_path = pathlib.Path(cv2.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"
print(cascade_path)