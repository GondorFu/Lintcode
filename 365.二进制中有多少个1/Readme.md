# GondorFu
---
## 描述
计算在一个 32 位的整数的二进制表式中有多少个 1.

## 样例
```
给定 32 (100000)，返回 1

给定 5 (101)，返回 2

给定 1023 (111111111)，返回 9
```

## 挑战
If the integer is n bits with m 1 bits. Can you do it in O(m) time?

## 标签 
比特位操作 二进制

## 解题思路
- 思路：
    
    num = num & (num - 1)
    
- 具体操作：

    见程序。














