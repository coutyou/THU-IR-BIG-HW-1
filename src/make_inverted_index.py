from glob import glob
import jieba
import re
import pickle
from time import time
import argparse
from math import sqrt
from collections import defaultdict

from utils import *

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--gap", type=int, default=0, help="gap of skip pointer")
    args = parser.parse_args()
    
    inverted_index = defaultdict(Vector)
    html_list = glob('.\cacm\*.html')
    
    start = time()
    for idx,html in enumerate(html_list):
        with open(html,'r',encoding="utf-8") as f:
            html = f.readlines()

        tmp = []
        for line in html:
            if '<' in line or '\t' in line or line == '\n':
                pass
            else:
                tmp.append(line[:-1])

        tittle = ""
        for line in tmp:
            if "CACM" in line:
                break
            tittle += " " + line

        tittle = re.sub(r"[%s]+" %punc, " ", tittle)
        text_list = jieba.cut(tittle, cut_all=True)
        text_list = filter(lambda s:s and s.strip(), list(text_list))
        text_list = list(map(lambda s:s.lower(), list(text_list)))
        
        text_list = list(set(text_list))
        
        for text in text_list:
            text = text.lower()
            if inverted_index.get(text):
                inverted_index[text].insert(idx+1)
            else:
                vec = Vector([idx+1])
                inverted_index[text] = vec

    stop = time()
    print(f"--------------Length Of Inverted Index:  {len(inverted_index.items())}----------------------------------")
    print(f"--------------Time Used To Make Inverted Index:  {stop-start}s-------------")

    for _,vec in inverted_index.items():
        if args.gap == 0:
            gap = int(sqrt(len(vec)))
        else:
            gap = args.gap
        vec.make_skip(gap=gap)

    save_obj(inverted_index, "inverted_index")