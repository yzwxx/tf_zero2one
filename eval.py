
# coding: utf-8

# In[2]:

import tensorflow as tf
import numpy as np


# In[3]:

# to print the value of tf.constant,tf.placeholder and tf.Variable
a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
b = tf.placeholder(tf.float32,shape=[2,3])
c = tf.Variable(tf.zeros([784,10]))


# In[15]:

sess = tf.Session()
# for constant
print sess.run(a)
print a.eval(session = sess)
print a.get_shape()
print type(a)


# In[12]:

# for  placeholder it must have a feed_dict
_b = np.array([[1,2,3],[9,6,7]])
print sess.run(b, feed_dict={b:_b})
print b.eval(session = sess, feed_dict={b:_b})
# every time we evaluate a node with connection to placeholders we need feed_dict to assign value to placeholders
print sess.run(tf.argmax(b,1),feed_dict={b:_b})
print b.get_shape()
print type(b)


# In[13]:

# for variable must be initialized before evaluation
sess.run(tf.global_variables_initializer())
print sess.run(c)
print c.eval(session = sess)
print c.get_shape()
print type(c)


# In[ ]:



