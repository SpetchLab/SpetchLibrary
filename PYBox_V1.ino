

//NOTE: SET THESE VALUES
int checksum
byte key1LightPinR
byte key1LightPinG
byte key1LightPinB
byte key2LightPinR
byte key2LightPinG
byte key2LightPinB
byte key3LightPinR
byte key3LightPinG
byte key3LightPinB
byte houseLightPin
byte hopperLightPin
byte hopperPlungerPin
byte key1ButtonPin
byte key2ButtonPin
byte key3ButtonPin
byte irLightPin
byte irSensorPin
boolean key1ButtonState
boolean key2ButtonState
boolean key3ButtonState
int port
boolean hopperIRState


void setup(){
	//Flash house and hopper lights, make a rainbow on key lights

	//Start serial
	Serial.begin(9600);

	//Set pin modes on all pins
  	pinMode(key1LightPinR, OUTPUT);
  	pinMode(key1LightPinG, OUTPUT);
  	pinMode(key1LightPinB, OUTPUT); 

  	pinMode(key2LightPinR, OUTPUT);
  	pinMode(key2LightPinG, OUTPUT);
  	pinMode(key2LightPinB, OUTPUT); 

  	pinMode(key3LightPinR, OUTPUT);
  	pinMode(key3LightPinG, OUTPUT);
  	pinMode(key3LightPinB, OUTPUT); 

  	pinMode(hopperLightPin, OUTPUT);

  	pinMode(hopperPlungerPin, OUTPUT);

  	pinMode(key1ButtonPin, INPUT);
  	pinMode(key2ButtonPin, INPUT);
  	pinMode(key3ButtonPin, INPUT);

  	pinMode(irLightPin, OUTPUT);

  	pinMode(irSensorPin, INPUT);


	//Send checksum over serial in a loop
	//Wait for serial response (instruction type 0)
	//When serial response is confirmed, flash confirmation indicator (keys light up all green?) for a second

	//Jump into loop
}

void loop(){
	//Read serial in loop
	listenForInstructions()
	//Based on number received by serial, do appropriate thing
	//If incorrect response received, give error message
}

// SUPPORTING FUNCTIONS:

void listenForInstructions(){
	//Read serial for input from USB port (instruction type 1)
	//Instruction format:
	// instruction_type(0 or 1), red_value(0-255), green_value(0-255), blue_value(0-255), hopper_light_value(0 or 1), house_light_value(0 or 1), plunger_value(0 or 1), hopper_ir_value(0 or 1)
}

void doInstruction(int instruction){
}

int setKeyLightColour(byte redPin, byte greenPin, byte bluePin, byte red, byte green, byte blue){

  #ifdef COMMON_ANODE
    red = 255 - red;
    green = 255 - green;
    blue = 255 - blue;
  #endif

  analogWrite(redPin, red);
  analogWrite(greenPin, green);
  analogWrite(bluePin, blue);  
}

// NOTE: NOT SURE IF THIS IS NECESSARY, OR IF SETTING ALL TO 0 WOULD ACHIEVE THE SAME RESULT
void key1LightOff(){
	pinMode(key1LightPinR, LOW);
	pinMode(key1LightPinG, LOW);
	pinMode(key1LightPinB, LOW);
}

void key2LightOff(){
	pinMode(key2LightPinR, LOW);
	pinMode(key2LightPinG, LOW);
	pinMode(key2LightPinB, LOW);
}

void key3LightOff(){
	pinMode(key3LightPinR, LOW);
	pinMode(key3LightPinG, LOW);
	pinMode(key3LightPinB, LOW);
}

void houseLightOn(){
	pinMode(houseLightPin, HIGH);
}

void houseLightOff(){
	pinMode(houseLightPin, LOW);
}

void hopperLightOn(){
	pinMode(hopperLightPin, HIGH);
}

void hopperLightOff(){
	pinMode(hopperLightPin, LOW);
}

void hopperPlungerIn(){
	//do whatever you need to do to turn the hopper on
}

void hopperPlungerOut(){
	//do whatever you need to do to turn the hopper off
}

void readKeyPin(keyNumber, timeout){
	//If key matches key number, then read its button value
	//True if pressed within timeout time, false if not
	//Send button value over serial

}

void readHopperIRState(){
	//Turn on IR beam
	//Read IR photosensor in a loop
	//If beam broken, return value
	//If beam unbroken, read value from serial for potential termination
	//If exiting for any reason, always turn IR beam off
}