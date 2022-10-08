"""Hops flask middleware example"""
from flask import Flask
import ghhops_server as hs
import rhino3dm


# register hops app as middleware
app = Flask(__name__)
hops: hs.HopsFlask = hs.Hops(app)


# flask app can be used for other stuff drectly
@app.route("/help")
def help():
    return "Welcome to Grashopper Hops for CPython!"


@hops.component(
    "/binmult",
    inputs=[hs.HopsNumber("A"), hs.HopsNumber("B")],
    outputs=[hs.HopsNumber("Multiply")],
)
def BinaryMultiply(a: float, b: float):
    return a * b


@hops.component(
    "/add",
    name="Add",
    nickname="Add",
    description="Add numbers with CPython",
    inputs=[
        hs.HopsNumber("A", "A", "First number"),
        hs.HopsNumber("B", "B", "Second number"),
    ],
    outputs=[hs.HopsNumber("Sum", "S", "A + B")]
)
def add(a: float, b: float):
    return a + b


@hops.component(
    "/pointat",
    name="PointAt",
    nickname="PtAt",
    description="Get point along curve",
    icon="pointat.png",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("t", "t", "Parameter on Curve to evaluate")
    ],
    outputs=[hs.HopsPoint("P", "P", "Point on curve at t")]
)
def pointat(curve: rhino3dm.Curve, t=0.0):
    return curve.PointAt(t)


@hops.component(
    "/srf4pt",
    name="4Point Surface",
    nickname="Srf4Pt",
    description="Create ruled surface from four points",
    inputs=[
        hs.HopsPoint("Corner A", "A", "First corner"),
        hs.HopsPoint("Corner B", "B", "Second corner"),
        hs.HopsPoint("Corner C", "C", "Third corner"),
        hs.HopsPoint("Corner D", "D", "Fourth corner")
    ],
    outputs=[hs.HopsSurface("Surface", "S", "Resulting surface")]
)
def ruled_surface(a: rhino3dm.Point3d,
                  b: rhino3dm.Point3d,
                  c: rhino3dm.Point3d,
                  d: rhino3dm.Point3d):
    edge1 = rhino3dm.LineCurve(a, b)
    edge2 = rhino3dm.LineCurve(c, d)
    return rhino3dm.NurbsSurface.CreateRuledSurface(edge1, edge2)

"""
 █████╗ ██╗     ██╗         ██████╗ ███████╗                                     
██╔══██╗██║     ██║         ╚════██╗██╔════╝                                     
███████║██║     ██║          █████╔╝███████╗                                     
██╔══██║██║     ██║         ██╔═══╝ ╚════██║                                     
██║  ██║███████╗███████╗    ███████╗███████║                                     
╚═╝  ╚═╝╚══════╝╚══════╝    ╚══════╝╚══════╝                                     
                                                                                 
 █████╗ ██╗      ██████╗  ██████╗ ██████╗ ██╗████████╗██╗  ██╗███╗   ███╗███████╗
██╔══██╗██║     ██╔════╝ ██╔═══██╗██╔══██╗██║╚══██╔══╝██║  ██║████╗ ████║██╔════╝
███████║██║     ██║  ███╗██║   ██║██████╔╝██║   ██║   ███████║██╔████╔██║███████╗
██╔══██║██║     ██║   ██║██║   ██║██╔══██╗██║   ██║   ██╔══██║██║╚██╔╝██║╚════██║
██║  ██║███████╗╚██████╔╝╚██████╔╝██║  ██║██║   ██║   ██║  ██║██║ ╚═╝ ██║███████║
╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
"""
"""
███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗ 
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝ 
███████╗█████╗  ███████║██████╔╝██║     ███████║██║██╔██╗ ██║██║  ███╗
╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║██║██║╚██╗██║██║   ██║
███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║██║██║ ╚████║╚██████╔╝
╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
"""

# searching algorithms
# linear search
@hops.component(
    "/linearsearch",
    name="Linear Search",
    nickname="LinearSearch",
    description="Linear search algorithm",
    inputs=[
        hs.HopsNumber("Target", "T", "Target number to search for"),
        hs.HopsNumber("List", "L", "List of numbers to search in", access = hs.HopsParamAccess.LIST)
    ],
    outputs=[hs.HopsNumber("Index", "I", "Index of target number")]
)
def linear_search(target: float, list: list):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1

# binary search
@hops.component(
    "/binarysearch",
    name="Binary Search",
    nickname="BinarySearch",
    description="Binary search algorithm",
    inputs=[
        hs.HopsNumber("Target", "T", "Target number to search for"),
        hs.HopsNumber("List", "L", "List of numbers to search in", access = hs.HopsParamAccess.LIST)
    ],
    outputs=[hs.HopsNumber("Index", "I", "Index of target number")]
)
def binary_search(target: float, list: list):
    list.sort()
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# depth first search
@hops.component(
    "/depthfirstsearch",
    name="Depth First Search",
    nickname="DepthFirstSearch",
    description="Depth first search algorithm",
    inputs=[
        hs.HopsNumber("Target", "T", "Target number to search for"),
        hs.HopsNumber("List", "L", "List of numbers to search in", access = hs.HopsParamAccess.LIST)
    ],
    outputs=[hs.HopsNumber("Index", "I", "Index of target number")]
)
def depth_first_search(target: float, list: list):
    for i in range(len(list)):
        if list[i] == target:
            return i
        elif type(list[i]) == list:
            index = depth_first_search(target, list[i])
            if index != -1:
                return index
    return -1

# breadth first search
@hops.component(
    "/breadthfirstsearch",
    name="Breadth First Search",
    nickname="BreadthFirstSearch",
    description="Breadth first search algorithm",
    inputs=[
        hs.HopsNumber("Target", "T", "Target number to search for"),
        hs.HopsNumber("List", "L", "List of numbers to search in", access = hs.HopsParamAccess.LIST)
    ],
    outputs=[hs.HopsNumber("Index", "I", "Index of target number")]
)
def breadth_first_search(target: float, list: list):
    for i in range(len(list)):
        if list[i] == target:
            return i
    for i in range(len(list)):
        if type(list[i]) == list:
            index = breadth_first_search(target, list[i])
            if index != -1:
                return index
    return -1

"""
███████╗ ██████╗ ██████╗ ████████╗██╗███╗   ██╗ ██████╗ 
██╔════╝██╔═══██╗██╔══██╗╚══██╔══╝██║████╗  ██║██╔════╝ 
███████╗██║   ██║██████╔╝   ██║   ██║██╔██╗ ██║██║  ███╗
╚════██║██║   ██║██╔══██╗   ██║   ██║██║╚██╗██║██║   ██║
███████║╚██████╔╝██║  ██║   ██║   ██║██║ ╚████║╚██████╔╝
╚══════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
"""

# sorting algorithms
# insertion sort
@hops.component(
    "/insertionsort",
    name="Insertion Sort",
    nickname="InsertionSort",
    description="Insertion sort algorithm",
    inputs=[
        hs.HopsNumber("List", "L", "List of numbers to sort", access = hs.HopsParamAccess.LIST)
    ],
    outputs=[hs.HopsNumber("List", "L", "Sorted list of numbers")]
)
def insertion_sort(list: list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key
    return list

# insertion sort add a number
@hops.component(
    "/insertionsortadd",
    name="Insertion Sort Add",
    nickname="InsertionSortAdd",
    description="Insertion sort algorithm",
    inputs=[
        hs.HopsNumber("List", "L", "List of numbers to sort", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("Number", "N", "Number to add to list")
    ],
    outputs=[hs.HopsNumber("List", "L", "Sorted list of numbers")]
)
def insertion_sort_add(list: list, number: float):
    list.append(number)
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key
    return list

# heap sort
@hops.component(
    "/heapsort",
    name="Heap Sort",
    nickname="HeapSort",
    description="Heap sort algorithm",
    inputs=[
        hs.HopsNumber("List1", "L1", "List of numbers to sort", access = hs.HopsParamAccess.LIST),
        hs.HopsNumber("List2", "L2", "List of numbers to sort", access = hs.HopsParamAccess.LIST)
    ],
    outputs=[
        hs.HopsNumber("List1", "L1", "Sorted list of numbers"), 
        hs.HopsNumber("List2", "L2", "Sorted list of numbers")]
)   
def heap_sort(list1: list, list2: list):
    for i in range(len(list1)):
        list2.append(list1[i])
    for i in range(len(list2)):
        heapify(list2, len(list2), i)
    for i in range(len(list2) - 1, 0, -1):
        list2[i], list2[0] = list2[0], list2[i]
        heapify(list2, i, 0)
    return list1, list2

def heapify(list: list, n: int, i: int):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and list[i] < list[l]:
        largest = l
    if r < n and list[largest] < list[r]:
        largest = r
    if largest != i:
        list[i], list[largest] = list[largest], list[i]
        heapify(list, n, largest)

# selection sort
@hops.component(
    "/selectionsort",
    name="Selection Sort",
    nickname="SelectionSort",
    description="Selection sort algorithm",
    inputs=[
        hs.HopsNumber("List", "L", "List of numbers to sort", access = hs.HopsParamAccess.LIST)
    ],
    outputs=[hs.HopsNumber("List", "L", "Sorted list of numbers")]
)
def selection_sort(list: list):
    for i in range(len(list)):
        min_index = i
        for j in range(i + 1, len(list)):
            if list[min_index] > list[j]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    return list

# merge sort
@hops.component(
    "/mergesort",
    name="Merge Sort",
    nickname="MergeSort",
    description="Merge sort algorithm",
    inputs=[
        hs.HopsNumber("List", "L", "List of numbers to sort", access = hs.HopsParamAccess.LIST)
    ],
    outputs=[hs.HopsNumber("List", "L", "Sorted list of numbers")]
)
def merge_sort(list: list):
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1
    return list

# quick sort
@hops.component(
    "/quicksort",
    name="Quick Sort",
    nickname="QuickSort",
    description="Quick sort algorithm",
    inputs=[
        hs.HopsNumber("List", "L", "List of numbers to sort", access = hs.HopsParamAccess.LIST)
    ],
    outputs=[hs.HopsNumber("List", "L", "Sorted list of numbers")]
)
def quick_sort(list: list):
    quick_sort_helper(list, 0, len(list) - 1)
    return list

def quick_sort_helper(list: list, low: int, high: int):
    if low < high:
        pi = partition(list, low, high)
        quick_sort_helper(list, low, pi - 1)
        quick_sort_helper(list, pi + 1, high)

def partition(list: list, low: int, high: int):
    i = (low - 1)
    pivot = list[high]
    for j in range(low, high):
        if list[j] <= pivot:
            i = i + 1
            list[i], list[j] = list[j], list[i]
    list[i + 1], list[high] = list[high], list[i + 1]
    return (i + 1)


# counting sort
@hops.component(
    "/countingsort2",
    name="Counting Sort",
    nickname="CountingSort",
    description="Counting sort algorithm",
    inputs=[
        hs.HopsInteger("List", "L", "List of numbers to sort", access = hs.HopsParamAccess.LIST)
    ],
    outputs=[hs.HopsInteger("List", "L", "Sorted list of numbers")]
)
def counting_sort2(list: list):
    max_element = int(max(list))
    min_element = int(min(list))
    range_of_elements = max_element - min_element + 1
    count_list = [0 for _ in range(range_of_elements)]
    output_list = [0 for _ in range(len(list))]
    for i in range(0, len(list)):
        count_list[list[i] - min_element] += 1
    for i in range(1, len(count_list)):
        count_list[i] += count_list[i - 1]
    for i in range(len(list) - 1, -1, -1):
        output_list[count_list[list[i] - min_element] - 1] = list[i]
        count_list[list[i] - min_element] -= 1
    for i in range(0, len(list)):
        list[i] = output_list[i]
    return list



# radix sort
@hops.component(
    "/radixsort2",
    name="Radix Sort",
    nickname="RadixSort",
    description="Radix sort algorithm",
    inputs=[
        hs.HopsInteger("List", "L", "List of numbers to sort", access = hs.HopsParamAccess.LIST)
    ],
    outputs=[hs.HopsInteger("List", "L", "Sorted list of numbers")]
)
def radix_sort2(list: list):
    max_element = int(max(list))
    place = 1
    while max_element // place > 0:
        counting_sort_helper(list, place)
        place *= 10
    return list

def counting_sort_helper(list: list, place: int):
    size = len(list)
    output = [0] * size
    count = [0] * 10
    for i in range(0, size):
        index = list[i] // place
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = size - 1
    while i >= 0:
        index = list[i] // place
        output[count[index % 10] - 1] = list[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(0, size):
        list[i] = output[i]

# bucket sort
@hops.component(
    "/bucketsort",
    name="Bucket Sort",
    nickname="BucketSort",
    description="Bucket sort algorithm",
    inputs=[
        hs.HopsNumber("List", "L", "List of numbers to sort", access = hs.HopsParamAccess.LIST)
    ],
    outputs=[hs.HopsNumber("List", "L", "Sorted list of numbers")]
)
def bucket_sort(list: list):
    bucket = []
    for i in range(len(list)):
        bucket.append([])
    for j in list:
        index_b = int(10 * j)
        bucket[index_b].append(j)
    for i in range(len(list)):
        insertion_sort(bucket[i])
    k = 0
    for i in range(len(list)):
        for j in range(len(bucket[i])):
            list[k] = bucket[i][j]
            k += 1
    return list









if __name__ == "__main__":
    app.run(debug=True)
