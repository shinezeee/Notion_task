

receipts = [] # 빈리스트 #영수증
balance = 1000000
while True :
    num = input("사용하실 기능을 선택헤주세요 (1:입금, 2:출금, 3:영수증보기 4:종료)")
    if num =="1":
        #입금기능
        deposit_amount = int(input("입금할 금액을 입력해주세요 : "))
        balance += deposit_amount  # => balance= balance + deposit_amount
        receipts.append (f'입금 금액 : {deposit_amount}원, 현재 잔액 :{balance}입니다')
        print(f'입금 금액 :{deposit_amount} 원, 현재 잔액 :{balance} 원') 
    elif num == "2":
        #출금기능
        withdraw_amount = int(input("출금할 금액을 입력해주세요 : "))
        withdraw_amount = min(balance, withdraw_amount) #출금 금액은 잔액을 넘을 수 없다 #출금가능금액 = min 으로 최소값을 정해놓는다
        balance -= withdraw_amount
        receipts.append (f'출금 금액 : {withdraw_amount}원, 현재 잔액 :{balance}입니다')
        print(f'출금 금액 :{withdraw_amount} 원, 현재 잔액 :{balance} 원') 
    elif num == "3":
        # 영수증 내역 출력
        print(receipts)
    elif num == "4":
        break #반복문 바깥으로 나감 (while)
    
print('서비스를 종료합니다. 감사합니다.')


        
