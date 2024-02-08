#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define STEP_OUTA 27
#define STEP_OUTB 0
#define STEP_OUT2A 1
#define STEP_OUT2B 24
#define SW1 3
#define SW2 4
#define SW3 5

void rotateMotor(int steps, int delayTime) {
    int i;

    for (i = 0; i < steps; i++) {
        digitalWrite(STEP_OUTA, 1);
        delayMicroseconds(delayTime);
        digitalWrite(STEP_OUTA, 0);
        digitalWrite(STEP_OUTB, 1);
        delayMicroseconds(delayTime);
        digitalWrite(STEP_OUTB, 0);
        digitalWrite(STEP_OUT2A, 1);
        delayMicroseconds(delayTime);
        digitalWrite(STEP_OUT2A, 0);
        digitalWrite(STEP_OUT2B, 1);
        delayMicroseconds(delayTime);
        digitalWrite(STEP_OUT2B, 0);
    }
}

int main(void) {
    if (wiringPiSetup() == -1) {
        return 1;
    }

    pinMode(STEP_OUTA, OUTPUT);
    pinMode(STEP_OUTB, OUTPUT);
    pinMode(STEP_OUT2A, OUTPUT);
    pinMode(STEP_OUT2B, OUTPUT);
    pinMode(SW1, INPUT);
    pinMode(SW2, INPUT);
    pinMode(SW3, INPUT);

    while (1) {
        if (digitalRead(SW1) == LOW) {
            printf("SW1 Button pushed! Rotating motor 45 degrees.\n");
            rotateMotor(45*1.5, 2000);
        } else if (digitalRead(SW2) == LOW) {
            printf("SW2 Button pushed! Rotating motor 90 degrees.\n");
            rotateMotor(90*1.5, 2000);  
        } else if (digitalRead(SW3) == LOW) {
            printf("SW3 Button pushed! Rotating motor 180 degrees.\n");
            rotateMotor(180*1.5, 2000);  // 180도 회전
        }

        // 스위치 상태 체크 간격을 늘리기 위한 딜레이
        usleep(100000);  // 0.1초
    }

    return 0;
}

