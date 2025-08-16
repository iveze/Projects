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

s2 = "Привет! Как дела? А у меня нормально? Ты учился сегодня? Ура, я тоже."

# Находит все слова, начинающиеся с согласной буквы
def extract_consonant_words(text: str) -> str | None:
    pattern = r"\b[бвгдзжзклмнпрстфхцчшщБВГДЖЗКЛМНПРСТФХЦЧШЩ]\w*"
    consonant_words  = re.findall(pattern, s2)
    return consonant_words


print(extract_consonant_words(s2))