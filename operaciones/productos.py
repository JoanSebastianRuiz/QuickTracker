"""
- Registro de productos y servicios basados en sus características necesarias para que los empleados puedan ofrecerlos.
- Registro de cada una de las ventas, tanto de servicios como de productos. Así como, un registro de fechas de 
compra, cantidades, estado, etc.

"""
from validaciones import *

def agregar_producto(datos):
    producto={}
    bandera=False
    
    while bandera==False:
        nombre=input("Ingrese el nombre del producto a agregar: ") 
        if validar_contiene_contenido(nombre)==True and validar_contiene_letras(nombre)==True:
            bandera=True
    bandera=False
    
    if verificar_existencia_valor(datos,"nombre",nombre)==False:    
        producto["codigo"]=len(datos)+1
        producto["nombre"]= nombre
        
        while bandera==False:
            marca=input("Ingrese la marca del producto a agregar: ")
            if validar_contiene_contenido(marca)==True and validar_contiene_letras(marca)==True:
                bandera=True
        bandera=False
        producto["marca"]=marca
        
        while bandera==False:
            precio=input("Ingrese el precio del producto a agregar: ")
            if validar_contiene_contenido(precio)==True and validar_contiene_numeros(precio)==True:
                bandera=True
        bandera=False
        producto["precio"]=precio

        while bandera==False:
            cantidad=input("Ingrese la cantidad del producto a agregar: ")
            if validar_contiene_contenido(cantidad)==True and validar_contiene_numeros(cantidad)==True:
                bandera=True
        bandera=False
        producto["cantidad"]=cantidad
        
        while bandera==False:
            caracteristicas=input("Ingrese las caracteristicas del producto a agregar: ")
            if validar_contiene_contenido(caracteristicas)==True:
                bandera=True
        bandera=False
        producto["caracteristicas"]=caracteristicas
        
        producto["clientes"]=[]
        
        datos.append(producto)
        print("El producto se ha agregado correctamente")
        return datos
    
    else:
        print("El nombre ingresado ya se encuentra registrado en la lista de productos")
        return datos

def eliminar_producto(datos):
    while bandera==False:
        codigo=input("Ingrese el codigo del producto a eliminar:")
        if validar_contiene_contenido(codigo)==True and validar_contiene_numeros(codigo)==True:
            bandera=True
    bandera=False
    
    if verificar_existencia_valor(datos,"codigo",codigo)==True:
        diccionario=ubicacion_valor(datos,"codigo",codigo) 
        datos.remove(diccionario)
        print("El producto se ha eliminado correctamente")
        return datos
    else:
        print("El codigo ingresado no se encuentra registrado en la lista de productos")
        return datos

def actualizar_producto(datos):
    bandera=False
    while bandera==False:
        codigo=input("Ingrese el codigo del producto a actualizar:")
        if validar_contiene_contenido(codigo)==True and validar_contiene_numeros(codigo)==True:
            bandera=True
    bandera=False
    
    if verificar_existencia_valor(datos,"codigo",codigo)==True:
        diccionario=ubicacion_valor(datos,"codigo",codigo)    
        diccionario["codigo"]=codigo
        
        while bandera==False:
            nombre=input("Ingrese el nombre del producto a actualizar: ") 
            if validar_contiene_contenido(nombre)==True and validar_contiene_letras(nombre)==True:
                bandera=True
        bandera=False
        diccionario["nombre"]= nombre
        
        while bandera==False:
            marca=input("Ingrese la marca del producto a actualizar: ")
            if validar_contiene_contenido(marca)==True and validar_contiene_letras(marca)==True:
                bandera=True
        bandera=False
        diccionario["marca"]=marca
        
        while bandera==False:
            precio=input("Ingrese el precio del producto a actualizar: ")
            if validar_contiene_contenido(precio)==True and validar_contiene_numeros(precio)==True:
                bandera=True
        bandera=False
        diccionario["precio"]=precio

        while bandera==False:
            cantidad=input("Ingrese la cantidad del producto a actualizar: ")
            if validar_contiene_contenido(cantidad)==True and validar_contiene_numeros(cantidad)==True:
                bandera=True
        bandera=False
        diccionario["cantidad"]=cantidad
        
        while bandera==False:
            caracteristicas=input("Ingrese las caracteristicas del producto a actualizar: ")
            if validar_contiene_contenido(caracteristicas)==True:
                bandera=True
        bandera=False
        diccionario["caracteristicas"]=caracteristicas
        
        print("El producto se ha actualizado correctamente")
        return datos
    
    else:
        print("El codigo ingresado no se encuentra registrado en la lista de productos")
        return datos

def leer_productos(datos):
    for diccionario in datos:
        for llave, valor in diccionario.items():
            if llave=="clientes":
                print(f"{llave}:")
                for i in range(len(valor)):
                    print(f"-{valor[i]}")
                    
            else:
                print(f"{llave}: {valor}")
        print("")

