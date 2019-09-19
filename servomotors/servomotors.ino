char c;
#include <Servo.h> 
Servo myservo, myservo1;  // create servo object to control a servo 

void setup() 
{ 
  // Define que o servo esta ligado a porta 9
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  Serial.begin(9600);
  myservo.attach(9);
  myservo1.attach(10);
  myservo.write(180);
  myservo1.write(180);

  
} 


void loop(){
   
  

  String leitura = Serial.readString();

  if (leitura == "servo1_desligar"){
    myservo.write(90);
  }

  if (leitura == "servo1_ligar"){
    myservo.write(0);
  }

  if (leitura == "servo2_desligar"){
    myservo1.write(90);
  }

  if (leitura == "servo2_ligar"){
    myservo1.write(0);
  }

  if(leitura == "lampada1_desligar"){
    digitalWrite(2, LOW);
  }

  else if(leitura == "lampada1_ligar"){
    digitalWrite(2, HIGH);   
  }

  else if(leitura == "lampada2_desligar"){
    digitalWrite(3, LOW);
  }

  else if(leitura == "lampada2_ligar"){
    digitalWrite(3, HIGH);
  }
             

  // Converte o valor pra ser usado no servo (valores entre 0 e 180) 
       

  // Move o eixo do servo, de acordo com o angulo
              

  // Aguarda o servo atingir a posição
  //delay(200);   
}                        

