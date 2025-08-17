import re

# ^ указывает на начало строки (в данном случае из-за match не обязательно)
# [a-zA-Z0-9._%+-]{4,}@ имя пользователя должно состоять из символов заданного набора (символов >= 4)
# @ разделяет имя пользователя с доменным именем (встречается ровно 1 раз)
# [a-zA-Z0-9_]+ доменное имя из более чем 1 символа (на это указывает +)
# \. символ . выступает между доменным именем и доменным разрешением
# [a-zA-Z]{2,} доменное расширение (.com, .org) допускает только латинские буквы (не менее 2)
# $ указывает на окончание строки, т.е. после доменного расширения не должно быть символов
# ^(?=.*[a-zA-Z]) positive lookahead проверяет наличие хотя бы одной буквы
# вместо email_pattern можно было создать domain_pattern и проверять username and domain_name
# однако в таком случае нельзя использовать text.split('@')[index]
# т.к. это приведёт к ошибке IndexError: Index out of range. As example @google.com or username@
def check_email(text: str) -> str:
    email_pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9]{2,}\.[a-zA-Z]{2,}$'
    username_pattern = r'^(?=.*[a-zA-Z])[a-zA-Z0-9._]+'
    username = re.split(r'@', text)[0]
    email_check_result = re.match(email_pattern, text)
    username_check_result = re.match(username_pattern, username)
    if email_check_result is not None and username_check_result is not None:
        print(f"{text} is CORRECT")
    else:
        print(f"{text} is INCORRECT")

email: list[str] = ["user@gmail.com", "alan@mail.ru", "1231231232realname@yandex.ru",
                    "32143125631236123123@google.com", "plainaddress", "@missingusername.com", "username@.com", "username@domain..com","username@domain.c", "user@domain.com."]

for el in email:
    check_email(el)