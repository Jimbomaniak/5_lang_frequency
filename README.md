### 5_lang_frequency

#### Prerequisites:
Script needs a path to text. like *c:/users/mytext.txt

##### This script can help you to find top 10 the most frequent words in text



#### How to use:

Enter path to text file, like *c:/users/mytext.txt*

===========

###### Functions in script:

* load_text_file(filepath) - take *filepath* to text directory , return *text* in python
* remove_punct_marks(text) - take *text* , return *clear_text* without punctuation marks
* get_words_frequency(text) - take *text* , retrun *word_stat* - dictionary of most frequent words
* top_words_print(words_dict_counter, top_number) - take dictionary of most frequent words and *top_number*-number of top words you want to see, print top most frequent words

