from webbrowser import open_new
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
import IO_json

operation = 0
operands = []
path = "C:\\Users\\Asus\\Downloads\\GeekBrains\\Python\\Семинары\\Seminar 10\\Phone Book\\Task03\\db.json"


def help_command(update: Update, context: CallbackContext):
    global operation 
    operation = 0

    res_str = ""
    res_str += "ПРОГРАММА ТЕЛЕФОННЫЙ СПРАВОЧНИК\n"
    res_str += "Выберите действие и введите операнды:\n"
    res_str += "Добавить запись /add\n"
    res_str += "Показать записи /show\n"
    update.message.reply_text(res_str)


def add_command(update: Update, context: CallbackContext):
    msg = update.message.text.split(" ")
    if len(msg) == 3:
        if len(msg[1])!=0 and len(msg[2])!=0:
            IO_json.append_to_json(path,msg[1:])
            update.message.reply_text(f"Добавлена запись {msg[1]} {msg[2]}\n")
            return
    update.message.reply_text("Введены неправильные данные")


def show_command(update: Update, context: CallbackContext):
    db_list = IO_json.read_from_json(path)
    update.message.reply_text(db_list)