#include <Adafruit_GFX.h>
#include <Adafruit_ILI9341.h>
#include <SD.h>

#define TFT_CS 5
#define TFT_DC 4
#define TFT_RST RST
#define SD_CS 15

Adafruit_ILI9341 tft = Adafruit_ILI9341(TFT_CS, TFT_DC, TFT_RST);
File root;

void setup() {
  Serial.begin(115200);

  tft.begin();
  tft.fillScreen(ILI9341_BLACK);
  
  if (!SD.begin(SD_CS)) {
    Serial.println("Initialization failed!");
    return;
  }

  root = SD.open("/");
  printDirectory(root, 0);
}

void loop() {
  
  displayRandomImage();
  delay(10000);  
}

void displayRandomImage() {
  File entry = root.openNextFile();
  int files = 0;

  while (entry) {
    files++;
    entry.close();
    entry = root.openNextFile();
  }

  int randomIndex = random(files);

  entry = root.openNextFile();
  for (int i = 0; i < randomIndex; i++) {
    entry.close();
    entry = root.openNextFile();
  }

  if (entry) {
    tft.fillScreen(ILI9341_BLACK);

    String filename = entry.name();
    Serial.print("Displaying: ");
    Serial.println(filename);

    // I haven't loaded all the images on the SD card yet, so it just displays a color for now
    tft.fillScreen(random(0xFFFF));
    delay(3000);  
  } else {
    Serial.println("No more files. Restarting.");
    root.rewindDirectory();
  }
}

void printDirectory(File dir, int numTabs) {
  while (true) {
    File entry =  dir.openNextFile();
    if (!entry) {
      break;
    }
    for (uint8_t i = 0; i < numTabs; i++) {
      Serial.print('\t');
    }
    Serial.print(entry.name());
    if (entry.isDirectory()) {
      Serial.println("/");
      printDirectory(entry, numTabs + 1);
    } else {
      
      Serial.print("\t\t");
      Serial.println(entry.size(), DEC);
    }
    entry.close();
  }
}
