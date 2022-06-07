# **WebStore - Disappi**
## **Informática I.**

## **Realizado por**:

- Camilo Andres Nuñez Zabaleta - 20221099022
- Jorge Hernan Moreno Linares - 20221099021
- Jorge Luis Roncancio Turriago - 20221099019
- Cesar Augusto Orozco Manotas - 20221099023
- Carlos Enrique Hernandez Blanco - 20221099030

## **Introducción**

>El siguiente proyecto es una simulación de una tienda online, la cual se limita a la interacción entre clientes, productos y órdenes de compra. Para funcionar, realiza el consumo de una serie de servicios tipo **REST** que realizan todas las acciones asociadas al **CRUD** de la base de datos; estos servicios están cada uno en contenedores de Docker al igual que la base de datos. La organización y ejecución del proyecto se realizó utilizando la metodología **SCRUM**, simplificándola un poco por temas de tiempo, pero de igual manera realizando el planning correspondiente y sus dailys o seguimientos respectivos de las tareas planeadas por el equipo. En el siguiente enlace se puede ver la ejecución de SCRUM: https://trello.com/b/754aWgjQ/informaticai

>La tienda está compuesta por un backend, codificado en python, separando la lógica de negocio, utilizando una estructura de servicios que utilizan modelos para la representación de las entidades en la base de datos, conexiones estándar que permiten realizar el CRUD de la misma, configuraciones de archivos "Dockerfile" que definen la imagen y el código a implementar en el contenedor, utilización de archivos "requirements.txt" para la resolución de dependencias y finalmente el uso de pruebas unitarias que verifican las funcionalidades codificadas.

>Adicionalmente, cuenta con una capa visual que hace uso del backend anterior, renderizando templates de html para dar una interacción mucho más amigable del proyecto para el usuario (sin dejar de lado, en ningún momento, el consumo de servicios independientes para cada una de las tareas del CRUD a través de Docker) y configurando un archivo "nginx.conf" en donde se especifican las rutas de acceso para cada uno de los servicios de la tienda.

### **Las siguientes acciones se pueden realizar en la tienda online:**
1. Crear / Añadir
    - Clientes
    - Productos
    - Carro de compras
2. Consultar / Ver
    - Clientes
    - Productos
    - Carro de compras
    - Compras
3. Modificar / Finalizar
    - Clientes
    - Productos
    - Carro de compras
    - Compras
4. Eliminar
    - Clientes
    - Productos
    - Carro de compras

### **Tener en cuenta:**
- Se debe tener instalado Docker para la ejecución de los contenedores necesarios.
- Se recomienda tener instalado Git Bash para realizar la ejecución del instructivo.

**En entorno Windows***
- Ingresar al directorio raíz del proyecto.
- Para iniciar la ejecución, ejecutar en un git bash el archivo bash "start.sh".
```
bash strat.sh
```
- Verificar que los contenedores de Docker estén levantados.
```
docker-compose ps
```
- Para detener la ejecución, ejecutar en un git bash el archivo "stop.sh"
```
bash stop.sh
```

**En entorno Linux/MacOS**
- Abrir el proyecto en el editor de preferencia.
- Para iniciar la ejecución, ejecutar en consola el archivo bash "start.sh".
```
bash start.sh
```
- Para detener la ejecución, ejecutar en consola el archivo bash "stop.sh".
```
bash stop.sh
```

### **Instrucciones para utilizar la tienda**

1. Abrir en el navegador una nueva ventana e ingresar la URL "http://localhost:8080".
2. En la pantalla que se visualiza, se tiene un menú en la parte superior que contiene las funcionalidades del CRUD que se pueden utilizar.
3. Para crear clientes, productos o carros de compra, se debe dar click en "Crear / Añadir" y seleccionar la opción requerida del menú desplegable.
4. Ingresar los datos solicitados para guardar el registro.
5. Si se desea crear más clientes, productos o carros de compra, se puede hacer uso del mismo formulario o cambiar de opción de creación haciendo uso del menú en la parte superior.
6. Si se desea volver al menú principal se debe dar click en "TIENDA".
7. Cuanto se tengan los clientes, productos y carros de compra creados, se puede proceder a consultarlos haciendo click en "Consultar / Ver" y seleccionando la opción requerida del menú desplegable.
8. Se puede cambiar de opción de consulta haciendo uso del menú en la parte superior.
9. Volviendo al menú principal haciendo click en "TIENDA", se puede proceder a modificar los clientes, productos y carros de compra haciendo click en "Modificar / Finalizar" y seleccionando la opción requerida del menú desplegable.
10. Modificar la información necesaria o finalizar un carro de compras para guardar la información.
11. Si se desea modificar más clientes, productos o carros de compra, se puede hacer uso del mismo formulario o cambiar de opción de modificación haciendo uso del menú en la parte superior.
12. Finalmente, regresando al menú principal haciendo click en "TIENDA", se puede proceder a eliminar los clientes, productos y carros de compra haciendo click en "Eliminar" y seleccionando la opción requerida del menú desplegable.
13. Ingresar el id de la opción a eliminar para eliminar el registro.