import os

def get_path():
    path = os.getcwd().replace("\\rough","")
    return path

print(get_path())