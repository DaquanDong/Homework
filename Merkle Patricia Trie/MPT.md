# MERKLE PATRICIA  TREES

### Patricia Trie
Patricia trie 是一种数据结构，也称为前缀树、基数树或 trie。 Trie 使用键作为路径，因此共享相同前缀的节点也可以共享相同的路径。 这种结构在查找公共前缀方面最快，实现简单，并且需要很小的内存。 

![Image text](https://github.com/DaquanDong/Homework/blob/main/Merkle%20Patricia%20Trie/Example%20of%20Patricia%20Trie.png)

### Merkle Tree
Merkle树是一棵哈希树，叶节点存储数据，父节点包含其子节点的哈希值以及子节点哈希值之和的哈希值。 由于除叶子节点之外的所有节点都包含一个哈希，因此默克尔树也称为哈希树。

使用Merkle树可以有效地找出两个不同节点是否具有相同的数据。首先必须比较两个节点的Top Hash值。如果它们相同，则两个节点具有相同的数据。例如，如果上图，当有四个节点(L1, L2, L3, L4)时，只需要检查它们是否有相同的Top Hash。如果Top哈希不同，并且想知道哪些数据不同，应该比较Hash0和Hash1，并检查哪个分支不同。通过这样做，最终会发现哪些数据是不同的。

![Image text](https://github.com/DaquanDong/Homework/blob/main/Merkle%20Tree/result.png)

### Merkle Patricia Trie
在MPT和Merkle树中，每个节点都有一个散列值。每个节点的哈希值由其内容的sha3哈希值决定。这个散列也用作指向节点的键。Go-ethereum使用levelDB, parity使用rocksDB存储状态。它们是键值存储器。存储中保存的键和值不是以太坊状态的键值。存储在存储器中的值是MPT节点的内容，而键是该节点的散列。

![Image text](https://github.com/DaquanDong/Homework/blob/main/Merkle%20Tree/result.png)

以太坊状态的key值作为MPT上的路径。Nibble是用于区分MPT中的键值的单位，因此每个节点最多可以有16个分支。此外，由于节点有自己的值，所以分支节点是一个包含17项的数组，由1个节点值和16个分支组成。

没有子节点的节点称为叶节点。叶节点由两项组成:它的路径和值。例如，假设键“0xBEA”包含1000，键“0xBEE”包含2000。然后，应该有一个具有“0xBE”路径的分支节点，在该节点下，将附加两个具有两个路径(“0xA”和“0xE”)的叶节点。

![Image text](https://github.com/DaquanDong/Homework/blob/main/Merkle%20Tree/result.png)

在MPT中，除了分支节点和叶节点外，还有一种类型的节点。它们是扩展节点。扩展节点是分支节点的优化节点。在以太坊状态中，分支节点通常只有一个子节点。这就是为什么MPT将只包含一个子节点的分支节点压缩为具有子节点的路径和散列的扩展节点的原因。

因为叶子节点和扩展节点都是两个条目的数组，所以应该有一种方法来区分这两个不同的节点。为了进行这样的区分，MPT向路径添加了一个前缀。如果节点是叶子，且路径由偶数个小块组成，则添加0x20作为前缀。如果路径包含奇数个小块，则应该添加0x3作为前缀。当节点为扩展节点且路径为偶数个蚕食时，前缀为“0x00”。如果它包含奇数个小块，您应该添加0x1作为前缀。因为由奇数个nibble组成的路径会得到一个nibble作为前缀，而由偶数个nibble组成的路径会得到两个nibble作为前缀，所以路径总是用字节表示。



