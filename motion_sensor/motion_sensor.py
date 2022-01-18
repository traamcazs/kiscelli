from gpiozero import MotionSensor
import time
import subprocess

pir = MotionSensor(21)

pir.wait_for_no_motion()
print("Sensor is ready")

def detected():
    subprocess.run("/bin/play")

while True:
    pir.wait_for_active
    detected()
    subprocess.run("/bin/play")
    time.sleep(60)
