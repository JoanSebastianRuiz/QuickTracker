from datetime import *
from datos.manejo_datos import subir_datos_txt
from datos.manejo_datos import RUTA_DATOS_EXCEPCIONES

def escribir_excepcion(cadena):
    fecha_hora=datetime.now()
    fecha_hora_formateada=fecha_hora.strftime("%d-%m-%Y %H:%M")
    cadena_total=fecha_hora_formateada+" "+cadena
    subir_datos_txt(RUTA_DATOS_EXCEPCIONES,cadena_total)
    print("Dato erroneo")
    
    
