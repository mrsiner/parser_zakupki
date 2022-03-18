from aiogram.types import ParseMode
from aiogram import utils
from peeweee import *

db = SqliteDatabase('tender.db')

class BaseModel():
    class Meta:
        database = db



class Bitrix_FZ_44(BaseModel):
    title = CharField()
    url = TextField()


