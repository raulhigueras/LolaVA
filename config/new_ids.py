import pickle

ids = {
	"RSS2JSON":"",
	"OPENWEATHERMAP":"",
	"TELEGRAM_CHAT":"",
}

with open('ids.pickle', 'wb') as handle:
	pickle.dump(ids, handle, protocol=pickle.HIGHEST_PROTOCOL)
