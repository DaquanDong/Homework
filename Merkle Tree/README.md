##  在 Python 中实现 Merkle 树

* Merkle 树是一棵二叉树，其中每个叶节点都是数据块的哈希，每个内部节点都是其子节点的哈希。在比特币协议中，它通过获取每个数据交易的哈希值并生成一个唯一的根哈希值来表示整个交易集的哈希值，从而确保交易集的不变性。
* 该project 使用类对Merkle 树进行实现
* Node 类存储它的哈希和对左右子节点的引用，添加两个静态方法来使用 SHA-256 算法进行散列，使用两次哈希以提高安全性。
* 由于 Merkle 树的结构方式，我们需要偶数个叶节点来建树。如果有奇数个数据块，那么只需对最后一个块进行两次哈希处理，复制最后一个叶节点。
* Merkle 树类本身包含两种用于递归构建树的方法，另外两种用于按前缀顺序打印节点，另一种用于获取根哈希。
* 可以通过发送字符串列表并获取其对应的默克尔树根哈希来测试,测试结果如下：

![Image text](https://github.com/DaquanDong/Homework/blob/main/Merkle%20Tree/result.png)

* reference：https://onuratakan.medium.com/what-is-the-merkle-tree-with-python-example-cbb4513b8ad0
