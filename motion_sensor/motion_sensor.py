from gpiozero import MotionSensor
import subprocess

pir = MotionSensor(14)

pir.wait_for_no_motion()
print("Sensor is ready")

while True:
    pir.wait_for_active()
    subprocess.run(["omxplayer","/home/pi/Videos/timer.mp4"])
