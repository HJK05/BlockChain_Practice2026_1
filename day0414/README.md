# 🪙 ERC-20 토큰 및 스테이킹 스마트 컨트랙트 (Sepolia)

본 프로젝트는 ERC-20 토큰(`LabToken`)과 해당 토큰을 활용한 스테이킹 스마트 컨트랙트(`TokenStaking`)를 구현하고 Sepolia 테스트넷에 배포하는 것을 목표로 한다.

사용자는 다음과 같은 기능을 수행할 수 있다:
- 토큰 스테이킹 (예치)
- 스테이킹된 토큰 인출
- 개인 스테이킹 잔액 조회

---

## 스마트 컨트랙트 구성

### 1. LabToken (ERC-20 토큰)
기본적인 ERC-20 토큰 기능을 구현한 컨트랙트이다.

- 토큰 이름: Lab Token (LAB)
- 토큰 전송 (transfer)
- 토큰 사용 승인 (approve)
- 승인 기반 전송 (transferFrom)

### 2. TokenStaking (스테이킹 컨트랙트)
LabToken과 연동되어 동작하는 스테이킹 컨트랙트이다.

#### 주요 기능:
- stake(): 토큰 예치
- withdraw(): 토큰 인출
- getMyStakedBalance(): 개인 스테이킹 잔액 조회

---

##  동작 과정

###  Approve (사용 승인)
사용자가 스테이킹 컨트랙트가 자신의 토큰을 사용할 수 있도록 승인한다.

approve(스테이킹컨트랙트주소, 수량)

### Stake (예치)
승인된 토큰을 스테이킹 컨트랙트로 전송한다.

stake(수량)

### Withdraw (인출)
스테이킹한 토큰을 다시 사용자 지갑으로 반환한다.

withdraw(수량)

---

## 개발 및 실행 환경

- 네트워크: Sepolia Testnet
- 지갑: MetaMask
- 개발 도구: Remix IDE

---

## 수행한 트랜잭션

- ✔ 스마트 컨트랙트 배포
- ✔ 토큰 사용 승인 (approve)
- ✔ 스테이킹 (stake)
- ✔ 토큰 인출 (withdraw)

---

##  트랜잭션 해시

### 배포 (Deployment)
- LabToken: 0xc6aa9e514780f674e08791bb33ef71e3cb68bc9374a3c1c30e901e441d3e938e
- TokenStaking: 0x9efc0d22524a2ade70bf738443241971b8632f6ae3364075efbf59a5399fc57b

### 스테이킹 (Stake)
- 0x99c8494529fc51c7a35b3dda9e75fd32480ac06e791273480499c3aa31265214

### 인출 (Withdraw)
- 0x499d15e139fa1f27a60e286bbe54e7c23256cef2261ad33d5426535cf22b3a0a


## 학습 내용

- ERC-20 토큰 표준 이해
- 스마트 컨트랙트 배포 과정
- approve / transferFrom 메커니즘 이해
- 컨트랙트 간 상호작용 구조
- 기본적인 스테이킹 로직 구현

---

## 결론
본 프로젝트를 통해 ERC-20 토큰과 스테이킹 컨트랙트의 동작 원리를 이해하고, 실제 테스트넷 환경에서 배포 및 트랜잭션을 수행함으로써 블록체인 개발의 기초를 학습할 수 있었다.
