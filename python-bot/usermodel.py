import csv
from difflib import get_close_matches

courses = {}
with open('courselist.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile,delimiter=',')
    for row in csvReader:
        courses[row[0]] = row[1]

recommendations = {
  'course' : {
    'name' : 'Courses',
    'question' : "What are some courses that you liked?"
  }
}

greeting = '''Hello %s, my name is MyCI. I am a chatbot that can help you find recommendations around campus with the help of other students. Currently I can give recommendations on:
%s
To give you recommendations I need to know some of your preferences first.'''

# pending course confirmations for users
pending = {}

def start_model(ctx):
  reply = greeting % (ctx.user.name, recommendation_list())
  ctx.reply(reply)
  ctx.user.set_state('modeling')
  ctx.reply(recommendations['course']['question'])

def handle_model(ctx):
  user_id = ctx.user.id
  if user_id in pending.keys():
    closest = get_close_matches(ctx.message, ['yes','no'], cutoff=0)[0]
    if closest == 'yes':
      reply = 'Added `%s` to your preferences.' % (pending[user_id] + ' ' + courses[pending[user_id]])
    else:
      reply = 'Did not add `%s` to your preferences.' % (pending[user_id] + ' ' + courses[pending[user_id]])
    ctx.reply(reply)
    ctx.reply(recommendations['course']['question'])
    del pending[user_id]
  else:
    closest = get_close_matches(ctx.message, [code + ' ' + courses[code] for code in courses], cutoff=0)[0]
    reply = "Did you mean the course: `%s`" % closest
    coursecode = closest.split(' ')[0]
    ctx.reply(reply)
    pending[user_id] = coursecode

def recommendation_list():
  res = ""
  for r in recommendations:
    res += '`%s`\n' % recommendations[r]['name']
  return res


