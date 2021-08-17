# 堆排序
堆排序的最好、最差、平均的时间复杂度均为O(n)，此外最差的空间复杂度仅为O(1)，面试官**非常喜欢**考察对堆排序的理解

https://www.programiz.com/dsa/heap-sort

要理解堆排序，首先需要理解堆
1. 堆是一个完全二叉树，即任何分裂节点的子节点均满足：a. 如果右节点有值，则左节点必须有值；b. 如果一个分裂节点的子节点为空，则其右侧的分裂节点的子节点必须为空（通过这样一种限制，能将堆结构使用数组进行表示）；
2. 堆分为大顶堆和小顶堆：大顶堆的分裂节点上的值均大于其子节点，且根节点上的值最大；小顶堆的分裂节点上的值均小于其子节点，且根节点上的值最小。

堆的实现流程为：
1. 首先要进行整体建堆（heapify）：从最大的分裂节点开始，将分裂节点的值与其对应的子节点上的值进行比较，如果分裂节点的值大于（小于）其子节点，则构建小顶堆（大顶堆）时，将分裂节点的值与最小（最大）的子节点的值进行交换；交换后，对发生交换的子节点同样进行建堆操作；以上描述了Floyd建堆算法，即从下往上的建堆算法，整体时间复杂度为O(n)；
2. 随后进行排序（heap sort）：此处以大顶堆为例，首先将根节点元素与叶节点最后一个元素进行交换，并将数组长度-1，此时堆满足：除了叶节点不是大顶堆，其他分裂节点均满足大顶堆的定义；从根节点开始，从上往下进行heapify，此时其时间复杂度为O(logn)；
3. 重复过程2，完成排序，整体时间复杂度为O(nlogn)，空间复杂度为O(1)

以下以大顶堆为例，写一个heap_sort算法
```python
def heapify(arr, n, i):
    largest, l, r = i, 2 * i + 1, 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

arr = [1, 12, 9, 5, 6, 10]
heap_sort(arr)
print("Sorted array is", arr)
```
本处使用了自己实现的heapify进行建堆、堆排序操作，实际上python自带了heapq模组可以进行方便的建堆（但是由于模组限制，无法实现inplace的操作，因此使用此模组进行堆排序的空间复杂度为O(n)），但其仅可以建小顶堆，要使用该模组来建大顶堆，只需要给数组内的数全部变成其相反数即可。