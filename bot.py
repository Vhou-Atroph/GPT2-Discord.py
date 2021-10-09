import discord
from discord.ext import commands
from discord.ext.commands import Bot
import datetime
import tensorflow as tf
import gpt_2_simple as gpt2


#client = discord.Client()
prefix = '!'
desc = "Bot created by [your name]"
bot = Bot(command_prefix=prefix, description=desc)
version= 'v1'
token='xxxxx'

#On startup
@bot.event
async def on_ready():
    print('------')
    print('GPT2 time!'.format(bot))
    print('Logged in as...')
    print('USER: [bot]')
    print('ID: [botid]')
    print('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
    print('------')
    
#GPT2
class Ai(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        
    global sess
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess, run_name='run1')
        
    @commands.command(name='gpt', help='Generates hell')
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def gpt(self, ctx, heehoo=""):
        print('Generating...')
        print('{} wants to generate with GPT2.'.format(ctx.author.name))
        print("Prompt: {}".format(heehoo))
        async with ctx.channel.typing():
            hell = gpt2.generate(sess, 
                run_name='run1',
                length=150,
                temperature=.8,
                prefix=heehoo,
                nsamples=1,
                batch_size=1,
                return_as_list=True)[0]
            await ctx.channel.send(hell)
        print(hell)
    
#Add cogs
bot.add_cog(Ai(bot))

bot.run(token)
