# GondorFu
---
## 描述
给一个词典，找出其中所有最长的单词。

## 样例
```
在词典

{
  "dog",
  "google",
  "facebook",
  "internationalization",
  "blabla"
}
中, 最长的单词集合为 ["internationalization"]

在词典

{
  "like",
  "love",
  "hate",
  "yes"
}
中，最长的单词集合为 ["like", "love", "hate"]
```

## 挑战 
遍历两次的办法很容易想到，如果只遍历一次你有没有什么好办法？

## 标签 
字符串处理 枚举法

## 解题思路
- 思路：有点太**了
- 具体操作：直接遍历一遍，不断判断是否是更长的字符串就行了，然后把最长相同长度的字符串添加到结果数组就行了。




























