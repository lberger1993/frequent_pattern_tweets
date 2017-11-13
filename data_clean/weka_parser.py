import json
import re


def parse_weka():
    new_list = []
    with open("system_generated/weka100_005.txt") as f:
        line = f.readlines()
        for word in line:
            words = word.split('   ')
            words[0] = re.sub("\d+", " ", words[0]).replace('[', '')\
                .replace(']', '') \
                .replace('=y', '')\
                .replace('==>', '')\
                .replace('.', '')\
                .strip().replace(':', '')\
                .replace(',', '    ')
            temp = sorted(words[0].split('    '))
            print(temp)
            if len(temp) < 3 and temp not in new_list:
                new_list.append(temp)
    return new_list


def parsed_to_classes(weka_dict):
    weka_classes = []
    with open('data_sources/weka_classes.json', 'w') as f:
        count = 0
        for elems in class_dict:
            dict_item = dict()
            dict_item["className"] = ('_'.join(elems) + str(count)).upper()
            dict_item["includedWords"] = elems
            weka_classes.append(dict_item)
            count = count + 1
        f.write(str(json.dumps(weka_classes)))



if __name__ == '__main__':
    class_dict = parse_weka()
    parsed_to_classes(class_dict)

