import random
import string

#Функція що кодає можливість додати у генерування пороля цифри букви та символи
def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

#Функція що просить ввести довжину пароля або якщо ти напишеш нуль то напишеться список паролів та програма закінчіться
def main():
    passwords = []
    while True:
        password_length = int(input("Введіть довжину паролю (або 0 для виходу): "))
        if password_length == 0:
            break
#Генерування пароля та написання
        password = generate_password(password_length)
        passwords.append(password)
        print("Ваш новий пароль:", password)
#Написання списка с поролями
    print("Список згенерованих паролів:")
    for password in passwords:
        print(password)


if __name__ == "__main__":
    main()
#Писав вася))))