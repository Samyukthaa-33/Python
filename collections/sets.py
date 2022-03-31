s1={7,8,4,10.2,"python",(1,2,3)}
s2=set([10,8,6,4,2,7])

print("s1 : ",s1)
print("s2 : ",s2)

print("1. To print set elemenets")
print("2. datatype of t1")  
print("3. To add an element to s1")
print("4. To update elements")
print("5. To discard an element")
print("6. To remove an element")
print("7. To clear s1") 
print("8. union of s1 and s2")
print("9. intersection of s1 and s2")
print("10. difference of s1 and s2") 
print("11. symmetric difference of s1 and s2")
print("12. To check  s2 is disjoint of s1")
print("13. To check  s2 is subset of s1")
print("14. pop operation") 
print("15. To copy") 
print("16. To display elements in s1 using for loop")
print("17. To display maximum value")
print("18. To display minimum value") 
print("19. sum of elements in set")
print("20. sort operation") 
print("21. length of the set")

a=int(input("Enter any number to perform the required set operation : "))
if(a==1):
  print("s1 elements : ",s1)
  print("s1 elements : ",s2)
elif(a==2):
  print("datatype of s1 : ",type(s1))
  print("datatype of s2 : ",type(s2))
elif(a==3):
  e=str(input("enter a string element to be added to the s1 : "))
  s1.add(e)
  print(s1)
elif(a==4):
  s2.update([11,22,33,44,55])
  print("updated elements in s2 : ",s2)
elif(a==5):
  s2.discard(2)
  print("2 in s2 is discarded",s2)
elif(a==6):
  s2.remove(4)
  print("element 4 is removed from s2",s2)
elif(a==7):
  s1.clear()
  print("s1 is cleared : ",s1)
elif(a==8):
  print("Union of s1 and s2 : ",s1|s2)
elif(a==9):
  print("Intersection of s1 and s2 : ",s1&s2)
elif(a==10):
  print("difference of s1 and s2 : ",s1-s2)
elif(a==11):
  print("symmetric difference of s1 and s2 : ",s1^s2)
elif(a==12):
  print(" is s2 is disjoint of s1 ? :  ",s1.isdisjoint(s2))
elif(a==13):
  print("is s2 is superset of s1 ? : ",s1.issuperset(s2))
elif(a==14):
  v=s1.pop()
  print("poped element from s1 : ",v)
  print("s1 after poping a random element : ",s1)
elif(a==15):
  s3=s1.copy()
  print("s1 is copied to s3 : ",s3)
elif(a==16):
  print("elements in s1 : ")
  for i in set(s1):
    print(i)
elif(a==17):
  print("maximum value in s2 is : ",max(s2))
elif(a==18):
  print("minimum value in s2 is : ",min(s2))
elif(a==19):
  print("sum of elements in s2 : ",sum(s2))
elif(a==20):
  print("elements of s2 is sorted : ",sorted(s2))
elif(a==21):
  print("length of s1 is : ",len(s1))
