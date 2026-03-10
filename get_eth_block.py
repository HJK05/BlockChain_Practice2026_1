import requests
import json

# Infura endpoint (replace YOUR_PROJECT_ID)
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_PROJECT_ID"

# JSON-RPC function
def json_rpc(method, params=[]):
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": 1
    }

    response = requests.post(INFURA_URL, json=payload)
    return response.json()["result"]

# 1. Get latest block number
latest_block_hex = json_rpc("eth_blockNumber")
latest_block = int(latest_block_hex, 16)

print("Latest Block Number:", latest_block)

# 2. Get block data
block = json_rpc("eth_getBlockByNumber", [latest_block_hex, True])

tx_count = len(block["transactions"])

print("Transaction Count:", tx_count)
