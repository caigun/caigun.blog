class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.lsum = data
        self.lcount = 0

class tree_list:
    def __init__(self):
        self.root = None

    def rotate(self, x:Node, y:Node):
        if x == y.left:
            left_direction = True
        else:
            left_direction = False
        if left_direction:
            y.left = x.right
            x.right = y
            y.lsum -= x.lsum
            y.lcount -= x.lcount +1
            x.parent = y.parent
            y.parent = x
            if y.left != None:
                y.left.parent = y
        else:
            y.right = x.left
            x.left = y
            x.lsum += y.lsum
            x.lcount += y.lcount +1
            x.parent = y.parent
            y.parent = x
            if y.right != None:
                y.right.parent = y
        if x.parent != None:
            if x.parent.left is y:
                x.parent.left = x
            else:
                x.parent.right = x
    
    def findnext(self, x:Node):
        if x.right != None:
            temp = x.right
            while temp.left != None:
                temp = temp.left
            return temp
        else:
            temp = x
            if temp.parent == None:
                return None
            while temp.parent.right is temp:
                temp = temp.parent
                if temp.parent == None:
                    return None
            return temp.parent

    def spray(self, x:Node):
        while x.parent != None:
            self.rotate(x, x.parent)
        self.root = x

    def infunction_insert(self, x:Node, val:int):
        temp = self.findnext(x)
        if temp == None:    # this is the case where x is the final node.
            x.right = Node(val)
            x.right.parent = x
            return
        self.spray(temp)
        self.spray(x)
        temp.left = Node(val)
        temp.left.parent = temp
        temp.lsum += val
        temp.lcount += 1
        self.root = x

    def insert(self, index:int, val:int):
        if self.root == None:
            self.root = Node(val)
            return
        elif index == 0:
            temp = self.root
            while temp.left != None:
                temp.lcount += 1
                temp.lsum += val
                temp = temp.left
            temp.left = Node(val)
            temp.left.parent = temp
            temp.lcount += 1
            temp.lsum += val
        else:
            temp = self.root
            index -= 1
            while temp.lcount != index:
                if temp.lcount > index:
                    temp = temp.left
                else:
                    index -= temp.lcount +1
                    temp = temp.right
            self.infunction_insert(temp, val)

    def infunction_delete(self, x:Node):
        temp = self.findnext(x)
        if temp == None:    # this is the case where x is the final node.
            if x.left != None:
                x.parent.right = x.left
            else:
                x.parent.right = None
            return
        self.spray(temp)
        self.spray(x)
        x.right = temp.right
        if x.right != None:
            x.right.parent = x

    def delete(self, index):
        if self.root == None:
            return
        elif index == 0:
            if self.root.left == None and self.root.right == None:
                self.root = None
                return
            elif self.root.left == None:
                temp = self.root.right
                temp.parent = None
                self.root = temp
                return
            temp = self.root
            while temp.left != None:
                temp.lcount -= 1
                temp = temp.left
            if temp.right == None:
                temp.parent.left = None
            else:
                temp.parent.left = temp.right
            val = temp.data
            while temp != None:
                temp.lsum -= val
                temp = temp.parent
        else:
            temp = self.root
            index -= 1
            while temp.lcount != index:
                if temp.lcount > index:
                    temp = temp.left
                else:
                    index -= temp.lcount +1
                    temp = temp.right
            self.infunction_delete(temp)

    def find_cumulate_sum(self, index):
        if index == -1:
            return 0
        ans = 0
        temp = self.root
        while True:
            if temp.lcount < index:
                ans += temp.lsum
                index -= temp.lcount +1
                temp = temp.right
            elif temp.lcount > index:
                temp = temp.left
            elif temp.lcount == index:
                ans += temp.lsum
                return ans

    def find_interval_sum(self, lp:int, rp:int):
        ans = self.find_cumulate_sum(rp) - self.find_cumulate_sum(lp)
        return ans

ele = tree_list()
n = int(input())
ans = []
for i in range(n):
    order = input().split()
    if order[0] == '1':
        ele.insert(int(order[1]), int(order[2]))
    elif order[0] == '2':
        ele.delete(int(order[1]) -1)
    else:
        ans.append(ele.find_interval_sum(int(order[1]) -2, int(order[2]) -1))
for i in ans:
    print(i)