# Telegram Bots Example

    Ondrej Sika <ondrej@ondrejsika.com>
    MIT <https://ondrejsika.com/license/mit.txt>

## Install

    git clone git@github.com:ondrejsika/telegram-bots--example.git
    cd telegram-bots--example
    virtualenv .env
    . .env/bin/activate
    pip install python-telegram-bot
    cp conf--example.py conf.py
    # Update your conf.py


## Run bots

### bot.py

Handle `/start` and `/hello` calls. Just send him as message.

    python bot.py

### send.py

Every 30 seconds sends a notification.

    python send.py


