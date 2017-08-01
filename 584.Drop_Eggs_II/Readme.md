# GondorFu
---
## 描述
There is a building of n floors. If an egg drops from the k th floor or above, it will break. If it's dropped from any floor below, it will not break.

You're given m eggs, Find k while minimize the number of drops for the worst case. Return the number of drops in the worst case.

## 样例
```
Given m = 2, n = 100 return 14
Given m = 2, n = 36 return 8
```

## 标签 
动态规划

## 解题思路
- 思路：
    
    一道动态规划的题目。
    状态转移矩阵
        A[i, j] = 1 + min( max(A[k-1, j-1], A[i-k, j]) )
        A[i, j]表示i节楼梯j个鸡蛋，k为当前选择尝试的楼层，A[k-1, j-1]表示尝试鸡蛋碎了，A[i-k, j]表示尝试鸡蛋没碎。
    
- 具体操作：

    首先对dp初始化，因为只用到当前j和j-1个鸡蛋的情况，应该可以使用更少的空间处理。
    
    由于需要对尝试楼层进行遍历，因此需要三重循环。














