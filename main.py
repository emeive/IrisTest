import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
datos = pd.read_csv('datos_iris.csv', header=None)

# Asignar nombres de columnas
datos.columns = ['valorX', 'valorY']

# Separar los datos según el color
datos_rojo = datos[:20]
datos_verde = datos[20:40]
datos_azul = datos[40:]

# Crear una figura y ejes para el gráfico
fig, ax = plt.subplots()

# Graficar los datos de dispersión para cada color
ax.scatter(datos_rojo['valorX'], datos_rojo['valorY'], color='red')
ax.scatter(datos_verde['valorX'], datos_verde['valorY'], color='green')
ax.scatter(datos_azul['valorX'], datos_azul['valorY'], color='blue')

# Agregar título y etiquetas a los ejes
ax.set_title('Gráfico de Datos Simulados')
ax.set_xlabel('valorX')
ax.set_ylabel('valorY')

# Mostrar el gráfico
plt.show()
