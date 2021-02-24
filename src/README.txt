建立索引：
pip install jieba
python make_reverse_index.py
命令行参数：
-g , --gap , gap of skip pointer, type=int，默认为int(L^0.5)

查询：
python main.py
命令行参数：
-s , --skip,  use skip pointer or not, type=bool，默认为True

查询时需要输入合取范式，AND OR NOT 分别用& | !表示