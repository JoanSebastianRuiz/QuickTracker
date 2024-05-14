from datos.validaciones import *

def verificar_login(opcion, datos):
    bandera=False
    
    if opcion==1:
        while bandera==False:
            documento=input("Ingrese su documento: ")
            if validar_longitud_documento(documento)==True and validar_contiene_contenido(documento)==True and validar_contiene_numeros(documento)==True:
                bandera=True
        bandera=False
               
        if verificar_existencia_valor(datos,"documento",documento)==True:

            while bandera==False:
                contrasena=input("Ingrese la contraseña del usuario: ")
                if validar_contiene_contenido(contrasena)==True and validar_longitud_contrasena(contrasena)==True:
                    bandera=True
            bandera=False
        
            diccionario=ubicacion_valor(datos,"documento",documento)
            if diccionario["documento"]==documento and diccionario["contrasena"]==contrasena and diccionario["rol"]=="administrador":
                print("")
                return True
            elif diccionario["rol"]!="administrador":
                print("Administrador no registrado")
                print("")
                return False
            else:
                print("Contraseña equivocada")
                print("")
                return False
        else:
            print("El documento no existe en la lista de administradores")
            print("")
            return False
    
    elif opcion==2:
        while bandera==False:
            documento=input("Ingrese su documento: ")
            if validar_longitud_documento(documento)==True and validar_contiene_contenido(documento)==True and validar_contiene_numeros(documento)==True:
                bandera=True
        bandera=False
               
        if verificar_existencia_valor(datos,"documento",documento)==True:
            while bandera==False:
                contrasena=input("Ingrese la contraseña del usuario: ")
                if validar_contiene_contenido(contrasena)==True and validar_longitud_contrasena(contrasena)==True:
                    bandera=True
            bandera=False
        
            diccionario=ubicacion_valor(datos,"documento",documento)
            if diccionario["documento"]==documento and diccionario["contrasena"]==contrasena and diccionario["rol"]=="empleado":
                print("")
                return True
            elif diccionario["rol"]!="empleado":
                print("Empleado no registrado")
                print("")
                return False
            else:
                print("Contraseña equivocada")
                print("")
                return False
        else:
            print("El documento no existe en la lista de administradores")
            print("")
            return False