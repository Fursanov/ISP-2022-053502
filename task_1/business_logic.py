"""модуль предназначен для расчёта данных."""

from inp_info import ii
import re
from itertools import groupby


class bl:
    """класс содержит методы расчёта данных."""

    def wordlist_c(wordstring):
        """разбивает текст на слова."""
        wordlist = re.findall(r'[0-9]+|[A-z]+', wordstring)
        return wordlist

    def uniqueword_c(wordlist):
        """создаёт массив, в который вносит слова без повторений."""
        uniqueword = set(wordlist)
        return uniqueword

    def average_c(wordstring):
        """считает среднее количество слов в тексте."""
        stringlist = re.split('[.?!]+', wordstring, flags=re.IGNORECASE)
        literalintext = 0
        counter = 0
        for elm in stringlist:
            if elm == '':
                continue
            wordlisttemp = elm.split()
            for elm in wordlisttemp:
                literalintext += 1
            counter += 1
        return (literalintext / counter)

    def average_literalcounter_c(wordstring):
        """создаёт массив с количеством слов в каждом предложении."""
        stringlist = wordstring.split('.')
        literalcounter = []
        for elm in stringlist:
            if elm == '':
                continue
            symbols = 0
            wordlisttemp = elm.split()
            for elm in wordlisttemp:
                symbols += 1
            literalcounter.append(symbols)
        return literalcounter

    def median_c(literalcounter):
        """считает медианное количество слов в тексте."""
        literalcounter.sort()
        median = 0
        if len(literalcounter) % 2 == 0:
            median = (literalcounter[
                int(len(literalcounter) / 2)] + literalcounter[
                    int(len(literalcounter) / 2) - 1]) / 2
        else:
            median = literalcounter[int(len(literalcounter)/2)]
        return median

    def n_gramms_c(wordlist):
        """считает k самых популярных n-грамм в тексте."""
        wordlist.sort()
        n = ii.inp_n(wordlist)
        while n == 0:
            n = ii.inp_n(wordlist)
        ngrams = []
        for word in filter(lambda x: len(x) >= n, wordlist):
            for i in range(len(word)-n+1):
                ngrams.append(word[i:i+n])

        ngrams_freq = list(
            [[len(list(group)), key] for key, group in groupby(
                sorted(ngrams, key=str.lower))])

        ngrams_freq_sorted = sorted(ngrams_freq, reverse=True)
        return ngrams_freq_sorted
