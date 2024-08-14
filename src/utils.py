import os 
import sys 
import dill
from src.exception import CustomException

def save_object(file_path, obj):  # Add `obj` as a parameter
    try:
        # Ensure the directory exists where the file is to be saved
        dir_path = os.path.dirname(file_path)  # Corrected this line
        os.makedirs(dir_path, exist_ok=True)
        
        # Save the object to the specified file path using dill
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        # Raise a custom exception in case of any error
        raise CustomException(e, sys)
