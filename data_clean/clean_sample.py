"""module for cleaning tweet data"""

import pandas as pd
from data_sources.stop_words import get_stop_words


def remove_stop_words(df):
    """ removes all stop words from row"""
    for index, row in df.iterrows():
        split = row['tweet'].split(" ")
        for s in split:
            if s in get_stop_words():
                split.remove(s)
        fusion = ' '.join(split)
        row['tweet'] = fusion


if __name__ == '__main__':
    all_tweets = pd.DataFrame.from_csv('data_sources/tweets.csv', index_col=None)
    all_tweets['tweet'] = all_tweets['tweet'].str.lower()
    remove_stop_words(all_tweets)
    print(all_tweets['tweet'])




