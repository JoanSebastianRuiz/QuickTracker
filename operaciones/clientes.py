from datos import *
from operaciones.servicios import *
from validaciones import *
from datetime import *
from operaciones.excepciones import *

def agregar_cliente(datos):
    cliente={}
    bandera=False
    
    while bandera==False:
        documento=input("Ingrese el documento del cliente: ")
        if validar_longitud_documento(documento)==True and validar_contiene_contenido(documento)==True and validar_contiene_numeros(documento)==True:
            bandera=True
    bandera=False
    
    if verificar_existencia_valor(datos,"documento",documento)==False:
        cliente["documento"]=documento
        
        while bandera==False:
            nombre=input("Ingrese el nombre del cliente: ")
            if validar_contiene_contenido(nombre)==True and validar_contiene_letras(nombre)==True:
                bandera=True
        bandera=False
        cliente["nombre"]=nombre

        fecha_actual=datetime.now().strftime("%d-%m-%Y")
        fecha_actual_formato=datetime.strptime(fecha_actual,"%d-%m-%Y")
        while bandera==False:
            fecha_nacimiento=input("Ingrese la fecha de nacimiento del cliente (formato dd-mm-aaaa): ")
            if validar_contiene_contenido(fecha_nacimiento)==True:
                try:
                    fecha_nacimiento_formato=datetime.strptime(fecha_nacimiento,"%d-%m-%Y")
                    edad = fecha_actual_formato.year - fecha_nacimiento_formato.year - int((fecha_actual_formato.month, fecha_actual_formato.day) < (fecha_nacimiento_formato.month, fecha_nacimiento_formato.day))
                    edad=str(edad)
                    bandera=True
                except Exception:
                    escribir_excepcion("Excepcion al intentar agregar fecha de nacimiento al cliente "+"\""+fecha_nacimiento+"\"")
                    print("Dato erroneo")
        
        bandera=False
        cliente["fecha nacimiento"]=fecha_nacimiento
        cliente["edad"] =edad   
            
        while bandera==False:
            departamento=input("Ingrese el departamento del cliente: ")
            if validar_contiene_contenido(departamento)==True and validar_contiene_letras(departamento)==True:
                bandera=True
        bandera=False
        cliente["departamento"]=departamento
        
        while bandera==False:
            ciudad=input("Ingrese la ciudad del cliente: ")
            if validar_contiene_contenido(ciudad)==True and validar_contiene_letras(ciudad)==True:
                bandera=True
        bandera=False    
        cliente["ciudad"]=ciudad
        
        while bandera==False:
            direccion=input("Ingrese la direccion del cliente: ")
            if validar_contiene_contenido(direccion)==True:
                bandera=True
        bandera=False    
        cliente["direccion"]=direccion

        while bandera==False:
            telefono=input("Ingrese el telefono de contacto del cliente:")
            if validar_contiene_contenido(telefono)==True and validar_contiene_numeros(telefono)==True:
                bandera=True
        bandera=False      
        cliente["telefono"]=telefono

        while bandera==False:
            imprimir_opciones_categoria_cliente()
            posicion_categoria=socilitar_opcion()
            if posicion_categoria>=1 and posicion_categoria<=len(LISTA_CATEGORIA_CLIENTE) and validar_contiene_contenido(posicion_categoria)==True and validar_contiene_numeros(posicion_categoria)==True:
                bandera=True
            elif posicion_categoria<1 or posicion_categoria>len(LISTA_CATEGORIA_CLIENTE):
                print("Numero de opcion fuera de rango")

        cliente["categoria_cliente"]=LISTA_CATEGORIA_CLIENTE[posicion_categoria-1]

        print("El cliente se ha agregado correctamente")
        datos.append(cliente)
        return datos
    
    else:
        print("El documento ya esta registrado en la lista de clientes")
        return datos

  
def leer_clientes(datos):
    for diccionario in datos:
        for llave, valor in diccionario.items():
            print(f"{llave}: {valor}")
        print("")


def actualizar_cliente(datos):
    bandera=False
    
    while bandera==False:
        documento=input("Ingrese el documento del cliente que quiere actualizar: ")
        if validar_longitud_documento(documento)==True and validar_contiene_contenido(documento)==True and validar_contiene_numeros(documento)==True:
            bandera=True
    bandera=False
    
    if verificar_existencia_valor(datos,"documento",documento)==True:
        diccionario=ubicacion_valor(datos,"documento",documento)
                
        while bandera==False:
            nombre=input("Ingrese el nombre del cliente: ")
            if validar_contiene_contenido(nombre)==True and validar_contiene_letras(nombre)==True:
                bandera=True
        bandera=False
        diccionario["nombre"]=nombre
        
        while bandera==False:
            departamento=input("Ingrese el departamento del cliente: ")
            if validar_contiene_contenido(departamento)==True and validar_contiene_letras(departamento)==True:
                bandera=True
        bandera=False
        diccionario["departamento"]
        
        while bandera==False:
            ciudad=input("Ingrese la ciudad del cliente: ")
            if validar_contiene_contenido(ciudad)==True and validar_contiene_letras(ciudad)==True:
                bandera=True
        bandera=False
        diccionario["ciudad"]=ciudad
        
        while bandera==False:
            direccion=input("Ingrese la direccion del cliente: ")
            if validar_contiene_contenido(direccion)==True:
                bandera=True
        bandera=False                                                     
        diccionario["direccion"]=direccion
        
        while bandera==False:
            telefono=input("Ingrese el telefono de contacto del cliente:")
            if validar_contiene_contenido(telefono)==True and validar_contiene_numeros(telefono)==True:
                bandera=True
        bandera=False                  
        diccionario["telefono"]=telefono

        while bandera==False:
            imprimir_opciones_categoria_cliente()
            posicion_categoria=socilitar_opcion()
            if posicion_categoria>=1 and posicion_categoria<=len(LISTA_CATEGORIA_CLIENTE) and validar_contiene_contenido(posicion_categoria)==True and validar_contiene_numeros(posicion_categoria)==True:
                bandera=True
            elif posicion_categoria<1 or posicion_categoria>len(LISTA_CATEGORIA_CLIENTE):
                print("Numero de opcion fuera de rango")
        diccionario["categoria_cliente"]=LISTA_CATEGORIA_CLIENTE[posicion_categoria-1]

        print("El cliente se ha actualizado correctamente")  
        return datos
            
    else:
        print("El documento ingresado no se encuentra registrado en la lista de clientes")
        return datos


def eliminar_cliente(datos):
    bandera=False
    
    while bandera==False:
        documento=input("Ingrese el documento del cliente que quiere eliminar: ")
        if validar_longitud_documento(documento)==True and validar_contiene_contenido(documento)==True and validar_contiene_numeros(documento)==True:
            bandera=True   
    
    if verificar_existencia_valor(datos,"documento",documento)==True:
        diccionario=ubicacion_valor(datos,"documento",documento)
        datos.remove(diccionario)
        print("El cliente se ha eliminado correctamente")
        return datos
    else:
        print("El documento ingresado no se encuentra registrado en la lista de clientes")
        return datos

def imprimir_opciones_categoria_cliente():  
    print("Opciones de categoria de cliente: ")
    for i in range(len(LISTA_CATEGORIA_CLIENTE)):
            print(f"{i+1}. {LISTA_CATEGORIA_CLIENTE[i]}")

