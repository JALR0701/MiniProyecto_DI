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

int steps_left = 4095;
boolean Direction = true;
int Steps = 100;                       // Define el paso actual de la secuencia

void setup()
{
  Serial.begin(9600);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(der, OUTPUT);
  pinMode(izq, OUTPUT);
}

void loop()
{
  action = Serial.read();
  if(action == B00000001){
    digitalWrite(der, HIGH);
    digitalWrite(izq, LOW);
    //Serial.write(1);
  }else if(action == B00000010){
    digitalWrite(izq, HIGH);
    digitalWrite(der, LOW);
    //Serial.write(0);
  }else if(action == B00000011){
    Direction = true;
    stepper();
  }else if(action == B00000100){
    Direction = false;
    stepper();
  }else if(action == B00000101){
    
  }
  else{
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
