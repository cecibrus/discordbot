import discord
import time
from discord.ext import commands,tasks

client=commands.Bot(command_prefix='.')

class Materia:
    def __init__(self, nombre, dia, horas, mins,link):
        self.dia=dia
        self.nombre=nombre
        self.horas=horas
        self.mins=mins
        self.link=link

#aki le agregas el link como string nomas a cada uno al final
poo=Materia('POO',1,14,0,'')
fs_practica=Materia('FS Practica',2,7,30,'')
dinamica=Materia('Dinamica Charly',2,9,0,'')
teoriaDeCircuitos=Materia('Teoria de Circuitos',2,16,0,'')
mn=Materia('MN',3,13,0,'')
dinamicaP=Materia('Dinamica Practica',4,8,0,'')
tc=Materia('TC',4,16,0,'')
fs_teoria=Materia('FS Teoria',4,18,0,'')
mnt=Materia('MN Teoria',5,8,30,'')

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
        if(horario.tm_wday==x.dia and horario.tm_hour==x.horas and horario.tm_min==x.mins):
            print("OK")
            await channel.send(f"Es hora de la clase de {x.nombre} beep boop, el link es {x.link}")

client.run('aca se pone el client ID')
