'''
Created on 2014年10月30日

@author: xiongzenghui
'''

a,b = 20,10

if a == 20 and b == 10:
    print(a,b,10,"dawdawd",'cdwdawd', True)
    
if a == 20:
    print(a)
elif b == 10:
    print(b)
else:
    print(a+b)


for i in range(1, 10):
    print(i)
    
for i in ['a','b','c','dd','eee']:
    print(i)


str =  "the length of (%s) is %d" %('Hello World',len('Hello World'))
print(str)


print("I am %s" %('format print'))

list = [1, 2, 3, 'dawdawdawd', 3434]
for value in list:
	print(value)

dict = {1:'A', 2:'B', 3:'C', 4:'D'}

for key,value in dict.items():
	print(key, value)

for key in dict:
	print(key, ' : ' , dict[key])

a = input("请输入参数值： ")
print("输入的参数值 = " , a)











