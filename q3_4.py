"""
list_a = []
for i in range(1,101):
    #print(i)
    list_a.append(i)
"""


list_a = list(map(lambda i:i,range(1,101)))
print(list_a)
