
# GondorFu
---
## 描述
615: Course Schedule

There are a total of n courses you have to take, labeled from 0 to n - 1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

616: 安排课程

你需要去上n门九章的课才能获得offer，这些课被标号为 0 到 n-1 。
有一些课程需要“前置课程”，比如如果你要上课程0，你需要先学课程1，我们用一个匹配来表示他们： [0,1]

给你课程的总数量和一些前置课程的需求，返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，你只要返回一种就可以了。如果不可能完成所有课程，返回一个空数组。

## 样例
```
615：
Given n = 2, prerequisites = [[1,0]]
Return true

Given n = 2, prerequisites = [[1,0],[0,1]]
Return false

616：
给定 n = 2, prerequisites = [[1,0]]
返回 [0,1]

给定 n = 4, prerequisites = [1,0],[2,0],[3,1],[3,2]]
返回 [0,1,2,3] or [0,2,1,3]
```

## 标签 
亚马逊 宽度优先搜索 Zenefits Topological Sort 脸书

## 解题思路
- 思路：这是一道典型的拓扑排序题，主要涉及数据结构。

    基本思路是维持一个课程入度为零的数组，不断输出该数组中的元素，并将新的入度为零的课程加入该数组中。
- 具体操作：首先遍历先行课程，用一个二维数据保存所有课程必须的先后信息。

    具体二维数据的第i行保存的是以第i门课为先行的后续课程，比如[1,0][2,0]，那么第0行包含[1, 2]。

    然后维持一个每门课程当前还需要修的先行课程数量，即入度之后遍历一遍入度数组，找出所有入度为零的课程，将它们都放入入度为零的数据中，重复判断入度为零的数据是否为空，如果为空结束。如果不为空，那么输出其中的任意一个数，将它加入结果序列，同时通过之前保存的所有课程的先行课程信息，将它的直接后行课程的入度减一，如果后行课程的入度降为零，那么将此后行课程也加入到入度为零的数组中。如此重复，最后结果序列就是能够实现的课程。如果它的长度小于课程总数那么不能实现；反之可以。













