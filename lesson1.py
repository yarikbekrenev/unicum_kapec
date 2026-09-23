def convert_bytes():
    try:
        password = input("Enter user password")
    except ValueError:
        print("Error enter user password")

    password_bytes = password.encode("utf-8")
    size_in_bytes = len(password_bytes)

    user_choise = int(input(f"Choose\n"
                            f"1.KB\n"
                            f"2.MB\n"
                            f"3.GB\n"
                            f"4.TB"))

    units = {1:(1024,"KB"),
             2:(1024**2,"MB"),
             3:(1024**3,"GB"),
             4:(1024**4,"TB")}

    if user_choise in units:
        divider, unit_name = units[user_choise]
        res = size_in_bytes / divider

        print(f"Result:{size_in_bytes} bytes = {round(res,8)} {unit_name}")

    else:
        print("Error")
while True:
    convert_bytes()