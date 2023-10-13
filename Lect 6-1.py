#미니프로젝트 (1)
"""for i in range(1, 6) :
  print("*"* i)
"""
# #미니 프로젝트 (2)
"""for i in range(5, 0, -1) :
    print("*"* i)
"""

"""
# 미니 프로젝트 (3)
for i in range(1, 6) :
    spaces = " " * (6-i)
    stars = "*" * (2*i-1)
    print(spaces + stars)

#미니 프로젝트
for i in range(1,10):
    if i <= 5:
        for j in range(5-i):
            print(" ",end="")
        for j in range(2*i-1):
            print("*",end="")
        print()
    else:
        for j in range(i-5):
            print(" ",end="")
        for j in range((10-i)*2-1):
            print("*",end="")
        print()
 """
#5x5 출력 
"""num = 0 
line = []
for i in range (5) :
    for j in range (5):
        num += 1 
        line.append(num)
    print(line)
    line = []"""

#세로로 출력 
"""num = 0
line = []
for i in range (1, 6) :
    for j in range (1, 6):
        num = ((j-1)* 5) + i
        line.append(num)
    print(line)
    line = []
"""
# 역순 출력
"""num = 26
line = []
for i in range (5) :
    for j in range (5):
        num += - 1 
        line.append(num)
    print(line)
    line = []


"""
"""import random

sel = ['가위', '바위', '보']
result = {0: '승리했습니다.', 1: '패배했습니다.', 2: '비겼습니다.'}

def checkWin(user, com):

    if not user in sel:
       print('잘못입력하였습니다. 다시 입력하세요')
       return False

    print(f'사용자 ( {user} vs {com} ) 컴퓨터')
    if user == com:
        state = 2
    elif user == '가위' and com == '바위':
        state = 1
    elif user == '바위' and com == '보':
        state = 1
    elif user == '보' and com == '가위':
        state = 1
    else:
        state = 0
    print(result[state])
    return True


print('\n-------------------------------------------')
while True:
    user = input("가위, 바위, 보 : ")
    com = sel[random.randint(0, 2)]
    if checkWin(user, com):
        break
print('-------------------------------------------\n')
"""

# import random

# def get_computer_choice():
#     choices = ["1", "2", "3"]
#     return random.choice(choices)

# def determine_winner(user_choice):
#     pcnum = get_computer_choice()
#     print(user_choice, pcnum)
    
#     if user_choice == pcnum:
#         print("무승부")
#         return
#     elif (
#         (user_choice == "1" and pcnum == "3") or
#         (user_choice == "2" and pcnum == "1") or
#         (user_choice == "3" and pcnum == "2")
#     ):
#         print("승")
#         return
#     else:
#         print("패")
#         return


# print("1 : 가위")
# print("2 : 바위")
# print("3 : 보")
# print("1~3 숫자를 입력하세요")
# chnum = input()

# determine_winner(chnum)









#파일 생성
# f= open("new.txt", "w")

# f = open("tempt.txt", 'wt')
# f.close()

# file = open("temp.txt", "w")

# file.write("hello")
# file.write("world")

# file.close()

#1~ 100

# file = open("C:\\Users\\Catholic\\python\\eunsu\\temp.txt", "w")
# for i in range(100) :
#     file.write(f"{i}\n")
    
# file.close()



# file = open("C:\\Users\\Catholic\\python\\eunsu\\temp.txt", "r")
# res = file.read()
# print(res)
# file.close()

#readline
#f = open("temp.txt", "r")
# f = open("temp.txt","r")

# for i in range(110):
# res = f.readline()
# print(res)
# f.close()

#readlines 읽기
# f = open("temp.txt", "r")
# res = f.readlines()
# print(res)

# f.close()



#readlines 읽기
# f = open("temp.txt", "r")
# line = f.readlines()

# for l in line :
#     print(l)

# f.close()


#file object
f = open("temp.txt", "r")
for line in f :
    print(line)
    
f.close()