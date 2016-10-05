import collections
import re

def load_text_file(filepath):
    try:
        with open(filepath, mode='r', encoding='utf-8') as txt_file:
            text = txt_file.read()
        return text
    except FileNotFoundError:
        return 'No such file in directory'

def remove_punct_marks(text):
    clear_text = re.sub(u'[^А-Яа-яA-Za-z\s]*', u'', text)
    return clear_text


def get_words_frequency(text):
    words_stat = collections.Counter()
    words_list = text.split()
    for word in words_list:
        words_stat[word] += 1
    return words_stat


def top_words_print(words_list_counter):
    TOP_TEN = 10
    for num, word_freq in enumerate(words_list_counter.most_common(TOP_TEN)):
        print('{0}. {1} - {2} times in text'.format(num+1, *word_freq))


if __name__ == '__main__':
    txt_file = input('path to file: ')
    text = load_text_file(txt_file)
    clear_text = remove_punct_marks(text)
    popular_words_dict = get_words_frequency(clear_text)
    top_words_print(popular_words_dict)
