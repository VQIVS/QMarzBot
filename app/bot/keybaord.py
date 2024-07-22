from telebot import types
from ..repositories.tutorial_repository import TutorialRepository

from app import create_app

app = create_app()

class KeyboardCreator:
    def __init__(self):
        pass

    @staticmethod
    def create(buttons):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for button_row in buttons:
            keyboard.add(*button_row)
        return keyboard
    
    @staticmethod
    def createInlineTutorial():
        with app.app_context():
            repo = TutorialRepository()
            items = repo.get_all()
            print(f"items: {items}")  
            inline_keyboard_markup = types.InlineKeyboardMarkup()
            for i, item in enumerate(items, start=1):
                inline_button = types.InlineKeyboardButton(
                    text=item.name, callback_data=f"{item.name}"
                )
                inline_keyboard_markup.add(inline_button)
            return inline_keyboard_markup

class Keyboard:
    def __init__(self):
        pass

    mainButtons = [
        [types.KeyboardButton("⭐️ خرید سرویس")],
        [
            types.KeyboardButton("👤 اشتراک‌های من"),
            types.KeyboardButton("🧪دریافت سرور تست"),
        ],
        [types.KeyboardButton("💡 راهنما‌ی سرویس"), types.KeyboardButton("💬 پشتیبانی")],
        [
            types.KeyboardButton("🛍 خرید عمده️"),
            types.KeyboardButton("👨‍👩‍👧‍👧 معرفی به دوستان"),
        ],
    ]
    mainKeyboard = KeyboardCreator.create(mainButtons)
    tutorialKeyboard = KeyboardCreator.createInlineTutorial()
