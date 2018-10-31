import os
import json

f2 = open("/home/tong.guo/bilm-chinese/data/cn_train_data.txt",mode="w",encoding="utf-8")
dir_path = "/nas04/shidan/current/baidubaike/Four/datas0"
dir = os.listdir(dir_path)
for file in dir:
    dir_ = os.listdir(dir_path+"/"+file)
    for file2 in dir_:
        dir__ = os.listdir(dir_path+"/"+file+"/"+file2)
        for file3 in dir__:
            print(dir_path+"/"+file+"/"+file2+"/"+file3)
            f = open(dir_path+"/"+file+"/"+file2+"/"+file3,mode="r",encoding="utf-8")
            lines = f.readlines()
            one_string = ""
            for line in lines:
                one_string+=line.replace("\n","")
            jdata = json.loads(one_string)
            summary = jdata["summary"].replace("\n", "")
            if summary!="":
                f2.write(summary)
                f2.write("\n")
            if len(jdata["otherInfo"])>0:
                for text in jdata["otherInfo"]:
                    if len(text)>0:
                        t = text["text"].replace("\n","")
                        sentence_list = t.split("。")
                        for s in sentence_list:
                            if s!="" and len(s)>=10:
                                f2.write(s.replace("\n",""))
                                f2.write("\n")
            f.close()
f2.close()