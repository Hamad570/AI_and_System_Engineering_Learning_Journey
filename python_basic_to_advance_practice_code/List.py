#1. Create a list of 5 fruits and print it.
fruits=['Mango','Apple','Banana','Grapes']
print(fruits)
for i in fruits:
    print(f"I like {i}")

#2.Add a new item into list.
fruits.append('Orange')
fruits.extend(['cherry','lichie'])
fruits.insert(1,'melon')
#3.Remove an item from list.
fruits.remove('melon')
fruits.remove(fruits[0])
fruits.pop()
fruits.pop(1)
print(fruits)
#4.Find length of list.
print(len(fruits))
#Find maximum number in list.
num=[1,34,35,3,2,5,34,99,0]
print(max(num))
#5.Find minimum number in list.
print(f" Minimum number in the list num is {min(num)}")
#6.Sort a list in ascending order.
print(sorted(num))
print(sorted(fruits))
#7.Count how many times an item appears in list.
print(num.count(34))
print(fruits.count('Apple'))
#8.Reverse a list.
fruits.reverse()
print(fruits)

#9.Merge two lists.
new=fruits+num
print(new)
#10.Find sum of all list elements.
print(len(new))
sum=0
for i in num:
    sum+=i
print(sum)

#11.Print all elements of list using loop
for i in new:
    print(i,end=" ")
#12.Take 5 numbers from user and store in list.
n=[]
for i in range(5):
    num=int(input("\n Enter a number:"))
    n.append(num)
print(n)

#13.Find second largest number in list.
n.sort(reverse=True)
print(n[1])
