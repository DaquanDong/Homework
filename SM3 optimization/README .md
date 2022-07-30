# SM3 optimization

## 算法描述
### 概述
对长度为对长度为$l(l<2^{64})$比特的消息$m$，SM3杂凑算法经过填充和迭代压缩，生成杂凑值，杂凑值长度为256比特。

### 填充
假设消息 $m$ 的长度为 $l$ 比特。自先将比特“ 1 ”添加到消息的末尾, 再添加 $k$ 个 “ 0 ”, $k$ 是满 足 $l+1+k \equiv 448 \bmod 512$ 的最小的非负整数。然后再添加一个64位比特串, 该比特串是长度 $l$ 的二进 制表示。填充后的消息 $m^{\prime}$ 的比特长度为512的倍数

### 迭代压缩
##### 迭代过程
将填充后的消息 $m^{\prime}$ 按 512 比特进行分组: $m^{\prime}=B^{(0)} B^{(1)} \cdots B^{(n-1)}$
其中 $n=(l+k+65) / 512$ 。
对 $m^{\prime}$ 按下列方式迭代:
$For\, i=0\,\, to\, n-1$
$V^{(i+1)}=C F\left(V^{(i)}, B^{(i)}\right)$
$EndFor$
其中 $C F$ 是压缩函数, $V^{(0)}$ 为 256 比特初始值 $I V, B^{(i)}$ 为填充后的消息分组, 迭代压缩的结果 为 $V^{(n)}$ 
##### 消息扩展
将消息分组 $B^{(i)}$ 按以下方法扩展生成 132 个字 $W_{0}, W_{1}, \cdots, W_{67}, W_{0}^{\prime}, W_{1}^{\prime}, \cdots, W_{63}^{\prime}$, 用于压缩函 数 $C F$ :
a)将消息分组 $B^{(i)}$ 划分为 16 个字 $W_{0}, W_{1}, \cdots, W_{15}$ 。
b)$For\, j=16\, to \,67$
$W_{j} \leftarrow P_{1}\left(W_{j-16} \oplus W_{j-9} \oplus\left(W_{j-3} \lll 15\right)\right) \oplus\left(W_{j-13} \lll 7\right) \oplus W_{j-6}$
$EndFor$
c) $For \,j=0 \,to\, 63$
$W_{j}^{\prime}=W_{j} \oplus W_{j+4}$
$EndFor$

##### 压缩函数
令 $A, B, C, D, E, F, G, H$ 为字寄存器, $S S 1, S S 2, T T 1, T T 2$ 为中间变量,压缩函数 $V^{i+1}=C F\left(V^{(i)}, B^{(i)}\right), 0 \leq$ $i \leq n-1$ 。计算过程描述如下:
$A B C D E F G H \leftarrow V^{(i)}$
$For \,j=0 \,to\, 63$
$S S 1 \leftarrow\left((A \lll 12)+E+\left(T_{j} \lll j\right)\right) \lll 7$
$S S 2 \leftarrow S S 1 \oplus(A \lll 12)$
$T T 1 \leftarrow F F_{j}(A, B, C)+D+S S 2+W_{j}^{\prime}$
$T T 2 \leftarrow G G_{j}(E, F, G)+H+S S 1+W_{j}$
$D \leftarrow C$
$C \leftarrow B \lll 9$
$B \leftarrow A$
$A \leftarrow T T 1$
$H \leftarrow G$
$G \leftarrow F \lll 19$
$F \leftarrow E$
$E \leftarrow P_{0}(T T 2)$
$EndFor$
$V^{(i+1)} \leftarrow A B C D E F G H \oplus V^{(i)}$
其中, 字的存储为大端(big-endian)格式。

##### 杂凑值
$A B C D E F G H \leftarrow V^{(n)}$
输出256比特的杂凑值 $y=A B C D E F G H$ 

### 优化
* 使用右移代替除法，乘法一般都能被编译器优化，但除法因为DIV指令会将余数放在寄存器里面从而可以使用右移代替除法进行优化
* 多线程编程

### 结果
