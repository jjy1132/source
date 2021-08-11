sws = [60,65,55,70,65]
dbs = [50,60,65,65,70]
oss = [60,75,60,70,60]

number = 0



for number in range(len(sws)):
    
    total = sws[number]+ dbs[number]+oss[number]
    avg = total/3
    
    if sws[number]<40 or dbs[number]<40 or oss[number]<40 or avg<60:
         print("{}번 학생은 불합격입니다.".format(number+1))
    else:
         print("{}번 학생은 합격입니다.".format(number+1))
