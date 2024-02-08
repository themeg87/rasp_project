#include <stdio.h>
#include <wiringPi.h>
#include <unistd.h>

#define LED_RED 7
#define LED_GREEN 21
#define LED_BLUE 22

int main(void) {
    if (wiringPiSetup() == -1)
        return 1;

    pinMode(LED_RED, OUTPUT);
    pinMode(LED_GREEN, OUTPUT);
    pinMode(LED_BLUE, OUTPUT);

    digitalWrite(LED_RED, 0);
    digitalWrite(LED_GREEN, 0);
    digitalWrite(LED_BLUE, 0);

    printf("3 Color LED Control Start !!\n");

    for (int i = 0; i < 10; i++) {
        digitalWrite(LED_RED, 1);
        digitalWrite(LED_GREEN, 1);
        digitalWrite(LED_BLUE, 1);
        usleep(500000);

        digitalWrite(LED_RED, 0);
        digitalWrite(LED_GREEN, 0);
        digitalWrite(LED_BLUE, 0);
        usleep(500000);
    }

    return 0;
}

