import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

# logging.basicConfig(level=logging.INFO, format=f"%(actime)s - %(name)s - %(levelname)% - %(message)s")
# logger = logging.getLogger(__name__)

load_dotenv()
TOKEN_BOT = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(storage= MemoryStorage())