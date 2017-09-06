import pickle

def get_config():
  with open('config/profile.pickle', 'rb') as handle:
    return pickle.load(handle)