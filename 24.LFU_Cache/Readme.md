# GondorFu
---
## ����
LFU (Least Frequently Used) is a famous cache eviction algorithm.

For a cache with capacity k, if the cache is full and need to evict a key in it, the key with the lease frequently used will be kicked out.

Implement set and get method for LFU cache.

## ����
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

## ��ǩ 
���� Zenefits �Ų� �ȸ�

## ����˼·
- ˼·��
    
    Cache�����һ������Ӧ��ʵ����Cache������������䷽����LRU��Least Recently Used��134.LRU������ԣ���LFU��Least Frequently Used����LRU���ǽ�ʹ��ʱ�����֮ǰ��������ɾ������LFU���ǽ�ʹ�ô������ٵ�������ɾ����
    
    LFU��ʵ�ֱ�LRUҪ����һЩ����ΪҪ�洢���ʹ�õĴ��������Ȳ���134.LRU���������ʵ�ֱ��⡣
    
    ͬʱҲ����ֱ��ʹ��˫������ӹ�ϣ���д�����Ȼ��ʱ�������Ҫʹ��������ʽ�洢���ݣ�
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
    
- ���������

    ��������߼��Ƚϼ򵥣����岻��׸����














