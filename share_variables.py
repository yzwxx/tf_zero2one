
# coding: utf-8

# In[1]:

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys

from tensorflow.examples.tutorials.mnist import input_data

import tensorflow as tf


# In[2]:

def conv_relu(input, kernel_shape, bias_shape):
    # Create variable named "weights".
    weights = tf.get_variable("weights", kernel_shape,
        initializer=tf.random_normal_initializer())
    # Create variable named "biases".
    biases = tf.get_variable("biases", bias_shape,
        initializer=tf.constant_initializer(0.0))
    conv = tf.nn.conv2d(input, weights,
        strides=[1, 1, 1, 1], padding='SAME')
    return tf.nn.relu(conv + biases)


# In[4]:

def my_image_filter(input_images):
    with tf.variable_scope("conv1"):
        # Variables created here will be named "conv1/weights", "conv1/biases".
        relu1 = conv_relu(input_images, [5, 5, 32, 32], [32])
    with tf.variable_scope("conv2"):
        # Variables created here will be named "conv2/weights", "conv2/biases".
        relu2 = conv_relu(relu1, [5, 5, 32, 32], [32])
        return relu2


# In[20]:

def main(_):
    # Import data
    mnist = input_data.read_data_sets(FLAGS.data_dir, one_hot=True)

    # Create the model
    x = tf.placeholder(tf.float32, [None, 784])
#     x_image = tf.reshape(x, [-1, 28, 28, 1])
    
#     with tf.variable_scope("image_filters") as scope:
#         result1 = my_image_filter(x_image[0])
#         scope.reuse_variables()
#         result2 = my_image_filter(x_image[1])
    data = x
    
    with tf.Session() as sess:
#         sess.run(tf.global_variables_initializer())
        batch_x,batch_y = mnist.train.next_batch(50)
#         print result1.eval(feed_dict={x_image:batch_x})
        print(data.eval(feed_dict={x:batch_x}))
        print('ok')
    


# In[22]:

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str,
                        default='/home/hadoop/workspace/tf_zero2one/data/mnist',
                        help='Directory for storing input data')
    FLAGS, unparsed = parser.parse_known_args()
    print(FLAGS,unparsed)
    tf.app.run(main=main)


# In[ ]:



