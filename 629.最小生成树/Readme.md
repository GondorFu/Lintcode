# GondorFu
---
## 描述
给出一些Connections，即Connections类，找到一些能够将所有城市都连接起来并且花费最小的边。
如果说可以将所有城市都连接起来，则返回这个连接方法；不然的话返回一个空列表。

- 注意事项
    返回cost最小的连接方法，如果cost相同就按照city1进行排序，如果city1也相同那么就按照city2进行排序。

## 样例
```
给出 connections = ["Acity","Bcity",1], ["Acity","Ccity",2], ["Bcity","Ccity",3]

返回 ["Acity","Bcity",1], ["Acity","Ccity",2]
```

## 标签 
亚马逊 Minimum Spanning Tree

## 解题思路
- 思路：
    
    这是一个求最小生成树的问题。由于题目事先没有给出所有点的信息，因此只能使用Prim算法进行求解。Prim算法首先需要对边进行排序，然后依次遍历这些边，如果这条边刚好能够连接两个分离的图，那么将这条边加入最小生成树。而边连接的两个点是否属于图的同一部分可以使用并查集来处理（589.Connecting Graph）。
    
- 具体操作：

    首先使用sorted对connections按cost,city1,city2进行排序。依次遍历每一条边，如果这条边连接同一个点，那么这条边直接跳过。如果连接独立的两个点，那么将这两点构成一个连通子图。如果连接连通部分外一点，那么将该点加入连通部分。如果两点都已访问过，那么如果连接了两个分离的连通子图，那么将两部分连通。最后通过count记录图中独立子图的数目，判断该图是否连通，输出结果。













