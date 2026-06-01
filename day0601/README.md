# Upbit MCP Client-Server Project

## 프로젝트 개요

본 프로젝트는 Upbit의 실시간 암호화폐 데이터를 조회할 수 있는 MCP(Model Context Protocol) 기반 프로그램이다.

MCP 서버는 Upbit Open API를 이용하여 코인 가격, 마켓 정보, 호가창 데이터를 제공하는 Tool을 정의하고, MCP 클라이언트는 해당 Tool을 검색하고 호출하여 결과를 출력한다.

이를 통해 MCP의 핵심 개념인 Tool Discovery와 Tool Calling 과정을 구현하였다.

---

## 프로젝트 구조

```text
upbit-mcp-final/
├── serversupbit_server.py
├── clientsupbit_client.py
├── pyproject.toml
└── README.md
```

### 서버(Server)

MCP 서버는 Upbit API와 통신하며 다음 기능을 제공한다.

* get_upbit_markets()

  * KRW 마켓 목록 조회
* get_coin_price()

  * 특정 코인의 현재가 조회
* get_orderbook()

  * 특정 코인의 호가창 조회

### 클라이언트(Client)

MCP 클라이언트는 서버에 연결한 뒤

1. Tool 목록 조회
2. Tool 선택
3. Tool 호출
4. 결과 출력

과정을 수행한다.

---

## 사용 기술

* Python 3.11+
* MCP (Model Context Protocol)
* Upbit Open API
* HTTPX

---

## MCP 동작 구조

```text
사용자
   ↓
MCP Client
   ↓ list_tools()
MCP Server
   ↓
Upbit Open API
   ↓
MCP Server
   ↓ call_tool()
MCP Client
   ↓
결과 출력
```

---

## 실행 방법

필요 패키지 설치

```bash
pip install mcp httpx
```

프로그램 실행

```bash
python clientsupbit_client.py
```

---

## 실행 결과

프로그램 실행 시 다음 기능이 수행된다.

### 1. MCP 서버 연결

```text
[1] MCP 서버 연결 완료
```

### 2. Tool 목록 조회

```text
get_upbit_markets
get_coin_price
get_orderbook
```

### 3. 마켓 정보 조회

```text
KRW-BTC
KRW-ETH
KRW-XRP
...
```

### 4. 비트코인 현재가 조회

```json
{
  "market": "KRW-BTC",
  "trade_price": 106925000
}
```

### 5. 이더리움 현재가 조회

```json
{
  "market": "KRW-ETH",
  "trade_price": 2916000
}
```

### 6. 비트코인 호가창 조회

```json
{
  "ask_price": 106925000,
  "bid_price": 106901000
}
```

---

## 결론

본 프로젝트는 MCP 서버와 MCP 클라이언트를 분리하여 구현하였으며, Upbit Open API를 활용하여 실시간 암호화폐 데이터를 조회할 수 있도록 구성하였다.

특히 MCP의 핵심 기능인 Tool Discovery(list_tools)와 Tool Calling(call_tool)을 구현하여 MCP 기반 애플리케이션의 기본 구조를 확인할 수 있었다.
