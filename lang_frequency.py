def load_data(filepath):
    try:
        with open(filepath, mode='r', encoding='utf-8') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        return 'No such file in directory'

def remove_punct_marks(text):
    clear_text = ''
    for symbol in text:
        if symbol not in (',.;:!?+-=_)(][}{/\%^@#$&*|`~><–"0123456789'):
            clear_text += symbol.lower()
    return clear_text


def get_words_frequency(text):
    words_stat = {}
    counter = 1
    words_list = text.split()
    for word in words_list:
        if word not in words_stat:
            words_stat[word] = counter
        else:
            words_stat[word] += 1
    return words_stat

def get_top_ten(popular_words_dict):
    top_ten_words=[]
    for popword in range(10):
        word = max(popular_words_dict, key=popular_words_dict.get)
        top_ten_words.append([word, popular_words_dict[word]])
        popular_words_dict.pop(word)
    return top_ten_words


if __name__ == '__main__':
    file = 'C:/Users/Jimbo/Desktop/1.txt' #input('path to file: ')
    text = load_data(file)
    clear_text = remove_punct_marks(text)
    popular_words_dict = get_words_frequency(clear_text)
    top_ten_words = get_top_ten(popular_words_dict)
    for num, word in enumerate(top_ten_words):
        print('{0}. {1} - {2} times in text'.format(num+1,*word))
