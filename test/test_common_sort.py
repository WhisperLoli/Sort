from common_sort.sort_asc import Sort
import unittest
import random


class MyTest(unittest.TestCase):  # 继承unittest.TestCase
    def tearDown(self):
        # 每个测试用例执行之后做操作
        pass

    def setUp(self):
        # 每个测试用例执行之前做操作
        pass

    @classmethod
    def tearDownClass(self):
        # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
        pass

    @classmethod
    def setUpClass(self):
        # 必须使用@classmethod 装饰器,所有test运行前运行一次
        pass

    def test_run(self):

        data = []

        for i in range(10):
            data.append(int(random.random()*10))

        print("\n")
        print("原始数据集为:" + str(data)+ "\n")
        print("冒泡排序结果:" + str(Sort.bubble_sort(data)))

        print("选择排序结果:" + str(Sort.select_sort(data)))

        print("插入排序结果:" + str(Sort.insert_sort(data)))

        print("希尔排序结果:" + str(Sort.shell_sort(data)))

        print("归并排序结果:" + str(Sort.merge_sort(data)))

        print("快速排序结果:" + str(Sort.quick_sort(data)))

        print("堆排序结果:" + str(Sort.heap_sort(data)))


if __name__ == "__main__":

    unittest.main() #运行所有的测试用例