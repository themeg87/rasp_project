import RPi.GPIO as GPIO
import time

# 사용할 GPIO 핀의 번호를 설정
button_pin1 = 22
button_pin2 = 23
button_pin3 = 24

# Define the pin numbers as global variables
STEP_OUTA = 16
STEP_OUTB = 17
STEP_OUT2A = 18
STEP_OUT2B = 19

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  # 핀모드 설정

# 버튼 핀의 입력설정
GPIO.setup(button_pin1, GPIO.IN)
GPIO.setup(button_pin2, GPIO.IN)
GPIO.setup(button_pin3, GPIO.IN)

# Motor control pin numbers as outputs
GPIO.setup(STEP_OUTA, GPIO.OUT)
GPIO.setup(STEP_OUTB, GPIO.OUT)
GPIO.setup(STEP_OUT2A, GPIO.OUT)
GPIO.setup(STEP_OUT2B, GPIO.OUT)

def rotate_motor(steps, delay_time, step_outa, step_outb, step_out2a, step_out2b):
    for i in range(steps):
        GPIO.output(step_outa, 1)
        time.sleep(delay_time)
        GPIO.output(step_outa, 0)
        GPIO.output(step_outb, 1)
        time.sleep(delay_time)
        GPIO.output(step_outb, 0)
        GPIO.output(step_out2a, 1)
        time.sleep(delay_time)
        GPIO.output(step_out2a, 0)
        GPIO.output(step_out2b, 1)
        time.sleep(delay_time)
        GPIO.output(step_out2b, 0)

while True:
    if GPIO.input(button_pin1) == GPIO.LOW:
        rotate_motor(60, 0.01, STEP_OUTA, STEP_OUTB, STEP_OUT2A, STEP_OUT2B)  # Rotate 45 degrees
    if GPIO.input(button_pin2) == GPIO.LOW:
        rotate_motor(120, 0.01, STEP_OUTA, STEP_OUTB, STEP_OUT2A, STEP_OUT2B)  # Rotate 90 degrees
    if GPIO.input(button_pin3) == GPIO.LOW:
        rotate_motor(240, 0.01, STEP_OUTA, STEP_OUTB, STEP_OUT2A, STEP_OUT2B)  # Rotate 180 degrees

# Clean up the GPIO pins
GPIO.cleanup()

