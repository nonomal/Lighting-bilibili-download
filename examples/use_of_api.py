"""
bilix 提供了各个网站的api，如果你有需要当然可以使用，并且它们都是异步的

bilix provides api for various websites. You can use them if you need, and they are asynchronous
"""
import asyncio

from bilix.sites.bilibili import api
from httpx import AsyncClient


async def main():
    # 需要先实例化一个用来进行http请求的client
    # first we should initialize a http client
    client = AsyncClient(**api.dft_client_settings)
    data = await api.get_video_info(client, 'https://www.bilibili.com/bangumi/play/ep90849')
    print(data)


asyncio.run(main())
