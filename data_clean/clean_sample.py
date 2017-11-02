"""module for cleaning tweet data"""

import pandas as pd
from data_sources.stop_words import get_stop_words


def remove_stop_words(df):
    df['tweet'] = df['tweet'].apply(lambda x: [item for item in x if item not in get_stop_words()])
    return df


if __name__ == '__main__':
    all_tweets = pd.DataFrame.from_csv('data_sources/tweets.csv', index_col=None)
    all_tweets['tweet'] = all_tweets['tweet'].str.lower().str.split()
    all_tweets = remove_stop_words(all_tweets)







