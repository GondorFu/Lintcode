# GondorFu
---
## 描述
给定两个值 k1 和 k2（k1 < k2）和一个二叉查找树的根节点。找到树中所有值在 k1 到 k2 范围内的节点。即打印所有x (k1 <= x <= k2) 其中 x 是二叉查找树的中的节点值。返回所有升序的节点值。

## 样例
```
如果有 k1 = 10 和 k2 = 22, 你的程序应该返回 [12, 20, 22].

    20
   /  \
  8   22
 / \
4   12
```

## 标签 
二叉查找树 二叉树

## 解题思路
- 思路：
    
    使用递归得到左子树序列，根节点，右子树序列。组合得到最后结果。
    
- 具体操作：

    见程序。














