import os
import telebot
from telebot import types

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)

    markup.add(
        types.InlineKeyboardButton("📚 Fanficlar haqida", callback_data="fanfics"),
        types.InlineKeyboardButton("👑 Owner", callback_data="owner"),
        types.InlineKeyboardButton("🔐 VIP kanal", callback_data="vip"),
        types.InlineKeyboardButton("📅 Fanfic sanalari", callback_data="dates")
    )

    bot.send_message(
        message.chat.id,
        "🥀 <b>BALLADONA FAMILY</b>\n\n"
        "FF olamimizga xush kelibsiz. 🖤\n"
        "Kerakli bo‘limni tanlang:",
        parse_mode="HTML",
        reply_markup=markup
    )


@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    if call.data == "fanfics":
        bot.answer_callback_query(call.id)
        bot.send_message(
            call.message.chat.id,
            "📚 <b>FANFICLAR HAQIDA</b>\n\n"
            "Hozircha fanficlar qo‘shilmagan.",
            parse_mode="HTML"
        )

    elif call.data == "owner":
        bot.answer_callback_query(call.id)
        bot.send_message(
            call.message.chat.id,
            "👑 <b>OWNER</b>\n\n"
            "@xnythv",
            parse_mode="HTML"
        )

    elif call.data == "vip":
        bot.answer_callback_query(call.id)
        bot.send_message(
            call.message.chat.id,
            "🔐 <b>VIP KANAL</b>\n\n"
            "Qaysi fanfic uchun VIP kanalga kirishni xohlaysiz?\n\n"
            "Hozircha fanficlar qo‘shilmagan.",
            parse_mode="HTML"
        )

    elif call.data == "dates":
        bot.answer_callback_query(call.id)
        bot.send_message(
            call.message.chat.id,
            "📅 <b>FANFIC SANALARI</b>\n\n"
            "Hozircha sanalar qo‘shilmagan.",
            parse_mode="HTML"
        )


print("Balladona Family Bot ishga tushdi!")

bot.infinity_polling()
