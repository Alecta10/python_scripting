import pandas as pd
import json

# Exportar csv con panda
nombre_csv = 'datos.csv'

data = {
    'nombre' : ['Pablo ', 'Luis', 'Pepe', 'Alex'],
    'edad' : ['23', '25', '19', '13'],
    'ciudad' : ['Madrid', 'Cordoba', 'Cadiz', 'Barcelona']
}

dataframe = pd.DataFrame(data)
# Index false para que no este enumerado
dataframe.to_csv(nombre_csv, index=False)
print("Escrito en datos.csv: \n", dataframe.to_string(index=False))

# Importar csv con panda
data_read = pd.read_csv(nombre_csv)
print("\n \n Leido desde datos.csv \n", data_read)

filtro_nombre = data_read['nombre']
filtro_edad = data_read['edad']
filtro_ciudad = data_read['ciudad']

print("\n \n Solo cabecera: \n", data_read.head())

# filtro = data_read['nombre'].str.startswith('L')
# filtro = data_read['nombre'].str.contains('L')
# filtro = data_read['edad'].str.startswith('2')
# filtro = data_read['edad'].str.endswith('2')
# resultado_filtro = data_read.loc(filtro_edad)

filtro_edad = data_read[data_read['edad'] > 18]
print("\n \n Filtro para mayor de edad \n", filtro_edad)

# Importar json
archivo_json = 'libros.json' 

with open(archivo_json, 'r') as archivo_leido:
    # Datos en json
    datos_json = json.load(archivo_leido)

# Datos normalizados en dataframe
dataframe = pd.json_normalize(datos_json, 'libros')
print("\n \n Datos desde un json: \n", dataframe)