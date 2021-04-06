from get_data import read_content_txt
from preprocessing import preprocessing
from model import nlp_based
from get_summary import print_txt


# 1. Getting article text from dataset & Preprocessing
FileName = './data/what_is_python.txt'

article = read_content_txt(FileName)

(article_text, formatted_article_text) = preprocessing(article)

# 2. Runing Model
sentence_scores, total_number_of_sentences = nlp_based(article_text, formatted_article_text)

# 5. Getting the Summary
summary, name_file_bin = print_txt(sentence_scores, total_number_of_sentences)

print('Name of exported File:', name_file_bin)