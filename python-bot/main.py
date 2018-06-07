
import logging
import settings
from bot import Bot
from usermodel import start_model
from usermodel import handle_model

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=settings.LOGLEVEL)

bot = Bot(token=settings.TOKEN)

@bot.on_message
def on_message(ctx):

  if(ctx.user.state == "asking"):
    handle_question(ctx)
  if(ctx.user.state == "answering"):
    handle_answer(ctx)
  if(ctx.user.state == "modeling"):
    handle_model(ctx)
  if(ctx.user.state == "idle"):
    handle_idle(ctx)

# Figure out new state here
def handle_idle(ctx):
  echo(ctx)

# Figure out crowdsource task here
def handle_question(ctx):
  echo(ctx)

# Figure out answer to question here
def handle_answer(ctx):
  echo(ctx)

# placeholder
def echo(ctx):
  ctx.reply("Hi " + ctx.user.name)

# start user modeling state
@bot.command('start')
def start(ctx):
  start_model(ctx)

bot.start_polling()