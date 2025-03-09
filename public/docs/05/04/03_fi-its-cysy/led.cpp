// Pins für RGB-LED
int redPin = 1;    // PWM-Pin für Rot
int greenPin = 2; // PWM-Pin für Grün
int bluePin = 3;  // PWM-Pin für Blau

void setup() {
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
}

void loop() {
  // Von Rot zu Weiß pulsieren
  for (int i = 0; i <= 255; i++) {  // Farbanteil erhöhen
    digitalWrite(redPin, 255);       // Rot bleibt auf Maximum
    digitalWrite(greenPin, i);       // Grün steigern
    digitalWrite(bluePin, i);        // Blau steigern
    delay(10);                      // Kurze Pause für glattes Pulsieren
  }
  for (int i = 255; i >= 0; i--) {  // Farbanteil verringern
    digitalWrite(redPin, 255);       // Rot bleibt auf Maximum
    digitalWrite(greenPin, i);       // Grün verringern
    digitalWrite(bluePin, i);        // Blau verringern
    delay(10);
  }
}
 