"""
На вход поступают текстовые данные.

прорама считает и выводит:
сколько раз повторяется каждое слово в указанном тексте, среднее
количество слов в предложении, медианное количество слов в предложении,
top-K самых часто повторяющихся буквенных N-грамм
"""

import re
from itertools import groupby


def inp_k():
    """проверяет k на валидность."""
    number = input()
    while number.isdigit() is False:
        print("ошибка ввода: введена буква или знак")
        print("Введите k, количество в топе n-грамм")
        return 0
    while int(number) > len(ngrams_freq_sorted) or int(number) <= 0:
        print("ошибка ввода: текст не имеет так много n-грамм или введён 0")
        print("Введите k, количество в топе n-грамм")
        return 0
    return int(number)


def inp_n():
    """проверяет n на валидность."""
    number = input()
    while number.isdigit() is False:
        print("ошибка ввода: введена буква или знак")
        print("Введите n, количество букв n-грамм")
        return 0
    max_string = wordlist[len(wordlist)-1]
    while int(number) > len(max_string) or int(number) <= 0:
        print(
            "ошибка ввода: текст не имеет таких больших n-грамм или введён 0")
        print("Введите n, количество букв n-грамм")
        return 0
    return int(number)


print("Введите текст")
wordstring = input()
while len(wordstring) == 0:
    print("Ошибка ввода: текст не может быть пустым")
    print("Введите текст")
    wordstring = input()
print("Список слов в тексте и их колличество:")
wordlist = re.findall(r'[0-9]+|[A-z]+', wordstring)
uniqueword = set(wordlist)

for elm in uniqueword:
    print(elm+":")
    print(wordlist.count(elm))

stringlist = wordstring.split('.')
literalintext = 0
counter = 0
literalcounter = []
for elm in stringlist:
    if elm == '':
        continue
    symbols = 0
    wordlisttemp = elm.split()
    for elm in wordlisttemp:
        literalintext += 1
        symbols += 1
    literalcounter.append(symbols)
    counter += 1
print("Среднее количество слов в предложении: ", literalintext/counter)
literalcounter.sort()
if len(literalcounter) % 2 == 0:
    print("Медианное количество слов в предложении: ", (literalcounter[
        int(len(literalcounter)/2)]+literalcounter[
            int(len(literalcounter)/2)-1])/2)
else:
    print("Медианное количество слов в предложении: ", literalcounter[
        int(len(literalcounter)/2)])

wordlist.sort()

print("Введите n, количество букв n-грамм")
n = 0
while n == 0:
    n = inp_n()

ngrams = []
for word in filter(lambda x: len(x) >= n, wordlist):
    for i in range(len(word)-n+1):
        ngrams.append(word[i:i+n])

ngrams_freq = list([[len(list(group)), key] for key, group in groupby(sorted(
    ngrams, key=str.lower))])

ngrams_freq_sorted = sorted(ngrams_freq, reverse=True)

print("Введите k, количество в топе n-грамм")
k = 0
while k == 0:
    k = inp_k()

for i in range(k):
    print(i+1, "popular ngram: ", ngrams_freq_sorted[i])
