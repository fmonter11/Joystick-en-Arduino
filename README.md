# Joystick en Arduino
## Tabla de contenidos 
* [Información General](#información-general)
* [Desarrollo](#desarrollo)
* [Setup](#setup)
* [Uso](#uso)
* [Contacto](#contacto)
## Información General
El proyecto consiste en obtener los valores máximos y mínimos de traslación de un joystick gráficamente. Un joystick es un arreglo de 2 potenciómetros que permite conocer la posición de la palanca en un eje X y un eje Y. Para leer estos valores se conectaron los canales analógicos de los potenciómetros del joystick a un Arduino MEGA y se escribió un programa en el software de Arduino que recibe los valores X y Y y los traduce de un intervalo entre 0 y 1023 a un intervalo entre -1 y 1.
## Desarrollo
Para llevar a cabo la lectura correctamente la conexión se basó en el diagrama siguiente.
![Diagrama](https://github.com/fmonter11/Joystick-en-Arduino/blob/main/Imagenes/Diagrama.png)

|         |   Eje: Y  Valor: 0   |   |
| :-------------: |:-------------:| :-------------:|
| **Valor: 0**   | ![Joystick](https://github.com/fmonter11/Joystick-en-Arduino/blob/main/Imagenes/JoyTable.png) |**Eje: X   Valor: 1023** |
|     | **X: 498 Y: 517**    |   |

Después se obtuvo el 
## Setup
![Monitor serial](https://github.com/fmonter11/Joystick-en-Arduino/blob/main/Imagenes/Monitor.png)
## Contacto
Elaborado por Fernanda Monter y Mauricio de Ariño
