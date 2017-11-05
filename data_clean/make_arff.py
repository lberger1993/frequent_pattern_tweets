import pandas as pd


def create_matrix(data_frame, hot_words):
    word_matrix = []
    for index, row in data_frame.iterrows():
        new_row = []
        for elem in row['tweet']:
            if elem in top_words:
                new_row.append('y')
            else:
                new_row.append('n')
        word_matrix.append(new_row)
    return word_matrix


if __name__ == '__main__':
    all_tweets = pd.DataFrame.from_csv('data_sources/tweets.csv', index_col=None)
    all_tweets['tweet'] = all_tweets['tweet'].str.lower().str.replace('[^\w\s]', '').str.split()
    top_words = \
        {"time": 45, "night": 37, "new": 36, "good": 34, "warner": 32, "love": 31, "nike": 26, "museum": 26, "im": 25,
     "see": 22, "gm": 22, "jquery": 21, "kindle2": 20, "out": 20, "lebron": 20, "go": 20, "google": 20, "great": 20,
     "safeway": 20, "hate": 19, "twitter": 19, "up": 19, "rt": 19, "more": 19, "today": 18, "now": 17, "api": 16,
     "amp": 15, "going": 15, "back": 14, "dentist": 14
         }
    with open('data_sources/sample.txt', 'w') as outfile:
        outfile.write("@relation  'twitter \n")
        for var in top_words:
            line = "@ATTRIBUTE " + "'" + var + "'" + " {'n', 'y'}" + '\n'
            outfile.write(line)
        outfile.write(str(create_matrix(all_tweets, top_words)))
    outfile.close()

