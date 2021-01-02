---

# Telegram Video Compressor Bot

A Telegram Video Compressor Bot By [BhardwajjEE](https://telegram.me/Priyanshu_bhardwaj). **This bot works for all!** No need to define each user IDs to use bot. Also works in Group.
With Bot Log Support .
### Demo Bot:
<a href="https://t.me/CompresserRobot"><img src="https://img.shields.io/badge/CompresserROBOT-Telegram-orange"></a>

## Easy Deploy:
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


#### The Hard Way

```sh
virtualenv -p python3 VENV
. ./VENV/bin/activate
pip install -r requirements.txt
# <Create config.py with variables as given below>
python bot.py
```

An example `config.py` file could be:

**Not All of the variables are mandatory**

```python3
from sample_config import Config

class Development(Config):
  APP_ID = 013332
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
  TG_BOT_TOKEN = "133235:ggutdii3rjjr2"
  AUTH_USERS = [
    134258
  ]
```

### [@BotFather](https://telegram.dog/BotFather) Commands

```
start - Checking bot live.
compress - To compress the video.
cancel - Stop the process.
log - Get log
help - To know about bot
```

## Required Configs:
* `TG_BOT_TOKEN` - Get this from [@BotFather](https://t.me/BotFather)
* `BOT_USERNAME` - Your Bot's Username which you send to [@BotFather](https://t.me/BotFather) while creating Bot. ***(Without `@` Before Username!!)***
* `APP_ID` - Get this from my.telegram.org
* `API_HASH` - Get this from my.telegram.org
* `AUTH_USERS` - Put your ID & other Sudo Users IDs. Separate with **Space**. Just for using ***Admin Commands***.



### All Thanks To :
* [AbirHasan2005](https://github.com/AbirHasan2005)
* [Jijinr](https://github.com/Jijinr)
* [SpEcHide](https://github.com/spechide)

![](https://github.com/bhardwajjEE/bhardwajjEE/blob/main/Assets/ezgif.com-gif-maker.gif)

