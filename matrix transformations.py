rows = int(input("enter number of rows: "))
cols = int(input("enter number of columns: "))

matrix = []
print("enter elements:")
for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input(f"enter element at position [{i+1}][{j+1}]: "))
        row.append(val)
    matrix.append(row)

print("\noriginal matrix:")
for r in matrix:
    print(r)

transpose = []
for i in range(cols):
    new_row = []
    for j in range(rows):
        new_row.append(matrix[j][i])
    transpose.append(new_row)

print("\ntransposed matrix:")
for r in transpose:
    print(r)

operation=input("\n enter operation to be performed :")
if(operation=="+"):
    num=(int(input("enter number to be added :")))
    changed=[]
    for i in range(rows):
        changed_row =[]
        for j in range(cols):
            changed_row.append((matrix[i][j])+num)
        changed.append(changed_row)
elif(operation=="-"):
    num=(int(input("enter number to be subtracted :")))
    changed=[]
    for i in range(rows):
        changed_row =[]
        for j in range(cols):
            changed_row.append((matrix[i][j])-num)
        changed.append(changed_row)
elif(operation=="/"):
    num=int(input("enter number to be divided :"))
    changed=[]
    for i in range(rows):
        changed_row =[]
        for j in range(cols):
            changed_row.append((matrix[i][j])/num)
        changed.append(changed_row)
elif(operation=="*"):
    num=int(input("enter number to be multiplied :"))
    changed=[]
    for i in range(rows):
        changed_row =[]
        for j in range(cols):
            changed_row.append((matrix[i][j])*num)
        changed.append(changed_row)
else:
    print("pls enter valid operation (+,-,/,*)")


print("\n changed matrix is :\n")
for r in changed:
    print(r)

