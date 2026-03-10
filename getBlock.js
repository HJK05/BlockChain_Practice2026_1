require("dotenv").config();
const axios = require("axios");

const INFURA_API_KEY = process.env.INFURA_API_KEY;
const INFURA_URL = `https://mainnet.infura.io/v3/${INFURA_API_KEY}`;

async function main() {

    const response = await axios.post(INFURA_URL, {
        jsonrpc: "2.0",
        method: "eth_blockNumber",
        params: [],
        id: 1
    });

    const latestBlockHex = response.data.result;
    const latestBlockNumber = parseInt(latestBlockHex, 16);

    const blockResponse = await axios.post(INFURA_URL, {
        jsonrpc: "2.0",
        method: "eth_getBlockByNumber",
        params: [latestBlockHex, true],
        id: 2
    });

    const txCount = blockResponse.data.result.transactions.length;

    console.log("Latest Block Number:", latestBlockNumber);
    console.log("Transaction Count:", txCount);

}

main();