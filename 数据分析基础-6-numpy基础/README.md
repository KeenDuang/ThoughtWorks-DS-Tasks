在彩色图像中，一般有3个通道，分别是R、G、B三个通道，每个通道上都有一个相同大小的矩阵，矩阵上的元素取值范围为0～255。 
灰度图像则只有一个通道，即只有一个矩阵，元素取值范围为0～255. 

image_gray.py实现了一个方法，将一张彩色图片转为灰度图片。 
其中，彩色转灰度的方式可以采用平均法，即将R、G、B 3个通道的每个像素点加和取平均。



