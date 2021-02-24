import argparse
from time import time

from utils import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--skip", type=bool, default=True, help="use skip pointer or not")
    args = parser.parse_args()
    
    inverted_index = load_obj("inverted_index")
    
    query = input("请输入查询内容的合取范式，如：(data | math | science) & (!information) & (computer | !system)\n").lower()
    # query = "(data | math | science) & (!information) & (computer | !system)".lower()
    
    start = time()
    res_vec = parse_query(inverted_index, query, use_skip=args.skip)
    stop = time()

    res_show(res_vec)
    print(f"--------------Length Of Result Set:  {len(res_vec)}--------------------------------------")
    print(f"--------------Time Used To Process Query:  {stop-start}s-------------")
