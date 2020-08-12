from numpy.core.multiarray import ndarray
import numpy as np
from PIL import Image


def image_gray(image_ar: ndarray) -> ndarray:
    return np.mean(image_array,axis=2)


def read_image(image_path: str) -> ndarray:
    image = Image.open(image_path)
    return np.array(image)


def show_image_array(image_ar: ndarray):
    image = Image.fromarray(image_ar)
    image.show()


if __name__ == "__main__":
    image_array = read_image('image.jpg')
    array = image_gray(image_array)
    show_image_array(array)
