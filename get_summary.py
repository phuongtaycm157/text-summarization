import heapq

def heapq_retrieve_text(sentence_scores, total_number_of_sentences):
  # get number of summary sentents = 25% original text 
  num_of_sent = total_number_of_sentences//4
  summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
  summary = ' '.join(summary_sentences)
  return summary