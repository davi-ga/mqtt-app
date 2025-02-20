const int pinoLDR1 = A5; //Luminosidade
const int pinoLDR2 = A4; //Luminosidade
const int pinoLDR3 = A3; //Luminosidade

int pinopir = 3; //Presença

const int waterSensorPin1 = A0; //Nível de Água
const int waterSensorPin2 = A1; //Nível de Água
int lowThreshold = 300;   
int mediumThreshold = 600; 
int highThreshold = 900;  


void setup(){
  Serial.begin(9600);
  pinMode(pinoLDR1, INPUT); 
  pinMode(pinoLDR2, INPUT); 
  pinMode(pinoLDR3, INPUT); 
  pinMode(pinopir, INPUT);
  pinMode(waterSensorPin1, INPUT);
  pinMode(waterSensorPin2, INPUT);
}

void loop(){ 
  Serial.print(String("[('Luminosidade 1','") + analogRead(pinoLDR1) + "'), ");
  Serial.print(String("('Luminosidade 2','") + analogRead(pinoLDR2) + "'), ");
  Serial.print(String("('Luminosidade 3','") + analogRead(pinoLDR3) + "'), ");

  Serial.print(String("('Presenca', ") + (digitalRead(pinopir) ? "'Sim'), " : "'Nao'), "));

  Serial.print(String("('Nivel de agua 1', ") + 
                  (analogRead(waterSensorPin1) < lowThreshold ? "'Baixo'), " : 
                  (analogRead(waterSensorPin1) < mediumThreshold ? "'Medio'), " : "'Alto'), ")));
  Serial.print(String("('Nivel de agua 2', ") + 
                  (analogRead(waterSensorPin2) < lowThreshold ? "'Baixo')]" : 
                  (analogRead(waterSensorPin2) < mediumThreshold ? "'Medio')]" : "'Alto')]")));
  
  Serial.println("");
  
  delay(1000);
}