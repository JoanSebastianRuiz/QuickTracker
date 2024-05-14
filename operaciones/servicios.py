from datos.validaciones import *

def agregar_servicio(datos):
    servicio={}
    bandera=False
    
    while bandera==False:
        nombre=input("Ingrese el nombre del servicio a agregar: ") 
        if validar_contiene_contenido(nombre)==True and validar_contiene_letras(nombre)==True:
            bandera=True
    bandera=False
    
    if verificar_existencia_valor(datos,"nombre",nombre)==False:    
        servicio["codigo"]=len(datos)+1
        servicio["nombre"]= nombre
        
        while bandera==False:
            precio=input("Ingrese el precio del servicio a agregar: ")
            if validar_contiene_contenido(precio)==True and validar_contiene_numeros(precio)==True:
                bandera=True
        bandera=False
        servicio["precio"]=precio
        
        while bandera==False:
            caracteristicas=input("Ingrese las caracteristicas del servicio a agregar: ")
            if validar_contiene_contenido(caracteristicas)==True:
                bandera=True
        bandera=False
        servicio["caracteristicas"]=caracteristicas
        
        servicio["clientes"]=[]
        
        datos.append(servicio)
        print("El servicio se ha agregado correctamente")
        return datos
    
    else:
        print("El nombre ingresado ya se encuentra registrado en la lista de servicios")
        return datos

def eliminar_servicio(datos):
    while bandera==False:
        codigo=input("Ingrese el codigo del servicio a eliminar:")
        if validar_contiene_contenido(codigo)==True and validar_contiene_numeros(codigo)==True:
            bandera=True
    bandera=False
    
    if verificar_existencia_valor(datos,"codigo",codigo)==True:
        diccionario=ubicacion_valor(datos,"codigo",codigo) 
        datos.remove(diccionario)
        print("El servicio se ha eliminado correctamente")
        return datos
    else:
        print("El codigo ingresado no se encuentra registrado en la lista de servicios")
        return datos

def actualizar_servicio(datos):
    bandera=False
    while bandera==False:
        codigo=input("Ingrese el codigo del servicio a actualizar:")
        if validar_contiene_contenido(codigo)==True and validar_contiene_numeros(codigo)==True:
            bandera=True
    bandera=False
    
    if verificar_existencia_valor(datos,"codigo",codigo)==True:
        diccionario=ubicacion_valor(datos,"codigo",codigo)    
        diccionario["codigo"]=codigo
        
        while bandera==False:
            nombre=input("Ingrese el nombre del servicio a actualizar: ") 
            if validar_contiene_contenido(nombre)==True and validar_contiene_letras(nombre)==True:
                bandera=True
        bandera=False
        diccionario["nombre"]= nombre

        while bandera==False:
            precio=input("Ingrese el precio del servicio a actualizar: ")
            if validar_contiene_contenido(precio)==True and validar_contiene_numeros(precio)==True:
                bandera=True
        bandera=False
        diccionario["precio"]=precio

        while bandera==False:
            caracteristicas=input("Ingrese las caracteristicas del servicio a actualizar: ")
            if validar_contiene_contenido(caracteristicas)==True:
                bandera=True
        bandera=False
        diccionario["caracteristicas"]=caracteristicas
        
        print("El servicio se ha actualizado correctamente")
        return datos
    
    else:
        print("El codigo ingresado no se encuentra registrado en la lista de servicios")
        return datos

def leer_servicios(datos):
    for diccionario in datos:
        for llave, valor in diccionario.items():
            if llave=="clientes":
                print(f"{llave} y su cantidad de compras:")
                cantidad_compras=valor.copy()
                valor=set(valor)
                valor=list(valor)
                
                for i in range(len(valor)):
                    print(f"-{valor[i]}: {cantidad_compras.count(valor[i])}")
                    
            else:
                print(f"{llave}: {valor}")
        print("")

