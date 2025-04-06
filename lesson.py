# def add(x, y):
#     if x > 0 and y > 0:
#         print("I")
#     elif x < 0 and y > 0:
#         print("II")
#     elif x > 0 and y < 0:
#         print("III")
#     elif x < 0 and y < 0:
#         print("IV")
# add(3, 3)
# add(4, 4)
# add(-3, -3)
# add(-2, -2)
def ask_password():
    a = "Venom228"
    i = 3
    while i > 0:
        t = input("Пароль: ")
        
        if t == a:
            print("Доступ разрешён")
            return
        else:
            
            t -= 1
            if t > 0:
                print("Неверный пароль")
        print("Доступ отказан")
ask_password()