from operaciones.excepciones import *

def validar_longitud_documento(cadena):
        if len(cadena)>=8 and len(cadena)<=10:
            return True
        else:
            print("Longitud de documento invalida (8 a 10 numeros)")
            return False

def validar_longitud_contrasena(cadena):
        if len(cadena)>=6 and len(cadena)<=10:
            return True
        else:
            print("Longitud de contraseña invalida (6 a 10 caracteres)")
            return False

def validar_contiene_contenido(cadena):
        if bool(cadena)==True:
            return True
        else:
            print("El contenido ingresado esta vacio")
            return False

def validar_contiene_letras(cadena):
    lista_cadena=cadena.split(" ")
    for i in lista_cadena:
        if i.isalpha()==False:
            print("El dato solicitado debe contener solo letras")
            return False
    return True

def validar_contiene_numeros(cadena):
    if str(cadena).isdigit()==True:
        return True
    else:
        print("El dato solicitado debe contener solo numeros")
        return False

def socilitar_opcion():
    bandera=False
    while bandera==False:
        try:
            opcion=input("Ingrese el numero de la opcion que desea seleccionar: ")
            if validar_contiene_contenido(opcion)==True and validar_contiene_numeros(opcion)==True:
                bandera=True
        except Exception:
            escribir_excepcion("Excepcion al solicitar opcion ")

    print("")
    return int(opcion)

def verificar_existencia_valor(datos,llave,valor):
    for diccionario in datos:
        if diccionario[llave]==valor:
            return True
    return False

def ubicacion_valor(datos,llave,valor):
    for diccionario in datos:
        if diccionario[llave]==valor:
            return diccionario
    
