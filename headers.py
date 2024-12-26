import emoji
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from keyboards import inline_main

router = Router()

help_cmd_tx =emoji.emojize("""

:robot:<strong>Список доступных команд</strong>:robot::

:cyclone:<strong>/start</strong> - <em>Базовая информация об нашем отряде</em>
:cyclone:<strong>/help</strong> - <em>Список всех существующих команд</em> 
:cyclone:<strong>/about_student_squad</strong> - <em>инфа об студотрядах(0 самой структуре + ссылка на презентацию от Андрея</em>
:cyclone:<strong>/contact</strong> - <em>информация для обратной связи</em> 
:cyclone:<strong>/info_about_squad</strong> - <em>Подробная информация</em>             
:cyclone:<strong>/upcoming_events</strong> - <em>информация о мероприятих отряда</em>
:cyclone:<strong>/our_content</strong> - <em>видео из группы студотряда</em>
""")


about_student_squad_tx = """<strong>Студенческие отряды</strong> — это <em>крупнейшая молодежная организация нашей страны</em>, которая обеспечивает временной трудовой занятостью молодых людей.
<em>Строительные отряды появились</em> в <strong>1959 году и имели численность 339 бойцов</strong>, но сегодня их численность составляет <strong>более 30 000 человек</strong>, которые трудятся более чем на <strong>20 трудовых проектов всероссийского, межрегионального и международного уровня</strong>. Студенты работают на объектах Госкорпорации <strong>«Росатом»</strong> и <strong>ПАО «Газпром»</strong>.

<strong>Студенческие отряды</strong> – <em>больше, чем просто работа! Проведи свое лучшее лето в ССО!</em>"""


cmd_contact = """Наш штаб расположен в главном корпусе НГТУ им. Р.Е.Алексеева, он находится по адрессу ул. Минина 24/1\n 
Командир отряда - Андрей Евдокимов
номер телефона: +7 (915) 948-69-52\n
Комиссар отряда - Даня Ковалев
номер телефона: +7 (950) 602-77-84\n
Руководитель прессы - Яна Ватагина
"""





@router.message(Command('help'))
async def help_cmd(message:Message):
    await message.answer(help_cmd_tx, parse_mode="HTML")# cписое всех команд, которые есть в боте
    # может быть ещё нужно ещё что-то добавить


@router.message(Command("contact"))
async def contact_cmd(message: Message):
    await message.answer_location(latitude=56.326552, longitude=44.024662)# Выводим расположение нашего отряда
    await message.answer(cmd_contact, reply_markup=inline_main)  # текст с контактами: командира, начальника прессы, комисар, email@, номер телефона
    #добавить медиагруппу с фотками из VK


@router.message(Command("about_student_squad"))
async def student_squad_cmd(message: Message):
    await message.answer_photo(photo="AgACAgIAAxkBAAIBRWc4NqZ4iVfBCIvgQrY0eagwUo2qAAKX6jEbqzPBSWbigZbb6wTLAQADAgADeQADNgQ")
    await message.answer(about_student_squad_tx, parse_mode="HTML", )

@router.message(Command('feedback'))
async def feedback_user(message:Message):
    await message.answer("пока в ТЕСТЕ.\n По задумке должна выводиться форма, в которой пользователь может вносить свои предложения, например, улучшение или добавление какого-либо функционала,  ")


# @ router.message(F.photo)#"""Нужны видео от Андрея"""
# async def our_content_cmd(message: Message):
#     data = message.photo[-1].file_id
#     await message.answer(f"{data}")



