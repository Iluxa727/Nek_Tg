#meta developer: @iluha_sh
from .. import loader
from asyncio import sleep


@loader.tds
class WHI(loader.Module):
    strings = {"name": "WHI"}

    @loader.owner
    async def whcmd(self, message):
        for _ in range(1):
            for wh in ["Запускаем Батник для установки \nхикка на виндовс","Установка пакетов 100%",
"Копирование репозиторий 100%🖥️",
"скачиваем зависимости 100%🛑",
"Запуск пакетов 100%🙂",
"Cloning HIKKA🖥️",
"HIKKA STARTING😉"]:
                await message.edit(wh)
                await sleep(1.2)