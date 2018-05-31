import copy
import json
import os

import aiohttp
import clashroyale
import discord
from discord.ext import commands

real_os_environ = copy.copy(os.environ)

try:
    with open('data/config.json') as f:
        os.environ = json.load(f)
except FileNotFoundError:
    pass

class AuroraBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=None, case_insensitive=True)
        self.session = aiohttp.ClientSession(loop=self.loop)
        self.royaleapi = clashroyale.Client(os.environ.get('ROYALEAPI'), is_async=True, timeout=10, session=self.session)

        self.add_command(self.ping)

        for c in os.listdir('cogs'):
            if c.endswith('.py') and c not in ():
                try:
                    self.load_extension('cogs.' + c.replace('.py', ''))
                except Exception as e:
                    print(f'Failed {c}: {e}')
                else:
                    print(f'Loaded {c}')

        self.run(os.environ.get('TOKEN'), activity=discord.Game('for Aurora eSports'))

    async def get_prefix(self, message):
        if os.environ == real_os_environ:
            return '>'
        return 'b>'

    async def on_ready(self):
        print('Ready')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {self.latency * 1000:.4f}')

if __name__ == '__main__':
    AuroraBot()
