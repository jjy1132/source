a = dict()

#1
a['name'] = 'python'
#2
a[('a',)] = 'python'
#3
#a[[1]] = 'python'
#4
a[250] = 'python'




print(a,'\n a[[1]] = \'python\' 같은 경우 key값이 리스트형으로는 올수가 없기때문이며\n key값은 변하면 안된다.')
# 3번 같은 경우 키값이 리스트형으로는 올수가 없기때문이다.
