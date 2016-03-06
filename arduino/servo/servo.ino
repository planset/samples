#include <Servo.h>

#define SERVOPIN	(9)
#define VOLUMEPIN	(0)

Servo g_servo;


void setup() 
{ 
  g_servo.attach(SERVOPIN);
} 


/**
 * Move servo motor
 */
void output_move_motor() {
  
  g_servo.write(120); // ギアがスイッチを押す角度
  delay(1000); // モーターが動き終わるまで1秒待つ
  g_servo.write(60); // ギアがスイッチから離れる角度
  delay(1500); // モーターの動作とWebアクセスの処理を4秒待つ
  
}

void loop() 
{ 
  output_move_motor();
} 

