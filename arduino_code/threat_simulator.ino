// For Arduino Uno/Nano (serial communication)
// Use ESP8266/ESP32 with WiFiClientSecure for direct MQTT if preferred

void setup() {
  Serial.begin(9600);
}

void loop() {
  // Simulate normal sensor data
  String data = "Temp: " + String(random(20, 30)) + "C";
  Serial.println(data);
  delay(1000);  // Normal interval

  // Occasionally simulate a threat (rapid data)
  if (random(0, 100) < 10) {  // 10% chance
    for (int i = 0; i < 50; i++) {
      Serial.println("Threat: Flood " + String(i));
      delay(10);  // Rapid fire
    }
  }
}
