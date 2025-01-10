from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.methods.delete_message import DeleteMessage
from aiogram.filters import Filter, BaseFilter, CommandStart
from aiogram.methods.send_message import SendMessage
from aiogram.utils.formatting import Text, Bold, TextLink
from aiogram.enums.parse_mode import ParseMode


router = Router()

def create_link(link: str):
    new_link = link.replace('instagram', 'ddinstagram')

    return new_link


class ChatTypeFilter(BaseFilter):
    def __init__(self, chat_type: str | list):
        self.chat_type = chat_type

    async def __call__(self, message: Message) -> bool:
        if isinstance(self.chat_type, str):
            return message.chat.type == self.chat_type
        else:
            return message.chat.type in self.chat_type
        


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Let's go")


@router.message()
async def message_handler(msg: Message):
    if 'instagram' in msg.text and not 'ddinstagram':
        answer = Text(Bold(msg.from_user.full_name), ' send:\n')
        await msg.answer(**answer.as_kwargs(),
                         link_preview_options={'url': create_link(msg.text),
                                              'is_disabled':False,
                                              'prefer_large_media': True},
                         )
        await msg.delete()


