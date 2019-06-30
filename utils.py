# utility functions

# Use this file for all functions you create and might want to reuse later.
# Import them in the `main.py` script


# mkdir function creates folder if it doesn't exist already. 

def mkdir(folder):
    folder.mkdir(parents=True,exist_ok=True)
