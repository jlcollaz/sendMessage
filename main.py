import pywhatkit
from datetime import datetime
import time

file1 = open('numbers.txt', 'r')
file2 = open('names.txt', 'r')
count = 0

while True:
  count += 1
  line = file1.readline()
  line2 = file2.readline()

  if not line:
    print("Se terminó")
    break

  seconds = time.time() + 60;
  date = datetime.fromtimestamp(seconds);
  numero = str(line.strip());
  nombre = str(line2.strip());
  mensaje = "Hola " + nombre + ". Tal vez el mejor adorno para esta noche tan mágica es una gran sonrisa. La tuya será la mejor, feliz navidad <3.";

  pywhatkit.sendwhatmsg(numero, mensaje, date.hour, date.minute);

  print("Line{}: {}".format(count, line.strip()))

file1.close()