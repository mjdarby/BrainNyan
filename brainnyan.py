#!/usr/bin/python

import json, re, sys

def get_parentheses(text):
    stack = []
    parentheses = {}
    for idx, instr in enumerate(text):
        if instr == '[':
            stack.append(idx)
        elif instr == ']':
            old_idx = stack.pop()
            parentheses[old_idx] = idx
            parentheses[idx] = old_idx
    return parentheses

def read_keywords(json_string):
    keyword_map = json.loads(json_string)
    return keyword_map

def strip_non_keywords(keyword_map, text):
    regex = "|".join(keyword_map.keys())
    regex = "(" + regex + ")"
    split = re.split(regex, text)
    stripped = [x for x in split if x in keyword_map.keys()]
    return stripped

def replace_tokens(keyword_map, stripped):
    return "".join([keyword_map[x] for x in stripped])

def interpret_bf(code):
    parentheses = get_parentheses(code)

def run_code(keyword_map, text):
    stripped = strip_non_keywords(keyword_map, text)
    code = replace_tokens(keyword_map, stripped)
    interpret_bf(code)

if __name__ == "__main__":
    print(sys.argv)
    if (len(sys.argv) < 2 or len(sys.argv) > 4 or
        (sys.argv[1] != "-i" and len(sys.argv) == 4)):
        print("Usage: ./brainnyan.py [-i] input.b > output.spl")
        sys.exit(2)

    case_sensitive = True
    keyword_file = sys.argv[1]
    input_file = sys.argv[2]
    if sys.argv[1] == '-i':
        case_sensitive = False
        keyword_file = sys.argv[2]
        input_file = sys.argv[3]

    keyword_file = open(keyword_file)
    json_string = keyword_file.read()
    keyword_file.close()
    text = open(input_file).read()
    if not case_sensitive:
        json_string = json_string.lower()
        text = text.lower()
    keyword_map = read_keywords(json_string)
    text = run_code(keyword_map, text)
