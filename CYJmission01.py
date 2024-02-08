import RPi.GPIO as GPIO
import time

# GPIO 핀 번호 설정
LED_RED = 7
LED_GREEN = 21
LED_BLUE = 22

# GPIO 초기화
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.setup(LED_BLUE, GPIO.OUT)

try:
    print("3 Color LED Control Start !!")
    for i in range(10):
        GPIO.output(LED_RED, GPIO.HIGH)
        GPIO.output(LED_GREEN, GPIO.HIGH)
        GPIO.output(LED_BLUE, GPIO.HIGH)
        time.sleep(0.5)
        
        GPIO.output(LED_RED, GPIO.LOW)
        GPIO.output(LED_GREEN, GPIO.LOW)
        GPIO.output(LED_BLUE, GPIO.LOW)
        time.sleep(0.5)

except KeyboardInterrupt:
    pass

# GPIO 리소스 정리
GPIO.cleanup()

