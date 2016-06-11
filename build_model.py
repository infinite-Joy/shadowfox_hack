'''Trains a LSTM on the IMDB sentiment classification task.

The dataset is actually too small for LSTM to be of any advantage
compared to simpler, much faster methods such as TF-IDF+LogReg.

Notes:

- RNNs are tricky. Choice of batch size is important,
choice of loss and optimizer is critical, etc.
Some configurations won't converge.

- LSTM loss decrease patterns during training can be quite different
from what you see with CNNs/MLPs/etc.
'''
from __future__ import print_function
import numpy as np
np.random.seed(1337)  # for reproducibility

import theano
theano.config.floatX = 'float32'


from keras.preprocessing import sequence
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Embedding
from keras.layers import LSTM, GRU

print('Loading data...')


#load the data	
# x_train = np.loadtxt(fname="X_data.csv", delimiter=',' ,dtype=theano.config.floatX)
x_train = np.loadtxt(fname="X_data.csv", delimiter=',' ,dtype=theano.config.floatX)
# y_train = np.loadtxt(fname="Y_data.csv", delimiter=',' ,dtype=theano.config.floatX)
y_train = np.loadtxt(fname="Y_data.csv", delimiter=',' ,dtype=theano.config.floatX)
print(x_train[0])
print(y_train[0])

X_test = x_train
y_test = y_train

print(len(x_train), 'train sequences')
print(len(X_test), 'test sequences')

# print('Pad sequences (samples x time)')
# x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
# X_test = sequence.pad_sequences(X_test, maxlen=maxlen)
# print('x_train shape:', x_train.shape)
# print('X_test shape:', X_test.shape)

print('Build model...')
model = Sequential()
# model.add(Embedding(max_features, 128, input_length=maxlen, dropout=0.2))
#model.add(Embedding(max_features, 128, dropout=0.2))
model.add(Embedding(10000, 128, dropout=0.2))
model.add(LSTM(128, dropout_W=0.2, dropout_U=0.2))  # try using a GRU instead, for fun
model.add(Dense(1))
model.add(Activation('sigmoid'))

# try using different optimizers and different optimizer configs
model.compile(loss="mean_squared_error",
              optimizer = 'rmsprop',
              metrics=['accuracy'])

print('Train...')
print(x_train.shape)
print(y_train.shape)
# model.fit(x_train, y_train, batch_size=batch_size, nb_epoch=15,
          # validation_data=(X_test, y_test))
model.fit(x_train, y_train, nb_epoch=1,
          validation_data=(X_test, y_test))
score, acc = model.evaluate(X_test, y_test)
print('Test score:', score)
print('Test accuracy:', acc)
