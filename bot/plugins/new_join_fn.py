#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | pratyush


from bot.localisation import Localisation
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

async def new_join_f(client, message):
    # delete all other messages, except for AUTH_USERS
    await message.delete(revoke=True)
    # reply the correct CHAT ID,
    # and LEAVE the chat
    chat_type = message.chat.type
    if chat_type != "private":
        await message.reply_text(
            Localisation.WRONG_MESSAGE.format(
                CHAT_ID=message.chat.id
            )
        )
        # leave chat
        await message.chat.leave()


async def help_message_f(client, message):
    # display the /help message
    await message.reply_text(
        Localisation.HELP_MESSAGE,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('My Father 🖤', url='https://telegram.me/priyanshu_bhardwaj')
                ],
                [
                    InlineKeyboardButton('Support Group', url='https://t.me/video_Compress')
                ],
                [
                    InlineKeyboardButton('GitProfile', url='https://github.com/bhardwajjEE'),
                    InlineKeyboardButton('Source 🌟', url='https://github.com/bhardwajjEE/TGCompressBOT') 
                ]
            ]
        ),
        quote=True
    )
