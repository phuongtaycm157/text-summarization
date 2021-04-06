import pandas as pd

# Output is a array of Articals Content: [article1, article2, article3...]
# Output apply for all of functions in this module

def read_contents_csv(FileName):
  dataset = pd.read_csv(FileName)
  content = dataset['content'].values
  return content
