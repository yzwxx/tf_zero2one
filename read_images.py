#! /usr/bin/env python 
# -*-coding:utf-8 -*-

'''
This script is used as a tutorial of tensorflow to read in image data
'''
import os
from os.path import join,isfile
import tensorflow as tf
from glob import glob
from random import shuffle

# cur_dir = os.getcwd()
# data_dir = join(cur_dir,'test_input')
# all_files = [join(data_dir,file) for file in os.listdir(data_dir)]
all_files = glob('./test_input/*.jpg')
# print all_files
# shuffle(all_files)
# print all_files

with tf.Session() as sess:
	# filename list to read from
	filenames = all_files
	# create a filename queue
	filename_queue = tf.train.string_input_producer(filenames,shuffle = False, num_epochs = 3)
	# create a reader
	reader = tf.WholeFileReader()
	key,value = reader.read(filename_queue)

	# if missed then error will be raised(Attempting to use uninitialized value input_producer/limit_epochs/epochs)
	tf.local_variables_initializer().run()
	threads = tf.train.start_queue_runners(sess = sess)

	i=0
	try:
		while True:
			i+=1
			image_data = sess.run(value)
			if not os.path.exists('test_output/'):
					os.makedirs('test_output/')
			with open('test_output/test_%d.jpg'%i,'wb+') as f:
				f.write(image_data)
	except tf.errors.OutOfRangeError:
		print('Done training -- epoch limit reached')