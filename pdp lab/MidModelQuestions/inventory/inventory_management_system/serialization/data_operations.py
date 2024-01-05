import pickle

def serialize_data(data, filename="data.pickle"):
    """
    Serialize the given data and save it to a file.

    Parameters:
    - data: The data to be serialized (e.g., a list of dictionaries).
    - filename: The name of the file to save the serialized data (default is "data.pickle").
    """
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

def deserialize_data(filename="data.pickle"):
    """
    Deserialize data from a file.

    Parameters:
    - filename: The name of the file containing serialized data (default is "data.pickle").

    Returns:
    - The deserialized data.
    """
    try:
        with open(filename, 'rb') as file:
            deserialized_data = pickle.load(file)
            return deserialized_data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except EOFError:
        print(f"Error: Reached EOF while deserializing '{filename}'.")
        return None
