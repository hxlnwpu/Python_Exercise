import uuid

def getCoupon(n):
    uuids = []
    for i in range(n):
	    uuids.append(uuid.uuid1())
    return uuids

if __name__=='__main__':
    coupon=getCoupon(int(input("请输入想要想要获取的优惠码数：")))
    for i in range(len(coupon)):
        print(coupon[i])
    

