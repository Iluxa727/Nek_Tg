##
#
# 
# 
# Name: ZigaPing
# Author: @iluha_sh
#meta developer: @FoxiModules
from .. import loader, utils
import time
import asyncio
import psutil

@loader.tds
class zing(loader.Module):
    """"""
    strings = {
    "name": "Zing"
    }

    @loader.command()
    async def zing(self, message):
        """показ характеристик вашего сервера подпишись """
        CPU = psutil.cpu_percent()
        RAM = psutil.virtual_memory().percent
        ping_start = time.time()
        await message.edit(
        f"<b>проверка характеристик иди покури🍌💦...</b>"
        )
        ping_finish = time.time()

        await message.edit(
        f"<emoji document_id=5172533495162995360><emoji document_id=5375119663631965285>🐓</emoji></emoji> <b>PING:</b> {round((ping_finish - ping_start)*1000, 2)} ms\n"
        f"<emoji document_id=5172861866887611077><emoji document_id=5381964278133693296>⚡</emoji></emoji> <b>CPU:</b> {CPU}%\n"
        f"<emoji document_id=5174693704799093859>🖥️</emoji> <b>RAM:</b> {RAM}%"
        )