#define rfTransmitPin 12  //RF Transmitter pin = digital pin 4

 void setup(){
   pinMode(rfTransmitPin, OUTPUT);     
 }

 void loop(){
   while(true){
     digitalWrite(rfTransmitPin, HIGH );     //Transmit a HIGH signal
   }
 }
 
