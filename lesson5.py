import math

def bits():
    while True:
        input("привет, это прога для того чтобы вычислять количество информации в пароле\n"
              "расчитывается это формулой n = i**2, ну и вот\n"
              "нажмите для начала")
        power_alph = int(input("напиши сколько всего символов в алфавите (мощность алфавита)"))
        length_password = int(input("напиши длину своего пароля"))
        user_digit = int(input(f"напиши сколько пользователей ввели эти пароли длительностью {length_password}"))

        input("нажмите чтобы продолжить")

        #n = 2**i

        bits_symbol = math.ceil(math.log2(power_alph))

        pass_bits = length_password * bits_symbol

        pass_bytes = math.ceil(pass_bits / 8 )

        memory_bytes = password_bytes * user_digit
        memory_kb = memory_bytes / 1024

        print("\nРезультаты расчета:")
        print(f"{bits_symbol} бит")
        print(f"{pass_bytes} байт")
        print(f"{memory_bytes} байт ({memory_kb:.3f} Кбайт)")

bits()
