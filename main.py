from datos.manejo_datos import *
from datos.validaciones import *
from datos.menus import *
from operaciones.productos import *
from operaciones.clientes import *
from operaciones.servicios import *
from operaciones.ventas import *
from operaciones.pqr import *
from operaciones.excepciones import *
from operaciones.analisis_ventas import *
from operaciones.personalizacion_servicio import *
from operaciones.reportes import *
from operaciones.login import *
from operaciones.usuarios import *


bandera=0
bandera2=0
bandera3=0


def ejecucion_menu_principal():
    bandera=0
    bandera2=0
          
    while bandera==0:
        bandera2=0
        menu_principal()
        opcion=socilitar_opcion()

        if opcion==1:
            while bandera2==0:
                menu_clientes()
                opcion=socilitar_opcion()
                datos=cargar_datos_json(RUTA_DATOS_CLIENTES)     
                datos_subir=datos      
                if opcion==1:
                    try:
                        datos_subir=agregar_cliente(datos)
                    except Exception:
                        escribir_excepcion("Excepcion al intentar agregar cliente ")
                elif opcion==2:
                    try:
                        datos_subir=eliminar_cliente(datos)
                    except Exception:
                        escribir_excepcion("Excepcion al intentar eliminar cliente ")
                elif opcion==3:
                    try:
                        datos_subir=actualizar_cliente(datos)
                    except Exception:
                        escribir_excepcion("Excepcion al intentar actualizar cliente ")
                elif opcion==4:
                    try:
                        leer_clientes(datos)
                    except Exception:
                        escribir_excepcion("Excepcion al intentar leer clientes ")
                elif opcion==5:
                    bandera2=1
                else:
                    print("Numero fuera de rango")
                    print("") 
                subir_datos_json(RUTA_DATOS_CLIENTES, datos_subir)

        elif opcion==2:
            while bandera2==0:
                menu_productos()
                opcion=socilitar_opcion()
                datos=cargar_datos_json(RUTA_DATOS_PRODUCTOS)
                datos_subir=datos
                if opcion==1:
                    try:                
                        datos_subir=agregar_producto(datos)
                    except Exception:
                        escribir_excepcion("Excepcion al intentar agregar producto ")
                elif opcion==2:
                    try:
                        datos_subir=eliminar_producto(datos)
                    except Exception:
                        escribir_excepcion("Excepcion al intentar eliminar producto ")
                elif opcion==3:
                    try:
                        datos_subir=actualizar_producto(datos)
                    except Exception:
                        escribir_excepcion("Excepcion al intentar actualizar producto ")
                elif opcion==4:
                    try:
                        leer_productos(datos)
                    except Exception:
                        escribir_excepcion("Excepcion al intentar leer productos ")
                elif opcion==5:
                    bandera2=1
                else:
                    print("Numero fuera de rango")
                    print("") 
                subir_datos_json(RUTA_DATOS_PRODUCTOS,datos_subir)

        elif opcion==3:
            while bandera2==0:
                menu_servicios()
                opcion=socilitar_opcion()
                datos=cargar_datos_json(RUTA_DATOS_SERVICIOS)
                datos_subir=datos
                if opcion==1:
                    try:
                        datos_subir=agregar_servicio(datos)
                    except Exception:
                        escribir_excepcion("Excepcion al intentar agregar servicio ")
                elif opcion==2:
                    try:
                        datos_subir=eliminar_servicio(datos)
                    except Exception:
                        escribir_excepcion("Excepcion al intentar eliminar servicio ")
                elif opcion==3:
                    try:
                        datos_subir=actualizar_servicio(datos)
                    except Exception:
                        escribir_excepcion("Excepcion al intentar actualizar servicio ")
                elif opcion==4:
                    try:
                        leer_servicios(datos)
                    except Exception:
                        escribir_excepcion("Excepcion al intentar leer servicios ")
                elif opcion==5:
                    bandera2=1
                else:
                    print("Numero fuera de rango")
                    print("") 
                subir_datos_json(RUTA_DATOS_SERVICIOS, datos_subir)

        elif opcion==4:
            while bandera2==0:
                menu_ventas()
                opcion=socilitar_opcion()
                datos=cargar_datos_json(RUTA_DATOS_VENTAS)
                datos_subir=datos
                if opcion==1:
                    try:
                        datos_subir=registrar_venta(datos)
                    except Exception:
                        escribir_excepcion("Excepcion al intentar registrar venta ")
                elif opcion==2:
                    try:
                        datos_subir=eliminar_venta(datos)
                    except Exception:
                        escribir_excepcion("Excepcion al intentar eliminar venta ")
                elif opcion==3:
                    try:
                        leer_ventas(datos)
                    except Exception:
                        escribir_excepcion("Excepcion al intentar leer ventas ")
                elif opcion==4:
                    bandera2=1
                else:
                    print("Numero fuera de rango")
                    print("") 
                subir_datos_json(RUTA_DATOS_VENTAS,datos_subir)
                
        elif opcion==5:
            while bandera2==0:
                menu_pqr()
                opcion=socilitar_opcion()
                datos=cargar_datos_json(RUTA_DATOS_PQR)
                datos_subir=datos
                if opcion==1:
                    try:
                        datos_subir=registrar_pqr(datos)
                    except Exception:
                        escribir_excepcion("Excepcion al intentar registrar PQR ")
                elif opcion==2:
                    try:
                        leer_pqr(datos)
                    except Exception:
                        escribir_excepcion("Excepcion al intentar leer PQRs ")
                elif opcion==3:
                    bandera2=1
                else:
                    print("Numero fuera de rango")
                    print("") 
                subir_datos_json(RUTA_DATOS_PQR, datos_subir)    

        elif opcion==6:
            while bandera2==0:
                menu_analisis_ventas()
                opcion=socilitar_opcion()
                datos=cargar_datos_json(RUTA_DATOS_VENTAS)
                
                if opcion==1:
                    try:
                        imprimir_ventas_totales(datos)
                    except Exception:
                        escribir_excepcion("Excepcion al intentar imprimir ventas totales ")
                elif opcion==2:
                    try:
                        numero_ventas_articulo(datos)
                    except Exception:
                        escribir_excepcion("Excepcion al intentar imprimir ventas por articulo ")
                elif opcion==3:
                    try:
                        numero_ventas_ubicacion(datos)
                    except Exception:
                        escribir_excepcion("Excepcion al intentar imprimir ventas por ubicacion ")
                elif opcion==4:
                    try:
                        numero_ventas_rango_edad(datos)
                    except Exception:
                        escribir_excepcion("Excepcion al intentar imprimir ventas por rango de edad ")  
                elif opcion==5:
                    bandera2=1
                else:
                    print("Numero fuera de rango")
                    print("") 
                    
        elif opcion==7:
            while bandera2==0:
                menu_personalizacion_servicio()
                opcion=socilitar_opcion()
                datos=cargar_datos_json(RUTA_DATOS_VENTAS)
                
                if opcion==1:
                    try:
                        personalizacion_persona_registrada(datos)
                    except Exception:
                        escribir_excepcion("Excepcion al intentar realizar personalizacion para persona registrada ")
                elif opcion==2:
                    try:
                        personalizacion_persona_sin_registrarar(datos)
                    except Exception:
                        escribir_excepcion("Excepcion al intentar realizar personalizacion para persona sin registrar ")
                elif opcion==3:
                    bandera2=1
                else:
                    print("Numero fuera de rango")
                    print("") 
        elif opcion==8:
            while bandera2==0:
                menu_reportes()
                opcion=socilitar_opcion()
                if opcion==1:
                    datos=cargar_datos_json(RUTA_DATOS_SERVICIOS)
                    try:
                        generar_reporte_servicios(datos)
                    except Exception:
                        escribir_excepcion("Excepcion al intentar generar reporte de servicios ")
                elif opcion==2:
                    datos=cargar_datos_json(RUTA_DATOS_PRODUCTOS)
                    try:
                        generar_reporte_productos(datos)
                    except Exception:
                        escribir_excepcion("Excepcion al intentar generar reporte de productos ")
                elif opcion==3:
                    bandera2=1
                else:
                    print("Numero fuera de rango")
                    print("") 
        elif opcion==9:
            bandera=1
        else:
            print("Numero fuera de rango")
            print("") 

#try:
while bandera==0:
        menu_login()
        opcion=socilitar_opcion()
        datos=cargar_datos_json(RUTA_DATOS_USUARIOS)
        if opcion==1:
            try:
                verificacion=verificar_login(opcion, datos)
            except Exception:
                escribir_excepcion("Excepcion al verificar login ")
            if verificacion==True:
                while bandera2==0:
                    bandera3=0
                    menu_administrador()
                    opcion=socilitar_opcion()
                    
                    if opcion==1:
                        while bandera3==0:
                            menu_usuarios()
                            datos=cargar_datos_json(RUTA_DATOS_USUARIOS)
                            datos_subir=datos
                            opcion=socilitar_opcion()     
                            if opcion==1:
                                try:
                                    datos_subir=agregar_usuario(datos)
                                except Exception:
                                    escribir_excepcion("Excepcion al agregar usuario ")
                            elif opcion==2:
                                try:
                                    datos_subir=eliminar_usuario(datos)
                                except Exception:
                                    escribir_excepcion("Excepcion al eliminar usuario ")
                            elif opcion==3:
                                try:
                                    datos_subir=actualizar_usuario(datos)
                                except Exception:
                                    escribir_excepcion("Excepcion al actualizar usuario ")
                            elif opcion==4:
                                try:
                                    leer_usuarios(datos)
                                except Exception:
                                    escribir_excepcion("Excepcion al leer usuarios ")
                            elif opcion==5:
                                bandera3=1
                            else:
                                print("Numero fuera de rango")
                                print("") 
                            subir_datos_json(RUTA_DATOS_USUARIOS, datos_subir)
                            
                            
                    elif opcion==2:
                        #try:
                            ejecucion_menu_principal()
                        #except Exception:
                            #escribir_excepcion("Excepcion al ejecutar menu principal ")
                    elif opcion==3:
                        bandera2=1
                    else:
                        print("Numero fuera de rango")
                        print("")        
                                
        elif opcion==2:
            try:
                verificacion=verificar_login(opcion, datos)
            except Exception:
                escribir_excepcion("Excepcion al verificar login ")
            if verificacion==True:
                try:
                    ejecucion_menu_principal()
                except Exception:
                    escribir_excepcion("Excepcion al ejecutar menu principal ")
        elif opcion==3:
            bandera=1
        else:
            print("Numero fuera de rango")
            print("")   

#except Exception:
    #escribir_excepcion("Excepcion al ejecutar el main ")