# GondorFu
---
## ����
There is a building of n floors. If an egg drops from the k th floor or above, it will break. If it's dropped from any floor below, it will not break.

You're given m eggs, Find k while minimize the number of drops for the worst case. Return the number of drops in the worst case.

## ����
```
Given m = 2, n = 100 return 14
Given m = 2, n = 36 return 8
```

## ��ǩ 
��̬�滮

## ����˼·
- ˼·��
    
    һ����̬�滮����Ŀ��
    ״̬ת�ƾ���
        A[i, j] = 1 + min( max(A[k-1, j-1], A[i-k, j]) )
        A[i, j]��ʾi��¥��j��������kΪ��ǰѡ���Ե�¥�㣬A[k-1, j-1]��ʾ���Լ������ˣ�A[i-k, j]��ʾ���Լ���û�顣
    
- ���������

    ���ȶ�dp��ʼ������Ϊֻ�õ���ǰj��j-1�������������Ӧ�ÿ���ʹ�ø��ٵĿռ䴦��
    
    ������Ҫ�Գ���¥����б����������Ҫ����ѭ����














