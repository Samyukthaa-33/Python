Tuple1=(1, 33, 38, "sam", "apple")
Tuple2=(33, 38, 23, 40)
Tuple3=("samyukthaa")
print("Tuple1:", Tuple1)
print("Tuple2:", Tuple2)
print("Tuple3:", Tuple3)

print("1. To define a tuple")
print("2. datatype of tuple")
print("3. To Find the number of elements")
print("4. To Repeat the elements in tuple")
print("5. To Get the element")
print("6. To Unpack the elements in tuple")
print("7. Tuple concatenation")
print("8. To remove the first element")
print("9. To print all characters except last 5 characters")
print("10. To reverse the elements of tuple3")
print("11. To fetch elements tuple")
print("12. To fetch a portion from an element")
print("13. To delete the tuple")
print("14. To Find the maximum value")
print("15. To find the minimum value")
print("16. To find the sum")
print("17. To perform sorting")
print("18. To perform reverse sorting")
print("19. To convert into immutable sequence of elements")
print("20. reverse indexing")

a=int(input("Enter any number to perform the required Tuple operation : "))

if(a==1):
  print("Tuple1 elements : ",Tuple1)
  print("Tuple2 elements : ",Tuple2)
  print("Tuple3 elements : ",Tuple3)
 
elif(a==2):
  print("datatype of Tuple1 : ",type(Tuple1))
  print("datatype of Tuple2 : ",type(Tuple2))
  print("datatype of Tuple3 : ",type(Tuple3))
elif(a==3):
  print("no of elements in Tuple1 : ",len(Tuple1))
  print("no of elements in Tuple2 : ",len(Tuple2))
  print("no of elements in Tuple3 : ",len(Tuple3))

elif(a==4):
  r=str(input("enter the tuple to be repeated : "))
  rn=int(input("enter no of times the tuple to be repeated : "))
  if(r=='Tuple1'):
    print("tuple1 repeatation : ",Tuple1*rn)
  else:
    print("tuple2 repeatation : ",Tuple2*rn)
elif(a==5):
  t=str(input("enter the tuple name : "))
  i=int(input("enter the index value : "))
  if(t=='Tuple1'):
    print("element at index ",i," is : ",Tuple1[i])
  else:
    print("element at index ",i," is : ",Tuple2[i])
elif(a==6):
  Tuple1=(1, 33, 38, "sam", "apple")
  print("unpacked the elementsin t1 : " ,(1, 33, 38, "sam", "apple"))
elif(a==7):
  print("concatenated the tuples, t1 and t2 : ",Tuple1+Tuple2)
elif(a==8):
  print("removed the first element of t1 : ",Tuple1[1:])
elif(a==9):
  print("all elements expect the last 3 of t1 : ",Tuple1[:-3])
elif(a==10):
  print("last element of tuple t1 : ",Tuple1[-1])
elif(a==11):
  print("reversed the order of tuple : ",Tuple1[::-1])
elif(a==12):
  print("elements from 2 to 5 : ",Tuple1[2:6])
elif(a==13):
  print("portion of an element : ",Tuple1[3][:5])
elif(a==14):
  print("maximum of elements in tuple t2 is : ",max(Tuple2))
elif(a==15):
  print("minimum of elements in tuple t2 is : ",min(Tuple2))
elif(a==16):
  print("sum of elements in tuple t2 is : ",sum(Tuple2))
elif(a==17):
  print("sorted t2 : ",sorted(Tuple2))
elif(a==18):
  print("reverse sorting of t2 : ",sorted(Tuple2,reverse=True))
elif(a==19):
  del Tuple2
  print("t2 is deleted : ",Tuple2)
elif(a==20):
  strv="python programming"
  print("datatype of strv is : ",type(strv))
  t3=tuple(strv)
  print("converted into immutable sequence of elements : ",type(t3))
else:
  print("Invalid number") 

