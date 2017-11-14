import json
import re


def parse_weka():
    new_list = []
    with open("system_generated/weka.txt") as f:
        line = f.readlines()
        for word in line:
            word = word.replace(', ', '] [')
            words = word.split(' ')
            words = [x for x in words if '[' in x and ']' in x]
            words = [x.replace(':','').replace('=y','').replace('[','').replace(']','').strip() for x in words]

            words=sorted(words)
            if len(words) ==2 and words not in new_list:
                new_list.append(words)
    return new_list


def parsed_to_classes(weka_dict):
    weka_classes = []
    with open('data_sources/weka_classes.json', 'w') as f:
        for elems in class_dict:
            dict_item = dict()
            print(elems)
            dict_item["className"] = ('_'.join(elems)).upper()
            dict_item["includedWords"] = elems
            weka_classes.append(dict_item)
        f.write(str(json.dumps(weka_classes)))

if __name__ == '__main__':
    class_dict = parse_weka()
    print(class_dict)
    parsed_to_classes(class_dict)

