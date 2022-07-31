# Homework

山东大学网安学院网络空间安全创新创业实践课程作业

------

## 小组成员：

| 小组成员姓名 | 小组成员学号 |                  Github账户名称                   |
| :----------: | :----------: | :-----------------------------------------------: |
|    董大铨    | 201900460054 |  [**DaquanDong**](https://github.com/DaquanDong)  |
|    吕洪宽    | 201918202216 | [**HongkuanLv** ](https://github.com/HongkuanLv)  |
|    邵鹏翔    | 201800203045 | [**YuQingGuoYu**](https://github.com/YuQingGuoYu) |

## 项目及完成情况：

| 编号 | 名称                                                         | 文件夹对应                                                   | 完成人         |
| :--: | :----------------------------------------------------------- | ------------------------------------------------------------ | -------------- |
|  1   | Implement the naïve birthday attack of reduced SM3           | [SM3_BirthdayAttack](https://github.com/DaquanDong/Homework/tree/main/SM3_BirthdayAttack) | 董大铨         |
|  2   | Implement the Rho method of reduced SM3                      | [SM3_RhoMethod](https://github.com/DaquanDong/Homework/tree/main/SM3_RhoMethod) | 董大铨         |
|  3   | Implement length extension attack for SM3, SHA256, etc       | [SM3 LengthExtensionAttack](https://github.com/DaquanDong/Homework/tree/main/SM3_length%20extension%20attack) | 吕洪宽         |
|  4   | Do your best to optimize SM3 implementation (software)       | [SM3 optimization](https://github.com/DaquanDong/Homework/tree/main/SM3%20optimization) | 吕洪宽         |
|  5   | Impl Merkle Tree following RFC6962                           | 1.[Merkle Tree](https://github.com/DaquanDong/Homework/tree/main/Merkle%20Tree) (吕洪宽) 2.[Merkle_ Tree](https://github.com/DaquanDong/Homework/tree/main/Merkle_Tree)（董大铨） | 吕洪宽、董大铨 |
|  6   | Try to Implement this scheme                                 | [Merkle_ Tree](https://github.com/DaquanDong/Homework/tree/main/Merkle_Tree) | 董大铨         |
|  7   | Report on the application of this deduce technique in Ethereum with ECDSA | [ECDSA](https://github.com/DaquanDong/Homework/tree/main/ECDSA) | 董大铨         |
|  8   | Impl sm2 with RFC6979                                        | [sm2](https://github.com/DaquanDong/Homework/tree/main/sm2)  | 董大铨，邵鹏翔 |
|  9   | Verify the above pitfalls with proof-of-concept code         |                                                              |                |
|  10  | Implement the above ECMH scheme                              | [ECMH](https://github.com/DaquanDong/Homework/tree/main/ECMH) | 邵鹏翔，董大铨 |
|  11  | Implement a PGP scheme with SM2                              | [PGP](https://github.com/DaquanDong/Homework/tree/main/PGP)  | 董大铨，邵鹏翔 |
|  12  | Implement sm2 2P sign with real network communication        |                                                              |                |
|  13  | Implement sm2 2P decrypt with real network communication     |                                                              |                |
|  14  | Send a tx on Bitcoin testnet, and parse the tx data down to every bit, better write script yourself |                                                              |                |
|  15  | PoC impl of the scheme, or do implement analysis by Google   |                                                              |                |
|  16  | Forge a signature to pretend that you are Satoshi            |                                                              |                |
|  17  | Research report on MPT                                       | 1.[MPT](https://github.com/DaquanDong/Homework/tree/main/Merkle%20Patricia%20Trie)（吕洪宽）                     2.[MPT研究报告 ](https://github.com/DaquanDong/Homework/tree/main/MPT研究报告)（董大铨）3.[MPT-研究报告](https://github.com/DaquanDong/Homework/blob/main/MPT-%E7%A0%94%E7%A9%B6%E6%8A%A5%E5%91%8A.pdf) （邵鹏翔）| 吕洪宽，董大铨，邵鹏翔 |
|  18  | Find a key with hash value `sdu_cst_20220610` under a message composed of your name followed by your student ID. For example, `San Zhan 202000460001` |                                                              |                |
|  19  | Find a 64-byte message under some k fulfilling that their hash value is symmetrical |                                                              |                |
|  20  | Write a circuit to prove that your CET6 grade is larger than 425.（a. Your grade info is like `(cn_id, grade, year, sig_by_moe)`. These grades are published as commitments onchain by MoE. b. When you got an interview from an employer, you can prove to them that you have passed the exam without letting them know the exact grade.） | [Real world zk](https://github.com/DaquanDong/Homework/tree/main/Real%20world%20zk) | 董大铨         |
|  21  | The commitment scheme used by MoE is SHA256-based.（`commit` = `SHA256(cn_id, grade, year, sig_by_moe, r)`） |                                                              |                |
