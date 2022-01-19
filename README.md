# Caigun's Notes
## (Extension) Sum of two numbers in the form of node
[Caigun](/my_page.html) 
Last updated on 2022-1-19 [View history pages](/content.html)
Python

[View previous](/content/t04.html)

This is the solution using node.

It is faster than my last program, but there is no big difference. The difficulty for me is creating answers in the form of nodes, regardless how I solve the sum problem. Now I can only use recursion to create such Nodes from a list of numbers, so maybe I should learn some other methods to solve such problems, such as loop.

Below are my solution:
```Markdown
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def newNode(self, fromNode = ListNode(), aList = []):   #Create nodes
        if aList:
            nextNode = ListNode(aList.pop(), fromNode)
            return self.newNode(nextNode, aList)
        else:
            return fromNode
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        answerList = []
        plus = False
        while True:
            a = b = 0   #if the node is Node, than this default will take place of the node.val
            if l1 != None:
                a = l1.val
            if l2 != None:
                b = l2.val
            if plus == True:
                answer = a + b + 1
                plus = False
            else:
                answer = a + b
            if answer >= 10:
                answerList.append(answer - 10)
                plus = True
            else:
                answerList.append(answer)
            if l1 == None:
                pass
            else:
                l1 = l1.next
            if l2 == None:
                pass
            else:
                l2 = l2.next
            if l1 == None and l2 == None:
                if plus == True:
                    answerList.append(1)   #add another digit if last sum is larger or equal to 10
                return self.newNode(None, answerList)
```

### Debug process
During debug process, I found that no matter what the answer is, my node always starts with 0, which is nonsense.
After going through the program, I realize that the default value of the node is 0, which I used it as the start of the nodes. Solution: I changed the start of the nodes to None, and solved the problem.

-------------------------------------------

## Sum of two numbers in the form of node
[Caigun](/my_page.html) 
Last updated on 2022-1-17 [View history pages](/content.html)
Python

### Task
Given two nonempty nodes, representing two nonminus integers. They are stored in reverse order for each digit, and every node can only store one digit.

Please add the two numbers and return the result in the form of node, just like what has been given. You can assume that except the number 0, no other numbers will start with 0.
(Problem from Leetcode)

### Analysis
First method I thought was just transform these two nodes into numbers and calculate the sum of them, them transform the result back into node to satisfy the requirements. But how can I transform a number back into node? I used recursion to create the node one by one.

### Solution
```Markdown
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def transform(self, num: str, result = None):
        if num == '':
            return result
        else:
            newresult = ListNode(int(num[0]), result)
            return self.transform(num[1:], newresult)
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a, b = str(l1.val), str(l2.val)
        while l1.next != None:
            a = str(l1.next.val) + a
            l1 = l1.next
        while l2.next != None:
            b = str(l2.next.val) + b
            l2 = l2.next
        result = str(int(a) + int(b))
        return self.transform(result)
```
I think this code is not efficient, because it did not used the feature of the node. However, this is method is really easy to deploy. The only challenge is the process that transform the number back to node form, whose difficulty mainly came from recursion. So this kind of silly method might be the last method I would use.

### Advanced solution
Calculating sum by digit is how we add two numbers together. Now that two numbers are provided in the form of digit, why not use this feature to solve the problem? It must be much easier to write and the program will be more efficient.

### Debug process
During the debug process, I noticed a point that I need to remenber: when defining a new function in a class containing self, you need to add 'self.' to your function name while using it, otherwise an error will occur:
```Markdown
NameError: name 'transform' is not defined
    return transform(result, ListNode() , init = True)
Line 24 in addTwoNumbers (Solution.py)
    ret = Solution().addTwoNumbers(param_1, param_2)
Line 50 in _driver (Solution.py)
    _driver()
Line 61 in <module> (Solution.py)
```

-------------------------------------------

## Finding the sum of two numbers
[Caigun](/my_page.html) 
Posted on 2022-1-17 [View history pages](/content.html)
Python

### Task
Given a list containing integers and a integer target value.

You are required to find two integers in this list which sum equals to the target value, and return their index. Suppose that every input will only lead to one answer, but no repeated occurance of same element index in the list are allowed.

(Problem from Leetcode)

### Analysis
This is easy to write regardless of the time complexity. We can go through every element in the list and combine them and test whether the sums equal to the target value.
```Markdown
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            pivot = i + 1
            while pivot < len(nums):
                    return  [i,pivot]
                else:
                    pivot += 1
```
The time complexity is O(n^2).

### Advanced Task
Find a solution whose time complexity is less than O(n^2).

### Advanced Task Analysis
When looking at the method I used above, it seems to be very similar to the sort method. So I am thinking to make the solution similar to the quick sort, which can make the time complexity lower to less than O(n^2), and I think it can be O(nlogn).
Than I find that if the list is sorted, then it can be easily done by compare the sum with the target value from two side of the list.

If the list is sorted, we can use this method to find the solution:
```Markdown
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lpivot = 0
        rpivot = len(nums)-1
        while nums[lpivot] + nums[rpivot] != target:
            while nums[lpivot] + nums[rpivot] < target:
                lpivot += 1
            if nums[lpivot] + nums[rpivot] == target:
                return [lpivot, rpivot]
            else:
                lpivot = 0
                rpivot -= 1
        return [lpivot, rpivot]
```
But if we use the function list.sort(), the index of the element will change, and thus make the result not accurate. One solution for this problem is that we get the result and then go back the original list and just search for the element and return the index. But when the list contains identical value elements, the program will return the same index, which is not allowed. So I use for loop to go through the element, so that we can find another target element.

### Advanced Task Solution
```Markdown
class Solution:
    def twoSumElement(self, nums: list[int], target: int):
        nums1 = nums[:]
        nums1.sort()
        lpivot = 0
        rpivot = len(nums1)-1
        while nums1[lpivot] + nums1[rpivot] != target:
            while nums1[lpivot] + nums1[rpivot] < target:
                lpivot += 1
            if nums1[lpivot] + nums1[rpivot] == target:
                return [nums1[lpivot], nums1[rpivot]]
            else:
                lpivot = 0
                rpivot -= 1
        return [nums1[lpivot], nums1[rpivot]]
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = self.twoSumElement(nums, target)
        l, r = False, False
        for i in range(len(nums)):
            if nums[i] == result[0] and l == False:
                result[0] = i 
                l = True
            elif nums[i] == result[1] and r == False:
                result[1] = i
                r = True
        return result
```
I think the average time complexity of this code is O(nlogn) from the sort() function.

-------------------------------------------

## 头文件注释
[Caigun](/my_page.html) 
Posted on 2022-1-14 [View history pages](/content.html)
C language

C语言与python不同，大多数使用的命令都需要预先声明（#include)头文件（.h）才能够使用。
目前使用到的头文件：
```Markdown
#include <stdio.h> 
//用于输入和输出
//用到的函数:
//printf() 用于输出
//scanf() 用于输入
#include <string.h> 
//用于处理字符
```

-------------------------------------------

## Welcome to Caigun's Blog!
[Caigun](/my_page.html) 
Posted on 2022-1-13 [View history updates](/content.html)
Introduction

This is the first blog I write. I am intended to write this blog to record my learning process of coding. I learnt python at the very beginning, and recently I have started learning C. I am only taking formal Python lessons from the University while watching video clips of teaching C languages. So I may write down my working process dealing with the python project problem ,and for C language contents may only contain notes or some simple practices.

```markdown
print('Hello world!')
```

```markdown
#include <stdio.h>
int main()
{
    printf("Hello world!");
    return 0;
}
```

-------------------------------------------

[View all history updates](/content.html)