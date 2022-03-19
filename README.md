# Joystick en Arduino
## Por Fernanda Monter y Mauricio de Ariño

## Tabla de contenidos 
* [Información General](#información-general)
* [Desarrollo](#desarrollo)
* [Setup](#setup)
## Información General
El proyecto consiste en obtener gráficamente los valores máximos y mínimos de traslación de un joystick, además de su valor promedio en reposo. Un joystick es un arreglo de 2 potenciómetros que permite conocer la posición de la palanca en un eje X y un eje Y. Para leer estos valores se conectaron los canales analógicos de los potenciómetros del joystick a un Arduino MEGA y se escribió un programa en el software de Arduino que recibe los valores X y Y y los traduce de un intervalo entre 0 y 1023 a un intervalo entre -1 y 1 para desplegarlos gráficamente.
## Desarrollo
Para llevar a cabo la lectura correctamente se escribió un código que toma los valores del X y Y del joystick como entradas y los regresa como una tabla y una gráfica. También se basó la conexión del joystick al Arduino en el diagrama siguiente.

![Diagrama](https://github.com/fmonter11/Joystick-en-Arduino/blob/main/Imagenes/Diagrama.png)

Después se realizó una práctica física que consistió en mover la palanca del joystick en diversas direcciones para obtener los valores de los ejes de traslación deseados, como puede observarse en la siguiente tabla.
|         |   Eje: Y  Valor: 0   |   |
| :-------------: |:-------------:| :-------------:|
| **Valor: 0**   | ![Joystick](https://github.com/fmonter11/Joystick-en-Arduino/blob/main/Imagenes/JoyTable.png) |**Eje: X   Valor: 1023** |
|     | **X: 498 Y: 517**    |   |

Por último, se tradujeron los valores del joystick a un intervalo de -1 a 1 y se desplegó el movimiento de la palanca de forma gráfica a través de un intervalo de tiempo.

![Monitor serial](https://github.com/fmonter11/Joystick-en-Arduino/blob/main/Imagenes/Monitor.png)
## Setup
