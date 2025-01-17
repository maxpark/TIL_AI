import numpy as np
import keras

from keras.datasets import mnist
from keras import layers
from keras import models
from keras.utils import to_categorical

(train_images, train_labels),(test_images, test_labels) = mnist.load_data()

print(train_images.shape,test_images.shape,train_labels.shape,test_labels.shape)

network = models.Sequential()
network.add(layers.Dense(512, activation='relu',input_shape=(28 * 28,)))
network.add(layers.Dense(10,activation='softmax'))

train_images = train_images.reshape((60000, 28 * 28))

train_images = train_images.astype('float32')/ 255.

test_images = test_images.reshape((10000, 28 * 28))

test_images = test_images.astype('float32')/ 255.

train_labels = to_categorical(train_labels)

test_labels = to_categorical(test_labels)

network.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

network.fit(train_images,train_labels,batch_size=32,epochs=1)
test_loss, test_acc = network.evaluate(test_images, test_labels)
print('test loss : {}, test accuracy : {} '.format(test_loss, test_acc))