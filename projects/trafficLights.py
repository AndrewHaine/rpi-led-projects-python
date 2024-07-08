from gpiozero import LED
from time import sleep

red = LED(23)
yellow = LED(18)
green = LED(17)

try:
  print("RED")
  red.on()
  sleep(1)
  red.off()
  print("YELLOW")
  yellow.on()
  sleep(1)
  yellow.off()
  print("GREEN")
  green.on()
  sleep(1)
  green.off()
except KeyboardInterrupt:
  print("Process stopped by user")