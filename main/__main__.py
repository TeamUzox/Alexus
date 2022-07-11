

from main.client import bot, asst
from pyrogram.errors import AccessTokenInvalid, ApiIdInvalid, ApiIdPublishedFlood
from pytgcalls import idle as pyidle
from pytgcalls import PyTgCalls



if __name__ == "__main__":
    try:
        asst.start()  # Not using run as wanna print 
        print("•×•Yeahhhh boi Assistant bot Started•×•")
        bot.run() # using run for session client
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your TOKEN is not valid.")

bot = bot
call_py = PyTgCalls(bot)

call_py.start()
print("Vc Client Started")
pyidle()
