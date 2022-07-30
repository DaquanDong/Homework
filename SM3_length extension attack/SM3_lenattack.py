
import sys
sys.path.append(r"C:\Users\yyq\Desktop") # add work dir to sys path
from gmssl import sm3, func
import random
import my_sm3
import struct

def generate_h2(h1, m1_len, m2):
    vectors = []
    message = ""
    for r in range(0, len(h1), 8):    
        vectors.append(int(h1[r:r + 8], 16))
    if m1_len > 64:
        for i in range(0, int(m1_len / 64) * 64):
            message += 'a'
    for i in range(0, m1_len % 64):
        message += 'a'
    message = func.bytes_to_list(bytes(message, encoding='utf-8'))
    message = padding(message)
    message.extend(func.bytes_to_list(bytes(m2, encoding='utf-8')))
    return my_sm3.sm3_hash(message, vectors)

#填充
def padding(msg):
    mlen = len(msg)
    msg.append(0x80)
    mlen += 1
    tail = mlen % 64
    range_end = 56
    if tail > range_end:
        range_end = range_end + 64
    for i in range(tail, range_end):
        msg.append(0x00)
    bit_len = (mlen - 1) * 8
    msg.extend([int(x) for x in struct.pack('>q', bit_len)])
    for j in range(int((mlen - 1) / 64) * 64 + (mlen - 1) % 64, len(msg)):
        global pad
        pad.append(msg[j])
        global pad_str
        pad_str += str(hex(msg[j]))
    return msg

m1 = str(random.random())  # 随机生成消息m1
h1 = sm3.sm3_hash(func.bytes_to_list(bytes(m1, encoding='utf-8')))
m1_len = len(m1)
m2 =str(random.random())    # 附加消息
pad_str = ""
pad = []
h2 = generate_h2(h1, m1_len, m2)
new_msg = func.bytes_to_list(bytes(m1, encoding='utf-8'))
new_msg.extend(pad)
new_msg.extend(func.bytes_to_list(bytes(m2, encoding='utf-8')))
new_msg_str = m1 + pad_str + m2
h3 = sm3.sm3_hash(new_msg)

print("m1: "+m1)
print("h1:" + h1)
print("------------------------------------------------------------------")
print("m2:", m2)
print("h2:" + h2)
print("------------------------------------------------------------------")
print("new message: \n" + new_msg_str)
print("h3:" +h3)
print("------------------------------------------------------------------")
if h3 == h2:
    print("h3==h2,成功")
else:
    print("h3!=h2,失败")
