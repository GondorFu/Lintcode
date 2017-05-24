# GondorFu
---
## 描述
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

## 样例
```
n = 10, I pick 4 (but you don't know)

Return 4. Correct !
```

## 标签 
二分法 谷歌

## 解题思路
- 思路：这是一道很简单的题，典型的二分法。
- 具体操作：定义两个指针l和r分别表示1和n，不断判断两个之间中间的数与目标数的大小。如果小了，就把l加大；如果大了，就把r减小，直到选中要求数字。

唯一需要注意的是返回1表示猜的数字小了，返回-1表示猜的数字大了。

























