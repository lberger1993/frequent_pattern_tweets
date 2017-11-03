"""module for cleaning tweet data"""

import collections
import itertools
import json
import pandas as pd
from data_sources.stop_words import get_stop_words

count_of_word_in_row = []


def remove_stop_words(df):
    df['tweet'] = df['tweet'].apply(lambda x: [item for item in x if item not in get_stop_words()])
    return df


def remove_user_names(df):
    for index, row in df.iterrows():
        for elem in row['tweet']:
            if 'http' in elem:
                row['tweet'].remove(elem)
            if '@' in elem:
                row['tweet'].remove(elem)
    return df


def count_words(df):
    totals = collections.Counter(i for i in list(itertools.chain.from_iterable(df['tweet'])))
    with open('most_common_words.json', 'w') as outfile:
        json.dump(dict(totals.most_common()), outfile)


if __name__ == '__main__':
    all_tweets = pd.DataFrame.from_csv('data_sources/tweets.csv', index_col=None)
    all_tweets['tweet'] = all_tweets['tweet'].str.lower().str.replace('[^\w\s]', '').str.split()
    all_tweets = remove_stop_words(all_tweets)
    count_words(all_tweets)








