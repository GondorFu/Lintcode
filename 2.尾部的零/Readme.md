# GondorFu
---
## 描述
设计一个算法，计算出n阶乘中尾部零的个数

## 样例
```
11! = 39916800，因此应该返回 2
```

## 挑战 
O(logN)的时间复杂度

## 标签 
数学

## 解题思路
- 思路：
    
    要出现0，就需要2*5.而2比5要多很多，所以只要统计出现的5的次数。而1-24只有一个5,25-124有2个5.依此不断除5就能得到最后的结果。

- 具体操作：
    
    见程序。














