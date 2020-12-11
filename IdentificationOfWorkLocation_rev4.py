#!/usr/bin/env python
# coding: utf-8

# In[1]:


####################################################
#File name:IdentificationOfWorkLocation_rev4
#Creation date:2020/9/30
#Updating date:2020/10/20
#Shizuka Hamajima
# rev4はテストデータを読み込んでファイルに結果出力させる。
# 精度検証に用いるためのプログラム
####################################################
import pandas as pd
from pandas import Series, DataFrame

#正規表現操作のインポート
import re


# In[2]:


cd ./ThresholdData/


# In[3]:


#最低賃金表の読み込み
minimum_wage_list = pd.read_csv('minimum_wage.csv',encoding="SHIFT-JIS")


# In[4]:


#最低賃金表読み込み結果
minimum_wage_list


# In[5]:


cd ..


# In[6]:


cd ./TestData/


# In[7]:


#チェック対象テキストデータの読み込み
check_data = pd.read_csv('WorkLocationTest_Input.csv',encoding="SHIFT-JIS")
#check_data


# In[8]:


#勤務地初期値設定
check_data['WorkLocation'] = "不明"
#最低賃金の閾値初期化
check_data['MinimumWage'] = minimum_wage_list.Minimum_wage.max()
check_data.head()


# In[9]:


#勤務地クラス数　改訂時に可変にするため
N = minimum_wage_list.Class.max()
#print(N)  #確認
###勤務地判定
#勤務地判定用正規表現初期化
pattern = [""] * N
#print(pattern)  #確認
for i in range(N):
    pattern[i] = minimum_wage_list.loc[i,"Regular_Expressions"]
#print(pattern)  #確認
#最賃昇順に勤務地判定
for j in range(len(check_data)):
    for i in range(N):
        work_location_text = re.findall(pattern[i], check_data.loc[j,"text"])
        if len(work_location_text) != 0:
            check_data.loc[j,"WorkLocation"] = minimum_wage_list.loc[i,"Class"]
            check_data.loc[j,"MinimumWage"] = minimum_wage_list.loc[i,"Minimum_wage"]


# In[10]:


#勤務地判定結果ファイル出力
check_data.to_csv("WorkLocationTest_Output.csv",encoding="SHIFT-JIS")
check_data.head()


# In[ ]:




