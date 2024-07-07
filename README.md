# QuickTracker

Backend para la gestión de servicios y ventas de equipos de una empresa de comunicaciones que permite un sistema integral de registro y seguimiento


## Tabla de contenido 📋

- [Comenzando](#comenzando-)
  * [Pre-requisitos](#pre-requisitos-)
  * [Instalación](#instalación-)
- [Funcionamiento](#funcionamiento-%EF%B8%8F)
  * [Módulos](#módulos-)
  * [Uso](#uso-%EF%B8%8F)
- [Construido con](#construido-con-%EF%B8%8F)
- [Autor](#autor-)


## Comenzando 🚀

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.


### Pre-requisitos 📝

- Text editor(Visual Studio Code)

### Instalación 🔧

Primero se debe descargar el proyecto como ZIP.

![image](https://github.com/JoanSebastianRuiz/QuickTracker/assets/166556013/3800bc21-753d-42a4-9c3e-022e3e1a3d85)

En seguida, descomprimir el archivo, abrir el proyecto en Visual Studio Code, seleccionar el archivo main.py y ejecutar el archivo.

![image](https://github.com/JoanSebastianRuiz/QuickTracker/assets/166556013/63474dae-1976-4cc5-a136-fd28bb9da949)


## Funcionamiento ⚙️

### Módulos 🔩

El código del proyecto se organiza en cuatro módulos, que son:

- Archivos

En este módulo se encuentran todos los JSON que contienen la información de los clientes, PQR, productos, servicios, usuarios y ventas. Además de un archivo txt donde se registran las excepciones que ocurran durante la ejecución del proyecto.

![image](https://github.com/JoanSebastianRuiz/QuickTracker/assets/166556013/016c3d34-3fe9-44cc-abc9-83b7dd1c61da)

- Datos

Acá se pueden encontrar todas las funciones que permiten subir y bajar datos de los JSON y archivos txt (manejo_datos), los menús que se le muestran al usuario al elegir cada opción y las validaciones que se hacen cuando los usuarios ingresan datos.

![image](https://github.com/JoanSebastianRuiz/QuickTracker/assets/166556013/02614234-f954-42a4-9206-a23c56af5ef1)

- Operaciones

En este módulo se encuentran todas las funciones que se ejecutan cuando el usuario elige una opción de algún menú, que igualmente se encuentran ordenadas por archivos.

![image](https://github.com/JoanSebastianRuiz/QuickTracker/assets/166556013/161349cb-a6e5-4c5e-8f61-e736e693fa68)

- Reportes

Por último, acá se encuentran los reportes que se generan de los productos o servicios con su información relacionada.

![image](https://github.com/JoanSebastianRuiz/QuickTracker/assets/166556013/78e71acb-81dc-4fe5-b484-c215e6007a7a)

### Uso ⌨️

El proyecto presenta un menu principal donde se debe elegir el tipo de usuario

![image](https://github.com/JoanSebastianRuiz/QuickTracker/assets/166556013/63474dae-1976-4cc5-a136-fd28bb9da949)

Con la finalidad de poder utilizar el proyecto, a continuación se dejan credenciales para cada tipo de usuario:

```
Administrador:
- Usuario: 91218991
- Contraseña: 91218991

Empleado:
- Usuario: 64332445
- Contraseña: 64332445
```

Al ingresar con las credenciales de administrador se desplegara este menú:

![image](https://github.com/JoanSebastianRuiz/QuickTracker/assets/166556013/6a077381-eb05-4d19-8baa-f43e161e01d8)

Donde se pueden administrar los usuarios del sistema o acceder a todas las demas funcionalidades. Al seleccionar administrar usuarios, se obtendra este menú:

![image](https://github.com/JoanSebastianRuiz/QuickTracker/assets/166556013/928d198c-42f3-46ba-84a0-3ea3a324bceb)

En el cual se pueden agregar, eliminar, actualizar o listar los usuarios.
Por ejemplo, acá se listaron los usuarios, donde se imprimen todos los datos de estos mismos:

![image](https://github.com/JoanSebastianRuiz/QuickTracker/assets/166556013/71c0d198-bca4-4e30-90a3-15df3e595c69)

Igualmente, el proyecto solo termina de ejecutarse cuando el usuario lo decida, por lo cual se puede navegar entre los menus.
Acá pasamos al menú principal, que seria el mismo al que tendría acceso un empleado.

![image](https://github.com/JoanSebastianRuiz/QuickTracker/assets/166556013/556240a6-3b28-4f65-aacf-038e406c9524)

Al seleccionar la opción 1 (clientes) se desplegará el menú de clientes, donde se pueden agregar, eliminar, actualizar o listar los clientes del sistema.

![image](https://github.com/JoanSebastianRuiz/QuickTracker/assets/166556013/74951da6-8acf-467d-a236-74530f3806c5)

De la misma forma, al elegir la opción 2 (productos) se podrán agregar, eliminar, actualizar o listar los productos del sistema.

![image](https://github.com/JoanSebastianRuiz/QuickTracker/assets/166556013/6221e9cc-faac-4744-abc7-fab6363de20a)

Igualmente, al elegir la opción 3 (servicios) se pueden agregar, eliminar, actualizar o listar los servicios del sistema.

![image](https://github.com/JoanSebastianRuiz/QuickTracker/assets/166556013/c56de30d-ed3b-4de2-82ad-38a5ea6dd5ff)

Por otro lado, al seleccionar la opción 4 (ventas) será posible registrar, eliminar o listar las ventas.

![image](https://github.com/JoanSebastianRuiz/QuickTracker/assets/166556013/78f40023-b367-433c-a27e-4ca4b22cc793)

E igualmente, se puede elegir que tipos de ventas se quieren observar (ventas de servicios, productos o totales).

![image](https://github.com/JoanSebastianRuiz/QuickTracker/assets/166556013/9dca51fc-939f-4da2-bbd8-de96d1bfbc42)

A continuación, se debe escoger las fechas entre las que se se quieren observar las ventas, para ello se puede elegir desde una fecha inicial hasta una final, una fecha incicial hasta la fecha actual o solo de la fecha actual, donde se indica el formato en que se debe ingresar la fecha.

![image](https://github.com/JoanSebastianRuiz/QuickTracker/assets/166556013/be9c186e-7728-4f7b-bce7-8907cb429392)

Por otra parte, al seleccionar la opción 5 (PQR) se podrán registrar, eliminar o registrar PQRs.

![image](https://github.com/JoanSebastianRuiz/QuickTracker/assets/166556013/db09abc0-4d45-4640-b1fb-b33df94d2b27)

De igual forma, al elegir la opción 6 (Análisis ventas) se desplegará un menú donde se podrá observar el número de ventas totales, el número de ventas por articulo, el número de ventas por ubicación geográfica o el número de ventas por rango de edad. E igualmente cada opción tiene el filtrado de fechas mencionado previamente.

![image](https://github.com/JoanSebastianRuiz/QuickTracker/assets/166556013/c2343211-dc26-4c1f-bb19-6dbc1922061b)

Igualmente, al seleccionar la opción 7 (personalización servicio) se da una sugerencia de que servicio o producto ofrecer a un cliente dependiendo de si está o no registrado en el sistema. Donde se ofrecera información de los productos o servicios mas comprados por el cliente, o si el cliente no se encuentra registrado, dará información del producto o servicio más popular en el rango de edad de esta persona.

![image](https://github.com/JoanSebastianRuiz/QuickTracker/assets/166556013/cc681c06-b351-4c23-8065-349a8ef92028)

Por último, al elegir la opción 8 (reportes), el sistema permitirá generar reportes con los productos y servicios que se tienen registrados.

![image](https://github.com/JoanSebastianRuiz/QuickTracker/assets/166556013/0a0f0dd6-4756-4911-8c4b-6580ecf8c9b1)

## Construido con 🛠️

* Python


## Autor 🧑

* **Joan Sebastian Ruiz Angarita** 

---
