import discord
import time
import datetime
from discord.ext import commands,tasks

client=commands.Bot(command_prefix='.')

class Materia:
    def __init__(self, nombre, dia, horas, mins,link="NN",sgteExamen=0):
        self.dia=dia
        self.nombre=nombre
        self.horas=horas
        self.mins=mins
        self.link=link
        self.sgteExamen=sgteExamen
    
    def getNombre(self):
        return self.nombre
    def setNombre(self,arg):
        self.nombre =arg

    def getDia(self):
        return self.dia
    def setDia(self,arg):
        self.dia =arg

    def getHoras(self):
        return self.horas
    def setHoras(self,arg):
        self.horas =arg  

    def getMins(self):
        return self.mins
    def setMins(self,arg):
        self.mins =arg

    def getLink(self):
        return self.link
    def setLink(self,arg):
        self.link =arg

    def getSgteExamen(self):
        return self.sgteExamen
    def setSgteExamen(self,arg):
        self.sgteExamen =arg              

#aki le agregas el  
# li    
# def nk como string nomas a cada uno al final
poo=Materia('POO',1,14,0,'https://meet.google.com/aek-behh-hkr',datetime.datetime(2020,8,31))
fs_practica=Materia('FS Practica',2,7,30,'https://meet.google.com/gri-gvoy-gip',)
dinamica=Materia('Dinamica Charly',2,9,0)
teoriaDeCircuitos=Materia('Teoria de Circuitos',2,16,0,'https://meet.google.com/lookup/akks57i7ph',datetime.datetime(2020,9,8))
mn=Materia('MN Practica',3,13,0,'https://meet.google.com/lookup/e5fl37ajgl')
dinamicaP=Materia('Dinamica Practica C',4,8,0,'https://meet.google.com/lookup/bgk5osrwbj',datetime.datetime(2020,8,27))
tc=Materia('TC Practica',4,16,0,'https://meet.google.com/lookup/akks57i7ph')
fs_teoria=Materia('FS Teoria',4,18,0,'https://meet.google.com/gri-gvoy-gip',datetime.datetime(2020,8,24))
mnt=Materia('MN Teoria',5,8,30,'https://meet.google.com/lookup/e5fl37ajgl',datetime.datetime(2020,9,5))

materias=[poo,fs_practica,dinamica,teoriaDeCircuitos,mn,dinamicaP,tc,fs_teoria,mnt]

@client.event
async def on_ready():
    print('Yasta el bot')
    hora.start()


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency* 1000)}ms')

@tasks.loop(seconds=60)
async def hora():
    channel=client.get_channel(701182086937051198) #aca tenes que poner el channel ID del canal al que queres enviar el mensaje
    for x in materias:
        horario = time.localtime(time.time())
        if(horario.tm_wday==x.getDia() and horario.tm_hour==x.getHoras and horario.tm_min==x.getMins()):
            print("OK")
            await channel.send(f"Es hora de la clase de {x.getNombre()} beep boop, el link es {x.getLink()}")

client.run('aca se pone el client ID')
