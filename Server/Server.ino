#include <SPI.h>
#include <Ethernet.h>

byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };    // MAC address
byte ip[] = { 192, 168, 0, 117 };            // IP address. Change when use DHCP
byte gateway[] = { 192, 168, 0, 1 };  // Router's gateway address. Change when use another network
byte mask[] = { 255, 255, 255, 0 }; // Mask. Change when use another network

EthernetServer server(5000); // Port 5000 to use on this socket, must be the same on client

boolean alreadySent = true;
String recvMSG = "";
String sendMSG = "Hello, client!";

void setup() {
  Ethernet.begin(mac, ip, gateway, mask);
  server.begin();
  Serial.begin(9600);
  
  Serial.print("Server address: ");
  Serial.println(Ethernet.localIP());
}

void loop() {
  EthernetClient client = server.available();

  if (client) {
    client.flush();

    while (client.available() > 0) {
      char thisChar = client.read();
      recvMSG += thisChar;
      alreadySent = false;
    }
    
    if (!alreadySent){
      Serial.println(recvMSG);
      client.println(sendMSG);
      alreadySent = true;
      recvMSG = "";
    }
  }
}
