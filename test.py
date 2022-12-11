import pyupbit

access = "r61Vxnli0iv555YTUw4KKTPcFLbtuApGBqLDbODO"          # 본인 값으로 변경
secret = "A5rfbjbCJmlNaoTF5WTIpUpGQPxjHjC42a2sgNvc"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회