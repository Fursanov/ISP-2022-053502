"""модуль предназначен для вывода данных на экран пользователя."""

from business_logic import bl
from inp_info import ii


class oi():
    """класс содержит методы вывода данных."""

    def print_wordlist(wordstring):
        """вывод все слова и их количество в тексте."""
        print("Список слов в тексте и их колличество:")
        wordlist = bl.wordlist_c(wordstring)
        uniqueword = bl.uniqueword_c(wordlist)
        for elm in uniqueword:
            print(elm+":")
            print(wordlist.count(elm))

    def print_average(wordstring):
        """вывод среднего количества слов в тексте."""
        average = bl.average_c(wordstring)
        print("Среднее количество слов в предложении: ", average)

    def print_median(literalcounter):
        """вывод медианного количества слов в тексте."""
        median = bl.median_c(literalcounter)
        print("Медианное количество слов в предложении: ", median)

    def print_n_gramms(wordlist):
        """выводит k самых популярных n-грамм в тексте."""
        ngrams_freq_sorted = bl.n_gramms_c(wordlist)
        k = ii.inp_k(ngrams_freq_sorted)
        while k == 0:
            k = ii.inp_k(ngrams_freq_sorted)
        for i in range(k):
            print(i+1, "popular ngram: ", ngrams_freq_sorted[i])
