# input eger reqemdirse iki qat artirilmalidir. input eger str-dirse error mesaji verilir.


# N = input("Enter a value: ")

# if N.isdigit():
#     N = int(N)
#     if isinstance(N, int):
#         M = N ** 2
#         print(M)
# else:
#     print("N is not an integer")

valid_response = False


while not valid_response:

 try:
    N = int(input("Enter a value: "))
    M = N **2
    print(f'{M} \nMission is complated')
    valid_response = True

 except ValueError as e:
    print(e)

 except Exception as e:
    print(e)

 else:
     print("I'm in the else")
     break
 
 finally:
    print("Code is end")
