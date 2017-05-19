
# GondorFu
---
## 描述：
[Lintcode: www.lintcode.com](http://www.lintcode.com)中题目的个人解题代码和思路。

解题代码可能包含**C++，Java，Python**的一种或几种语言。

## 样例
1.A + B问题

**C++:** 
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

<p></p>
<p></p>

> ## ***人生，是从不充分的证据开始引出完美结论的一种艺术.***
![Past, Present, Future](http://cdn1.itpro.co.uk/sites/itpro/files/images/dir_215/it_photo_107815.jpg)
