###Function syntax
"""------------------------------
def function_name(parameters):
    '''documentation'''      
    #function body
function_name(arguments)
------------------------------
a=int(input("enter a:"))
b=int(input("enter b:"))
def add (a,b):
    return(a+b)
c=add(a,b)
print(c)
def sub (a,b):
    return(a-b)
c=sub(a,b)
print(c)
def mul (a,b):
    return(a*b)
c=mul(a,b)
print(c)
def div (a,b):
    return(a/b)
c=div(a,b)
print(c)"""
"""function using list"""

def even_odd(arr):
    list1=[]
    list2=[]
    for i in arr:
        if i%2==0:
            list1.append(i)
        else:
            list2.append(i)
        
    return list1,list2
list1=[1,2,3,4,5,6,7,8,9]
num1,num2=even_odd(list1)

print("even numbers",num1)
print("odd numbers",num2)































        
