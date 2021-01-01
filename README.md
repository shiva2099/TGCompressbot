---

## Video Compressor Bot



#### The Easy Way

  [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/bhardwajjEE/TGcompressbot)

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
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
  TG_BOT_TOKEN = ""
  AUTH_USERS = [
    7351948
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




#### LICENSE
- GPLv3
# VideoCompress
A Telegram Video Compressor Bot By [@AbirHasan2005](https://t.me/linux_repo). **This bot works for all!** No need to define each user IDs to use bot. Also works in Group.

### Logger Mode:
For Logger Mode use [Beta Branch](https://github.com/AbirHasan2005/VideoCompress/tree/beta). In Logger Mode Bot will send it's Live Status to your Telegram Logs Channel! For more Help to Deploy that ask in [Support Group](https://t.me/linux_repo).

### Demo Bot:
<a href="https://t.me/VidCom_Robot"><img src="https://img.shields.io/badge/BhardwajjEE-Telegram-orange"></a>

## Easy Deploy:
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### Support Group:
<a href="https://t.me/linux_repo"><img src="https://img.shields.io/badge/BhardwajjEE-Telegram-orange"></a>

## Required Configs:
* `TG_BOT_TOKEN` - Get this from [@BotFather](https://t.me/BotFather)
* `BOT_USERNAME` - Your Bot's Username which you send to [@BotFather](https://t.me/BotFather) while creating Bot. ***(Without `@` Before Username!!)***
* `APP_ID` - Get this from my.telegram.org
* `API_HASH` - Get this from my.telegram.org
* `AUTH_USERS` - Put your ID & other Sudo Users IDs. Separate with **Space**. Just for using ***Admin Commands***.

### Admin Commands:
```
log - Bot Will Send it's Logs File.
cancel - Bot will Cancel Last Process.
```




### Credits:
* [Jijinr](https://github.com/Jijinr)
* [SpEcHide](https://github.com/spechide)
* [AbirHasan2005](https://github.com/AbirHasan2005)
