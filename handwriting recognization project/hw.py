import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

mnist = tf.keras.datasets.mnist
(X_train, Y_train),(X_test, Y_test) = mnist.load_data()

X_train = tf.keras.utils.normalize(X_train, axis=1)
X_test = tf.keras.utils.normalize(X_test, axis=1)

# model = tf.keras.models.Sequential()
# model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
# model.add(tf.keras.layers.Dense(128, activation='relu'))
# model.add(tf.keras.layers.Dense(128, activation='relu'))
# model.add(tf.keras.layers.Dense(10, activation='softmax'))

# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# model.fit(X_train, Y_train, epochs=3)

model = tf.keras.models.load_model('handwritten.model')

loss, accuracy = model.evaluate(X_test, Y_test)
print(loss)
print(accuracy)

img_no = 1
while os.path.isfile(f"digits/digit{img_no}.png"):
    try:
        img = cv2.imread(f"digits/digit{img_no}.png")[:,:,0]
        img = np.invert(np.array([img]))
        pred = model.predict(img)
        print(f"This didgit is probably a {np.argmax(pred)}")
        plt.imshow(img[0], cmap=plt.cm.binary)
        plt.show()
    except:
        print("error!")
    finally:
        img_no +=1