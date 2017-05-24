# GondorFu
---
## 描述
LFU (Least Frequently Used) is a famous cache eviction algorithm.

For a cache with capacity k, if the cache is full and need to evict a key in it, the key with the lease frequently used will be kicked out.

Implement set and get method for LFU cache.

## 样例
```
Given capacity=3

set(2,2)
set(1,1)
get(2)
>> 2
get(1)
>> 1
get(2)
>> 2
set(3,3)
set(4,4)
get(3)
>> -1
get(2)
>> 2
get(1)
>> 1
get(4)
>> 4
```

## 标签 
链表 Zenefits 优步 谷歌

## 解题思路
- 思路：
    
    Cache管理的一个经典应用实例。Cache管理的两个经典方法是LRU（Least Recently Used，134.LRU缓存策略）和LFU（Least Frequently Used）。LRU就是将使用时间最久之前的数据先删除，而LFU就是将使用次数最少的数据先删除。
    
    LFU的实现比LRU要复杂一些，因为要存储最近使用的次数。请先参与134.LRU缓存策略再实现本题。
    
    同时也不能直接使用双向链表加哈希进行处理，不然超时。因此需要使用如下形式存储数据：
    ```
    head --- FreqNode1 ---- FreqNode2 ---- ... ---- FreqNodeN
              |               |                       |               
            first           first                   first             
              |               |                       |               
           KeyNodeA        KeyNodeE                KeyNodeG           
              |               |                       |               
           KeyNodeB        KeyNodeF                KeyNodeH           
              |               |                       |               
           KeyNodeC         last                   KeyNodeI           
              |                                       |      
           KeyNodeD                                 last
              |
            last
    ```
    
- 具体操作：

    具体操作逻辑比较简单，具体不再赘述。














