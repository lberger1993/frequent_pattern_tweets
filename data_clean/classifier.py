import json
import sys
import pandas as pd


def classify_tweets(tweets, file_to_process):
    mydict = dict()
    mydict["Other"] = []
    with open(file_to_process, "r") as file:
        data = json.load(file)
        for index, row in tweets.iterrows():
            assignedToSomething = False
            for cl in data:
                print('here', cl)
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
                    break
            if assignedToSomething == False:
                mydict["Other"].append(row["other"])
    with open("system_generated/classification_result.json", "w") as outfile:
        finalStr = "[\n"
        first = True
        print(mydict)
        for item in mydict:
            if not first:
                finalStr += ",\n"
            finalStr += "{\n\"className\" : \"%s\",\n\"tweetIDs\" : [ %s ]\n}" % (
            item, ", ".join(str(x) for x in mydict[item]))
            first = False

        finalStr += "\n]"
        outfile.write(finalStr)

    return


def write_classes():
    all_tweets = pd.DataFrame.from_csv('data_sources/tweets.csv', index_col=None)
    all_tweets['classifications'] = all_tweets['other']
    data = json.load(open('system_generated/classification_result.json'))
    for key in data:
        class_label = key.get('className')
        if key.get('tweetIDs'):
            for val in key.get('tweetIDs'):
                all_tweets['classifications'].replace(val, class_label, inplace=True)
                all_tweets['classifications']
    all_tweets.to_csv('data_sources/classified_tweets_processed100.csv')


if __name__ == '__main__':
    all_tweets = pd.DataFrame.from_csv('data_sources/clean_tweets.csv', index_col=None)
    classify_tweets(all_tweets,  sys.argv[1])
    write_classes()
