import pandas as pd

def deleteRecords(df, col, col_or_row):
    if col_or_row == 1:
        df.drop([col], axis=1, inplace=True)#ojo aca que el inplace true hace que los cambios se efectuen en el mismo dataframe
        print(f'columna {col} eliminada exitosamente') 
    elif col_or_row == 2:
        df.dropna(subset=[col], inplace=True)#lo mimso aca viejo, que esperabas? jajajja
        return print(f'todas las filas con la columna {col} han sido eliminadas')   


def process_null_values(data: pd.DataFrame) ->pd.Series: #tipamos la funcion hermano
    data_null_values = data.isnull().sum()
    missing_percentage = (data_null_values / len(data)) * 100  
    
    missing_data = pd.DataFrame({
    	'Total': data_null_values,
    	'Porcentaje': missing_percentage
	})

    # Filtrando las columnas con valores faltantes
    columns_with_missing = missing_data[missing_percentage > 0]
    listavalores =[]
    if not columns_with_missing.empty:  # empty nos devuelve True si la serie está vacia
        missingDict = columns_with_missing.to_dict()
        for key, value in missingDict.items():
            print(key, 'de registros:')
            for subkey, subValues in value.items():
                print('la columna',subkey,'tiene un',key,'de:',subValues, 'valores vacios')
                if subkey not in listavalores: #para eviastr duplicados jeje
                    listavalores.append(subkey)
            print('----'*20)
        print('Si las columnas son irrelevantes, podemos hacer algo con sus datos, que te gustaria eliminarlos o los conservamos?')
        for col in listavalores:
            vardeleteCol = input(f"Te gustaría eliminar la columna {col}? Digita 'S' para confirmar: ")
            if vardeleteCol == 'S' or vardeleteCol == 's':
                deleteRecords(data, col, 1)
            else:
                vardeleteRow = input(f"Te gustaría eliminar las filas vacias de la columna {col}? Digita 'S' para confirmar: ")
                if vardeleteRow == 'S' or vardeleteRow == 's':
                    deleteRecords(data, col, 2)
        print('data limpiada maestro, que tengas un buen dia :)')
    else:
        print('No hay columnas con valores faltantes')
        