import pymongo

##创建客户端
#格式：
client = pymongo.MongoClient('localhost')

##创建数据库
db = client['test1029']

##创建表
table = db['users']

##插入数据
# table.insert({'name':'zhangsan'})
# table.insert({'name':'lisi'})

##插入多条数据：
user1 = {'name':'wang','age':19}
user2 = {'name':'zhi','age':20}
user3 = {'name':'jian','age':21}

# table.insert_many([user1,user2,user3])

##查找(高级)
# user = table.find({'name':'wang','age':19})

# user = table.find({'age':{'$lt':20}})

# users = table.find({'$or':[{'name':'wang'},{'age':19}]})
#
# for i in users:
#     print(i)

#查询数量
# print(table.count())