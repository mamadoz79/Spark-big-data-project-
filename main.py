import os

def docx_action(file_path):
    os.system(f"python spark.py {file_path}")


file_path = input('please enter file path:\n')
if file_path.split('.')[-1] == 'doc':
    os.system(f'python doc2docx.py {file_path}')
    docx_action(file_path+'x')
elif file_path.split('.')[-1] == 'docx':
    docx_action(file_path)
