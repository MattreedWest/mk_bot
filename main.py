# Импортируем настройки бота

try:
    import conf
except ImportError:
    pass




import discord



from discord.ext import commands
import img_handler as imhl
import os, random



# # Настройки INTENTS
intentse = discord.Intents.default()
intentse.members = True



bot = commands.Bot(command_prefix = "!", intents = intentse)


whitelist = {
    825328622654193675 : {825328622654193675: "Bots /general"},
}


# Декоратор - проверка @allowed_channel => True/False
def allowed_channel():
    async def predicate(ctx:coommands.Context):
        if ctx.guild.id in whitelist:
            if ctx.channel.id in whitelist[ctx.guild.id]:
                return True
        

        return False


    return commands.check(predicate)

@bot.command(name="get_member")
async def get_member(ctx, member:discord.Member=None):
    msg = None
    global channel
    if ctx.channel.id == channel:

        if member:
            msg = f'Member {member.name} {"({member.nick})" if member.nick else ""} - {member.id}'


        if msg == None:
            msg = "error"
        
        await ctx.channel.send(msg)


#команда !mk
@bot.command(name="mk")
async def mk(ctx,f1:discord.Member=None,f2:discord.Member=bot.user):
    global channel
    if ctx.channel.id == channel:
        if f1 and f2:
            await imhl.vs_create_animated(f1.avatar_url, f2.abatar_url)

            await ctx.channel.send( file=discord.File(os.path.join("./img/result.gif")) )


@bot.command(name="join")
@allowed_channel()
async def vs_join(ctx):
    global channel
    if ctx.channel.id == channel:
        voice_channel = ctx.author.voice.channel

        if voice_channel:
            msg =f"Подключаюсь к {voice_channel.name}"
            await ctx.channel.send(    msg    )
            await voice_channel.connect()


@bot.command(name="leave")
async def vs_leave(ctx):
    msg =""
    global channel

    voice_channel = ctx.author.voice.channel

    if voice_channel and ctx.channel.id == channel:
        voice_channel = ctx.author.voice.channel
        msg =f"Отключаюсь от {voice_channel.name}"
        await ctx.channel.send(    msg    )
        await voice_client.disconnect()

@bot.command(name="ost")
async def vs_ost(ctx):
    msg = ""
    global channel

    if ctx.channel.id == channel:
        voice_client = discord.utils.get(bot.voice_clients, guild = ctx.guild)
        msg = f"Mortal Kombat"

        await ctx.channel.send(msg)
        await voice_client.play(discord.FFmpegPCMAudio(source = "./sound/mk.mp3"))

@bot.command(name="fight")
@allowed_channel()
async def fight(ctx,f1:discord.Member=None,f2:discord.Member=bot.user):
    f1 = None

    f2 = bot.user

    voice_channel = ctx.author.voice.channel

    if voice_channel:
        await vc_join(ctx)

        voice_members = voice_channel.members

        voice_members = [member for member in voice_members if member.bot == False]

        if len(voice_members) > 1:

            f1,f2 = [voice_members.pop(random.randit(0, len(voice_members)-1)), voice_members.pop(random.randit(0, len(voice_members)-1))]
        else:
            f1 = ctx.author


        await imhl.vs_create_animated(f1.avatar_url, f2.abatar_url)
        await ctx.channel.send( file=discord.File(os.path.join("./img/result.gif")) )
        


bot.run(os.environ["BOT_TOKEN"])