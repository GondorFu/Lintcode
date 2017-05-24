# GondorFu
---
## 描述
Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.

You need to support the following method:
1. connect(a, b), add an edge to connect node a and node b. 2.query(a, b)`, check if two nodes are connected

## 样例
```
5 // n = 5
query(1, 2) return false
connect(1, 2)
query(1, 3) return false
connect(2, 4)
query(1, 4) return true
```

## 标签 
Union Find

## 解题思路
- 思路：
    这题直接想到的就是使用广度或深度首先搜索，不过发现超时。不过经过分析可以发现题目中并不要求完成给出关联路径，因此图中两点连通性能够使用集合进行简单的表述。两点之间建立一条边就相当于将包含两个点的集合合并。实现这个集合功能的数据结构或者说算法就是并查集（Union Find）。为高效地判断两点是否属于同一集合，它将同一集合中的每一个元素使用同一个数据标示。由此需要建立一个数据量同维的数组保存它的标示信息，而并查集最关键的就是在使用过程中始终使标示数据保持正确的标示信息。
    
- 具体操作：

    开始时，由于所有节点都分离，所以标示数组分别使用自身的标号进行标示。当连接一条边时，相当于合并包含两个点的集合，可以通过__find_index()函数找出它们各自的标示数组，并使用小的标示为大的标示标示。
    
    比如：[0 1 1 3 3]，它意味着点1和点2连通，点3和点4连通，其中0号位没有任何意义。若新建一条边连接点2和点4，由于点2的标示号为1，点4的标示号为3，那么3的标示号将也被设为1.
    
    同理，对于查询操作，只要使用__find_index()函数分别查询它们的标示号，并判断标识号是否相等就能判断这两个点是否连通。
    
    不过，你可能会发现这样查找效率很低，因为每次使用__find_index()都需要一直回溯到最开始的那个节点来判断。不过，其实只要简单的优化__find_index()让它在求解过程中不断把中间的过渡节点直接关联到标示节点就能使这样的查询操作时间复杂度为O(1)。具体实现见程序。














