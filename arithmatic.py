#Arithmatic operator      +,-,*,/,%,**,//
#addition operator
my_salary=10000
our_salary=30000
#expendture=9000

Addition=my_salary+our_salary
print(Addition)
print(my_salary+our_salary)


count,amount=500,1000                                    # single line declaration
print(count+amount)
add=count+amount
print(add)


cost=100;price=200                             # semi colon used for variable declaration in single line
add1=cost+price 
print(add1)

 #line continuation
cost=100+200+\
    3000+4000+\
        5000
print(cost)

print(1000+20000+30000)


add1=(10+20+30)                                # tuple add
add2=(40+50+60)
print(add1)
print(add2)
print(add1+add2)

plus=[1+2+3+4+5]                         # list add
plus1={6+7+8+9+10}                          # set add
print(plus)
print(plus1)
 
floating=99.99+10.99                       # float+float
floating1=100+50.50                         # int+float
print(floating)
print(floating1)
print(99.50+10+20j)                         # float+complex


binary=0b1010+0o1020+0x123+0xabc         # binary+octal+hexa-decimal
print(binary)

comp=10+20j+50                          # complex+int
comp1=10+20j+100+50j                # complex+complex
print(comp)
print(comp1)
print(99.50+10+20j)              # float+complex


boolean=True+False              # bool+bool
print(boolean)
print(True+20)                 # bool+int
print(False+59.90)              # bool+float
print(True+10+20j)               # boolean+complex

print("prasanth"+ " " + "manoharam")
print("prasanth" + "manoharan")
#print("kavi"+10)                 # str + int invalid
print("kavi"+"10")
#print("vasanth"+99.99)              # string + float invalid
print("vasanth"+"99.99")
#print("appu"+20j)          # str  + complex invalid
print("appu"+"10+20j")                 


print("kavi"+str(10))                      # str + int convert to str
print("appu"+str(20j))               # str + complex convert to str
print("vasanth"+str(99.99))                  # str + float convert to str
print("kavi"+str(10))                      # str + int convert to str

print("*******************************")
#subtraction operator
print(1000-5000)
print(5000-1000)
print(5000-4000-3000-2000-1000)
print(1000-2000-3000-4000-5000)
print(99.99-88.88)              # float - float
print(90-88.88)                # int - float
print(45.96-10-20j)            # float - complex
print(49-True)                # int - Bool
print(50-int("10"))                   # str convert to int
#print(50-"10")                   # int - str integral invalid
#print(500-"String")              # str - int invalid
#print("string"-"appu")
#print("string"-"string")              # str-str invalid
print(True-False)
print("*******************************")
#multiplication operator
#print("appu"*"kavi")
#print("appu"*"appu")                  # str * str
print("appu"*20)                       # str * int
#print("appu"*2.5)                     # str * float invalid
print("string"*True)                  # str * bool
print("kavi"*0)                        # str * 0 zero
#print("kavi"*None)                   # str * None type
#print("appu"-None)                  # str - None
#print(None*None)                     # None * None
#print(None+None)                    # None + None
#print(None-None)                     # None - None
#print(10-None)                      # int - None
#print(10+None)                      # int + None
print(True*True)                   # bool * bool
print(True*False)                   # bool * bool


print("*******************************")
#division operator
print(110/5)                 #int
print(100.0/10)
print(10.99/4)                  #float
print(10/3.5)
print(10.50/4.5)
#print(True/False)                 # division by zero error
print(True/True)                # bool division
print(10/True)                 # int divided by bool
#print(10/False)               # division by zero error    
#print(10/0)                 # division by zero error
print(10/10j+20)                        #int divided by complex division
#print("appu"/"appu")
print(10+20j/5+10j)                  #complex / complex


print("*******************************")
#modulus operator

print(10%3)              
print(10.50%2)
print(10.0%2)
print(True%True)               # bool % bool
print(10%True)                 # int % bool
print(3%7)
print(0%4)
#print(10+20j%5+10j)
print("*******************************")

#floor division operator

print(10//3)
print(10//5)
print(10//2)
print(10.0//3)
print(10.0//5)
print(10.0//2)
print(True//True)
print(5//True)
#print(10+20j//5+10j)

print("*******************************")
# exponential operator

print(10**3)
#print(10***3)                                # *** invalid syntax
print(10.0**3)
print(10**3.0)
print(10.5**3.5)
print(True**True)
print(True**False)
#print("appu"**3)                             # str unsupport error
#print("kavi"**True)
print(10+20j**5+10j)

print(0**0)
#print(None**None)


#print('a'+'b')
#print('a'-'b')
#print('a'*'b')
#print('a'/'b')
#print('a'%'b')
#print('a'**'b')
#print('a'//'b')


print(ord('a')+ord('b'))
print(ord('a')-ord('b'))
print(ord('a')*ord('b'))
print(ord('a')/ord('b'))
print(ord('a')%ord('b'))
print(ord('a')**ord('b'))
print(ord('a')//ord('b'))


print(10**3*3)
print(10**-3)





