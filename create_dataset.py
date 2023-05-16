import pickle

data = {"faces": [], "names": []}

file = open("dataset", "wb")         # Путь!!!!!
file.write(pickle.dumps(data))
file.close()

