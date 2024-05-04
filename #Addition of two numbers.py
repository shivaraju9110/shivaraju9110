#Addition of two numbers
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
add=a+b
print("Sum of two numbers: ",add)


#Division of two numbers
def check(a):
	if(a != "" and a[0] == '-'):
		return 1
	else:
		return 0	
a=input("Enter the number: ")
b=input("Enter the number: ")
acopy = a.replace(".", "")
bcopy = b.replace(".", "")
if (check(a)):
	acopy = acopy.replace("-", "")
if (check(b)):
	bcopy = bcopy.replace("-", "") 

if ((a.isnumeric() or acopy.isnumeric()) and (b.isnumeric() or bcopy.isnumeric()) ):
	print(float(a) / float(b))
else:
	print("Incorrect data")
	
	
#Dot Product
l1=[]
l2=[]
sum=0
n=int(input("No of orders: "))
for i in range(n):
	a=int(input("Enter number: "))
	b=int(input("Enter number: "))
	l1.append(a)
	l2.append(b)
print("Vector1= ",l1)
print("Vector2= ",l2)
for i in range(len(l1)):
	sum+=l1[i]*l2[i]
print("Dot product: ", sum)


#Determinant of Matrix
matrix=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
	for j in range(3):
		inp=int(input("Enter any number: "))
		matrix[i][j]=inp
print()
#determinant
det=0
for j in range(3):
	det=det+matrix[0][j]*((matrix[(1)%3][(j+1)%3]*matrix[(2)%3][(j+2)%3])-(matrix[(2)%3][(j+1)%3]*matrix[(1)%3][(j+2)%3]))
print("Given matrix: ")
for i in range(3):
	for j in range(3):
		print(matrix[i][j],end=" ")
	print()
print("The determinant of the matrix is: %d"%det)	