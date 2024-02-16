import os
import pandas as pd 

def csv_file(file_path):
    try:
        df = pd.read_csv(file_path)
        info = f'Filas: {df.shape[0]}\nColumnas: {df.shape[1]}\n'

        column_info = ''
        for column in df.columns:
            column_info += f'\n{column}\n'
            column_info += str(df[column].describe()) + '\n'
        
        name = os.path.splitext(os.path.basename(file_path))[0]
        df.to_json(f'{name}.json')
        return 'csv_to_json', info + column_info
    except Exception as e:
        try:
            df = pd.read_json(file_path)
            name = os.path.splitext(os.path.basename(file_path))[0]
            df.to_csv(f'{name}.csv')
            return 'json_to_csv', f'El archivo JSON se ha convertido exitosamente a CSV.'
        except Exception as e:
            return 'otro_formato', f'Error: {str(e)}'
