import heapq
from datetime import datetime

def heapq_retrieve_text(sentence_scores, total_number_of_sentences):
  # get number of summary sentents = 25% original text 
  num_of_sent = total_number_of_sentences//4
  summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
  summary = ' '.join(summary_sentences)
  return summary

def print_txt(sentence_scores, total_number_of_sentences):
  # get summary text
  num_of_sent = total_number_of_sentences//4
  summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)
  summary = ' '.join(summary_sentences)

  # Create name file
  path = './bin/'
  name = 'TextSummary'
  time_now = datetime.now()
  time_str = time_now.strftime('%Y-%d-%b_%H:%M:%S.%f')
  name_file_bin = path + name + '_' + time_str + '.txt'

  # Create and write text to file
  f = open(name_file_bin, 'w')
  f.write(summary)
  f.close()

  return (summary, name_file_bin)