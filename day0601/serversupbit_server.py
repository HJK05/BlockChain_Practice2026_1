import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("upbit-server")

BASE_URL = "https://api.upbit.com/v1"


@mcp.tool()
async def get_upbit_markets(quote: str = "KRW") -> list[dict]:
    """
    Upbit 마켓 목록을 조회합니다.
    예: quote='KRW' → KRW-BTC, KRW-ETH 등
    """
    quote = quote.upper()

    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(
            f"{BASE_URL}/market/all",
            params={"isDetails": "false"}
        )
        response.raise_for_status()
        markets = response.json()

    result = []
    for market in markets:
        if market["market"].startswith(f"{quote}-"):
            result.append({
                "market": market["market"],
                "korean_name": market["korean_name"],
                "english_name": market["english_name"],
            })

    return result


@mcp.tool()
async def get_coin_price(market: str = "KRW-BTC") -> dict:
    """
    특정 코인의 현재가 정보를 조회합니다.
    예: market='KRW-BTC'
    """
    market = market.upper()

    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(
            f"{BASE_URL}/ticker",
            params={"markets": market}
        )
        response.raise_for_status()
        data = response.json()

    if not data:
        return {"error": "해당 마켓 정보를 찾을 수 없습니다."}

    item = data[0]

    return {
        "market": item["market"],
        "trade_price": item["trade_price"],
        "opening_price": item["opening_price"],
        "high_price": item["high_price"],
        "low_price": item["low_price"],
        "change": item["change"],
        "signed_change_price": item["signed_change_price"],
        "signed_change_rate": item["signed_change_rate"],
        "acc_trade_price_24h": item["acc_trade_price_24h"],
        "acc_trade_volume_24h": item["acc_trade_volume_24h"],
        "trade_date": item["trade_date"],
        "trade_time": item["trade_time"],
    }


@mcp.tool()
async def get_orderbook(market: str = "KRW-BTC") -> dict:
    """
    특정 코인의 주문장/호가창 데이터를 조회합니다.
    예: market='KRW-BTC'
    """
    market = market.upper()

    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(
            f"{BASE_URL}/orderbook",
            params={"markets": market}
        )
        response.raise_for_status()
        data = response.json()

    if not data:
        return {"error": "호가창 정보를 찾을 수 없습니다."}

    item = data[0]

    orderbook_units = []
    for unit in item["orderbook_units"][:10]:
        orderbook_units.append({
            "ask_price": unit["ask_price"],
            "bid_price": unit["bid_price"],
            "ask_size": unit["ask_size"],
            "bid_size": unit["bid_size"],
        })

    return {
        "market": item["market"],
        "timestamp": item["timestamp"],
        "total_ask_size": item["total_ask_size"],
        "total_bid_size": item["total_bid_size"],
        "orderbook_units": orderbook_units,
    }


if __name__ == "__main__":
    mcp.run(transport="stdio")
