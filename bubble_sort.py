'''
v1
1.比较相邻的元素，如果前者比后者大，就交换二者
2.对每一对相邻元素实施同样的方法，直到最后
3.重复1、2步骤，除了最后一个元素

'''
def bubblesort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

'''
v2
添加flag，遍历一次后如果没有交换，则证明有序，不再进行后续的排序
'''
def bubblesort(arr):
    for i in range(len(arr)-1):
        flag = False
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                flag=True
        if not flag:
            return
    return arr
    
