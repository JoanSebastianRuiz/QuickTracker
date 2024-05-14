from datos.manejo_datos import *
from operaciones.servicios import *
from datos.validaciones import *
from datetime import *
from operaciones.excepciones import *

def agregar_usuario(datos):
    usuario={}
    bandera=False
    
    while bandera==False:
        documento=input("Ingrese el documento del usuario: ")
        if validar_longitud_documento(documento)==True and validar_contiene_contenido(documento)==True and validar_contiene_numeros(documento)==True:
            bandera=True
    bandera=False
    
    if verificar_existencia_valor(datos,"documento",documento)==False:
        usuario["documento"]=documento
        usuario["rol"]="empleado"
        
        while bandera==False:
            nombre=input("Ingrese el nombre del usuario: ")
            if validar_contiene_contenido(nombre)==True and validar_contiene_letras(nombre)==True:
                bandera=True
        bandera=False
        usuario["nombre"]=nombre
        
        while bandera==False:
            contrasena=input("Ingrese la contraseña del usuario: ")
            if validar_contiene_contenido(contrasena)==True and validar_longitud_contrasena(contrasena)==True:
                bandera=True
        bandera=False
        usuario["contrasena"]=nombre
        
        fecha_actual=datetime.now().strftime("%d-%m-%Y")
        fecha_actual_formato=datetime.strptime(fecha_actual,"%d-%m-%Y")
        while bandera==False:
            fecha_nacimiento=input("Ingrese la fecha de nacimiento del usuario (formato dd-mm-aaaa): ")
            if validar_contiene_contenido(fecha_nacimiento)==True:
                try:
                    fecha_nacimiento_formato=datetime.strptime(fecha_nacimiento,"%d-%m-%Y")
                    edad = fecha_actual_formato.year - fecha_nacimiento_formato.year - int((fecha_actual_formato.month, fecha_actual_formato.day) < (fecha_nacimiento_formato.month, fecha_nacimiento_formato.day))
                    edad=str(edad)
                    bandera=True
                except Exception:
                    escribir_excepcion("Excepcion al intentar agregar fecha de nacimiento del usuario "+"\""+fecha_nacimiento+"\"")
                    print("Dato erroneo")
        
        bandera=False
        usuario["fecha nacimiento"]=fecha_nacimiento
        usuario["edad"] =edad   
            
        while bandera==False:
            departamento=input("Ingrese el departamento del usuario: ")
            if validar_contiene_contenido(departamento)==True and validar_contiene_letras(departamento)==True:
                bandera=True
        bandera=False
        usuario["departamento"]=departamento
        
        while bandera==False:
            ciudad=input("Ingrese la ciudad del usuario: ")
            if validar_contiene_contenido(ciudad)==True and validar_contiene_letras(ciudad)==True:
                bandera=True
        bandera=False    
        usuario["ciudad"]=ciudad
        
        while bandera==False:
            direccion=input("Ingrese la direccion del usuario: ")
            if validar_contiene_contenido(direccion)==True:
                bandera=True
        bandera=False    
        usuario["direccion"]=direccion

        while bandera==False:
            telefono=input("Ingrese el telefono de contacto del usuario:")
            if validar_contiene_contenido(telefono)==True and validar_contiene_numeros(telefono)==True:
                bandera=True
        bandera=False      
        usuario["telefono"]=telefono

        print("El usuario se ha agregado correctamente")
        datos.append(usuario)
        return datos
    
    else:
        print("El documento ya esta registrado en la lista de usuarios")
        return datos

  
def leer_usuarios(datos):
    for diccionario in datos:
        for llave, valor in diccionario.items():
            print(f"{llave}: {valor}")
        print("")


def actualizar_usuario(datos):
    bandera=False
    
    while bandera==False:
        documento=input("Ingrese el documento del usuario que quiere actualizar: ")
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
        diccionario["fecha nacimiento"]=fecha_nacimiento
        diccionario["edad"] =edad   
        
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
