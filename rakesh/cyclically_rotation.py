#arr1[1,2,3,4,5]
#o/p arr1[3,4,5,1,2]
def cyclically(lst,d,n):
	c=len(lst)-d
	lst1=[]
	for i in range(0,c):
		lst1.append(lst[i])
	lst2 = [i for i in lst + lst1 if i not in lst or i not in lst1]
	lst=lst2 + lst1
	return lst
	#print(lst)

lst=[]
n=int(input("How many number:"))
d=int(input("D="))
for i in range(n):
	ele=int(input())
	lst.append(ele)
cyclically(lst,d,n)
print(lst)
