"""
    **Seguimiento del Historial de Usuarios:**

        - Registro y almacenamiento de servicios utilizados por cada usuario.
        - Seguimiento de las interacciones de los usuarios con la empresa, como consultas de servicio al cliente, reclamaciones
        y sugerencias.
"""
from datos import *
from datetime import *
from validaciones import *


def registrar_pqr(datos):
    bandera=False
    pqr={}
    datos_clientes=cargar_datos_json(RUTA_DATOS_CLIENTES)
    
    while bandera==False:
        documento=input("Ingrese el documento del usuario con el que quiere registrar el PQR: ")
        if validar_longitud_documento(documento)==True and validar_contiene_contenido(documento)==True and validar_contiene_numeros(documento)==True:
            bandera=True
    bandera=False
    
    if verificar_existencia_valor(datos_clientes,"documento",documento)==True:
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
        pqr["tipo de pqr"]==LISTA_PQR[posicion_lista_pqr-1]
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
    for diccionario in datos:
        for llave, valor in diccionario.items():
            print(f"{llave}: {valor}")
        print("")
   
    
def imprimir_opciones_pqr():
    print("Opciones de PQR: ")
    for i in range(len(LISTA_PQR)):
                print(f"{i+1}: {LISTA_PQR[i]}")