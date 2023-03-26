import pandas as pd
import math
import numpy as np
df=pd.read_csv("C:\Users\gvija\Downloads\weather.nominal.csv")
# df['windy'].astype('string')
features=[feat for feat in df]
features.remove('play')
class Node:
  def __init__(self):
    self.children=[]
    self.value=''
    self.isLeaf=False
    self.pred=""
    self.IG=0
def entropy(examples):
  pos=0.0
  neg=0.0
  for _,row in examples.iterrows():
    if row["play"]=="yes":
      pos+=1
    else:
      neg+=1
  if pos==0.0 or neg==0.0:
    return 0.0
  else:
    p=pos/(pos+neg)
    n=neg/(pos+ neg)
    return -(p*math.log(p,2)+n*math.log(n,2))
def IG(examples,attr):
  uniq=np.unique(examples[attr])
  gain=entropy(examples)
  for u in uniq:
    # print("Uniq",u)
    subdata=examples[examples[attr]==u]
    # print("subdata",subdata)
    # subdata
    sub_e=entropy(subdata)
    # print("sub_e",sub_e)
    gain-=(float(len(subdata))/float(len(examples)))*sub_e
  return gain
# print(IG(df,'humidity'))
def ID3(examples,attrs):
  root=Node()
  max_gain=0
  max_feat=""
  for feature in attrs:
    gain=IG(examples,feature)
    if gain>max_gain:
      max_gain=gain
      max_feat=feature
  root.value=max_feat
  # print("maxFeat",max_feat)
  uniq=np.unique(examples[max_feat])
  for u in uniq:
    # print("U",u)
    subdata=examples[examples[max_feat]==u]
    if entropy(subdata)==0.0:
      newNode=Node()
      newNode.isLeaf=True
      newNode.value=u
      newNode.pred=np.unique(subdata["play"])
      newNode.IG=max_gain
      root.children.append(newNode)
    else:
      dummyNode=Node()
      dummyNode.value=u
      dummyNode.IG=max_gain
      new_attrs=attrs.copy()
      new_attrs.remove(max_feat)
      child=ID3(subdata,new_attrs)
      dummyNode.children.append(child)
      root.children.append(dummyNode)
  return root
root=ID3(df,features)
def printTree(root: Node, depth=0):
    for i in range(depth):
        print("\t", end="")
    print(root.value, end="")
    if root.isLeaf:
        print(" -> ", root.pred)
    print()
    for child in root.children:
        printTree(child, depth + 1)
printTree(root)