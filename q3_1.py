a= "Life is too short, you need python"

if "wife" in a : print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a : print("shirt")
elif "need" in a : print("need")
else : print("none")

print("---------------------------------------------------")

i = 1
total = 0
while i <= 1000:
    if i % 3 == 0:
        total += i
    i +=1
print(total)

print("---------------------------------------------------")

j = 1
while j<=5 :
    print('*'*j)
    j += 1

print("---------------------------------------------------")

list_a = []
for i in range(1,101):
    #print(i)
    list_a.append(i)
print(list_a)

print("---------------------------------------------------")

list_score = [70,60,55,75,95,90,80,80,85,100]
total_5 = 0
avg = 0

for score in list_score:
    total_5 += score

avg = total_5/len(list_score)
print(avg)

print("---------------------------------------------------")

numbers = [1, 2, 3, 4, 5]

result = [n*2 for n in numbers if n%2 ==1 ]

print(result)
