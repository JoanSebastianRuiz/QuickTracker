"""
    **Módulo de Gestión de Servicios:**

        - Operaciones CRUD para cada tipo de servicio ofrecido, como Internet de Fibra Óptica, planes pospago, prepago, etc.
        - Capacidad para agregar, modificar y eliminar servicios según sea necesario.
        - Registro de información detallada sobre cada servicio, incluyendo características, precios, entre otros.
"""

def agregar_servicio(datos):
    servicio={}
    servicio["codigo"]=input("Ingrese el codigo del servicio que quiere agregar: ")
    servicio["nombre"]=input("Ingrese el nombre del servicio que quiere agregar: ")
    servicio["caracteristicas"]=input("Ingrese las caracteristicas del servicio: ")
    servicio["precio"]=input("Ingrese el precio del servicio: ")
    datos.append(servicio)
    print("Se ha agregado correctamente el servicio")
    return datos

def eliminar_servicio(datos):
    codigo=input("Ingrese el codigo del servicio que quiere agregar: ")
    for diccionario in datos:
        if diccionario["codigo"]==codigo:
            datos.remove(diccionario)
            print("Se ha eliminado correctamente el servicio")
    return datos

def actualizar_servicio(datos):
    codigo=input("Ingrese el codigo del servicio que quiere agregar: ")
    for diccionario in datos:
        if diccionario["codigo"]==codigo:
                diccionario["nombre"]=input("Ingrese el nombre del servicio: ")
                diccionario["caracteristicas"]=input("Ingrese las caracteristicas del servicio: ")
                diccionario["precio"]=input("Ingrese el precio del servicio: ")
                print("Se ha actualizado correctamente el servicio")

def leer_servicios(datos):
    for diccionario in datos:
        for llave, valor in diccionario.items():
            print(f"{llave}: {valor}    ", end="")
        print("")

