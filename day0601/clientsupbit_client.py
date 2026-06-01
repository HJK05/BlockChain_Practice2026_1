import asyncio
import json

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


def print_json(title: str, data):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

    if hasattr(data, "content"):
        for content in data.content:
            if hasattr(content, "text"):
                try:
                    parsed = json.loads(content.text)
                    print(json.dumps(parsed, indent=2, ensure_ascii=False))
                except json.JSONDecodeError:
                    print(content.text)
            else:
                print(content)
    else:
        print(data)


async def main():
    server_params = StdioServerParameters(
        command="python",
        args=["serversupbit_server.py"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            print("\n[1] MCP 서버 연결 완료")

            print("\n[2] 사용 가능한 MCP Tool 목록 조회")
            tools = await session.list_tools()

            for tool in tools.tools:
                print(f"- {tool.name}: {tool.description}")

            print("\n[3] Upbit 마켓 목록 조회")
            markets = await session.call_tool(
                "get_upbit_markets",
                {"quote": "KRW"}
            )
            print_json("KRW 마켓 목록 일부", markets)

            print("\n[4] 비트코인 현재가 조회")
            btc_price = await session.call_tool(
                "get_coin_price",
                {"market": "KRW-BTC"}
            )
            print_json("KRW-BTC 현재가", btc_price)

            print("\n[5] 이더리움 현재가 조회")
            eth_price = await session.call_tool(
                "get_coin_price",
                {"market": "KRW-ETH"}
            )
            print_json("KRW-ETH 현재가", eth_price)

            print("\n[6] 비트코인 호가창 조회")
            btc_orderbook = await session.call_tool(
                "get_orderbook",
                {"market": "KRW-BTC"}
            )
            print_json("KRW-BTC 호가창", btc_orderbook)


if __name__ == "__main__":
    asyncio.run(main())
    
print("\n프로그램 종료")