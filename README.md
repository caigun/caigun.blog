# Caigun's Notes
## Finding the sum of two numbers
[Caigun](/my_page.html) 
Last updated on 2022-1-17 [View history pages](/content.html)
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