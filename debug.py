from typing import Tuple
import asyncio
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("httpx-issue-634")


async def open_connection(host: str, ssl: bool = True) -> (asyncio.StreamReader, asyncio.StreamWriter):
    reader, writer = await asyncio.open_connection(host, port=443 if ssl else 80, ssl=ssl)
    return reader, writer


async def main(host: str):
    reader, writer = await open_connection(host)
    logger.debug(f"Connection to {host} opened")

    logger.debug(f"Close stream writer...")
    writer.close()
    await writer.wait_closed()


asyncio.run(main("login.microsoftonline.com"), debug=True)
#asyncio.run(main("www.google.fr"), debug=True)
