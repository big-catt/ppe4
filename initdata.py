#初始化将存贮与文件、pickle和shelve的数据

#记录

bob = {'name':'Bob Smith','age':43,'pay':40000,'job':'hhhh'}
sue = {'name':'Sue Jones','age':46,'pay':70000,'job':'kkkk'}
tom = {'name':'Tom','age':56,'pay':90000,'job':None}

#数据库

db = {}
db['db'] = bob
db['sue'] = sue
db['tom'] = tom

if __name__ == '__main__':
    for key in db:
        print(key,'=>\n',db[key])