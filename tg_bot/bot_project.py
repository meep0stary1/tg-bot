import asyncio
import random

from aiogram import Bot, Dispatcher, types

TOKEN = "BOT_TOKEN"

bot = Bot(token=TOKEN)
dp = Dispatcher()

schedule = [
    {
        "name": "Алижан",
        "day": "Понедельник",
        "time": "",
        "subject" : "Нет пар",
        "type": ""
    },

    {
        "name": "Алижан",
        "day": "Вторник",
        "time": "8:00 - 8:50",
        "subject" : "Discrete Math",
        "type": "practice"
    },

    {
        "name": "Алижан",
        "day": "Вторник",
        "time": "9:00 - 9:50",
        "subject" : "Discrete Math",
        "type": "practice"
    },

    {
        "name": "Алижан",
        "day": "Вторник",
        "time": "10:00 - 10:50",
        "subject" : "Foreign Language",
        "type": "practice"
    },

    {
        "name": "Алижан",
        "day": "Вторник",
        "time": "11:00 - 11:50",
        "subject" : "Foreign Language",
        "type": "practice"
    },

    {
        "name": "Алижан",
        "day": "Среда",
        "time": "8:00 - 8:50",
        "subject" : "Calculus",
        "type": "lecture"
    },

    {
        "name": "Алижан",
        "day": "Среда",
        "time": "9:00 - 9:50",
        "subject" : "Calculus",
        "type": "lecture"
    },

    {
        "name": "Алижан",
        "day": "Среда",
        "time": "11:00 - 11:50",
        "subject" : "Political science",
        "type": "practice"
    },

    {
        "name": "Алижан",
        "day": "Среда",
        "time": "12:00 - 12:50",
        "subject" : "Discrete Math",
        "type": "lecture"
    },

    {
        "name": "Алижан",
        "day": "Среда",
        "time": "13:00 - 13:55",
        "subject" : "Discrete Math",
        "type": "lecture"
    },

    {
        "name": "Алижан",
        "day": "Четверг",
        "time": "8:00 - 8:50",
        "subject" : "Database Management Systems",
        "type": "practice"
    },

    {
        "name": "Алижан",
        "day": "Четверг",
        "time": "9:00 - 9:50",
        "subject" : "Database Management Systems",
        "type": "practice"
    },

    {
        "name": "Алижан",
        "day": "Четверг",
        "time": "10:00 - 10:50",
        "subject" : "Descrete Math",
        "type": "practice"
    },

    {
        "name": "Алижан",
        "day": "Четверг",
        "time": "11:00 - 11:50",
        "subject" : "Descrete Math",
        "type": "practice"
    },

    {
        "name": "Алижан",
        "day": "Пятница",
        "time": "11:00 - 11:50",
        "subject" : "Object-Oriented Programming",
        "type": "practice"
    },

    {
        "name": "Алижан",
        "day": "Пятница",
        "time": "13:05 - 13:55",
        "subject" : "Database Management Systems",
        "type": "practice"
    },

    {
        "name": "Алижан",
        "day": "Суббота",
        "time": "9:00 - 9:50",
        "subject" : "Object-Oriented Programming",
        "type": "practice"
    },

    {
        "name": "Алижан",
        "day": "Суббота",
        "time": "10:00 - 10:50",
        "subject" : "Object-Oriented Programming",
        "type": "practice"
    },

    {
        "name": "Алижан",
        "day": "Суббота",
        "time": "12:00 - 12:50",
        "subject" : "Calculus",
        "type": "lecture"
    },

    {
        "name": "Алижан",
        "day": "Суббота",
        "time": "13:05 - 13:55",
        "subject" : "Calculus",
        "type": "lecture"
    },

    {
        "name": "Олег",
        "day": "Понедельник",
        "time": "",
        "subject" : "Корейский",
        "type": ""
    },

    {
        "name": "Олег",
        "day": "Вторник",
        "time": "",
        "subject" : "Корейский",
        "type": ""
    },

    {
        "name": "Олег",
        "day": "Среда",
        "time": "",
        "subject" : "Корейский",
        "type": ""
    },

    {
        "name": "Олег",
        "day": "Четверг",
        "time": "",
        "subject" : "Корейский",
        "type": ""
    },

    {
        "name": "Олег",
        "day": "Пятница",
        "time": "",
        "subject" : "Корейский",
        "type": ""
    },

    {
        "name": "Олег",
        "day": "Суббота",
        "time": "",
        "subject" : "Корейский",
        "type": ""
    },
    
    {
        "name": "Адина",
        "day": "Понедельник",
        "time": "",
        "subject": "Мобилка (243)",
        "type": ""
    },
    
    {
        "name": "Адина",
        "day": "Понедельник",
        "time": "",
        "subject": "Джава (243)",
        "type": ""
    },
    
    {
        "name": "Адина",
        "day": "Понедельник",
        "time": "",
        "subject": "Ардуино (243)",
        "type": ""
    },
    
    {
        "name": "Адина",
        "day": "Вторник",
        "time": "",
        "subject": "Ардуино (250)",
        "type": ""
    },
    
    {
        "name": "Адина",
        "day": "Вторник",
        "time": "",
        "subject": "Социология (263)",
        "type": ""
    },
    
    {
        "name": "Адина",
        "day": "Вторник",
        "time": "",
        "subject": "Мобилка (250)",
        "type": ""
    },
    
    {
        "name": "Адина",
        "day": "Среда",
        "time": "",
        "subject": "Экономика (222)",
        "type": ""
    },
    
    {
        "name": "Адина",
        "day": "Среда",
        "time": "",
        "subject": "Джава (367)",
        "type": ""
    },
    
    {
        "name": "Адина",
        "day": "Среда",
        "time": "",
        "subject": "Физра",
        "type": ""
    },
    
    {
        "name": "Адина",
        "day": "Четверг",
        "time": "",
        "subject": "Мобилка (231)",
        "type": ""
    },
    
    {
        "name": "Адина",
        "day": "Четверг",
        "time": "",
        "subject": "Социология (125)",
        "type": ""
    },
    
    {
        "name": "Адина",
        "day": "Четверг",
        "time": "",
        "subject": "Ардуино (231)",
        "type": ""
    },
    
    {
        "name": "Адина",
        "day": "Пятница",
        "time": "",
        "subject": "Джава (243)",
        "type": ""
    },
    
    {
        "name": "Адина",
        "day": "Пятница",
        "time": "",
        "subject": "Ардуино (243)",
        "type": ""
    },
    
    {
        "name": "Адина",
        "day": "Пятница",
        "time": "",
        "subject": "Экономика (246)",
        "type": ""
    },

    {
        "name": "Адина",
        "day": "Суббота",
        "time": "",
        "subject" : "Нет пар",
        "type": ""
    },

    {
        "name": "Алтынай",
        "day": "Понедельник",
        "time": "",
        "subject" : "Нет пар",
        "type": ""
    },

    {
        "name": "Алтынай",
        "day": "Вторник",
        "time": "10:00-11:50",
        "subject": "Database Management Systems (C1.1.361K)",
        "type": "practice"
    },
    
    {
        "name": "Алтынай",
        "day": "Вторник",
        "time": "12:00-12:50",
        "subject": "News Writing & Fact Checking (C1.2.249L)",
        "type": "practice"
    },
    
    {
        "name": "Алтынай",
        "day": "Среда",
        "time": "10:00-10:50",
        "subject": "Cultural Studies (C1.1.255P)",
        "type": "practice"
    },
    
    {
        "name": "Алтынай",
        "day": "Среда",
        "time": "11:00-11:50",
        "subject": "Psychology (C1.1.235P)",
        "type": "practice"
    },
    
    {
        "name": "Алтынай",
        "day": "Среда",
        "time": "12:00-13:55",
        "subject": "News Writing & Fact Checking (C1.1.328L)",
        "type": "lecture"
    },
    
    {
        "name": "Алтынай",
        "day": "Четверг",
        "time": "08:00-08:50",
        "subject": "Database Management Systems (C1.1.361K)",
        "type": "practice"
    },
    
    {
        "name": "Алтынай",
        "day": "Четверг",
        "time": "09:00-10:50",
        "subject": "News Writing & Fact Checking (C1.2.249L)",
        "type": "practice"
    },

    {
        "name": "Алтынай",
        "day": "Четверг",
        "time": "11:00-11:50",
        "subject": "Introduction to Programming (C1.2.228K)",
        "type": "practice"
    },
    
    {
        "name": "Алтынай",
        "day": "Пятница",
        "time": "14:00-15:50",
        "subject": "Корейский (C1.2.224P)",
        "type": "practice"
    },
    
    {
        "name": "Алтынай",
        "day": "Суббота",
        "time": "10:00-11:50",
        "subject": "Introduction to Programming (C1.2.228K)",
        "type": "practice"
    }
   
    ]

VALID_NAMES = ["алижан", "олег", "адина", "алтынай"]
VALID_DAYS = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота"]

# Обработчик ВСЕХ сообщений
@dp.message()
async def trigger_handler(message: types.Message) -> None:
    
    # Если message.text равно None (стикер, фото, голосовое сообщение и т.д.), 
    # просто выходим из функции (ничего не делаем).
    if message.text is None:
        return 

    inputt = message.text.lower()

    # --- ЛОГИКА ДЛЯ "ДАБЛ Ю?" ---
    if "дабл ю?" in inputt:
        answers = ["Дабл ю", "Не дабл ю"]
        random_answer = random.choice(answers) 
        await message.answer(random_answer)

    # --- ЛОГИКА ДЛЯ "РАСПИСАНИЯ" ---
    elif "расписание" in inputt: 
        
        # Инициализируем name и day безопасными значениями по умолчанию
        name_found = None
        day_found = None

        for n in VALID_NAMES:
            if n in inputt:
                name_found = n 
                break 

        for d in VALID_DAYS:
            if d in inputt:
                day_found = d
                break 

        if name_found is None or day_found is None:
            return 

        lessons = [l for l in schedule if l["name"].lower() == name_found and l["day"].lower() == day_found]
        
        if not lessons:
            await message.answer(f"{name_found.title()} в {day_found.title()} пар нет.")
            return
        
        response = f"Расписание для {name_found.title()} на {day_found.title()}:\n"
        for lesson in lessons:
            if lesson["time"]:
                response += f"{lesson['time']} - {lesson['subject']} ({lesson['type']})\n"
            else:
                response += f"{lesson['subject']}\n"
        
        await message.answer(response)

    # --- ЛОГИКА ДЛЯ "КАМЕНЬ-НОЖНИЦЫ-БУМАГА" ---
    elif "камень" in inputt or "ножницы" in inputt or "бумага" in inputt:
        
        answers = ["камень", "ножницы", "бумага"]
        random_answer = random.choice(answers)
        
        await message.answer(f"Я выбираю: {random_answer}") 


# Запуск бота
async def main() -> None:
    print("!!! БОТ С ТРИГГЕРОМ ЗАПУЩЕН !!!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):

        print("!!! БОТ ОСТАНОВЛЕН !!!")
