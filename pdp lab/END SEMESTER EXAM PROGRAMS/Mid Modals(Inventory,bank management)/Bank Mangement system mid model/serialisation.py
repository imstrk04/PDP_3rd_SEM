import pickle

def save_data(data,file_name):
    with open(file_name,'wb')as file:
        pickle.dump(data,file)

def load_data(file_name):
    with open(file_name,'rb')as file:
        loaded_data=pickle.load(file)
    return loaded_data
