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
                    datos_subir=agregar_cliente(datos)
                elif opcion==2:
                    datos_subir=eliminar_cliente(datos)
                elif opcion==3:
                    datos_subir=actualizar_cliente(datos)
                elif opcion==4:
                    leer_clientes(datos)
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
                    datos_subir=agregar_producto(datos)
                elif opcion==2:
                    datos_subir=eliminar_producto(datos)
                elif opcion==3:
                    datos_subir=actualizar_producto(datos)
                elif opcion==4:
                    leer_productos(datos)
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
                    datos_subir=agregar_servicio(datos)
                elif opcion==2:
                    datos_subir=eliminar_servicio(datos)
                elif opcion==3:
                    datos_subir=actualizar_servicio(datos)
                elif opcion==4:
                    leer_servicios(datos)
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
                    datos_subir=registrar_venta(datos)
                elif opcion==2:
                    datos_subir=eliminar_venta(datos)
                elif opcion==3:
                    leer_ventas(datos)
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
                    datos_subir=registrar_pqr(datos)
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
                    imprimir_ventas_totales(datos)
                elif opcion==2:
                    numero_ventas_articulo(datos)
                elif opcion==3:
                    numero_ventas_ubicacion(datos)
                elif opcion==4:
                    numero_ventas_rango_edad(datos)  
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
                        personalizacion_persona_registrada(datos)
                    if opcion==2:
                        personalizacion_persona_sin_registrarar(datos)
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
                        generar_reporte_servicios(datos)
                    if opcion==2:
                        datos=cargar_datos_json(RUTA_DATOS_PRODUCTOS)
                        generar_reporte_productos(datos)
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


while bandera==0:
    menu_login()
    opcion=socilitar_opcion()
    datos=cargar_datos_json(RUTA_DATOS_USUARIOS)
    if opcion==1:
        verificacion=verificar_login(opcion, datos)
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
                            datos_subir=agregar_usuario(datos)
                        elif opcion==2:
                            datos_subir=eliminar_usuario(datos)
                        elif opcion==3:
                            datos_subir=actualizar_usuario(datos)
                        elif opcion==4:
                            leer_usuarios(datos)
                        elif opcion==5:
                            bandera3=1
                        else:
                            print("Numero fuera de rango")
                            print("") 
                        subir_datos_json(RUTA_DATOS_USUARIOS, datos_subir)
                        
                        
                elif opcion==2:
                    ejecucion_menu_principal()
                elif opcion==3:
                    bandera2=1
                else:
                    print("Numero fuera de rango")
                    print("")        
                            
    elif opcion==2:
        verificacion=verificar_login(opcion, datos)
        if verificacion==True:
            ejecucion_menu_principal()
    elif opcion==3:
        bandera=1
    else:
        print("Numero fuera de rango")
        print("")   
