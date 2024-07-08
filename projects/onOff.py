from gpiozero import LED
from time import sleep

# Output on pin 18(12)
# Input on GND(6)
# Anode connected to pin 18 via 330Ω resistor
# Cathode connected to first GND pin

led = LED(18)

try:
  print("LED on")
  led.on()
  sleep(5)
  print("LED off")
  led.off()
except KeyboardInterrupt:
  print("Process stopped by user")