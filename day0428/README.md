학교 프린터 요금 결제 DApp

KUSDC 스테이블 코인을 이용하여 학교 프린터 사용 요금을 결제하는 블록체인 기반 DApp 프로젝트입니다.
MetaMask 지갑을 연결하여 KUSDC 토큰 승인(Approve) 후 프린터 사용 요금을 결제할 수 있습니다.

1. KUSDC.sol
ERC-20 기반 스테이블 코인
OpenZeppelin ERC20 사용
Mint 기능 포함

2. SchoolPrintPayment.sol
프린터 요금 결제 컨트랙트
토큰 whitelist 기능
수수료 관리 기능
결제 내역 이벤트 기록

3. print.html
프론트엔드 DApp
MetaMask 연동
KUSDC 잔액 조회
Approve 및 결제 기능 구현

주요 기능
MetaMask 지갑 연결
KUSDC 토큰 발행 및 조회
ERC20 Approve 기능
프린터 요금 결제
결제 내역 및 TX Hash 출력
수수료 및 수령 주소 관리
배포 네트워크
Sepolia Testnet
GIWA Sepolia Testnet

프로젝트 목적

블록체인 기반 결제 시스템의 동작 원리를 이해하고,
ERC-20 토큰과 스마트 컨트랙트를 활용한 실제 DApp 구조를 실습하기 위해 제작하였습니다.
