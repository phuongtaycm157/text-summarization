import re

# Output: 
#   [article_text, formatted_article_text],



def preprocessing(article_text):
  # text list: [article1, article2...]
  article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
  article_text = re.sub(r'\s+', ' ', article_text)

  formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
  formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

  return (article_text, formatted_article_text)