import requests
from bs4 import BeautifulSoup as Soup
import pandas as pd
from pandas import DataFrame
import seaborn as sns
import matplotlib.pyplot as plt

#Functions Start
def parse_row(row):
    return [str(x.string) for x in row.find_all('td')]

def get_secret_message(url):
  response = requests.get(url)
  html_soup = Soup(response.text, 'html.parser')

  tables = html_soup.find_all('table')
  len(tables)

  msg_table = tables[0]
  rows = msg_table.find_all('tr')
  list_of_parsed_rows = [parse_row(row) for row in rows[1:]]
  df = DataFrame(list_of_parsed_rows)
  df.columns = [str(x.string) for x in rows[0].find_all('td')]
  int_cols = ['x-coordinate', 'y-coordinate']
  df[int_cols] = df[int_cols].apply(pd.to_numeric)
  g = sns.relplot(data=df, x='x-coordinate', y='y-coordinate', kind='scatter', style='Character', height=6, aspect=10)
  g.set(xticks=[], yticks=[], xlabel=None, ylabel=None)
  g.despine(left=True, bottom=True)
  plt.show()
  return g
#Functions End

get_secret_message('https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub')
