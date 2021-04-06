import nltk
nltk.download('stopwords')


def nlp_based(article_text, formatted_article_text):
  # Converting article text to Sentences
  sentence_list = nltk.sent_tokenize(article_text)
  total_number_of_sentences = len(sentence_list)

  # Find weighted Frequency of Occurrence
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

  # Calculating Sentence Scores
  sentence_scores = {}
  for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
      if word in word_frequencies.keys():
        if len(sent.split(' ')) < 30:
          if sent not in sentence_scores:
            sentence_scores[sent] = word_frequencies[word]
          else:
            sentence_scores[sent] += word_frequencies[word]
  
  return (sentence_scores, total_number_of_sentences)