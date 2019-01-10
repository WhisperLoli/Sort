from utils.swap import Swap
import copy

class Sort:

    @classmethod
    def quick_sort(self, data):
        """快速排序"""
        if len(data) <= 1:
            return data
        else:
            # 采用递归，小于首位置的list + 等于首位置的list + 大于首位置的list
            return self.quick_sort(list(filter(lambda x: x < data[0], data))) + \
                   list(filter(lambda x: x == data[0], data)) + self.quick_sort(
                list(filter(lambda x: x > data[0], data)))

    @classmethod
    def bubble_sort(self, data_bak):
        """冒泡排序"""
        data = copy.copy(data_bak)
        for i in range(len(data)):
            # 外层循环，控制最大的数移到最后面
            for j in range(len(data) - i - 1):
                # 内层循环，比较相邻的数的大小，大的数往后移
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = Swap.swap(data[j], data[j + 1])
        return data

    @classmethod
    def select_sort(self, data_bak):
        """选择排序"""
        data = copy.copy(data_bak)
        # 外层循环控制第i个元素
        for i in range(len(data)):
            # 内层循环控制第i个数和剩余的数比较，并交换
            for j in range(i, len(data)):
                if data[i] > data[j]:
                    data[i], data[j] = Swap.swap(data[i], data[j])
        return data

    @classmethod
    def insert_sort(self, data_bak):
        """插入排序"""
        data = copy.copy(data_bak)
        for i in range(len(data)):
            j = i
            while j > 0:
                # 比较data[i]值与已排完序的list,插入到已排完序的list中
                if data[j] < data[j - 1]:
                    data[j], data[j - 1] = Swap.swap(data[j], data[j - 1])
                    j -= 1
                else:
                    break
        return data

    @classmethod
    def shell_sort(self, data_bak):
        """希尔排序"""
        data = copy.copy(data_bak)
        n = len(data)
        # 初始步长
        gap = n // 2
        while gap > 0:  # 每个步长进行排序
            for i in range(gap, n):
                temp = data[i]  # 取每一列的最末尾元素
                j = i
                while j >= gap and data[j - gap] > temp:  # 对每列进行纵向排序
                    data[j] = data[j - gap]
                    j -= gap
                data[j] = temp
            gap = gap // 2  # 得到新的步长
        return data

    @classmethod
    def merge_sort(self, data_bak):
        """归并排序"""
        data = copy.copy(data_bak)

        def split_list(data):
            """拆分数组至不可拆分"""
            result = []
            if len(data) <= 1:
                return data
            if len(data) == 2:
                mid = len(data) // 2
                left, right = data[:mid], data[mid:]
                return merge_list(left, right, result)
            else:
                mid = len(data) // 2
                left, right = data[:mid], data[mid:]
                left = split_list(left)
                right = split_list(right)
                return merge_list(left, right, result)

        def merge_list(left, right, result):
            """合并小数组"""
            while left != [] and right != []:
                if left[0] < right[0]:
                    result.append(left[0])
                    left = left[1:]
                else:
                    result.append(right[0])
                    right = right[1:]

            if left == []:
                result.extend(right)
                return result
            else:
                result.extend(left)
                return result

        return split_list(data)

    @classmethod
    def heap_sort(self, data_bak):
        """堆排序，升序大顶堆，降序小顶堆"""
        data = copy.copy(data_bak)

        def create_max_heap(length):
            for i in range((len(data[:length + 1]) - 1) // 2, -1, -1):  # 遍历非叶子节点
                harmonize_nope_leaf_node(i, len(data[:length + 1]))

        def harmonize_nope_leaf_node(index, length):
            """当前节点与子节点比较，如果子节点还有子节点，递归子节点的子节点"""
            # 完全二叉树
            child_base_index = 2 * index
            # 与子节点比较大小
            if child_base_index + 2 < length:  # 存在左右子节点
                if data[child_base_index + 1] >= data[child_base_index + 2]:  # 左子节点大于右子节点
                    if data[child_base_index + 1] > data[index]:  # 左子节点大于父节点
                        data[child_base_index + 1], data[index] = Swap.swap(data[child_base_index + 1], data[index])
                        harmonize_nope_leaf_node(child_base_index + 1, length)
                else:
                    # 右子节点大于左子节点
                    if data[child_base_index + 2] > data[index]:  # 右子节点大于父节点
                        data[child_base_index + 2], data[index] = Swap.swap(data[child_base_index + 2], data[index])
                        harmonize_nope_leaf_node(child_base_index + 2, length)
            elif child_base_index + 1 < length:
                if data[child_base_index + 1] > data[index]:  # 只存在左子节点且左子节点大于父节点
                    data[child_base_index + 1], data[index] = Swap.swap(data[child_base_index + 1], data[index])
                    harmonize_nope_leaf_node(child_base_index + 1, length)
            else:  # 叶子节点
                pass

        for j in range(len(data) - 1, -1, -1):
            # 长度每次-1，首元素与当前长度尾元素交换
            create_max_heap(j)
            data[0], data[j] = Swap.swap(data[0], data[j])

        return data