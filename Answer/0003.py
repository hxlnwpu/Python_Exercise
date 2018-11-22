#coding=utf-8
import redis, uuid

def getCoupon(n):
    uuids = []
    for i in range(n):
	    uuids.append(uuid.uuid1())
    return uuids


rcon = redis.Redis(host='localhost', port=6379, decode_responses=True)   # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
coupon=getCoupon(10)
print(type(coupon[1]))   ## uuids 类型是class

for i in range(10):
    rcon.lpush('promot', uuid.uuid1())     #lpush第三个参数类型是byte,string,number
result=rcon.lrange('promot',0,10)
for j in range(len(result)):
    print(result[j])




