# GondorFu
---
## 描述
写出一个函数 anagram(s, t) 判断两个字符串是否可以通过改变字母的顺序变成一样的字符串。

## 说明
What is Anagram?
- Two strings are anagram if they can be the same after change the order of characters.

## 样例
```
O(n) time, O(1) extra space
```

## 挑战 
O(n) time, O(1) extra space

## 标签 
Cracking The Coding Interview 字符串处理

## 解题思路
- 思想：
    
    通过哈希存储每一个字符出现的次数，然后判断是否两字符串中字符出现的次数相等。
    
    由于出现的字符是有限的，所以满足O(1)的空间复杂度。
    
- 具体操作：

    首先判断两字符串长度是否相等，如果相等，使用哈希为每个字符出现的次数计数。然后对第二个字符串进行遍历，一旦出现计数结果小于0，那么返回假。如果直至最后也没有返回，那么返回真。














