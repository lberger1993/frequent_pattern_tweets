import collections
import itertools
import json
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


def classify_tweets(tweets):
    mydict = dict()
    mydict["Other"] = []
    with open('data_sources/classes.json', "r") as file:
        data = json.load(file)
        for index, row in tweets.iterrows():
            assignedToSomething = False
            for cl in data:
                TweetisCurrentClass = True
                for attr in cl["includedWords"]:
                    if (attr not in row["tweet"]):
                        TweetisCurrentClass = False
                        break
                if TweetisCurrentClass:
                    if not cl["className"] in mydict:
                        mydict[cl["className"]] = []
                    mydict[cl["className"]].append(row["other"])
                    assignedToSomething = True

            if assignedToSomething == False:
                mydict["Other"].append(row["other"])
    with open("data_sources/classification_result.json", "w") as outfile:

        finalStr="[\n"
        first=True
        for item in mydict:
            if not first:
                finalStr += ",\n"
            finalStr+="{\n\"className\" : \"%s\",\n\"tweetIDs\" : [ %s ]\n}" % (item, ", ".join(str(x) for x in mydict[item]))
            first = False

        finalStr+="\n]"
        outfile.write(finalStr)

    return


if __name__ == '__main__':
    all_tweets = pd.DataFrame.from_csv('data_sources/tweets.csv', index_col=None)
    all_tweets['tweet'] = all_tweets['tweet'].str.lower().str.replace('[^\w\s]', '').str.split()
    all_tweets = remove_stop_words(all_tweets)

    classify_tweets(all_tweets)
