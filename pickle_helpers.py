try:
	import cPickle as pickle
except:
	import pickle

import os

def load_pickle(dir = "data.pkl"):
      if os.path.exists(dir):
            pkl_file = open(dir, 'rb')
            data = pickle.load(pkl_file)
            pkl_file.close()
      return data 


def save_pickle(data , name = "data.pkl"):
      output = open( name, 'wb')
      pickle.dump(data, output)
      output.close()
