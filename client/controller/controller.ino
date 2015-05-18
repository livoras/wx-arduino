/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.

  Most Arduinos have an on-board LED you can control. On the Uno and
  Leonardo, it is attached to digital pin 13. If you're unsure what
  pin the on-board LED is connected to on your Arduino model, check
  the documentation at http://arduino.cc

  This example code is in the public domain.

  modified 8 May 2014
  by Scott Fitzgerald
 */
 
#define LED 13
#define BUTTON 7
int old_val = 0;
int new_val = 0;
int state = 0;

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin 13 as an output.
  pinMode(LED, OUTPUT);
  pinMode(BUTTON, INPUT);
  Serial.begin(9600);
}

// the loop function runs over and over again forever
void loop() {
  new_val = digitalRead(BUTTON);
  if (Serial.available() > 0) {
    int data = int(Serial.read() - '0');
    Serial.print("You send me ");
    Serial.println(data);
    if (data == 1) state = 1 - state;
  }
  if (new_val == HIGH && old_val == LOW) {
    state = 1 - state;
    Serial.println(state);
  }
  old_val = new_val;
  digitalWrite(LED, state);
}

