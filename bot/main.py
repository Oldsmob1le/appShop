# application = Application.builder().token("6338177542:AAFS7Ynqe6tu_ftGcNTP2fZPwK1uxPztOp0").build()

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, CallbackQueryHandler

ADMIN_ID = 945368215

async def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    buttons = [
        [InlineKeyboardButton("Сделать Заказ", callback_data='order')],
        [InlineKeyboardButton("Задать Вопрос", callback_data='question')]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await update.message.reply_text(f"Привет, {user.first_name}!", reply_markup=reply_markup)
    await update.message.reply_text("Чтобы перейти в магазин, нажми на кнопочку «Shop» 👇")

async def handle_message(update: Update, context: CallbackContext):
    user = update.message.from_user
    text = update.message.text

    if text == "Сделать Заказ":
        await update.message.reply_text("Наш менеджер уже бежит к Вам в Личные сообщения 🏃‍♀️")
        await context.bot.send_message(ADMIN_ID, f"Заказ.\nКлиент: @{user.username}!")
    elif text == "Задать Вопрос":
        await update.message.reply_text("Наш менеджер уже бежит к Вам в Личные сообщения 🏃‍♀️")
        await context.bot.send_message(ADMIN_ID, f"Вопрос.\nКлиент: @{user.username}!")

async def set_menu_button(update: Update, context: CallbackContext):
    await update.message.reply_text("Вызвать меню можно с помощью команд, но сайт не изменяется.")

async def button_click_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    user = query.from_user 
    await query.answer()
    
    if query.data == 'order':
        await context.bot.send_message(ADMIN_ID, f"Заказ.\nКлиент: @{user.username}!")
        await query.message.reply_text("Наш менеджер уже бежит к Вам в Личные сообщения 🏃‍♀️")
    elif query.data == 'question':
        await context.bot.send_message(ADMIN_ID, f"Вопрос.\nКлиент: @{user.username}!")
        await query.message.reply_text("Наш менеджер уже бежит к Вам в Личные сообщения 🏃‍♀️")

def main():
    application = Application.builder().token("6338177542:AAFS7Ynqe6tu_ftGcNTP2fZPwK1uxPztOp0").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("setmenubutton", set_menu_button))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(CallbackQueryHandler(button_click_handler))
    
    application.run_polling()

if __name__ == '__main__':
    main()
