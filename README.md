# Algoritmos y Estructuras de Datos Examen Final 16/02/2023 - Regulares 2015+ [Python y PE]
>  Una agencia de turismo requiere un programa para gestionar los paquetes de viajes que vende a sus clientes. Por cada paquete vendido se tienen los siguientes datos: número de identificación (un entero), nombre o título descriptivo (una cadena), un número entre 0 y 9 para indicar medio de transporte (Por ejemplo: 0: aéreo, 1: ómnibus, etc.), un número flotante para indicar el monto que se cobró, otro número entero pero entre 1 y 50 para indicar el destino final del viaje pactado, y finalmente el nombre del cliente que compró el paquete (una cadena).
## En base a lo anterior, desarrollar un programa completo que disponga al menos de dos módulos [Máximo 4 puntos por este requerimiento, incluyendo también convenciones de estilo y otros aspectos del programa general]:
### En uno de ellos, definir la clase Paquete que represente al registro a usar en el programa, y las funciones básicas para operar con registros de ese tipo.
### En otro módulo, incluir el programa principal y las funciones generales que sean necesarias. Para la carga de datos, aplique las validaciones que considere necesarias. El programa debe basarse en un menú de opciones para desarrollar las siguientes tareas:
1. Generar un arreglo de n registros de tipo Paquete que contenga los datos de los paquetes vendidos (cargue el
valor de n por teclado validando que sea correcto). Puede generar el arreglo cargando los datos en forma manual o generando los datos en forma aleatoria. El arreglo debe permanecer en todo momento ordenado por el número de ticket durante la carga. Cada vez que se seleccione esta opción, el arreglo debe ser generado nuevamente desde cero. Será considerada la eficiencia de la estrategia de carga y los algoritmos que aplique. [Máximo 4 puntos entre los ítems 1 y 2 juntos].

2. Mostrar todos los datos del arreglo generado en el punto 1, a razón de un registro por renglón. Al final del listado,
muestre una línea adicional con el la cantidad de registros que se mostraron. [Máximo 4 puntos entre los ítems 1 y 2 juntos].

3. En base al arreglo generado en el punto 1 determinar si existe un paquete cuyo título o descripción sea tit (cargar
tit por teclado). Si existe, informe solo el número de identificación de ese paquete y el nombre del cliente que lo compró. Si no existe, informe con un mensaje. La búsqueda debe detenerse al encontrar el primer registro que cumpla el criterio de búsqueda pedido. [Máximo 4 puntos].

4. En base al arreglo generado en el punto 1, determinar cuántos paquetes hay para combinación entre tipo de
medio de transporte y destino final (un contador para los que sean tipo de transporte 0 y destino 1, otro para el tipo 0 y destino 2, y así sucesivaente para las 10*50 = 500 combinaciones posibles). Mostrar solo los contadores diferentes de cero. [Máximo 4 puntos],

5. En base al arreglo generado en el punto 1 determinar el monto acumulado que haya pagado el cliente cuyo
nombre es nom (cargue la cadena nom por teclado). Note que ese nombre podría estar varias veces en el vector, y ahora sí se pide acumular todos sus pagos. Si no existe ningún cliente con ese nombre, informe con un mensaje. [Máximo 4 puntos].

6. Grabar en un archivo binario los datos de los registros del arreglo generado en el punto 1 que correspondan a
paquetes cuyo monto sea mayor a 100.000 [Máximo 4 puntos].

7. Mostrar el archivo generado en el punto 6. Muestre al final una línea extra indicando el monto acumulado entre
los registros que se mostraron. [Máximo 4 puntos].

# Criterios generales de corrección: La suma total de puntos llega a un máximo de 28 (considerando los 4 puntos por el programa general y convenciones de estilo), y la nota final del práctico (que puede ser modificada de acuerdo al eventual coloquio teórico) sale de la tabla siguiente (observe que necesita un 60% del total para aprobar):

| NOTA | PORCENTAJE | CAUFICACIÓN |
|------|------------|-------------|
| 1    |     X      | Insuficiente|
| 2    |     X      | Insuficiente|
| 3    |     X      | Insuficiente|
| 4    |     X      | Insuficiente|
| 5    |     X      | Insuficiente|
| 6    | 60% a 68%  | Aprobado    |
| 7    | 69% a 77%  | Bueno       |
| 8    | 78% a 86%  | Muy Bueno   |
| 9    | 87% a 95%  | Distinguido |
| 10   | 96% a 100% |Sobresaliente|
