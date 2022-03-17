"""модуль предназначен для ввода данных пользователем в консоль."""


class ii():
    """класс содержит методы ввода данных."""

    def inp_k(ngrams_freq_sorted):
        """ввод k и проверка на алидность."""
        print("Введите k, количество в топе n-грамм")
        number = input()
        while number.isdigit() is False:
            print("ошибка ввода: введена буква или знак")
            return 0
        while int(number) > len(ngrams_freq_sorted) or int(number) <= 0:
            print(
                "ошибка ввода: текст не имеет так много n-грамм или введён 0")
            return 0
        return int(number)

    def inp_n(wordlist):
        """ввод n и проверка на алидность."""
        print("Введите n, количество букв n-грамм")
        number = input()
        while number.isdigit() is False:
            print("ошибка ввода: введена буква или знак")
            return 0
        max_string = wordlist[len(wordlist)-1]
        while int(number) > len(max_string) or int(number) <= 0:
            print(
                "ошибка ввода: текст не",
                "имеет таких больших n-грамм или введён 0")
            return 0
        return int(number)

    def inp_text():
        """ввод обрабатываемого текста."""
        print("Введите текст")
        wordstring = input()
        while len(wordstring) == 0:
            print("Ошибка ввода: текст не может быть пустым")
            print("Введите текст")
            wordstring = input()
        return wordstring
