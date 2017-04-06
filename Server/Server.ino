#include <SPI.h>
#include <Ethernet.h>
#define POTENTIOMETER A0
#define LDR A1
#define RED 2
#define YELLOW 3
#define BLUE 4

byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };    // MAC address
byte ip[] = { 192, 168, 25, 8 };            // IP address. Change when use DHCP
byte gateway[] = { 192, 168, 25, 1 };  // Router's gateway address. Change when use another network
byte mask[] = { 255, 255, 255, 0 }; // Mask. Change when use another network

EthernetServer server(5000); // Port 5000 to use on this socket, must be the same on client

int pot;
unsigned short lr;
boolean redLD = false;
boolean yellowLD = false;
boolean blueLD = false;

boolean alreadySent = true;
char command;
String response = "";

void setup() {
  Ethernet.begin(mac, ip, gateway, mask);
  server.begin();
  Serial.begin(9600);
  pinMode(RED, OUTPUT);
  pinMode(YELLOW, OUTPUT);
  pinMode(BLUE, OUTPUT);
  
  Serial.print("Arduino IP address: ");
  Serial.println(Ethernet.localIP());
}

void loop() {
  EthernetClient client = server.available();

  if (client) {
    client.flush();

    while (client.available() > 0) {
      command = char(client.read());
    }
    
    Serial.println(command);
    
    if (command == 'a'){
      pot = analogRead(POTENTIOMETER);
      response = String(pot);
      alreadySent = false;
    } else if (command == 'b'){
      lr = analogRead(LDR);
      response = String(lr);
      alreadySent = false;
    } else if (command == 'c'){
      if (redLD){
        digitalWrite(RED, LOW);
        redLD = false;
      } else {
        digitalWrite(RED, HIGH);
        redLD = true;
      }
    } else if (command == 'd'){
      if (yellowLD){
        digitalWrite(YELLOW, LOW);
        yellowLD = false;
      } else {
        digitalWrite(YELLOW, HIGH);
        yellowLD = true;
      }
    } else if (command == 'e'){
      if (blueLD){
        digitalWrite(BLUE, LOW);
        blueLD = false;
      } else {
        digitalWrite(BLUE, HIGH);
        blueLD = true;
      }
    }
    
    if (!alreadySent){
      client.println(response);
      alreadySent = true;
      command = 'x';
    }
  }
}
