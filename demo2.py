#循环语句：有规律切重复操作的语句

#列表
# a = [1,2,3,4]
# for i in a : # for 中的in不是判断
#     print(i)

# #元组
# b = ("123",1,3,4)
# for i in b:
#     print(i)

# #字符串变量
# c = "儿童节快乐"
# for i in c:
#     print(i)

#字典
d = {"username":"张三","password":"123456"}
for i in d:
    print(i) #i 第一次循环是username
    #print(d[i]) #下标key值方式取值
    print(d.get(i)) #get的方式取值
    print("========")
#如果键值对不存在，get取空值，key值会报错