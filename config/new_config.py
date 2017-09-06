import pickle

opciones = {
  "nombre":"raul",
  "periodico":"pais",
  "ciudad":"barcelona",
  "asistente":"maria",
  "modo":"texto"
}

with open('profile.pickle', 'wb') as handle:
  pickle.dump(opciones, handle, protocol=pickle.HIGHEST_PROTOCOL)
