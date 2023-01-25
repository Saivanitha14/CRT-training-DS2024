s="hello world"
res1=s.split(' ')
print(res1)
print('-'.join(res1))  #join will return str as a result
t=s.capitalize() #only first alpbet capital
print(t)
l=s.title()
print(l)


s1="hello world"
s2="HI"
print(s1.upper())
print(s2.lower())


s1.count('l')#how many times l is repeated in s1

r1="hello world"
r2="HI HELLO"
out=s1.isdigit()#returns true or false
print(out)

out1=r2.swapcase()#lower-upper and upper to lower
print(out1)

#string formatting
first="Mr.x"
age=32
last="yeaars "
print(first+str(age)+last)
#formatting without change data type of age
print("Mr.x is {} years".format(age))
num=6
print("the asquare of {} is {}".format(num,num*num))

print("the asquare of {} is {:.2f}".format(num,num*num))#.2f round of the decimal output to 2 dec places
print("the asquare of {} is {:.1f}".format(num,num*num))

#to represent int to float without chnage data type
print("the asquare of {:10} is {:.6f}".format(num,num*num))#10 spaces
#before f is put fstrings adv is directly put variable name withinn curly braces
print(f"the asquare of {num} is {num*num}")
print(f"the asquare of {num} is {num*num:.5f}")

#exception handling
a=int(input('enter a:'))
b=int(input('enter b:'))
print(a/b)
