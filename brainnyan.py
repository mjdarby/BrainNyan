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
    keywords_by_length = list(keyword_map.keys())
    keywords_by_length.sort(key=lambda s:-len(s))
    regex = "|".join([re.escape(x) for x in keywords_by_length])
    regex = "(" + regex + ")"
    split = re.split(regex, text)
    stripped = [x for x in split if x in keyword_map.keys()]
    return stripped

def replace_tokens(keyword_map, stripped):
    return "".join([keyword_map[x] for x in stripped])

def interpret_bf(code):
    numCells = 30000
    data = [0] * numCells
    instr_pointer = 0
    data_pointer = 0
    parentheses = get_parentheses(code)
    while instr_pointer < len(code):
        instr = code[instr_pointer]
        if instr == '>':
            data_pointer += 1
        elif instr == '<':
            data_pointer -= 1
        elif instr == '+':
            data[data_pointer] += 1
        elif instr == '-':
            data[data_pointer] -= 1
        elif instr == '.':
            print(chr(data[data_pointer]), end='')
        elif instr == ',':
            data[data_pointer] = bytes(input(), 'utf-8')[0]
        elif instr == '[':
            if not data[data_pointer]:
                instr_pointer = parentheses[instr_pointer]
        elif instr == ']':
            if data[data_pointer]:
                instr_pointer = parentheses[instr_pointer]
        instr_pointer += 1

def run_code(keyword_map, text):
    stripped = strip_non_keywords(keyword_map, text)
    code = replace_tokens(keyword_map, stripped)
    interpret_bf(code)

if __name__ == "__main__":
    if (len(sys.argv) < 2 or len(sys.argv) > 4 or
        (sys.argv[1] != "-i" and len(sys.argv) == 4)):
        print("Usage: ./brainnyan.py [-i] <keyword mapping file> <code file>")
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
