"""
На вход поступают текстовые данные.

прорама считает и выводит:
сколько раз повторяется каждое слово в указанном тексте, среднее
количество слов в предложении, медианное количество слов в предложении,
top-K самых часто повторяющихся буквенных N-грамм
"""

from out_info import oi
from business_logic import bl
from inp_info import ii


def main():
    """метод, через который пользователь взаимодействует с программой."""
    input_command = "hello"
    wordstring = ii.inp_text()
    wordstring = ii.inp_text
    while input_command != "0":
        print(
            "список команд:\n",
            "1. ввести новый текст.\n",
            "2. вывести все слова и их количество в тексте.\n",
            "3. вывести среднее количество слов в тексте.\n",
            "4. вывести медианное количество слов в тексте.\n",
            "5. вывести k самых популярных n-грамм в тексте.\n",
            "0. выйти из программы\n\n",
            "введите цифру команды")
        input_command = input()
        if input_command == "1":
            wordstring = ii.inp_text()
        elif input_command == "2":
            oi.print_wordlist(wordstring)
        elif input_command == "3":
            oi.outprint_average(wordstring)
        elif input_command == "4":
            oi.print_median(bl.average_literalcounter_c(wordstring))
        elif input_command == "5":
            oi.print_n_gramms(bl.wordlist_c(wordstring))
        elif input_command == "0":
            print("До встречи)")
        else:
            print("нет такой команды")


if __name__ == '__main__':
    main()
