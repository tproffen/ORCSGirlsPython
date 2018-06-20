import csv
import json
import numpy as np
import matplotlib.pyplot as plt


def plot_image(data, labels, im_idx=0):
    im = data[im_idx, :]

    im_r = im[0:1024].reshape(32, 32)
    im_g = im[1024:2048].reshape(32, 32)
    im_b = im[2048:].reshape(32, 32)

    img = np.dstack((im_r, im_g, im_b))

    print("label: ", labels[im_idx])       

    plt.imshow(img) 
    plt.show()
    
    
def load_cat_data():
    labels = []
    data = []
    with open('Data/Cats.csv') as fp:
        reader = csv.reader(fp)
        for row in reader:
            labels.append(row[0])
            data.append(json.loads(row[1]))
    return np.array(data, dtype='uint8'), np.array(labels)
