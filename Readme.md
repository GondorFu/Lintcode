
# GondorFu
---
## 描述：
[Lintcode](http://www.lintcode.com)中题目的个人解题代码和思路。
解题代码可能包含**C++，Java，Python**的一种或几种语言。

## 样例
**C++** 1. A + B问题
```
class Solution {
public:
    /*
     * @param a: The first integer
     * @param b: The second integer
     * @return: The sum of a and b
     */
    int aplusb(int a, int b) {
        // write your code here, try to do it without arithmetic operators.
        return (!b ? a : aplusb(a ^ b, (a & b) << 1));
    }
};
```

## 标签 
涉及的数据结构和主要算法

## 解题思路
- 思想：介绍个人思考问题的过程。- 具体操作：具体使用某算法和数据结构的解题步骤。

## > ***人生，是从不充分的证据开始引出完美结论的一种艺术.***
![Past, Present, Future](http://www.luke54.org/images/0/20120326104830962302.jpg)
