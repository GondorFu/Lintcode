# GondorFu
---
## 描述
There is a building of n floors. If an egg drops from the k th floor or above, it will break. If it's dropped from any floor below, it will not break.

You're given two eggs, Find k while minimize the number of drops for the worst case. Return the number of drops in the worst case.

## 说明
For n = 10, a naive way to find k is drop egg from 1st floor, 2nd floor ... kth floor. But in this worst case (k = 10), you have to drop 10 times.

Notice that you have two eggs, so you can drop at 4th, 7th & 9th floor, in the worst case (for example, k = 9) you have to drop 4 times.

## 样例
```
Given n = 10, return 4.
Given n = 100, return 14.
```

## 解题思路
- 思路：
    
    能够发现如下规律：
    n:   1 2 3 4 5 6 7 8 9 10 11 12 13 14 ... 
    k:   1 2 2 3 3 3 4 4 4 4  5  5  5  5
    rule:1 2   3     4        5
    
- 具体操作：

    根据规律得到公式k = (sqrt(8n-7)+1)/2，最后向下取整。














