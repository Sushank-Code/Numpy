n= int(input("Enter how many input you wan to take:"))

inputs=[]

for i in range(n):
    user_input= int(input(f"Enter the input{i+1}: "))
    inputs.append(user_input)

print("The inputs are:",inputs)