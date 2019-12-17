from typing import Tuple
import asyncio
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("httpx-issue-634")


async def open_connection(host: str, ssl: bool = True) -> (asyncio.StreamReader, asyncio.StreamWriter):
    reader, writer = await asyncio.open_connection(host, port=443 if ssl else 80, ssl=ssl)
    return reader, writer


async def make_get(host: str, reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    query = (
        f"GET / HTTP/1.1\r\n"
        f"Host: {host}\r\n"
        f"\r\n"
    )

    writer.write(query.encode('latin-1'))
    while True:
        line = await reader.readline()
        if not line:
            break

        line = line.decode('latin1').rstrip()
        if line:
            logger.debug(f'HTTP header> {line}')


async def close(writer: asyncio.StreamWriter) -> None:
    print("Done?", writer._protocol._closed.done())
    writer.close()
    print("Done?", writer._protocol._closed.done())
    await writer.wait_closed()
    print("Done?", writer._protocol._closed.done())
    # Will be stuck here


async def main(host: str):
    reader, writer = await open_connection(host)
    logger.debug(f"Connection to {host} opened")
    #await make_get(host, reader, writer)

    logger.debug(f"Close stream writer...")
    await close(writer)


asyncio.run(main("login.microsoftonline.com"), debug=True)
#asyncio.run(main("www.google.fr"), debug=True)