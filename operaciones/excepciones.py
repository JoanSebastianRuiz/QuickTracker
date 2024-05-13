from datetime import *
from datos import *

def escribir_excepcion(cadena):
    fecha_hora=datetime.now()
    fecha_hora_formateada=fecha_hora.strftime("%d-%m-%Y %H:%M")
    cadena_total=fecha_hora_formateada+" "+cadena+"\n"
    subir_datos_txt(RUTA_DATOS_EXCEPCIONES,cadena_total)
    
    
