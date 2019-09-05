seq = []  #intialization of the list
print("Enter the number: ")
for i in range(5):
    ele = eval(input())
    seq.append(ele+1)
for i in range(5):
    print(seq[i], end=" ")
print("\n")
delete = eval(input("Enter delete index: "))
seq.pop(delete)

for i in range(len(seq)):
    print(seq[i], end=" ")

#seq = input("Enter data upto 5 data set: ").split()  #intialization and list data accept in single line using spacebar
#for i in range(5):
 #   seq
#for i in range(5):
 #   print(seq[i], end=" ")