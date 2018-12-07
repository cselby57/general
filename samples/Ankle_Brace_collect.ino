// define pins for sensors
#define FSback 4
#define FSright 1
#define FSfront 2
#define FSleft 3
#include <EEPROM.h>

/*  this a data collection program
 *  for an ankle worn device that
 *  measures ankle position based on
 *  voltages from 4 flexible variable resitors
 *  voltage dividers. Crated for final project in
 *  24-673: Soft Robotics: Materials and Methods
 *  by Cameron Selby April 2018
 *  
 *  (using Adafruit Pro Trinket 5V)
 */

// timing variables
unsigned long now = 0;
unsigned long last = 0;
unsigned long mill = 0;

// Flex sensor voltages
int FSB = 0;
int FSR = 0;
int FSF = 0;
int FSL = 0;

int iter = 1;         // iterations

// decide whether to collect or export ("dump") data
bool dump = false;    
// first bit in the EEPROM is used as flag for collection/dump
byte collect = EEPROM.read(0); 

void setup() {
  // initialize pins and serial
  pinMode(FSback, INPUT);
  pinMode(FSright, INPUT);
  pinMode(FSfront, INPUT);
  pinMode(FSback, INPUT);
  // just always turn it on
  Serial.begin(9600);
  Serial.println("read from eeprom");
  Serial.println(collect);
}

void loop() {
  // collect or dump data to/from eeprom
  if(collect == 0){
    // if the eeprom is empty fill it with sensor data
    now = micros();
    if(now - last > 10000){
      // collect at roughly 100hz
      // get the data from each voltage divider
      /* initial test showed front and
      *  front and back sensors did
      *  not provide data not captured
      *  by left and right, so disable 
      *  for longer duration
       */
      //FSB = analogRead(FSback); 
      FSR = analogRead(FSright);
      //FSF = analogRead(FSfront);
      FSL = analogRead(FSleft);
      mill = millis();
      // if there is room in eeprom add new data points
      // wait 5 seconds so the user has time to get ready for behavior
      if(iter < EEPROM.length() && mill > 5000){
        digitalWrite(13,HIGH);  // turn on LED for feedback
        // again only store left/right
        EEPROM.write(iter,FSR);
        EEPROM.write(iter+1,FSL);
        iter+=2;
      }
      // if eeprom is full change the flag and 
      else if(iter > EEPROM.length()){
        Serial.print("EEPROM Full");
        collect = 1;
        EEPROM.write(0,1);
        digitalWrite(13,LOW); // turn of LED to indicate end of collection
      }
      last = micros(); // update timing
    }
  }
  // if the eeprom is full of sensor data print it to serial monitor
  else if(collect == 1){
    // wait for command to dump
    int input = Serial.parseInt();
    if(input == 57){
      for(int i = 0; i < EEPROM.length(); i+=2){
        Serial.print(EEPROM.read(i));
        Serial.print("\t");
      //Serial.print(FSF);
      //Serial.print("\t");
        Serial.print(EEPROM.read(i+1));
        Serial.print("\n");
        // don't bother clearing old data t save some read/write lifetime
      }
      // once dump is done set flags so we don't do it again 
      // and know to be ready for collection on restart
      dump = true;      
      EEPROM.write(0,0);
    }
  }
}
