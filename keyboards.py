from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder="Выберите пункт из меню", keyboard=[
    [
        KeyboardButton(text="/help")],
    [KeyboardButton(text="/info_about_squad"), KeyboardButton(text='/upcoming_events')],
    [KeyboardButton(text='/our_content'), KeyboardButton(text='/contact')],
    [KeyboardButton(text='/about_student_squad')]

])

inline_main = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Группа в VK', url='https://vk.com/sio.python')],
                                                    [InlineKeyboardButton(text='Сайт СИО', url='https://vk.com/sio.python')]])