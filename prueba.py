from datos.validaciones import *

bandera=False
while bandera==False:
    fecha_inicial=input("Ingrese la fecha inicial desde la cual quiere realizar el analisis (formato dd-mm-aaaa): ")
    if validar_contiene_contenido(fecha_inicial)==True:
        try:
            fecha_inicial_formato=datetime.strptime(fecha_inicial,"%d-%m-%Y")
            bandera=True
        except Exception:
            escribir_excepcion("Excepcion al intentar agregar fecha de nacimiento del cliente "+"\""+fecha_inicial+"\"")
bandera=False

while bandera==False:
    fecha_final=input("Ingrese la fecha final hasta la cual quiere realizar el analisis (formato dd-mm-aaaa): ")
    if validar_contiene_contenido(fecha_final)==True:
        try:
            fecha_final_formato=datetime.strptime(fecha_final,"%d-%m-%Y")
            bandera=True
        except Exception:
            escribir_excepcion("Excepcion al intentar agregar fecha de nacimiento del cliente "+"\""+fecha_final+"\"")
bandera=False

print(fecha_final_formato>fecha_inicial_formato)