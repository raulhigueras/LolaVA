# coding: utf-8
import random, time
from speech import input, output

scoreCPU = 0
scorePlayer = 0
totalPlayer = 0
totalCPU = 0
primeraPartida = True

def partida():
  global scoreCPU
  global scorePlayer
  global totalPlayer 
  totalPlayer = 0
  global totalCPU
  totalCPU = 0
  
  def turno_player():
    global totalPlayer
    carta = random.randint(1,12)
    output.say("Ha salido un: " + str(carta))
    totalPlayer += carta
    if(totalPlayer > 21):
      output.say("¡Te has pasado!")
      return 0
    else:
      output.say("Llevas un total de " + str(totalPlayer) + ". ¿Quieres continuar?")
      r = input.ask()
      if(r == "si"):
        return turno_player()
      elif(r == "no"):
        return totalPlayer
  
  def turno_cpu():
    global totalCPU
    carta = random.randint(1,12)
    output.say("Me ha salido un: " + str(carta))
    totalCPU += carta
    if(totalCPU > 21):
      output.say("¡Me he pasado!")
      return 0
    else:
      r = random.randint(12,21)
      if(totalCPU < r):
        output.say("Sigo")
        return turno_cpu()
      else:
        output.say("Me planto con " + str(totalCPU))
        return totalCPU
  
  turno = random.randint(0,1)
  if(turno == 0):
    output.say("Empiezas tú")
    resultadoPlayer = turno_player()
    output.say("Me toca")
    resultadoCPU = turno_cpu()
  else:
    output.say("Empiezo yo")
    resultadoCPU = turno_cpu()
    output.say("Tu turno")
    resultadoPlayer = turno_player()
  
  if(resultadoPlayer > resultadoCPU):
    output.say("¡Tú ganas!")
    scorePlayer += 1
  elif(resultadoPlayer < resultadoCPU):
    output.say("¡He ganado!")
    scoreCPU += 1
  else:
    output.say("¡Empate!")

def jugar():
  global primeraPartida
  jugando = True
  while(jugando):
    if(primeraPartida == False):
      output.say("Vamos " + str(scorePlayer) + " - " + str(scoreCPU) +". Quieres jugar otra partida?")
      r = input.ask()
      if(r == "si"):
        partida()
      else:
        return "Bueno, aquí te espero para darte una paliza la próxima vez"
        jugando = False
    else:
      partida()
      primeraPartida = False
    
def inicio():
    output.say("Podemos jugar al Blackjack ¿Quieres jugar ya, ver las instrucciones o salir?")
    r = ""
    while("jugar" not in r or "salir" not in r):
        r = input.ask()
        if("jugar" in r):
            return jugar()
        elif("instrucciones" in r):
            output.say("Yo iré sacando cartas de mi baraja, cada carta tiene un valor que se irá sumando, tu objetivo es " +    
            "acercarte lo máximo posible a 21 sin pasarte")
            output.say("¿Quieres jugar ya o salir del juego?")
        elif("salir" in r) :
            return "Ya jugaremos en otra ocasión"
        else:
            output.say("Perdona, no te he entendido. ¿Quieres jugar, ver las instrucciones o salir?")

