from datos.manejo_datos import *

def generar_reporte_productos(datos):
    vaciar_datos_txt(RUTA_REPORTE_PRODUCTOS)
    
    for diccionario in datos:
        for llave, valor in diccionario.items():
            if llave=="clientes":
                cadena=llave+" y su cantidad de compras: "
                subir_datos_txt(RUTA_REPORTE_PRODUCTOS,cadena)
                cantidad_compras=valor.copy()
                valor=set(valor)
                valor=list(valor)
                
                for i in range(len(valor)):
                    cadena="-"+valor[i]+": "+str(cantidad_compras.count(valor[i]))
                    subir_datos_txt(RUTA_REPORTE_PRODUCTOS,cadena)
               
            else:
                cadena=llave+": "+str(valor)
                subir_datos_txt(RUTA_REPORTE_PRODUCTOS,cadena)
                
        cadena=""
        subir_datos_txt(RUTA_REPORTE_PRODUCTOS,cadena)
        
    print("El reporte se ha generado correctamente")
    print("")


def generar_reporte_servicios(datos):
    vaciar_datos_txt(RUTA_REPORTE_SERVICIOS)
    
    for diccionario in datos:
        for llave, valor in diccionario.items():
            if llave=="clientes":
                cadena=llave+" y su cantidad de compras: "
                subir_datos_txt(RUTA_REPORTE_SERVICIOS,cadena)
                cantidad_compras=valor.copy()
                valor=set(valor)
                valor=list(valor)
                
                for i in range(len(valor)):
                    cadena="-"+valor[i]+": "+str(cantidad_compras.count(valor[i]))
                    subir_datos_txt(RUTA_REPORTE_SERVICIOS,cadena)
                    
            else:
                cadena=llave+": "+str(valor)
                subir_datos_txt(RUTA_REPORTE_SERVICIOS,cadena)
                
        cadena=""
        subir_datos_txt(RUTA_REPORTE_SERVICIOS,cadena)
    
    print("El reporte se ha generado correctamente")
    print("")