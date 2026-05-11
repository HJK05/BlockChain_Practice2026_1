// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract SchoolPrintPayment is Ownable {
    address public receiver;

    uint256 public feeRate;
    uint256 public constant FEE_DENOMINATOR = 10000;
    uint256 public constant MAX_FEE_RATE = 1000;

    mapping(address => bool) public whitelistedTokens;
    mapping(address => uint256) public collectedFees;

    event PrintPaid(
        address indexed payer,
        address indexed token,
        uint256 amount,
        uint256 fee,
        uint256 netAmount,
        string studentId,
        string printerId,
        uint256 pages,
        uint256 timestamp
    );

    event TokenWhitelisted(address indexed token);
    event TokenRemovedFromWhitelist(address indexed token);
    event ReceiverUpdated(address oldReceiver, address newReceiver);
    event FeeRateUpdated(uint256 oldFeeRate, uint256 newFeeRate);
    event FeeWithdrawn(address indexed token, uint256 amount);

    constructor(address _receiver, uint256 _feeRate) Ownable(msg.sender) {
        require(_receiver != address(0), "Invalid receiver");
        require(_feeRate <= MAX_FEE_RATE, "Fee too high");

        receiver = _receiver;
        feeRate = _feeRate;
    }

    function payForPrint(
        address token,
        uint256 amount,
        string calldata studentId,
        string calldata printerId,
        uint256 pages
    ) external {
        require(whitelistedTokens[token], "Token not allowed");
        require(amount > 0, "Amount must be greater than 0");
        require(pages > 0, "Pages must be greater than 0");

        uint256 fee = (amount * feeRate) / FEE_DENOMINATOR;
        uint256 netAmount = amount - fee;

        IERC20(token).transferFrom(msg.sender, receiver, netAmount);

        if (fee > 0) {
            IERC20(token).transferFrom(msg.sender, address(this), fee);
            collectedFees[token] += fee;
        }

        emit PrintPaid(
            msg.sender,
            token,
            amount,
            fee,
            netAmount,
            studentId,
            printerId,
            pages,
            block.timestamp
        );
    }

    function addWhitelistedToken(address token) external onlyOwner {
        require(token != address(0), "Invalid token");
        whitelistedTokens[token] = true;
        emit TokenWhitelisted(token);
    }

    function removeWhitelistedToken(address token) external onlyOwner {
        whitelistedTokens[token] = false;
        emit TokenRemovedFromWhitelist(token);
    }

    function setReceiver(address newReceiver) external onlyOwner {
        require(newReceiver != address(0), "Invalid receiver");

        address oldReceiver = receiver;
        receiver = newReceiver;

        emit ReceiverUpdated(oldReceiver, newReceiver);
    }

    function setFeeRate(uint256 newFeeRate) external onlyOwner {
        require(newFeeRate <= MAX_FEE_RATE, "Fee too high");

        uint256 oldFeeRate = feeRate;
        feeRate = newFeeRate;

        emit FeeRateUpdated(oldFeeRate, newFeeRate);
    }

    function withdrawFees(address token) external onlyOwner {
        uint256 amount = collectedFees[token];
        require(amount > 0, "No fees");

        collectedFees[token] = 0;
        IERC20(token).transfer(owner(), amount);

        emit FeeWithdrawn(token, amount);
    }
}
