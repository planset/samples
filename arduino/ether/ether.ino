/**
 *
 */
#include <SPI.h>
#include <Ethernet.h>
#include <Servo.h>
/*
#include <SPI.h>
#include <Dhcp.h>
#include <Dns.h>
#include <Ethernet.h>
#include <EthernetClient.h>
#include <EthernetServer.h>
#include <EthernetUdp.h>
#include <util.h>
*/

// test button alalog pin number
#define BUTTON 0

// dhcp
#define DHCP_ENABLED false

// サーボモータ制御のピン番号
#define PIN_SERVO 9

// イーサシールドに書いてあるMACアドレスを書くよ。
byte mac[] = { 0x90, 0xA2, 0xDA, 0x0D, 0x0F, 0x3F };
// 設定したいIPアドレス
IPAddress ip(192, 168, 10, 177);

// Initialize the Ethernet server library
// with the IP address and port you want to use 
// (port 80 is default for HTTP):
EthernetServer server(80);

// servo motor
Servo servo;


void setup()
{
  Serial.begin(9600);
  
  // start the Ethernet connection and the server:
  if (DHCP_ENABLED) {
    if (Ethernet.begin(mac) == 0) {
      Ethernet.begin(mac, ip);
    }
  } else {
    Ethernet.begin(mac, ip);
  }
  
  // print your local IP address:
  print_local_ip();
  
  // start listening for clients
  server.begin();
  
  // start 
  servo.attach(PIN_SERVO);
  servo_reset_position();
}


void loop()
{
  // listen for incoming clients
  EthernetClient client = server.available();
  
  String request = "";
  
  //if (analogRead(BUTTON) < 10) {
  //  output_move_motor();
  //}
  
  if (Serial.available() > 0) {
    char inChar = (char)Serial.read(); 
    if (inChar == '\n') {
      output_move_motor();
    }
  }
  
  if (client) {
    boolean currentLineIsBlank = true;
    while (client.connected()) {
      if (client.available()) {
        request += char(client.read());
        if (request.endsWith("\n") && currentLineIsBlank) {          
            action(&client, &request);
            break;
        }
        if (request.endsWith("\n")) {
          currentLineIsBlank = true;
        } else if (!request.endsWith("\r")) {
          currentLineIsBlank = false;
        }
          
      }
    }
    // give the web browser time to receive the data
    delay(1);
    // close the connection:
    client.stop();
  }
}



/**
 * print local ip address to serial.
 */
void print_local_ip() {
  
  Serial.print("My IP address: ");
  ip = Ethernet.localIP();
  for (byte thisByte = 0; thisByte < 4; thisByte++) {
    Serial.print(ip[thisByte], DEC);
    Serial.print("."); 
  }
  Serial.println();
  
}

/**
 * HTTPレスポンスヘッダ 200 の作成
 */
char * get_http_response_header_200() {
  return "HTTP/1.1 200 OK\nContent-Type: text/html\n\n";
}

/**
 * HTTPレスポンスヘッダ 404 の作成
 */
char * get_http_response_header_404() {
  return "HTTP/1.1 404 Not Found\n\n";
}

/**
 * HTTPレスポンスの終わり。
 */
char * get_http_response_end() {
  return "\n\n";
}

/**
 * route 404
 */
String route_404() {
  Serial.println("ROUTE 404");
  String response = "";
  response += get_http_response_header_404();
  response += "404 Not Found";
  return response;
}

/**
 * route /
 */
String route_root() {
  Serial.println("ROUTE /");
  String response = "";
  response += get_http_response_header_200();
  for (int analogChannel = 0; analogChannel < 6; analogChannel++) {
    response += "analog input ";
    response += analogChannel;
    response += " is ";
    response += analogRead(analogChannel);
    response += "<br />";
  }
  return response;
}

/**
 * route /motor
 */
String action_motor(String *path) {
  Serial.println("ACTION /motor path = " + *path);
  
  String motor_path = path->substring(strlen("/motor"));
  
  String response = "";
  if (motor_path.startsWith("/start")) {
    response = route_motor_start();
  } else if (motor_path.startsWith("/reset")) {
    response = route_motor_reset();
  } else {
    response = route_404();
  }
  return response;
}

/**
 * route /motor/start
 */
String route_motor_start() {
  Serial.println("ROUTE /motor/start");
  
  // arduinoを動かしてみる
  output_move_motor();
  
  String response;
  response += get_http_response_header_200();
  response += "route_motor_start";
  return response;
}

/**
 * route /motor/start
 */
String route_motor_reset() {
  Serial.println("ROUTE /motor/reset");
  
  servo_reset_position();
  
  String response = "";
  response += get_http_response_header_200();
  response +=  "route_motor_reset";
  return response;
}

/**
 * HTTPリクエストの振り分け
 * method GETとpath以外は放置。
 * :params client: 参照渡しね。忘れてるわー。
 * :params request: Stringのインスタンスは値渡しでもいいけど、参照渡し。
 */
void action(EthernetClient *client, String *request) {
  
  int method_end_pos = request->indexOf(" ");
  if (method_end_pos < 0) {
    return ;
  }
  String method = request->substring(0, method_end_pos);
  Serial.println("method = " + method);
  
  if (method == "GET") {
    int path_end_pos = request->indexOf(" ", method_end_pos + 1);
    if (path_end_pos < 0) {
      return ;
    }
    String path = request->substring(method_end_pos + 1, path_end_pos);
    Serial.println("path=" + path);
    
    String response = "";
    if (path == "/") {
      response += route_root();
    } else if (path.startsWith("/motor")) {
      response += action_motor(&path);
    } else {
      response = route_404();
    }
    
    response += get_http_response_end();
    client->println(response);
    
  } else if (method == "POST") {
  } else if (method == "PUT") {
  } else if (method == "DELETE") {
  } else {
  }
  
}

/**
 * Move servo motor
 */
void output_move_motor() {
  
  servo.write(120); // ギアがスイッチを押す角度
  delay(1000); // モーターが動き終わるまで1秒待つ
  servo.write(60); // ギアがスイッチから離れる角度
  delay(1500); // モーターの動作とWebアクセスの処理を4秒待つ
  
}

/**
 * モーターの位置をリセット
 */
void servo_reset_position() {
   
  servo.write(60); // ギアがスイッチから離れる角度
  delay(1000); // モーターの動作とWebアクセスの処理を4秒待つ
  
}

