import pandas as pd
import json

def limpiar_datos_libros(ruta_csv_entrada, ruta_json_salida):
    # Cargar el archivo CSV
    libros_df = pd.read_csv(ruta_csv_entrada)
    
    # Imputar valores faltantes en la columna 'Genre' con 'Desconocido'
    libros_df['Genre'].fillna('Desconocido', inplace=True)
    
    # Normalizar nombres de columnas
    libros_df.columns = [col.strip().lower().replace(' ', '_') for col in libros_df.columns]
    
    # Convertir el DataFrame a una lista de diccionarios
    libros_list = libros_df.to_dict(orient='records')
    
    # Guardar los datos JSON limpios en un archivo con formato legible
    with open(ruta_json_salida, 'w', encoding='utf-8') as f:
        json.dump(libros_list, f, ensure_ascii=False, indent=4)

# Define las rutas de entrada y salida según tu estructura de carpetas
ruta_csv_entrada = 'SetsDatos/nolimpios/best-selling-books/best-selling-books.csv'
ruta_json_salida = 'SetsDatos/limpios/libros_mas_vendidos_limpios.json'  

# Llamar a la función para limpiar y guardar los datos
limpiar_datos_libros(ruta_csv_entrada, ruta_json_salida)

print(f"Los datos limpios han sido guardados en {ruta_json_salida}")
