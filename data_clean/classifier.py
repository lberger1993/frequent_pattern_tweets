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
        for item in mydict:
            if not first:
                finalStr += ",\n"
            finalStr += "{\n\"className\" : \"%s\",\n\"tweetIDs\" : [ %s ]\n}" % (
            item, ", ".join(str(x) for x in mydict[item]))
            first = False

        finalStr += "\n]"
        outfile.write(finalStr)

    return


if __name__ == '__main__':
    all_tweets = pd.DataFrame.from_csv('data_sources/clean_tweets.csv', index_col=None)
    classify_tweets(all_tweets,  sys.argv[1])
