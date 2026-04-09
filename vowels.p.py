"""
s=input()
vowels=0
consonants=0
digits=0
for ch in s:
    if ch.isdigit():
        digits+=1
    elif ch.isalpha():
        if ch.lower() in "aeiou":
            vowels+=1
        else:
            consonants+=1
print("Vowels:",vowels)
print("Consonants:",consonants)
print("Digits:",digits)

n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
"""
#list=[1,2,3,4,5]
#print(list)
#list.append(6)
#list.insert(2,4)
#list.extend([7,8])
#list.remove(2)
#list.pop(2)
#list.clear()
#print(3 in list)
#print(6 in list)
#print(list)
"""
list=[9,4,7,6,3,1,2,5,8]
list.sort()
print(list)
list.sort(reverse=True)
print(list)
 
list1=[1,2,3]
list2=[4,5,6]
print(list1+list2)
print(list1*2)

list=[1,2,3,4,5,6,7]
print(len(list))
print(max(list))
print(min(list))
print(sum(list))

list1=[16,39,16]
list2=list1.copy()
print(id(list1))
print(id(list))

list3=[36,42,75]
list4=[84,34,74]
list3=list4
print(id(list3))
print(id(list4))

list=[[1,2,3],[4,5],[6,7],[8,9,0]]
print(list[3][2])
print(list[1])

list=[1,2.5,"sowmya","geethu"]
for variable in list:
    print(variable)

list=[16,39,18,47]
print(list[1:3])
print(list[:3])
print(list[:3:2])
print(list[::-1])
print(list[-1:-4:-1])
""" 














































