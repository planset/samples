/*
  chapter 2-2
  */
#define LED_COUNT 3
#define FADE_TIME 5


int led_pins[] = {6,9,10};
int led_pwm[] = {0, 64, 128};
int led_inc[] = {1, 1, 1};

void setup() {
  int i;
  
  for (i=0; i < LED_COUNT; i++) {
    pinMode(led_pins[i], OUTPUT);
  }
}

void loop() {
  int i;
  
  for (i=0; i < LED_COUNT; i++) {
    analogWrite(led_pins[i], led_pwm[i]);
    led_pwm[i] += led_inc[i];
    if (led_pwm[i] == 255 || led_pwm[i] == 0) {
      led_inc[i] *= -1;
    }
    delay(FADE_TIME);
  }
}
