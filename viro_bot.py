import asyncio
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
)

# Вставь сюда твой API токен
API_TOKEN = '8171150906:AAE_1Oncau2Lk7kvB7qA7N9LZy_k7HxwyCo'

# Словарь с именами и их значениями
names_dict = {
    "Иванов Иван Иванович": "Симонова Анна Петровна",
    "Петров Петр Петрович": "Гришина Анна Петровна",
    "Сидоров Сидр Сидорович": "Галицина Анна Петровна"
}

# Функция для обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Этот бот поможет узнать тебе твоего методиста, напиши свою фамилию, имя и отчество в иминительном падеже. Напимер: Иванов Иван Иванович, и мы найдем твоего методиста!')

# Функция для обработки текста и проверки на имя
async def check_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    for name, value in names_dict.items():
        if name.lower() in text.lower():
            await update.message.reply_text(f'Методист для {name} : {value}')
            return
    await update.message.reply_text('Такого имени нет в списке.')

# Основная функция
def main() -> None:
    app = ApplicationBuilder().token(API_TOKEN).build()

    # Обработчик команды /start
    app.add_handler(CommandHandler("start", start))

    # Обработчик текстовых сообщений
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_name))

    # Запуск бота
    print("Бот запущен...")
    app.run_polling()

if __name__ == '__main__':
    main()
