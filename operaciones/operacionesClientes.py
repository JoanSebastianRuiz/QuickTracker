#Operaciones CRUD para crear, leer, actualizar y eliminar perfiles de usuarios.
#Registro y almacenamiento de servicios utilizados por cada usuario.
#Ventas
#Servicios
from datos import *
from operaciones.operacionesServicios import *


def agregar_cliente(datos):
    usuario={}
    usuario["documento"]=input("Ingrese el documento del usuario: ")
    usuario["nombre"]=input("Ingrese el nombre del usuario: ")
    usuario["departamento"]=input("Ingrese el departamento del usuario: ")
    usuario["ciudad"]=input("Ingrese la ciudad del usuario: ")
    usuario["direccion"]=input("Ingrese la direccion del usuario: ")
    usuario["telefono"]=input("Ingrese el telefono de contacto del usuario:")

    for i in range(len(LISTA_CATEGORIA_CLIENTE)):
        print(f"{i+1}. {LISTA_CATEGORIA_CLIENTE[i]}")
    posicion_categoria=int(input("Seleccione la categoria del cliente: "))
    usuario["categoria_cliente"]=LISTA_CATEGORIA_CLIENTE[posicion_categoria-1]

    print("El cliente se ha agregado correctamente")
    datos.append(usuario)
    return datos

def leer_clientes(datos):
    for diccionario in datos:
        for llave, valor in diccionario.items():
            if llave=="servicios":
                print(f"{llave}: ",end="")
                for i in range(len(valor)):
                    if i==len(valor)-1:
                        print(f"{valor[i]}")
                    else:
                        print(f"{valor[i]}, ", end="")
            else:
                print(f"{llave}: {valor}")
        print("")

def actualizar_cliente(datos):
    documento_encontrado=False
    documento=input("Ingrese el documento del usuario que quiere actualizar: ")
    for diccionario in datos:
        if diccionario["documento"]==documento:
                documento_encontrado=True
                diccionario["nombre"]=input("Ingrese el nombre del usuario: ")
                diccionario["direccion"]=input("Ingrese la direccion del usuario: ")
                diccionario["telefono"]=input("Ingrese el telefono de contacto del usuario:")
                diccionario["departamento"]=input("Ingrese el departamento del usuario: ")
                diccionario["ciudad"]=input("Ingrese la ciudad del usuario: ")

                for i in range(len(LISTA_CATEGORIA_CLIENTE)):
                    print(f"{i+1}. {LISTA_CATEGORIA_CLIENTE[i]}")
                posicion_categoria=int(input("Seleccione la categoria del cliente: "))
                diccionario["categoria_cliente"]=LISTA_CATEGORIA_CLIENTE[posicion_categoria-1]

                print("El cliente se ha actualizado correctamente")  
               
                break
    if documento_encontrado==False:
        print("El documento ingresado no se encuentra registrado en la lista de clientes")
    return datos

def eliminar_cliente(datos):
    documento=input("Ingrese el documento del usuario que quiere eliminar: ")
    documento_encontrado=False

    for diccionario in datos:
        if diccionario["documento"]==documento:
            documento_encontrado=True
            datos.remove(diccionario)
            print("El cliente se ha eliminado correctamente")
            break
    if documento_encontrado==False:
        print("El documento ingresado no se encuentra registrado en la lista de clientes")
    return datos

