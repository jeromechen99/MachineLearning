

#get the data#

url = 'https://raw.githubusercontent.com/jeromechen99/MachineLearning/master/data/'


import pandas as pd

filepath_dict = {'amazon': url + 'amazon_cells_labelled.txt'
                  ,'yelp': url + 'yelp_labelled.txt'
                  ,'imdb': url + 'imdb_labelled.txt'}

filepath_dict = {'imdb': url + 'imdb_labelled.txt'}
df_list = []
for source, filepath in filepath_dict.items():
    df = pd.read_csv(filepath, names=['sentence', 'label'], sep='\t')
    df['source'] = source  # Add another column filled with the source name
    df_list.append(df)

df = pd.concat(df_list)
print(df.iloc[0])



