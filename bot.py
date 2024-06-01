import asyncio
import logging
import sys
from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, html, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

load_dotenv()

router = Router()

class Test(StatesGroup):
    Q1 = State()
    Q2 = State()

def webapp_builder():
    builder = InlineKeyboardBuilder()
    builder.button(text="Let's Click", web_app=WebAppInfo(url="https://e325-5-140-69-154.ngrok-free.app"))
    return builder.as_markup()


@router.message(CommandStart())
async def command_start(message: Message) -> None:
    await message.reply(text=f"ClickClickClick", reply_markup=webapp_builder())



async def main() -> None:
    dp = Dispatcher()
    dp.include_router(router)
    bot = Bot(token=os.environ.get("TOKEN"), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
