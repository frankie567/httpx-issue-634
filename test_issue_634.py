import pytest
import httpx


async def main():
    async with httpx.Client() as client:
        response = await client.get("https://login.microsoftonline.com")
    return True


@pytest.mark.asyncio
async def test_asyncio():
    result = await main()
    assert result is True


@pytest.mark.trio
async def test_trio():
    result = await main()
    assert result is True
