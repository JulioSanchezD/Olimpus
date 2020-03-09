import os

import pandas as pd

from flask import send_from_directory

def process():

    dir_path = os.path.dirname(os.path.realpath(__file__))

    df = pd.DataFrame({'a': [1, 2, 3]})
    file_name = 'test.xlsx'
    
    df.to_excel(file_name)

    return send_from_directory(directory=dir_path, filename='test.xlsx', as_attachment=True)
