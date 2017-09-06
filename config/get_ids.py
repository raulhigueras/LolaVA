import pickle

def get_ids():
	with open('config/ids.pickle', 'rb') as handle:
		return pickle.load(handle)
