"""module for cleaning tweet data"""

import pandas as pd
from data_sources.stop_words import get_stop_words


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



if __name__ == '__main__':
    all_tweets = pd.DataFrame.from_csv('data_sources/tweets.csv', index_col=None)
    # removes all punctuation & tweets
    all_tweets['tweet'] = all_tweets['tweet'].str.lower().str.replace('[^\w\s]', '').str.split()
    all_tweets = remove_stop_words(all_tweets)
    # all_tweets = remove_all_punc(all_tweets)
    #print(all_tweets)
    # all_tweets = remove_user_names(all_tweets)
    # print(all_tweets['tweet'][11])







