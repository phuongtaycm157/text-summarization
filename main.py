import heapq

from get_data import read_contents_csv
from preprocessing import preprocessing
from model import nlp_based
from get_summary import heapq_retrieve_text


# 1. Getting article text from dataset & Preprocessing
FileName = '.\\data\\articles1.csv'

article_list = read_contents_csv(FileName)

(article_text, formatted_article_text) = preprocessing(article_list[0])

# 2. Runing Model
sentence_scores, total_number_of_sentences = nlp_based(article_text, formatted_article_text)

# 5. Getting the Summary
summary = heapq_retrieve_text(sentence_scores, total_number_of_sentences)

print(summary)