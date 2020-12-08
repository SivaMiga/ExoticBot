import random
import discord
import os
import json
from discord.ext import commands

pyconfig = __import__("pyconfig")


def openjsonfile(name): 
    with open(name, "r") as theFile:
      return json.load(theFile)
      
def getRoleByName(ctx, name):
    allServerRoles = ctx.guild.roles
    for i in allServerRoles:
        if(i.name.lower() == name.lower()):
            return i


configjson = openjsonfile(pyconfig.configPath)
Exotics = ["Cerberus +1", "Monte Carlo", "SUROS Regime", "Sweet Business", "Wish Ender", "Ace of Spades", "Crimson", "Lumina", "Malfeasance", "Sturm", "Last Word", "Thorn", "Bad JuJu", "No Time to Explain", "Outbreak Perfected", "Vigilance Wing", "MIDA Multi-Tool", "The Jade Rabbit", "Rat King", "Traveler's Chosen", "Friends Choose", "The Huckleberry", "Hard Light", "Tommy's Matchbook", "Le Monarque", "Trinity Ghoul", "Fighting Lion","You Choose", "Sunshot", "Graviton Lance", "Polaris Lance", "Skyburner's Oath", "Symmetry", "Devil's Ruin", "Riskrunner", "Tarrabah", "Hawkmoon", "Khvostov 7G-02"]
Kinetic = ["Cerberus +1", "Monte Carlo", "SUROS Regime", "Sweet Business", "MIDA Multi-Tool", "Jade Rabbit", "Bad Juju", "No Time to Explain", "Outbreak Perfected", "Vigilance Wing", "Ace of Spades", "Crimson", "Lumina", "Malfeasance", "Sturm", "The Last Word", "Thorn", "Hawkmoon", "Rat King", "Traveler's Chosen", "Bastion", "Arbalest", "Witherhoard", "The Chaperone", "Izanagi's Burden"]
Energy = ["Hard Light", "Tommy's Matchbook", "Le Monarque", "Trinity Ghoul", "Jötunn", "Merciless", "Telesto", "Eriana's Vow", "Sunshot", "Polaris Lance", "Skyburner's Oath", "Symmetry", "Duality", "Lord of Wolves", "The Fourth Horseman", "Borealis", "Cloudstrike", "Riskrunner", "Tarrabah", "Coldheart", "Prometheus Lens", "Wavesplitter", "Divinty", "Ruinous Effigy", "Fighting Lion", "Devil's Ruin"]
Power = ["Anarchy", "Salvation's Grip", "The Colony", "The Prospector", "Sleeper Simulant", "The Queenbreaker", "Heir Apparent", "Thunderlord", "Xenophage", "Deathbringer", "Eyes of Tomorrow", "The Wardcliff Coil", "Truth", "Two-Tailed Fox", "Legend of Acrius", "Tractor Cannon", "D.A.R.C.I", "Whisper of the Worm", "Black Talon", "The Lament", "Worldline Zero", "Leviathan's Breath", "One Thousand Voices"]
Token = configjson["Token"]
Prefix = configjson["Prefix"]
bot = commands.Bot(command_prefix=Prefix)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=Prefix +"help"))
    print("Bot is ready")


#Roll Command
@bot.command(brief = "Roll An Exotic Weapon To Use")
async def roll(ctx):
    try:
        outputmessage = "Roulette Rolls:\n"
        members = ctx.author.voice.channel.voice_states.keys()
        for i in members:
            randexotic = random.choice(Exotics)
            print(i , "test")
            print(type (i))
            print(type (bot.get_user(i)))
            print(bot.get_user(i))
            outputmessage += ("<@!"+ str(i)+">")+ " got "+ randexotic +"\n"
        await ctx.send(outputmessage)
        print (members)
        print (len(members))
    except:
        randexotic = random.choice(Exotics)
        await ctx.send(ctx.author.mention + " Rolled " + randexotic)

#Re-roll Command
@bot.command(brief = "Re-Rolls an Exotic", description = "Re-Rolls A Prevoiusly Chosen Exotic If User Has A Re-Roll Token Role")
#Re-Roll A Previously Chosen Exotic
async def reroll(ctx):
    userHasRole = "Reroll Token".lower() in [i.name.lower() for i in ctx.author.roles]
    randexotic = random.choice(Exotics)
    if (userHasRole):
        await ctx.author.remove_roles(getRoleByName(ctx, "Reroll Token"))
        await ctx.send("<@!"+ str(ctx.author.id)+"> your re-roll was "+ randexotic)
    else:
        await ctx.send("You dont have a Reroll Token")

bot.run(Token)