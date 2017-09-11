# Obtener info de la configuracion
import pickle

def get_profile():
        with open('config/profile.pickle', 'rb') as handle:
                return pickle.load(handle)

def get_ids():
        with open('config/ids.pickle', 'rb') as handle:
                return pickle.load(handle)

