from datos.manejo_datos import *
from datetime import *
from datos.validaciones import *
from operaciones.analisis_ventas import *


def registrar_pqr(datos):
    bandera=False
    pqr={}
    datos_clientes=cargar_datos_json(RUTA_DATOS_CLIENTES)
    
    while bandera==False:
        documento=input("Ingrese el documento del cliente con el que registrara el PQR: ")
        if validar_longitud_documento(documento)==True and validar_contiene_contenido(documento)==True and validar_contiene_numeros(documento)==True:
            bandera=True
    bandera=False
    
    if verificar_existencia_valor(datos_clientes,"documento",documento)==True:
        pqr["codigo"]=len(datos)+1
        pqr["documento"]=documento
        fecha_actual=datetime.now()
        pqr["fecha"]=fecha_actual.strftime("%d-%m-%Y")
        pqr["hora"]=fecha_actual.strftime("%H:%M")

        while bandera==False:
            imprimir_opciones_pqr()
            posicion_lista_pqr=socilitar_opcion()
            if posicion_lista_pqr>=1 and posicion_lista_pqr<=len(LISTA_PQR) and validar_contiene_contenido(posicion_lista_pqr)==True and validar_contiene_numeros(posicion_lista_pqr)==True:
                bandera=True
            elif posicion_lista_pqr<1 or posicion_lista_pqr>len(LISTA_PQR):
                print("Numero de opcion fuera de rango")
        pqr["tipo de pqr"]=LISTA_PQR[posicion_lista_pqr-1]
        bandera=False
        
        while bandera==False:
            resumen=input("Ingrese un resumen de la razon del cliente para poner el PQR: ")
            if validar_contiene_contenido(resumen)==True:
                bandera=True
        pqr["resumen"]=resumen
        
        datos.append(pqr)
        print("PQR registrado correctamente")
        return datos
    
    else:
        print("El documento ingresado no se encuentra registrado en la lista de clientes")
        return datos

def leer_pqr(datos):
    bandera=False
    
    while bandera==False:
        imprimir_opciones_pqr()
        posicion_lista_pqr=socilitar_opcion()
        if posicion_lista_pqr>=1 and posicion_lista_pqr<=len(LISTA_PQR) and validar_contiene_contenido(posicion_lista_pqr)==True and validar_contiene_numeros(posicion_lista_pqr)==True:
            bandera=True
        elif posicion_lista_pqr<1 or posicion_lista_pqr>len(LISTA_PQR):
            print("Numero de opcion fuera de rango")
    
    lista_fechas=solicitar_fechas()
    fecha_inicial=lista_fechas[0]
    fecha_final=lista_fechas[1]
       
    for diccionario in datos:
        if diccionario["tipo de pqr"]==LISTA_PQR[posicion_lista_pqr-1] and datetime.strptime(diccionario["fecha"],"%d-%m-%Y")>=fecha_inicial and datetime.strptime(diccionario["fecha"],"%d-%m-%Y")<=fecha_final:
            for llave, valor in diccionario.items():
                print(f"{llave}: {valor}")
            print("")
   
def eliminar_pqr(datos):
    bandera=False
    while bandera==False:
        codigo=input("Ingrese el codigo del PQR a eliminar:")
        if validar_contiene_contenido(codigo)==True and validar_contiene_numeros(codigo)==True:
            bandera=True
    bandera=False
    codigo=int(codigo)
    
    if verificar_existencia_valor(datos,"codigo",codigo)==True:
        diccionario=ubicacion_valor(datos,"codigo",codigo) 
        datos.remove(diccionario)
        print("El PQR se ha eliminado correctamente")
        return datos
    else:
        print("El codigo ingresado no se encuentra registrado en la lista de PQRs")
        return datos

def imprimir_opciones_pqr():
    print("Opciones de PQR: ")
    for i in range(len(LISTA_PQR)):
                print(f"{i+1}: {LISTA_PQR[i]}")