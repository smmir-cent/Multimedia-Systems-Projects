import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import fftpack
import huffman
import pickle

height = 1
width = 1280
row = np.zeros((height,width,3), np.uint8)
row[:,:,[0,1,2]] = 255
ycrcb_black_row = cv2.cvtColor(row, cv2.COLOR_RGB2YCrCb)


def dct2(a):
    return scipy.fftpack.dct( scipy.fftpack.dct( a, axis=0, norm='ortho' ), axis=1, norm='ortho' )

def idct2(a):
    return scipy.fftpack.idct( scipy.fftpack.idct( a, axis=0 , norm='ortho'), axis=1 , norm='ortho')


def _to_Bytes(data):
  b = bytearray()
  for i in range(0, len(data), 8):
    b.append(int(data[i:i+8], 2))
  return bytes(b)




if __name__ == '__main__':
    B = 8 # blocksize (In Jpeg the
    img=cv2.imread("assets/photo1.png")
    # print(img.shape)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # plt.imshow(img, interpolation='nearest')
    ycrcb_img = cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb)
    # plt.imshow(rgb_img, interpolation='nearest')
    # plt.imshow(ycrcb_img, interpolation='nearest')
    ycrcb_img_subsampled = ycrcb_img.copy()
    for i in range(853,856):
      ycrcb_img_subsampled = np.vstack((ycrcb_img_subsampled,row))

    # print(ycrcb_img_subsampled.shape)
    # print(ycrcb_img[::0].shape)
    y,cr,cb = np.moveaxis(ycrcb_img_subsampled, -1, 0)
    # subsampling 
    cr[1::2, :] = cr[::2, :] 
    cr[:, 1::2] = cr[:, ::2] 
    cb[1::2, :] = cb[::2, :] 
    cb[:, 1::2] = cb[:, ::2]
    # plt.imshow(ycrcb_img_subsampled, interpolation='nearest')
    # mew = cv2.merge([y,cr,cb])
    # plt.imshow(mew, interpolation='nearest')

    # for i in range(0,8,856):
    #   for j in range(0,8,1280):


    imsize = (856,1280)
    dct_y = np.zeros(imsize)
    dct_cr = np.zeros(imsize)
    dct_cb = np.zeros(imsize)

    # Do 8x8 DCT on image (in-place)
    for i in range(0,856,8):
        for j in range(0,1280,8):
            dct_y[i:(i+8),j:(j+8)] = dct2( y[i:(i+8),j:(j+8)] )
            dct_cr[i:(i+8),j:(j+8)] = dct2( cr[i:(i+8),j:(j+8)] )
            dct_cb[i:(i+8),j:(j+8)] = dct2( cb[i:(i+8),j:(j+8)] )
            # print("*")

    QY=np.array([[16,11,10,16,24,40,51,61],
                            [12,12,14,19,26,48,60,55],
                            [14,13,16,24,40,57,69,56],
                            [14,17,22,29,51,87,80,62],
                            [18,22,37,56,68,109,103,77],
                            [24,35,55,64,81,104,113,92],
                            [49,64,78,87,103,121,120,101],
                            [72,92,95,98,112,100,103,99]])

    QC=np.array([[17,18,24,47,99,99,99,99],
                            [18,21,26,66,99,99,99,99],
                            [24,26,56,99,99,99,99,99],
                            [47,66,99,99,99,99,99,99],
                            [99,99,99,99,99,99,99,99],
                            [99,99,99,99,99,99,99,99],
                            [99,99,99,99,99,99,99,99],
                            [99,99,99,99,99,99,99,99]])

    f_hat_y = np.zeros(imsize)
    f_hat_cr = np.zeros(imsize)
    f_hat_cb = np.zeros(imsize)
    for i in range(0,856,8):
        for j in range(0,1280,8):
          for i2 in range(0,8):
            for j2 in range(0,8):
              f_hat_y[i+i2,j+j2] = np.round(dct_y[i+i2,j+j2]/QY[i2,j2])
              f_hat_cr[i+i2,j+j2] = np.round(dct_cr[i+i2,j+j2]/QC[i2,j2])
              f_hat_cb[i+i2,j+j2] = np.round(dct_cb[i+i2,j+j2]/QC[i2,j2])

    # print(f_hat_y.shape)
    # print(f_hat_cr.shape)
    # print(f_hat_cb.shape)
    y_huff_trees = []
    cr_huff_trees = []
    cb_huff_trees = []
    y_huff_values = ''
    cr_huff_values = ''
    cb_huff_values = ''         
    for i in range(0,856,8):
        for j in range(0,1280,8):
          y_freq = {}
          cr_freq = {}
          cb_freq = {}
          y_huff = {}
          cr_huff = {}
          cb_huff = {}                    
          for i2 in range(0,8):
            for j2 in range(0,8):          
              y_freq[f_hat_y[i+i2,j+j2]] = y_freq.get(f_hat_y[i+i2,j+j2],0) + 1
              cr_freq[f_hat_cr[i+i2,j+j2]] = cr_freq.get(f_hat_cr[i+i2,j+j2],0) + 1
              cb_freq[f_hat_cb[i+i2,j+j2]] = cb_freq.get(f_hat_cb[i+i2,j+j2],0) + 1              
          huffman.huff(list(y_freq.keys()),list(y_freq.values()),y_huff)
          huffman.huff(list(cr_freq.keys()),list(cr_freq.values()),cr_huff)
          huffman.huff(list(cb_freq.keys()),list(cb_freq.values()),cb_huff)
          y_huff_trees.append(y_huff)
          cr_huff_trees.append(cr_huff)
          cb_huff_trees.append(cb_huff)
          for key in y_freq.keys():
            for counter in range(y_freq[key]):
              y_huff_values += y_huff[key]

          for key in cr_freq.keys():
            for counter in range(cr_freq[key]):
              cr_huff_values += cr_huff[key]

          for key in cb_freq.keys():
            for counter in range(cb_freq[key]):
              cb_huff_values += cb_huff[key]     
    with open("compressed.bin", "wb") as f:
      pickle.dump(y_huff_trees, open("compressed.bin", "wb"))         
      pickle.dump(cr_huff_trees, open("compressed.bin", "wb"))         
      pickle.dump(cb_huff_trees, open("compressed.bin", "wb"))         
      pickle.dump(y_huff_values, open("compressed.bin", "wb"))         
      pickle.dump(cr_huff_values, open("compressed.bin", "wb"))         
      pickle.dump(cb_huff_values, open("compressed.bin", "wb"))         
