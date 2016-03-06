/**
 * distance sensor 
 */

#define DIST_S 0

void setup() {
  Serial.begin(9600);
}

void loop() {
  float volts;
  int cm;
  
  volts = 5.0 * (double)analogRead(DIST_S) / 1024.0; 
  cm = 60.495 * pow(volts, - 1.1904);
  
  long RealLength;
  RealLength=long(150.0/(volts-1.0)); 

  Serial.print(cm);
  Serial.print("\n");
  Serial.print(RealLength);
  Serial.print("\n");
  delay(1000);
}
