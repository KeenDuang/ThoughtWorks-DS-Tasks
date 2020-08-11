import requests
from io import BytesIO
from PIL import Image
import matplotlib.pyplot as plt

pic = requests.get('https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png')
im = Image.open(BytesIO(pic.content))
plt.imshow(im)
