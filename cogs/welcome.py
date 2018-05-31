import discord
from discord.ext import commands

class Welcome:
    def __init__(self, bot):
        self.bot = bot
        self.roles = {
            'visitor': 436285684920090624,
            'eu': 436274976845332490,
            'apac': 436275174845710356,
            'americas': 436275117471956992,
            'tryout': 449446972215132161
        }

    @commands.command(aliases=['EU', 'APAC', 'Americas', 'Tryout'])
    async def visitor(self, ctx, member: discord.Member):
        await member.add_roles(discord.utils.get(ctx.guild.roles, id=self.roles[ctx.invoked_with.lower()]))
        await ctx.send(f'Role given.')

def setup(bot):
    bot.add_cog(Welcome(bot))