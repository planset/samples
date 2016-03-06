/**
 * switch
 */

#define LED_PIN 10
#define BUTTON 0

void setup() {
  
  pinMode(LED_PIN, OUTPUT);
  
}

void loop() {
  if (analogRead(BUTTON) < 10) {
    digitalWrite(LED_PIN, HIGH);
    delay(500);
    digitalWrite(LED_PIN, LOW);
    delay(500);
  }
}

