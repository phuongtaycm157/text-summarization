import pandas as pd
import nltk
import re
import pprint
import heapq

nltk.download('stopwords')

# 1. Getting article text from dataset & Preprocessing
dataset = pd.read_csv('.\\data\\articles1.csv')

article_text = dataset.iloc[1].content

article_text = re.sub(r'\s+', ' ', article_text)

formatted_article_text = re.sub('[^a-zA-Z]', ' ',article_text)
formatted_article_text = re.sub(r'\s+', ' ',formatted_article_text)

# 2. Converting article text to Sentences
sentence_list = nltk.sent_tokenize(article_text)

# 3. Find weighted Frequency of Occurrence
stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}
for word in nltk.word_tokenize(formatted_article_text):
  if word not in stopwords:
    if word not in word_frequencies.keys():
      word_frequencies[word] = 1
    else:
      word_frequencies[word] += 1

maximum_frequncy = max(word_frequencies.values())
for word in word_frequencies.keys():
  word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

# 4. Calculating Sentence Scores
sentence_scores = {}
for sent in sentence_list:
  for word in nltk.word_tokenize(sent.lower()):
    if word in word_frequencies.keys():
      if len(sent.split(' ')) < 30:
        if sent not in sentence_scores:
          sentence_scores[sent] = word_frequencies[word]
        else:
          sentence_scores[sent] += word_frequencies[word]

# 5. Getting the Summary
summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

summary = ' '.join(summary_sentences)
print(summary)