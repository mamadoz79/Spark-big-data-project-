import docx
from pyspark import SparkConf, SparkContext
import re
import sys
if __name__ == '__main__':
    file_name = sys.argv[1]
    doc = docx.Document(f"{file_name}")
    all_words = [re.split('\t|\\u200f| ', i.text) for i in doc.paragraphs]
    dictionary_of_first_char = {}
    for sentences in all_words:
        for single_word in sentences:
            if len(single_word):
                continue
            try:
                dictionary_of_first_char[single_word[0]] += 1
            except:
                dictionary_of_first_char[single_word[0]] = 1
    for element in dictionary_of_first_char:
        print(element, ' contains ' ,dictionary_of_first_char[element], 'characters')
