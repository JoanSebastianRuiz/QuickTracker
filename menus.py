def menu_principal():
    print("Bienvenido, estos son los menus disponibles para realizar operaciones: ")
    print("1. Clientes")
    print("2. Productos")
    print("3. Servicios")
    print("4. Ventas")
    print("5. PQR")
    print("6. Salir")
    print("")

def menu_clientes():
    print("Menu clientes:")
    print("1. Agregar cliente")
    print("2. Eliminar cliente")
    print("3. Actualizar cliente")
    print("4. Listar clientes")
    print("5. Salir")
    print("")

def menu_productos():
    print("Menu productos:")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Listar productos")
    print("5. Salir")
    print("")

def menu_servicios():
    print("Menu servicios:")
    print("1. Agregar servicio")
    print("2. Eliminar servicio")
    print("3. Actualizar servicio")
    print("4. Listar servicios")
    print("5. Salir")
    print("")

def menu_ventas():
    print("Menu ventas:")
    print("1. Registrar venta")
    print("2. Ver ventas totales")
    print("3. Ver ventas segun ubicacion geografica")
    print("5. Salir")
    print("")

def menu_pqr():
    print("Menu pqr:")
    print("1. Registrar PQR")
    print("2. Listar PQR")
    print("5. Salir")
    print("")

def socilitar_opcion():
    opcion=int(input("Ingrese el numero de la opcion que desea realizar: "))
    print("")
    return opcion