from gpiozero import MotionSensor
import time
import subprocess

pir = MotionSensor(21)

pir.wait_for_no_motion()
print("Sensor is ready")

def detected():
    subprocess.call("/bin/play")

while True:
    pir.wait_for_active
    detected()
    subprocess.call("/bin/play")
    time.sleep(60)
