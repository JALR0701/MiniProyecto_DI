#include <Servo.h>

#define IN1  13
#define IN2  12
#define IN3  8
#define IN4  7
#define der 5
#define izq 4

byte action;

int Paso [ 8 ][ 4 ] =
{ {1, 0, 0, 0},
  {1, 1, 0, 0},
  {0, 1, 0, 0},
  {0, 1, 1, 0},
  {0, 0, 1, 0},
  {0, 0, 1, 1},
  {0, 0, 0, 1},
  {1, 0, 0, 1}
};

boolean Direction = true;
int Steps = 0;

Servo servoMotor1;
int angulo1 = 0;
Servo servoMotor2;
int angulo2 = 0;
Servo servoMotor3;
int angulo3 = 0;
Servo servoMotor4;
int angulo4 = 0;

void setup()
{
  Serial.begin(9600);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(der, OUTPUT);
  pinMode(izq, OUTPUT);
  servoMotor1.attach(11);
  servoMotor1.write(0);
  servoMotor2.attach(10);
  servoMotor2.write(0);
  servoMotor3.attach(9);
  servoMotor3.write(0);
  servoMotor4.attach(6);
  servoMotor4.write(0);
}

void loop()
{
  action = Serial.read();
  if(action == 1){
    digitalWrite(der, HIGH);
    digitalWrite(izq, LOW);
    //Serial.write(1);
  }else if(action == 2){
    digitalWrite(izq, HIGH);
    digitalWrite(der, LOW);
    //Serial.write(0);
  }else if(action == 3){
    Direction = true;
    stepper();
  }else if(action == 4){
    Direction = false;
    stepper();
  }else if(action == 5){
    angulo1++;
    servoMotor1.write(angulo1);
    delay(20);
  }else if(action == 6){
    angulo1--;
    servoMotor1.write(angulo1);
    delay(20);
  }else if(action == 7){
    angulo2++;
    servoMotor2.write(angulo2);
    delay(20);
  }else if(action == 8){
    angulo2--;
    servoMotor2.write(angulo2);
    delay(20);
  }else if(action == 9){
    angulo3++;
    servoMotor3.write(angulo3);
    delay(20);
  }else if(action == 10){
    angulo3--;
    servoMotor3.write(angulo3);
    delay(20);
  }else if(action == 11){
    angulo4++;
    servoMotor4.write(angulo4);
    delay(20);
  }else if(action == 12){
    angulo4--;
    servoMotor4.write(angulo4);
    delay(20);
  }else{
    digitalWrite(der, LOW);
    digitalWrite(izq, LOW);
  }
}

void stepper()            //Avanza un paso
{
  SetDirection();
  digitalWrite( IN1, Paso[Steps][ 0] );
  digitalWrite( IN2, Paso[Steps][ 1] );
  digitalWrite( IN3, Paso[Steps][ 2] );
  digitalWrite( IN4, Paso[Steps][ 3] );
}

void SetDirection()
{
  if (Direction)
    Steps++;
  else
    Steps--;
   delay (2);

  Steps = ( Steps + 8 ) % 8 ;
}
