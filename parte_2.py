import json

inicio = 'si'

while inicio == 'si':


    #Realizacion del menu de ingreso de datos del cliente

    print('-----------------------')
    print('Tipos de Vehiculo:'   )
    print('-----------------------')
    print('1. Motocicleta (Q.15)')
    print('2. Automovil (Q.30)'  )
    print('3. Camioneta (Q.50)'  )
    print('-----------------------')
    tipoVehiculo = input('Seleccione que tipo de vehiculo desea ingresar [1,2,3]: ')
    print('-----------------------')
    print('Tipo de Cliente:')
    print('-----------------------')
    print('1. Estandar')
    print('2. Miembro')
    print('-----------------------')
    tipoCLiente = input('Ingrese el tipo de Cliente [ 1 o 2 ]: ')
    print('-----------------------')
    fin_de_semana = input('Escriba si/no si es fin de semana: ')


    precio = 0
    tipo = ''
#validar los valores del fin de semana

    semana = True
    if fin_de_semana == 'si':
        semana = True
    else:
        semana = False
#validar el tipo de veiculo y su precio

    if tipoVehiculo == '1':
        precio = 15
        tipo = 'Motocicleta'
    if tipoVehiculo == '2':
        precio = 30
        tipo = 'Automovil'
    if tipoVehiculo == '3':
        precio = 50
        tipo = 'Camioneta'
#validar el tipo de cliente
    miembro = True

    if tipoCLiente == '1':
        miembro = False
        if tipoCLiente == '2':
            miembro = True

    if miembro:
        tipoCLiente = 'Miembro'
    else:
        tipoCLiente = 'Estandar'

#validar los descuentos
    descuento1 = 0
    descuento2 = 0
    if miembro:
        descuento1 = precio*0.10
    else: 
        descuento1 = 0

    if semana:
        descuento2 = 0
    else:
        descuento2 = precio*0.10

    descuentoTotal = descuento1 + descuento2

#imprimir resultados
    Total = descuentoTotal + precio
    print('Tipo: ' + tipo)
    print('Precio: ' + str(precio))
    print('Tipo de Cliente: ' + tipoCLiente)
    print('Fin de semana: ' + str(semana))
    print('Descuentos: ' + str(descuentoTotal))
    print('Total: ' + str(Total))
    print('-----------------------')





    direccion_exportar = input('Ingrese la direccion para guardar[Ejemplo: /Users/Walrus/Downloads]: ')
    nombre_exportar = input('Ingrese Nombre para exportar: ')
    print('-----------------------')

    registro = []
#repetidor para ingresar los datos en el diccionario
    for i in range (1):
        archivo = {}

        archivo['Tipo'] = tipo
        archivo['Precio'] = precio
        archivo['Tipo de Cliente'] = tipoCLiente
        archivo['Fin de semana'] = semana
        archivo['Descuentos'] = descuentoTotal
        archivo['Total'] = Total

        registro.append(archivo)
    #exportar a direccion dada por el usuario mas el nombre
    with open(direccion_exportar + '/' + nombre_exportar + '.json', 'w') as base:
        json.dump(registro, base)


        
    print('Archivos Esxportados con exito')
    print('-----------------------')

    inicio = input("Desea ingresar un nuevo cliente si/no: ")
    print('-----------------------')
    

print('Saliendo del sistema...')










