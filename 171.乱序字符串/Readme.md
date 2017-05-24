# GondorFu
---
## 描述
给出一个字符串数组S，找到其中所有的乱序字符串(Anagram)。如果一个字符串是乱序字符串，那么他存在一个字母集合相同，但顺序不同的字符串也在S中。

- 注意事项

    所有的字符串都只包含小写字母

## 样例
```
对于字符串数组 ["lint","intl","inlt","code"]

返回 ["lint","inlt","intl"]
```

## 挑战 
What is Anagram?
- Two strings are anagram if they can be the same after change the order of characters.

## 标签 
哈希表 字符串处理 优步 脸书

## 解题思路
- 思路：
    只写一个简单的思路：将每个字符串排序，之后用哈希存储字符串出现的次数。之后在遍历一遍字符串，将所有出现一次以上的字符串加入结果数组即可。
    
- 具体操作：
    见思路。














