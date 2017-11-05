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
    return  totals

def select_top_words():
    with open('most_common_words.json', 'r') as wordsfile:
        data = json.load(wordsfile)
        data = {word: count for word,count in data.items() if data[word]>5}
        data = data[:50]
        print(data)
        return data

def print_arff(tweets,attributes):
    with open("tweets.arff","w") as file:
        file.write("%\n")
        file.write("% Tweet Attributes\n")
        file.write("%\n")
        file.write("@relation 'tweeterfeed'\n")
        file.write("@attribute tweetID numeric\n")
        for item in attributes:
            file.write("@attribute '%s' {'n', 'y'}\n" % item[0])
        file.write("\n@data\n")
        for index, row in tweets.iterrows():
            line = "%d" %row['other']
            for item in attributes:
                if item[0] in row['tweet']:
                    line += ", 'y'"
                else:
                    line += ", 'n'"
            line += "\n"
            file.write(line)
            #print(row['other'],row['tweet'])



if __name__ == '__main__':
    all_tweets = pd.DataFrame.from_csv('data_sources/tweets.csv', index_col=None)
    all_tweets['tweet'] = all_tweets['tweet'].str.lower().str.replace('[^\w\s]', '').str.split()
    all_tweets = remove_stop_words(all_tweets)
    topWords = count_words(all_tweets).most_common(50)
    print_arff(all_tweets, topWords)









