/*
 * Just need to write a 0 to first 
 * location in EEPROM so that
 * it is ready to be used with 
 * ankle brace data collecion code
 */

#include <EEPROM.h>
void setup() {
  // write the flag to first index
  Serial.begin(9600);
  EEPROM.write(0,0);
  Serial.println("wrote 0 to eeprom 0");
}

void loop() {
  // 

}
