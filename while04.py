coffee = 10

while True :
    money = int(input("돈을 넣어 주세요 : "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
        print("남은 커피의 양은 {}개입니다.".format(coffee))
    elif money > 300:
        print("거스름돈 {}를 주고 커피를 줍니다.".format(money-300))
        coffee = coffee -1
        print("남은 커피의 양은 {}개입니다.".format(coffee))
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")    
        print("남은 커피의 양은 {}개입니다.".format(coffee))
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
