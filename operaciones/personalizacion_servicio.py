from datos.manejo_datos import *
from datos.validaciones import *


def personalizacion_persona_registrada(datos):
    datos_clientes=cargar_datos_json(RUTA_DATOS_CLIENTES)
    datos_productos=cargar_datos_json(RUTA_DATOS_PRODUCTOS)
    datos_servicios=cargar_datos_json(RUTA_DATOS_SERVICIOS)
    bandera=False
    
    while bandera==False:
        documento=input("Ingrese el documento del cliente al que le quiere personalizar el servicio: ")
        if validar_longitud_documento(documento)==True and validar_contiene_contenido(documento)==True and validar_contiene_numeros(documento)==True:
            bandera=True
    bandera=False
    
    if verificar_existencia_valor(datos_clientes,"documento",documento)==True:
        while bandera==False:
            print("Desea una personalizacion de:")
            print("1. Servicios ")
            print("2. Productos")

            opcion=socilitar_opcion()
            if opcion>=1 and opcion<=2 and validar_contiene_contenido(opcion)==True and validar_contiene_numeros(opcion)==True:
                bandera=True
            elif opcion<1 or opcion>2:
                print("Numero de opcion fuera de rango")  
        bandera=False
        
        if opcion==1:
            lista_productos_o_servicios=lista_valores_llave_json(datos_servicios, "nombre")
            tipo_venta="servicio"
        elif opcion==2:
            lista_productos_o_servicios=lista_valores_llave_json(datos_productos, "nombre")
            tipo_venta="producto"    

        diccionario_personalizacion={}
        cont_servicios_o_productos=[]
    
        for nombre_servicio_o_producto in lista_productos_o_servicios:
            cont=0
            for diccionario in datos:
                if diccionario["articulo"]==nombre_servicio_o_producto and diccionario["documento"]==documento:
                    cont+=1
            cont_servicios_o_productos.append(cont)

        for i in range(len(cont_servicios_o_productos)):
                    diccionario_personalizacion[lista_productos_o_servicios[i]]=cont_servicios_o_productos[i]
            
        valor_mayor=0
        llave_mayor=""
        
        for llave, valor in diccionario_personalizacion.items():
            if valor>=valor_mayor:
                llave_mayor=llave
                valor_mayor=valor
        
        print(f"El {tipo_venta} que mas compro el cliente es: {llave_mayor}")
        print(f"Y la informacion asociada a este {tipo_venta} es:")
        
        if tipo_venta=="servicio":
            diccionario_servicio=ubicacion_valor(datos_servicios,"nombre",llave_mayor)
            for llave, valor in diccionario_servicio.items():
                if llave!="nombre" and llave!="clientes":
                    print(f"{llave}: {valor}")
            print("")
                        
        elif tipo_venta=="producto":  
            diccionario_producto=ubicacion_valor(datos_productos,"nombre",llave_mayor)
            for llave, valor in diccionario_producto.items():
                if llave!="nombre" and llave!="clientes":
                    print(f"{llave}: {valor}") 
            print("")

        print("Ademas, estas son las compras que ha realizado el usuario: ")
        
        for diccionario in datos_servicios:
            for llave, valor in diccionario.items():
                
                if llave=="clientes":
                    cantidad_compras=valor.copy()
                    valor=set(valor)
                    valor=list(valor)
                    for i in range(len(valor)):
                        if valor[i]==documento:
                            print(f"-{diccionario["nombre"]}: {cantidad_compras.count(valor[i])}")
                        
    else:
        print("El documento no esta registrado en la lista de clientes")
    
    print("")


def personalizacion_persona_sin_registrarar(datos):
    bandera=False
    datos_productos=cargar_datos_json(RUTA_DATOS_PRODUCTOS)
    datos_servicios=cargar_datos_json(RUTA_DATOS_SERVICIOS)
    datos_clientes=cargar_datos_json(RUTA_DATOS_CLIENTES)
    
    while bandera==False:
        print("Desea una personalizacion de:")
        print("1. Servicios ")
        print("2. Productos")

        opcion=socilitar_opcion()
        if opcion>=1 and opcion<=2 and validar_contiene_contenido(opcion)==True and validar_contiene_numeros(opcion)==True:
            bandera=True
        elif opcion<1 or opcion>2:
            print("Numero de opcion fuera de rango")  
    bandera=False
    
    if opcion==1:
        lista_productos_o_servicios=lista_valores_llave_json(datos_servicios, "nombre")
        tipo_venta="servicio"
    elif opcion==2:
        lista_productos_o_servicios=lista_valores_llave_json(datos_productos, "nombre")
        tipo_venta="producto"


    while bandera==False:
        print("Desea una personalizacion para: ")
        print("1. Adolescentes (menor de 20 años)")
        print("2. Adultos jóvenes (20-39 años)")
        print("3. Adultos de mediana edad (40-60 años)")
        print("4. Adultos mayores (mayor de 60 años)")

        opcion=socilitar_opcion()
        if opcion>=1 and opcion<=4 and validar_contiene_contenido(opcion)==True and validar_contiene_numeros(opcion)==True:
            bandera=True
        elif opcion<1 or opcion>4:
            print("Numero de opcion fuera de rango")  
    
    diccionario_personalizacion={}
    cont_servicios_o_productos=[]
    
    if opcion==1:
        
        for nombre_servicio_o_producto in lista_productos_o_servicios:
            cont=0
            for diccionario in datos:
                documento=diccionario["documento"]
                diccionario_persona=ubicacion_valor(datos_clientes,"documento",documento)
                if diccionario["articulo"]==nombre_servicio_o_producto and int(diccionario_persona["edad"])<20:
                    cont+=1
            cont_servicios_o_productos.append(cont)    
    
    elif opcion==2:
        for nombre_servicio_o_producto in lista_productos_o_servicios:
            cont=0
            for diccionario in datos:
                documento=diccionario["documento"]
                diccionario_persona=ubicacion_valor(datos_clientes,"documento",documento)
                if diccionario["articulo"]==nombre_servicio_o_producto and int(diccionario_persona["edad"])>=20 and int(diccionario_persona["edad"])<=39:
                    cont+=1
            cont_servicios_o_productos.append(cont)
    
    elif opcion==3:
        for nombre_servicio_o_producto in lista_productos_o_servicios:
            cont=0
            for diccionario in datos:
                documento=diccionario["documento"]
                diccionario_persona=ubicacion_valor(datos_clientes,"documento",documento)
                if diccionario["articulo"]==nombre_servicio_o_producto and int(diccionario_persona["edad"])>=40 and int(diccionario_persona["edad"])<=60:
                    cont+=1
            cont_servicios_o_productos.append(cont)
    
    elif opcion==4:
        for nombre_servicio_o_producto in lista_productos_o_servicios:
            cont=0
            for diccionario in datos:
                documento=diccionario["documento"]
                diccionario_persona=ubicacion_valor(datos_clientes,"documento",documento)
                if diccionario["articulo"]==nombre_servicio_o_producto and int(diccionario_persona["edad"])>60:
                    cont+=1
            cont_servicios_o_productos.append(cont)

    for i in range(len(cont_servicios_o_productos)):
            diccionario_personalizacion[lista_productos_o_servicios[i]]=cont_servicios_o_productos[i]
    
    valor_mayor=0
    llave_mayor=""
    for llave, valor in diccionario_personalizacion.items():
        if valor>=valor_mayor:
            llave_mayor=llave
            valor_mayor=valor
    
    print(f"En el rango de edades {LISTA_EDADES[opcion-1]} el {tipo_venta} mas vendido es {llave_mayor} con {valor_mayor} ventas")
    print(f"Y la informacion asociada a este {tipo_venta} es:")
    
    if tipo_venta=="servicio":
        diccionario_servicio=ubicacion_valor(datos_servicios,"nombre",llave_mayor)
        for llave, valor in diccionario_servicio.items():
            if llave!="nombre" and llave!="clientes":
                print(f"{llave}: {valor}")
                
    elif tipo_venta=="producto":  
        diccionario_producto=ubicacion_valor(datos_productos,"nombre",llave_mayor)
        for llave, valor in diccionario_producto.items():
            if llave!="nombre" and llave!="clientes":
                print(f"{llave}: {valor}")
    print("")