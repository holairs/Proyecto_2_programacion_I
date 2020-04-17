import os,json
inicio = 1
while inicio > 0:

    direccion = input('escriba la direccion en donde desea buscar, ejemplo(/Users/Walrus/Downloads): ')
    tipo = input('Ingrese la extension que desea buscar: ')
    nombre = input('Que nombre desea aplicar a los archivos?: ')

    #Variable para la ruta al directorio
    path = direccion

    #Lista vacia para incluir los ficheros
    lstFiles = []

    datos = []

    #Lista con todos los ficheros del directorio:
    lstDir = os.walk(path)   #os.walk()Lista directorios y ficheros

    #Crea una lista de los ficheros 'x' que existen en el directorio y los incluye a la lista.

    for root, dirs, files in lstDir:
        for fichero in files:
            (nombreFichero, extension) = os.path.splitext(fichero)
            if(extension == "." + tipo):
                lstFiles.append(nombreFichero+extension)
                
    print('Archivos encontrados: ')
    for items in lstFiles:
        print(items)        
        print('')    
    print('--------------------------------------')
    print ('LISTADO FINALIZADO')
    print('--------------------------------------')
    print ('Cantidad de archivos a modificar = ', len(lstFiles))
        
    numero = 0
    total = int(len(lstFiles))

    for i in range (total):
        numero = numero + 1
        item = nombre
        archivo = {}
        Original = (lstFiles[i])
        Nuevo = (item + '_'+str(numero))
        archivo['Original']=Original
        archivo['Nuevo']=Nuevo
        datos.append(archivo)

    for items in datos:

        print(items)
        print('')
    print('----------------------------')
    print('----------------------------')

    with open('Base_de_datos_json_buscador.json', 'w') as base:
        json.dump(datos, base)
    print('Archivos Esxportados con exito')


    inicio = int(input('Si desea hacer una nueva busqueda presione (1) si desea salir presione (0): '))

    print("Programa terminado")


