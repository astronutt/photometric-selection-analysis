import numpy as np
import tensorflow as tf
import random
import glob
import PIL
from PIL import Image

#PERCEPTRON ALGORITHM

good_pics = glob.glob('./PNGS_GOOD/*.png')
bad_pics = glob.glob('./PNGS_BAD/*.png')

pics = []
labels = []

for file in good_pics:
    img = Image.open(file)
    pics.append(np.array(np.asarray(img)/127.5 - 1))
    labels.append(np.array([1])) #1 MEANS GOOD IRAC!

for file in bad_pics:
    img = Image.open(file)
    pics.append(np.array(np.asarray(img)/127.5 - 1))
    labels.append(np.array([0])) #0 MEANS BAD IRAC!

pics = np.array(pics)
labels = np.array(labels)

model = tf.keras.Sequential([tf.keras.layers.Flatten(input_shape = (16, 16)),
                             tf.keras.layers.Dense(128, activation = 'relu'),
                             tf.keras.layers.Dense(1, activation = 'sigmoid')])

model.compile(optimizer='adam',
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(pics, labels, epochs = 25)

test_img='./PNGS_GOOD/550goodc2.png'
test_img = Image.open(test_img)
test_img = np.array([np.array(np.asarray(test_img)/127.5 - 1)])

answer = model.predict(test_img)

print(answer)

if (1-answer) > (answer):
    print('bad IRAC')
else:
    print('good IRAC')

'''
pictures_test = np.array(random.sample(pictures, len(pictures)//5))
quality_test = np.array(random.sample(quality, len(quality)//5))

pictures = np.array(random.sample(pictures, int(len(pictures)*0.8)))
quality = np.array(random.sample(quality, int(len(quality)*0.8)))
'''