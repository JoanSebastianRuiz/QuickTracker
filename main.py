"""
Claro se enfrenta a varios desafíos en la gestión de sus servicios y las ventas de equipos a sus clientes debido a la 
falta de un sistema integral de registro y seguimiento. Estos desafíos incluyen:

    - **Gestión Ineficiente de Servicios**: La empresa carece de una plataforma centralizada que permita registrar y 
    gestionar eficientemente los diferentes servicios que ofrece, como Internet de Fibra Óptica, planes pospago, prepago, 
    entre otros. Esto conduce a una gestión fragmentada y desorganizada de los servicios, lo que dificulta la identificación 
    de áreas de mejora y la optimización de la oferta de productos.

    - **Falta de Análisis de Datos**: La ausencia de un sistema de registro adecuado dificulta la recopilación y análisis 
    de datos sobre el comportamiento de los usuarios y las tendencias de consumo. La empresa no puede identificar patrones de 
    uso de servicios, preferencias de los clientes o áreas geográficas con mayor demanda, lo que limita su capacidad para tomar
    decisiones estratégicas informadas.

    - **Ventas**: la ausencia de un sistema que permita identificar y hacer seguimiento a los productos que ofrece y las ventas
    de los mismos, Claro enfrenta dificultades para llevar un registro completo de las facturas (ventas) donde se pueda 
    identificar que productos se han han vendido, cuales clientes han sido los que mas han comprado, etc.



Dicho esto, se plantea la creación del sistema mencionado con las siguientes funcionalidades:

### Funcionalidades requeridas para el Módulo de Usuarios (Administrador)

    ***Registro y Gestión de Usuarios**:*

        - Operaciones CRUD para crear, leer, actualizar y eliminar perfiles de usuarios.
        - Captura de información detallada de cada usuario, incluyendo nombre, dirección, información de contacto, entre otros.
        - Funcionalidad para asignar categorías de usuarios, como nuevos clientes, clientes regulares y clientes leales.

    **Seguimiento del Historial de Usuarios:**

        - Registro y almacenamiento de servicios utilizados por cada usuario.
        - Seguimiento de las interacciones de los usuarios con la empresa, como consultas de servicio al cliente, reclamaciones
        y sugerencias.

    **Personalización de Servicios:**

        - Utilización de datos de usuario para ofrecer servicios y promociones personalizadas.
        - Análisis de patrones de comportamiento de los usuarios para adaptar la oferta de servicios a las necesidades 
        individuales.

    **Gestión de las ventas:**

        - Registro de productos vendidos en un catálogo de productos  con sus marcas, referencias, cantidades, valores, etc.
        - Registro de ventas de servicios y productos donde se asocien con los clientes que los adquieren.

### Funcionalidades Requeridas para Cada Módulo

    **Módulo de Gestión de Servicios:**

        - Operaciones CRUD para cada tipo de servicio ofrecido, como Internet de Fibra Óptica, planes pospago, prepago, etc.
        - Capacidad para agregar, modificar y eliminar servicios según sea necesario.
        - Registro de información detallada sobre cada servicio, incluyendo características, precios, entre otros.

    **Módulo de Reportes:**

        - Generación de informes sobre la cantidad de productos/servicios ofrecidos por la empresa.
        - Análisis de datos para identificar los servicios más populares que se prestan por la empresa.
        - Informes sobre usuarios que han adquirido cada servicio o producto y con ello la cantidad de este mismo.

    **Módulo de ventas:**

        - Registro de productos y servicios basados en sus características necesarias para que los empleados puedan ofrecerlos.
        - Registro de cada una de las ventas, tanto de servicios como de productos. Así como, un registro de fechas de 
        compra, cantidades, estado, etc.
        """
        
from datos import *
from validaciones import *
from operaciones.productos import *
from operaciones.clientes import *
from operaciones.servicios import *
from operaciones.ventas import *
from operaciones.pqr import *
from operaciones.excepciones import *
from menus import *
from operaciones.analisis_ventas import *


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
        subir_datos_json(RUTA_DATOS_PQR, datos_subir)    

    elif opcion==6:
        while bandera2==0:
            menu_analisis_ventas()
            opcion=socilitar_opcion()
            datos=cargar_datos_json(RUTA_DATOS_VENTAS)
            
            if opcion==1:
                numero_ventas_articulo(datos)
            elif opcion==2:
                imprimir_ventas_totales(datos)
            elif opcion==3:
                bandera2=1

    elif opcion==7:
        bandera=1









            