from selenium import webdriver
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from platform import system
import json
import os
import random
import math
import hashlib,json
import time
import string

#Merkel Tree生成
def Tree_Generate(Data):

    MerkleTree = [[]]
    #定义二维列表进行Merkeltree的存取
    l0 = len(Data)
    Depth = math.ceil(math.log(l0, 2))+1
    #初始化其深度
    MerkleTree[0] = [(hashlib.sha256(i.encode())).hexdigest() for i in Data]
    for i in range(1, Depth):
        l = math.floor(len(MerkleTree[i-1])/2)

        MerkleTree.append([(hashlib.sha256(MerkleTree[i-1][2*j].encode() + MerkleTree[i-1][2*j+1].encode())).hexdigest() for j in range(0, l)])
        if len(MerkleTree[i-1])%2 == 1:
            MerkleTree[i].append(MerkleTree[i-1][-1])

    return MerkleTree

def crawler():
    return [''.join(random.sample('0123456789abcdefghijklmnopqrstuvwxyz',5)) for i in range(0,100000)]

#节点存在性证明
def ShowEvidence(m,Tree):
    h = (hashlib.sha256(m.encode())).hexdigest()
    try:
        n=Tree[0].index(h)
    except:
        print("这个叶子节点不在树中")

    Depth = len(Tree)
    Evidence = []
    for d in range(0,Depth):
        if n%2==0:
            if n == len(Tree[d]) - 1:
                pass
            else:
                Evidence.append([Tree[d][n],Tree[d][n+1]])

        else:
            Evidence.append([Tree[d][n-1], Tree[d][n]])

        n = math.floor(n/2)

    Evidence.append([Tree[-1][0]])

    return Evidence

#验证证明的正确性
def Verify(m,Evidence,Top):
    h = (hashlib.sha256(m.encode())).hexdigest()
    if h != Evidence[0][0] and h != Evidence[0][1]:
        return False

    if Evidence[-1][0] != Top:
        return False

    Depth = len(Evidence)
    for i in range(0,Depth-1):
        node = (hashlib.sha256(Evidence[i][0].encode() + Evidence[i][1].encode())).hexdigest()
        if node != Evidence[i+1][0] and node != Evidence[i+1][1]:
            return False

    if (hashlib.sha256(Evidence[-2][0].encode() + Evidence[-2][1].encode())).hexdigest() != Evidence[-1][0]:
        return False

    return True


#对MerkelTree进行测试
DATA = ["111","222","333","456","789"]
Tree_1 = Tree_Generate(DATA)
print("已生成MerkleTree：")
print(Tree_1)


#再生成一个有100k个叶子节点的Merkel Tree
TestMessages = crawler()
Tree_2 = Tree_Generate(TestMessages)
print("已生成100k数据为叶子节点的Merkel Tree：")
print(Tree_2)


#证明对指定元素包含于Merkel Tree
n=random.randint(0,100000-1)
#我们从爬取的100k数据任选一个数据作为指定元素

Evidence = ShowEvidence(TestMessages[n],Tree_2)
print("指定元素n包含于Merkel Tree的evidence：")

print(Evidence)


#验证证明的正确性
print("验证证明正确性的依据：：")

print(Verify(TestMessages[n],Evidence,Tree_2[-1][0]))

