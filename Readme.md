
# GondorFu
---
## ������
[Lintcode](http://www.lintcode.com)����Ŀ�ĸ��˽�������˼·��
���������ܰ���**C++��Java��Python**��һ�ֻ������ԡ�

## ����
**C++** 1. A + B����
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

## ��ǩ 
�漰�����ݽṹ����Ҫ�㷨

## ����˼·
- ˼�룺���ܸ���˼������Ĺ��̡�- �������������ʹ��ĳ�㷨�����ݽṹ�Ľ��ⲽ�衣

## > ***�������ǴӲ���ֵ�֤�ݿ�ʼ�����������۵�һ������.***
![Past, Present, Future](http://www.luke54.org/images/0/20120326104830962302.jpg)
