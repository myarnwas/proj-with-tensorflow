import tensorflow as tf
print(tf.__version__)
import numpy as np
import matplotlib as matplotlib
print(np.__version__)
print(matplotlib.__version__)
from keras.datasets import reuters
(train_data,train_labels),(test_data,test_labels)= reuters.load_data(num_words=10000)
len(train_data)
len(test_data)
