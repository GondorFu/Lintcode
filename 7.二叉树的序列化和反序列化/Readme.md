# GondorFu
---
## 描述
设计一个算法，并编写代码来序列化和反序列化二叉树。将树写入一个文件被称为“序列化”，读取文件后重建同样的二叉树被称为“反序列化”。

如何反序列化或序列化二叉树是没有限制的，你只需要确保可以将二叉树序列化为一个字符串，并且可以将字符串反序列化为原来的树结构。

- 注意事项

    There is no limit of how you deserialize or serialize a binary tree, LintCode will take your output of serialize as the input of deserialize, it won't check the result of serialize.

## 样例
```
给出一个测试数据样例， 二叉树{3,9,20,#,#,15,7}，表示如下的树结构：

  3
 / \
9  20
  /  \
 15   7
我们的数据是进行BFS遍历得到的。当你测试结果wrong answer时，你可以作为输入调试你的代码。

你可以采用其他的方法进行序列化和反序列化。
```

## 标签 
二叉树 微软 雅虎

## 解题思路
- 思路：
    
    对于树进行中序遍历进行序列化，不过对于None节点添加'#'标示。同理进行反序列化。不过借鉴73,74题也可以使用中序和前序或后序来序列化。
    
- 具体操作：

    见思路。














