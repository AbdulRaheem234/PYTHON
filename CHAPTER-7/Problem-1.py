# n = int(input("Enter a number:"))
# for i in range(1, 11):
#     print(f"{n} X {i} = {n * 1}")
 


for n in range(1, 21):  # Loop from 1 to 20
    print(f"\nTable of {n}")
    print("-" * 15)
    for i in range(1, 11):  # Table from 1 to 10
        print(f"{n} X {i} = {n * i}")
