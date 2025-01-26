Users = [
    {
        "Email": "stefan.talkach@gmail.com",
        "Username": "StefanTolkach556634",
        "Password": "Stefan100214"
    },
    {
        "Email": "aboba.sigma@gmail.com",
        "Username": "AbobaSigma556634",
        "Password": "achtung100214"
    },
    {
        "Email": "danya.pro@gmail.com",
        "Username": "lucifer666",
        "Password": "imbest21712"
    }
]

print("Здарова, ваше вели... короче залогинься пж")

UserName = input("Введите юзернейм: ")

for User in Users:

    #print(User ['Email'])

    if UserName == User["Username"]:

        print(f"такой пользователь найден\nemail: {User['Email']}")

        i = 0
        while i < 3:
            


            Password = input("Введите ваш пароль: ") 

            if Password == User["Password"]:

                print("Вы успешно вошли в аккаунт!")

                i = 1000000000000000

            else:

                i += 1

                print(f"Упс, ваш пароль не  верный! Вы израсходовали {i} попытку")

































