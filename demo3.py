# 去判断用户是否登陆成功
db = [
    {"username":"张三","password":"123456"},
    {"username":"李四","password":"123321"}
]

zh = input("请输入账号:")
mm = input("请输入密码:")

for i in db:
    print(i)
    if zh == i.get("username") and mm == i.get("password"):
        print("输入账号{}登陆成功".format(zh))
    else:
        print("登陆失败！")