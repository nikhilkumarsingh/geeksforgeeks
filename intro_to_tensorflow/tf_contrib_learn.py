# importing the dependencies
import tensorflow as tf
import numpy as np
 
# declaring list of features
features = [tf.contrib.layers.real_valued_column("X")]
 
# creating a linear regression estimator
estimator = tf.contrib.learn.LinearRegressor(feature_columns=features)
 
# training and test data
train_X = np.asarray([3.3,4.4,5.5,6.71,6.93,4.168,9.779,6.182,7.59,2.167,
                         7.042,10.791,5.313,7.997,5.654,9.27,3.1])
train_y = np.asarray([1.7,2.76,2.09,3.19,1.694,1.573,3.366,2.596,2.53,1.221,
                         2.827,3.465,1.65,2.904,2.42,2.94,1.3])
test_X = np.asarray([6.83, 4.668, 8.9, 7.91, 5.7, 8.7, 3.1, 2.1])
test_y = np.asarray([1.84, 2.273, 3.2, 2.831, 2.92, 3.24, 1.35, 1.03])
 
# function to feed dict of numpy arrays into the model for training
input_fn = tf.contrib.learn.io.numpy_input_fn({"X":train_X}, train_y, 
                                              batch_size=4, num_epochs=2000)
 
# function to feed dict of numpy arrays into the model for testing
test_input_fn = tf.contrib.learn.io.numpy_input_fn({"X":test_X}, test_y)
 
# fit training data into estimator
estimator.fit(input_fn=input_fn)
 
# print value of weight and bias
W = estimator.get_variable_value('linear/X/weight')[0][0]
b = estimator.get_variable_value('linear/bias_weight')[0]
print("W:", W, "\tb:", b)
 
# evaluating the final loss
train_loss = estimator.evaluate(input_fn=input_fn)['loss']
test_loss = estimator.evaluate(input_fn=test_input_fn)['loss']
print("Final training loss:", train_loss)
print("Final testing loss:", test_loss)
