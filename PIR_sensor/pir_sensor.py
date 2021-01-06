import RPi.GPIO as GPIO # GPIO 라이브러리 사용
import time 

##### PIR SENSOR #####
# 1 VCC
# 2 OUTPUT
# 3 GND

pirPin = 7  # PIR 센서의 OUTPUT을 pin 7에 연결 

# 핀 번호를 라즈베리파이 보드 번호로 참조 
# <-> GPIO.setmode(GPIO.BCM) BCM(Broadcom chip-specific pin number) 모드
GPIO.setmode(GPIO.BOARD)  

GPIO.setup(pirPin, GPIO.IN) # 핀을 입력으로 설정 <-> GPIO.setup(pin, GPIO.OUT)
count = 0; # 몇번 감지 되었는지 체크하는 카운터

while True: 
  input_state = GPIO.input(pirPin) # Pir의 출력을 저장 
  if input_state == True:          # 0이 아니라면 감지된 것임!
    print("Motion Detected -- " + str(count))  # 감지 문구 출력
    count+=1
    time.sleep(0.3) # 0.3초 대기

GPIO.cleanup(); # 종료시 GPIO 모듈의 점유 리소스를 해제