# Joystick en Arduino
Por Fernanda Monter y Mauricio de Ariño

## Setup del repositorio
En el repositorio en GitHub del proyecto pueden encontrar:
- El archivo Practica_joystick.ino (código en Arduino para el joystick),
- El archivo README.md,
- La carpeta Imagenes que incluye las fotografías que se encuentran en el README.

## Información general
El proyecto consiste en obtener gráficamente los valores máximos y mínimos de traslación de un *joystick* para adaptarlo a un control, además de su valor promedio en reposo. Un joystick es un arreglo de 2 potenciómetros que permite conocer la posición de la palanca en un eje X y un eje Y. Para leer estos valores se conectaron los canales analógicos de los potenciómetros del joystick a un Arduino MEGA y se escribió un programa en el software de Arduino que recibe los valores X y Y y los traduce de un intervalo entre 0 y 1023 a un intervalo entre -1 y 1 para desplegarlos gráficamente.

## Desarrollo
Para llevar a cabo la lectura correctamente se escribió un código que toma los valores del X y Y del joystick a traves de entradas analógicas (A0 y A1) y los despliega en una tabla y una gráfica. La conexión del joystick al Arduino se basó en el diagrama de la Imagen 1.

![Diagrama](https://github.com/fmonter11/Joystick-en-Arduino/blob/main/Imagenes/Diagrama.png)
*Imagen 1. Circuito con joystick analógico*

Después se realizó un experimento físico que consistió en mover la palanca del joystick en diversas direcciones para obtener los valores de los ejes de traslación deseados, como puede observarse en la Tabla 1.

|         |   Eje: Y  Valor: 0   |   |
| :-------------: |:-------------:| :-------------:|
| **Valor: 0**   | ![Joystick](https://github.com/fmonter11/Joystick-en-Arduino/blob/main/Imagenes/JoyTable.png) |**Eje: X   Valor: 1023** |
|     | **X: 498 Y: 517**    |   |

*Tabla 1. Valores obtenidos con el joystick analógico*

Por último, se tradujeron los valores del joystick a un intervalo de -1 a 1 y se desplegó el movimiento de la palanca de forma gráfica a través de un intervalo de tiempo, como puede apreciarse en la Gráfica 1.

![Monitor serial](https://github.com/fmonter11/Joystick-en-Arduino/blob/main/Imagenes/Monitor.png)

*Gráfica 1. Captura del Serial Plotter con gráfica sinusoidal*

