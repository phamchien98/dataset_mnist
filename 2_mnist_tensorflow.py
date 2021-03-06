# -*- coding: utf-8 -*-
"""2_mnist_tensorflow.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ult6uiFHmKr5T5_viK3FB1wAxEINZKWr
"""

import tensorflow as tf
import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('data/mnist',one_hot = True)

X_train = mnist.train.images
X_test = mnist.test.images
X_val = mnist.validation.images

y_train = mnist.train.labels
y_test = mnist.test.labels
y_val = mnist.validation.labels

X_train.shape

y_train.shape

y_train[0]

X = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])

W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))

learning_rate = 0.01
batch_size = 128
nb_epochs = 128

logits = tf.matmul(X,W) + b
y_pred = tf.nn.softmax(logits = logits)

entropy = tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=logits)
loss=tf.math.reduce_sum(entropy)
correct_preds = tf.equal(tf.argmax(y_pred,1),tf.argmax(y,1))

accuracy = tf.reduce_mean(tf.cast(correct_preds, tf.float32))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(loss)

init = tf.global_variables_initializer()

sess = tf.Session()

sess.run(init)

nb_batch = X_train.shape[0] // batch_size

for i in range(nb_epochs):
    for _ in range(nb_batch):
        X_batch , y_batch = mnist.train.next_batch(batch_size=batch_size)
        _, batch_loss = sess.run([optimizer, loss], feed_dict={X : X_batch, y : y_batch})
        
    if i % 10 == 0:
        _, val_loss, val_accuracy = sess.run([optimizer, loss, accuracy], feed_dict={X : X_val, y : y_val})
        print("Epochs {} val_loss = {} val_accuracy = {}".format(i, val_loss, val_accuracy))

