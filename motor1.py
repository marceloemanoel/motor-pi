#alteracoes e adaptacoes : Arduino e Cia
#
#Baseado no codigo original de Matt Hawkins
#http://www.raspberrypi-spy.co.uk/

#Carrega bibliotecas
import sys
import time
import RPi.GPIO as GPIO
import math

#Utiliza numeros da GPIO ao inves
#da numeracao dos pinos
GPIO.setmode(GPIO.BCM)

#Pinos de conexao ao motor
#Pinos 7, 8, 25, 24
#GPIO7,GPIO8,GPIO25,GPIO24
StepPins = [7, 8, 25, 24]

#Define os pinos como saida
#for pin in StepPins:
#  print "pin %i "%(pin)
#  GPIO.setup(pin, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.output(7, False)
GPIO.output(8, False)
GPIO.output(25, False)
GPIO.output(24, False)

#Sequencia de ativacao
Seq = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1]
]

degrees = int(sys.argv[1])
numberOfSteps = degrees/float(360/float(4096))       
StepCount = len(Seq)-1

#Configura sentido de giro
StepDir = int(math.copysign(1, degrees)) 
            # 1 ou 2 para sentido horario
            # -1 ou-2 para sentido anti-horario

#Inicializa variaveis
StepCounter = 0

for step in range(int(math.floor(numberOfSteps))): 
  for pin in range(len(StepPins)): 
    GPIO.output(StepPins[pin], Seq[StepCounter][pin] == 1)
  StepCounter += StepDir

  #Ao final da sequencia, reinicia o processo
  if (StepCounter>=StepCount):
    StepCounter = 0
  if (StepCounter<0):
    StepCounter = StepCount

  #Delay para movimentar o motor
  time.sleep(0.001)
GPIO.cleanup()
