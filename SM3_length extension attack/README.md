#  SM3 Length Extension Attack
(By: Hongkuan Lv)

## The attack
* 随机生成比特串m1,使用SM3加密m1得到其hash值h1
* 随机生成比特串m2,使用SM3加密h1||m2得到其hash值h2
* 填充pading,使用SM3加密h1||pading||m2得到其hash值h3
* 判断h2是否等于h3,若相等，则攻击成功
  

## Pading

SM3的消息长度是64字节或者它的倍数，如果消息的长度不足则需要padding。在padding时，首先填充一个1，随后填充0，直到消息长度为56(或者再加整数倍的64)字节，最后8字节用来填充消息的长度。

对于大多数算法（包括 MD4、MD5、RIPEMD-160、SHA-0、SHA-1 和 SHA-256），字符串会被填充，直到其长度等于 56 字节（mod 64）。换句话说，它被填充直到长度比完整（64 字节）块少 8 个字节（8 个字节是编码长度字段的大小）。

## Directions
* 该project使用gmssl完成
* sm3le.py是该project的长度扩展攻击代码
* my_sm3.py对python库中的sm3实现部分稍作修改，以便完成长度扩展攻击
* func1.py：sm3实现部分用到的一些辅助函数，和python库中的一样，未作修改



## Result
![Image text](https://github.com/DaquanDong/Homework/blob/main/SM3_length%20extension%20attack/Result.png)

## Reference
https://github.com/hjzin/SM3LengthExtensionAttack


