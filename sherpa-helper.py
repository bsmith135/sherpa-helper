import random
import discord
from discord.ext import commands
import os

client = discord.Client()
dtok = os.environ.get("dtok")

bot = commands.Bot(command_prefix="Jervis, ")

priv_roles = ["VIP", "Head Sherpa", "Jervis"]


@bot.event
async def on_ready():
    print("JERVIS ONLINE AND READY TO ASSIST!")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if isinstance(message.channel, discord.channel.DMChannel):
        await message.channel.send("Greetings, I am Jervis, assistance to Benjibutt in his Destiny discord server.\n"
                                   "If you would like to use my services, speak to Benji. Otherwise, check his discord "
                                   "server.\nI am unavailable for work outside of this server for the moment.\n"
                                   "Ta-ta for now!")
        return
    if "Zavala" in message.content or "zavala" in message.content:
        await message.channel.send("Whether we wanted it or not, we've stepped into a war with the Cabal on Mars. "
                                   "So let's get to taking out their command, one by one. Valus Ta'aurc. From what I "
                                   "can gather he commands the Siege Dancers from an Imperial Land Tank outside of "
                                   "Rubicon. He's well protected, but with the right team, we can punch through those "
                                   "defenses, take this beast out, and break their grip on Freehold.")

    await bot.process_commands(message)


@bot.command(help="reply with pong.", brief="reply with pong.")
async def ping(ctx):
    await ctx.reply("pong")


@bot.command(help="gives specified role to the user invoking this command.", brief="give me specified role.")
async def make_me(ctx, role: discord.Role):
    if role.name in priv_roles:
        await ctx.reply("Sorry, I do not have permission to add you to this group.")
        return
    await ctx.author.add_roles(role)
    await ctx.reply("User " + ctx.author.name + " has been added to " + role.name + " group.")


@bot.command(help="removes specified role from the user invoking this command.", brief="remove this "
                                                                                      "specified role from me.")
async def unmake_me(ctx, role: discord.Role):
    if role.name in priv_roles:
        await ctx.reply("Sorry, I do not have permission to remove you from this group.")
        return
    await ctx.author.remove_roles(role)
    await ctx.send("User " + ctx.author.name + " has been removed from " + role.name + " group.")


@make_me.error
async def role_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.RoleNotFound):
        await ctx.send("This role does not exist! Please check spelling and capitalization to be sure.")
    else:
        print(error)


@unmake_me.error
async def role_error2(ctx, error):
    await role_error(ctx, error)


@bot.command(help="simulates the rolling of a die with the specified number of sides.", brief="roll a die of n sides.")
async def roll_die(ctx, sides: int):
    c = random.randrange(1, sides + 1)
    await ctx.send(c)


@roll_die.error
async def roll_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.BadArgument):
        await ctx.send("Please use a number ([0-9]+) as an argument.")
    else:
        print(error)

try:
    bot.run(dtok)
except KeyboardInterrupt:
    print("JERVIS, SHUTTING DOWN...")
    bot.close()
