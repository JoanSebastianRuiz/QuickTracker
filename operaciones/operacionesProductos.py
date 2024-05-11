"""
- Registro de productos y servicios basados en sus características necesarias para que los empleados puedan ofrecerlos.
- Registro de cada una de las ventas, tanto de servicios como de productos. Así como, un registro de fechas de 
compra, cantidades, estado, etc.

"""

def agregar_producto(datos):
    producto={}
    producto["codigo"]=input("Ingrese el codigo del producto a agregar:")
    producto["nombre"]=input("Ingrese el nombre del producto a agregar: ")  
    producto["precio"]=input("Ingrese el precio del producto a agregar: ")
    producto["marca"]=input("Ingrese la marca del producto a agregar: ")
    producto["cantidad"]=input("Ingrese la cantidad del producto a agregar: ")
    producto["caracteristicas"]=input("Ingrese las caracteristicas del producto: ")
    datos.append(producto)
    print("El producto se ha agregado correctamente")

def eliminar_producto(datos):
    codigo=input("Ingrese el codigo del producto a eliminar:")
    for diccionario in datos:
        if diccionario["codigo"]==codigo:
            datos.remove(diccionario)
            print("El producto se ha eliminado correctamente")
            break
    return datos

def actualizar_producto(datos):
    codigo=input("Ingrese el codigo del producto a actualizar:")
    for diccionario in datos:
        if diccionario["codigo"]==codigo:
            diccionario["nombre"]=input("Ingrese el nombre del producto: ")  
            diccionario["precio"]=input("Ingrese el precio del producto: ")
            diccionario["marca"]=input("Ingrese la marca del producto  ")
            producto["cantidad"]=input("Ingrese la cantidad del producto : ")
            diccionario["caracteristicas"]=input("Ingrese las caracteristicas del producto: ")
            print("El producto se ha actualizado correctamente")
            break

def leer_productos(datos):
    for diccionario in datos:
        for llave,valor in diccionario:
            print(f"{llave}: {valor}")
        print("")
            