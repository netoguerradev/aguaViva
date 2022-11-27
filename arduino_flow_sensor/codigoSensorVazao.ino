double flowCalc;
volatile int cont;
long int timeStemp = millis();

void setup() {
  pinMode(2,INPUT);
  attachInterrupt(0,flowRate,RISING); 
  Serial.begin(9600);
}

void loop() {
  cont = 0; 
  interrupts();
  delay(1000);
  noInterrupts();

  if ((millis() - timeStemp) < 5000){
    timeStemp = millis();
    calculoVazao = (cont*2,25);
    Serial.println("Liters per minute: ");
    Serial.println(flowCalc);
  }

  
}

void flowRate(){
  cont++;
}

//milis



