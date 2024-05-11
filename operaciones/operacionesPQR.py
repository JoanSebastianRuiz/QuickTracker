"""
    **Seguimiento del Historial de Usuarios:**

        - Registro y almacenamiento de servicios utilizados por cada usuario.
        - Seguimiento de las interacciones de los usuarios con la empresa, como consultas de servicio al cliente, reclamaciones
        y sugerencias.
"""
from datos import *
from datetime import *

def registrar_pqr(datos):
    pqr={}
    datos_clientes=cargar_datos_json(RUTA_DATOS_CLIENTES)
    documento_encontrado=False
    documento=input("Ingrese el documento del cliente: ")
    
    for diccionario in datos_clientes:
        if diccionario["documento"]==documento:
            documento_encontrado=True
            objeto_hora=datetime.strptime(input("Ingrese la hora: "), "%H:%M")
            pqr["hora"]=str(objeto_hora.time())

            objeto_fecha=datetime.strptime(input("Ingrese la fecha: "), "%d-%m-%Y")
            pqr["fecha"]=str(objeto_fecha.date())
            print("Opciones de PQR: ")

            for i in range(len(LISTA_PQR)):
                print(f"{i+1}: {LISTA_PQR[i]}")

            posicion_lista_pqr=int(input("Seleccione la opcion de pqr que desea registrar: "))-1
            pqr["tipo de pqr"]=LISTA_PQR[posicion_lista_pqr]
            pqr["resumen"]=input("Ingrese un resumen de la razon del cliente para poner el pqr: ")
            datos.append(pqr)
            break
    
    if documento_encontrado==False:
        print("El documento ingresado no se encuentra registrado en la lista de clientes")

#def leer_pqr(datos):
#    for diccionario in datos:
#        