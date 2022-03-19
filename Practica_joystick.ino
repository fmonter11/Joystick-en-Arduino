//Declaramos los pines que usaremos
//Dos de ellos analogicos para x & y
int VRx = A0;
int VRy = A1;
int SW = 2;

//Declaramos otras variables auxiliares
int xPosition = 0;
int yPosition = 0;
int SW_state = 0;
int mapX = 0;
int mapY = 0;

void setup() {
  //Inicializamos la velocidad en bits del monitos serial
  Serial.begin(9600); 

  //Declaramos el modo de uso de los pines
  pinMode(VRx, INPUT);
  pinMode(VRy, INPUT);
  //El pin del pushbutton utiliza una resistencia del arduino
  pinMode(SW, INPUT_PULLUP); 
  
}

void loop() {
  //Obtenemos los valores de entrada (leyendolos)
  xPosition = analogRead(VRx);
  yPosition = analogRead(VRy);
  SW_state = digitalRead(SW);

  //Mappeamos los valores de 0:1023 a -1023:1023 
  //mapX = map(xPosition, 0, 1023, -1023, 1023);
  //mapY = map(yPosition, 0, 1023, 1023, -1023);

  //Hacemos la impresiòn de los valores
  Serial.print("X: ");
  //Dividimos los valores entre 1023.0 (en decimal) para que se vuelvan de -1:1
  Serial.print(xPosition);
  Serial.print(" | Y: ");
  Serial.print(yPosition);
  Serial.print(" | Button: ");
  Serial.println(SW_state);
  //Ponemos un pequeño delay entre cada medición
  delay(100);
  
}
