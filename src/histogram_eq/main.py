# pillow
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

width, height = 0, 0
histogram_amount = np.zeros(256)
histogram_amount_result = np.zeros(256)
cumulative_histogram = np.zeros(256)


# convert grayscale  image of original image
def rgb2gray(image):
    global histogram_amount
    grayscale_image = Image.new(mode = 'L', size = (width, height)) 
    for i in range(height):
        for j in range(width):
            pix_val = image.getpixel((j,i))
            # print(pix_val)
            # gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
            temp = int(pix_val[0] * 0.2989 + pix_val[1] * 0.5870 + pix_val[2] * 0.1140)
            grayscale_image.putpixel((j, i), temp)
            histogram_amount[temp] += 1
    return grayscale_image



def step_1(image):
    global width, height
    # get image size
    width, height = image.size
    grayscale_image = rgb2gray(image=image)
    grayscale_image.save("assets/grayscale.png")
    return grayscale_image


def step_2():
    global histogram_amount
    x = np.arange(0, 256)
    plt.bar(x,histogram_amount) 
    plt.savefig('assets/histogram.jpg')

def step_3():
    global histogram_amount,cumulative_histogram
    cumulative_histogram = np.cumsum(histogram_amount)

def step_4_5(grayscale_image):
    global histogram_amount,cumulative_histogram,histogram_amount_result,width,height
    result_image = Image.new(mode = 'L', size = (width, height)) 
    for c in range(len(cumulative_histogram)):
        histogram_amount_result[c] = int(round((255*(cumulative_histogram[c])/(width*height))))
    
    # print("-----------gray-----------")
    for i in range(height):
        for j in range(width):
            pix_val = grayscale_image.getpixel((j,i))
            result_image.putpixel((j, i),int(histogram_amount_result[pix_val]))
    result_image.save("assets/final_result.png")


if __name__ == '__main__':
    img_location = input("Enter your image : ")
    image = Image.open(img_location)
    grayscale_image = step_1(image)
    step_2()
    step_3()
    step_4_5(grayscale_image)
    

### assets/image.png