#coding=utf-8
import pandas as pd

#### 创建数据集
ratings_filename = "ml-100k/u.data"

all_ratings = pd.read_csv(ratings_filename,delimiter="\t",header=None,
                          names=["UserID","MovieID","Rating","Datetime"])
all_ratings["Datetime"] = pd.to_datetime(all_ratings['Datetime'],unit='s')
all_ratings["Favorable"] = all_ratings["Rating"] > 3


#### 取前200名用户的打分数据
ratings = all_ratings[all_ratings['UserID'].isin(range(200))]



