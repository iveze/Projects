import re

s = "87+684654   --- kjgdsklfb98798790909^7 HKLJHLKJHfffggg"


# r <- указаывает на то, что используем сырую строку(отключено экранирование)

# . <- зааменяет 1 любой символ кроме символа \n
# print(result) -> <re.Match object; span=(16, 19), match='kjg'>
result = re.search(r"k.g", s)

# print(result) -> None
result = re.search(r"k..g", s)

# \d находит 1 цифру
# print(result) -> <re.Match object; span=(0, 1), match='8'>
result = re.search(r"\d", s) 

# \D <- any character other than a numebr
# print(result)-> <re.Match object; span=(2, 3), match='+'>
result = re.search(r"\D", s)

# \s -> любой пробельный символ: табуляция, конец строки, пробел и т.д.
result = re.search(r"\s\s", s)

# \S -> любой непробельный символ
result = re.search(r"\S", s)

# \w -> любая буква, цифра, нижнее подчёркивание
result = re.search(r"\w", s)

# \W -> любая НЕ буква, цифра, нижнее подчёркивание
result = re.search(r"\W", s)

# \b -> указывает начало или конец какого-либо слова ???
result = re.search(r"HKL\b", s)

s1 = "FOO BAR RHKLYY"
# \B -> по сути так можно проверить, является ли набор частью слова ???
# result = re.search(r"\BHKL", s1)

# * <- указыает на 0 или > символ вхождения после \d (так можно проверить начинается ли строка с цифры \d*)
result = re.search(r"\d*", s)

# + <- указыает на 1 или > символ вхождения после \d
result = re.search(r"\d+", s)

# поиск по набору внутри [], [0-7] <- диапазон цифр
result = re.search(r"[4-6]", s)

# поиск с исключением диапазона(набора) [^0-7]
result = re.search(r"[^4-6]", s)

# вывод либо | либо
result =re.search(r"8|\+", s)

# МОЖНО(НУЖНО) использовать квантификаторы \d\d\d == \d{3}
#\d{1,3} <- от 1 до 3 повторений цифры
#\d{4,} <- не менее 4
#\d{,4} <- не более 4

# result = re.search(r"\d{,2}", s)

# print(result)

s2 = "Привет! Как дела? А у меня нормально! Тебе нравится питон? Мне тоже."

# Находит все слова, начинающиеся с согласной буквы
def extract_consonant_words(text: str) -> str | None:
    pattern = r"\b[бвгдзжзклмнпрстфхцчшщБВГДЖЗКЛМНПРСТФХЦЧШЩ]\w*"
    consonant_words  = re.findall(pattern, s2)
    return consonant_words

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