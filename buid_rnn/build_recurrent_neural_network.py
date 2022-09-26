# -*- coding: utf-8 -*-
"""build_recurrent_neural_network.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PVKUxq2uBNh_u8osFJu1KCKY3lyNoTmC
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

(X_train, y_train), (X_test, y_test) = tf.keras.datasets.imdb.load_data(num_words=1000)

print(X_train[0])
print(y_train[0])
print(X_test[0])
print(y_test[0])

print(f"X_train: {len(X_train)}")
print(f"y_train: {len(y_train)}")
print(f"X_test: {len(X_test)}")
print(f"y_test: {len(y_test)}")

#preprocessing
X = np.concatenate((X_train, X_test), axis=0)
y = np.concatenate((y_train, y_test), axis=0)

#padding
X = tf.keras.preprocessing.sequence.pad_sequences(X,maxlen=1024)

#splitting
X_train = X[:40000]
y_train = y[:40000]
X_val = X[40000:45000]
y_val = y[40000:45000]
X_test = X[45000:50000]
y_test = y[45000:50000]

print(f"X_train: {len(X_train)}")
print(f"y_train: {len(y_train)}")
print(f"X_val: {len(X_val)}")
print(f"y_val: {len(y_val)}")
print(f"X_test: {len(X_test)}")
print(f"y_test: {len(y_test)}")

#constructing the neural network
model = tf.keras.Sequential()

#embedding layer
#word embedding
model.add(tf.keras.layers.Embedding(input_dim=10000, output_dim=256))
model.add(tf.keras.layers.Dropout(0.7))

model.add(tf.keras.layers.LSTM(256))
model.add(tf.keras.layers.Dropout(0.7))
model.add(tf.keras.layers.Dense(128, activation="relu"))
model.add(tf.keras.layers.Dropout(0.7))

#output layer
model.add(tf.keras.layers.Dense(1, activation="sigmoid"))

#optimizer
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

results = model.fit(X_train, y_train,epochs=5,validation_data=(X_val,y_val))

plt.plot(results.history["loss"],label="Train")
plt.plot(results.history["val_loss"], label="Validation")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()
plt.show()

plt.plot(results.history["accuracy"],label="Train")
plt.plot(results.history["val_accuracy"], label="Validation")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.legend()
plt.show()

#performance evaluation
model.evaluate(X_test, y_test)

prediction_results = model.predict(X_test[789].reshape(1,1024))

print(f"Label: {y_test[789]}|Prediction:{prediction_results}")