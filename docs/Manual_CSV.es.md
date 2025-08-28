# CSV
  
Módulo para el manejo de archivos CSV  

*Read this in other languages: [English](Manual_csv.md), [Español](Manual_csv.es.md).*
  
![banner](imgs/Banner_csv.png)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  



## Descripción de los comandos

### Leer CSV
  
Lee un archivo CSV y guarda el contenido en una variable
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta del archivo |Ruta del archivo CSV a leer|C:/User/Usuario/Folder/file.csv|
|Separador|Separador de columnas|,|
|Codificación|Codificación del archivo|UTF-8|
|Nombre de la varible donde guardar contenido|Nombre de la variable donde se guardará el contenido del archivo|Result|

### Exportar a CSV
  
Exporta datos a un archivo CSV
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a exportar|Datos que se exportarán a un archivo CSV|[[data, data], [data, data]]|
|Delimitador|Delimitador de los datos|,|
|Ruta del archivo |Ruta del archivo CSV a crear|C:/User/Usuario/Folder/file.csv|
