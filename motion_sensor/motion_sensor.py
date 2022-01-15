from gpiozero import MotionSensor
import time
import subprocess

pir = MotionSensor(21)
count = 0
pir.wait_for_no_motion()

pir.wait_for_no_motion()
print("Sensor is ready")

def detected():
    global count
    print(f"motion detected {count}")

    count +=1
while True:
    pir.wait_for_active
    detected()
    subprocess.call("/bin/play")
