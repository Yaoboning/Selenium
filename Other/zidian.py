#通过zip方法合并两个List为Dictionary
#遍历会按照原先的顺序

keys = ['b','a','c','e','d']
values = ['2','1','3','5','4']

for key,value in zip(keys,values):
    print (key,value)
