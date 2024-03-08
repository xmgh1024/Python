def heapify(arr, n, i):
    largest = i  # 初始化最大元素为根
    l = 2 * i + 1  # 左子节点
    r = 2 * i + 2  # 右子节点

    # 检查左子节点是否大于根
    if l < n and arr[i] < arr[l]:
        largest = l

    # 检查右子节点是否大于目前已知的最大元素
    if r < n and arr[largest] < arr[r]:
        largest = r

    # 如果最大元素不是根，则交换根和最大元素
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # 递归地调整受影响的子堆
        heapify(arr, n, largest)

# 堆排序函数
def heapSort(arr):
    n = len(arr)

    # 构建一个最大堆
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # 一个个从堆顶取出元素
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换
        heapify(arr, i, 0)


if __name__ == '__main__':
    # 测试堆排序算法
    arr = [12, 11, 13, 5, 6, 7]
    heapSort(arr)
    print("排序后的数组:", arr)
