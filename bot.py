import discord
from discord.ext import commands
import yt_dlp

intents = discord.Intents.all()
bot = commands.Bot("!", intents=intents)

@bot.event
async def on_ready():
  print("Bot inicializado com sucesso")

@bot.command()
async def falar(ctx:commands.Context, *,texto):
  await ctx.send(texto)
            #reply poderia ser usado nesse caso, o reply responde a mensagem, o send manda a mensagem sem responder nada
  
async def multiplique(ctx:commands.Context, num1:float, num2:float):
  resu = num1 * num2
  await ctx.send(f"a multiplicaçao de {num1} x {num2} é {resultardo}")



@bot.command()
async def play(ctx, *, search):
    if ctx.voice_client is None:
        await ctx.author.voice.channel.connect()

    voice = ctx.voice_client

    ydl_opts = {'format': 'bestaudio'}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{search}", download=False)
        url = info["entries"][0]["url"]
        title = info["entries"][0]["title"]

    source = await discord.FFmpegOpusAudio.from_probe(url)

    voice.play(source)

    await ctx.send(f"🎵 Tocando: {title}")



























bot.run()