Objective:

To predict where the next pickup might be taking place based on the historical data using predictive analytics. Also predicting alternative routes where pickups might be there.

Dependencies:
python, keras, theano

How to get the model:

first we get the x and y data into a file:
python get_x.py > X_data.csv
python get_y.py > Y_data.csv

we remove the white space from the files:
perl -i.bak -ne 'print if /\S/' X_data.csv

then we build the model:
python build_model.py

Output_for_now:

Using Theano backend.
Loading data...
[ 2213.          2765.            12.90595245    77.58557129    12.88467979
    77.58200073]
0.0
2438 train sequences
2438 test sequences
Build model...
Train...
(2438, 6)
(2438,)
Train on 2438 samples, validate on 2438 samples
Epoch 1/1
2438/2438 [==============================] - 6s - loss: 0.0469 - acc: 0.9459 - val_loss: 2.1705e-04 - val_acc: 1.0000
2438/2438 [==============================] - 1s
Test score: 0.000217053342791
Test accuracy: 1.0

