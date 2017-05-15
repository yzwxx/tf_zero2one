import argparse

parser = argparse.ArgumentParser()
'''
how to use add_argument?
command is the string to specify which argument to be set up.
type is what kind of type we treat the input data as.
default is the default setting of that argument.
help is the doc that will show up in helping page
'''
parser.add_argument(
	  '-lr', # shortcut
      '--learning_rate',
      type=float,
      default=0.01,
      help='Initial learning rate.'
  )
parser.add_argument(
	  '-ms',
      '--max_steps',
      type=int,
      default=2000,
      help='Number of steps to run trainer.'
  )
parser.add_argument(
      '--hidden1',
      type=int,
      default=128,
      help='Number of units in hidden layer 1.'
  )
parser.add_argument(
      '--hidden2',
      type=int,
      default=32,
      help='Number of units in hidden layer 2.'
  )
parser.add_argument(
      '--batch_size',
      type=int,
      default=100,
      choices=[100,200,300,400,500], # restricting choices for an argument
      help='Batch size.  Must divide evenly into the dataset sizes.'
  )
parser.add_argument(
      '--input_data_dir',
      type=str,
      default='/tmp/tensorflow/mnist/input_data',
      help='Directory to put the input data.'
  )
parser.add_argument(
      '--log_dir',
      type=str,
      default='/tmp/tensorflow/mnist/logs/fully_connected_feed',
      help='Directory to put the log data.'
  )
parser.add_argument(
      '--fake_data',
      default=False,
      help='If true, uses fake data for unit testing.',
      action='store_true'
  )
'''
to add some exclusive arguments:
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")

check:https://docs.python.org/2/howto/argparse.html
'''
def print_info():
	print(FLAGS.input_data_dir)

if __name__ == '__main__':
	args = parser.parse_args()
	print args

	FLAGS, unparsed = parser.parse_known_args()
	print(FLAGS,unparsed)
	print_info()

	if args.log_dir:
		print args.log_dir