class Node:
    def __init__(self,item):
        self.val=item
        self.left=None
        self.right=None
 
 
class BinaryTree:
    def __init__(self):
        self.head=Node(None)
 
 
    def insert(self,item):#루트존재여부 확인
        if self.head.val is None:
            self.head.val = item
        else:
            self.addnode(self.head,item)
 
    def addnode(self,cur,item):
        if cur.val>item:#새로운 인자가 현재보다 작다면 왼쪽
            if cur.left!=None:#왼쪽이 비어있지않다면
                self.addnode(cur.left,item)
            else:#비어있다면 넣어준다.
                cur.left=Node(item)
        elif cur.val<item:#새로운 인자가 현재보다 크다면 오른쪽
            if cur.right!=None:
                self.addnode(cur.right,item)
            else:
                cur.right=Node(item)
    def postorder(self,cur):#후위순회
        if cur.left != None:
            self.postorder(cur.left)
        if cur.right != None:
            self.postorder(cur.right)
        print(cur.val)
 
 
import sys
sys.setrecursionlimit(10**9)
 
 
b_tree=BinaryTree()#초기화
count = 0
while count <= 10000:
    try:
        num = int(input())
    except:break
    b_tree.insert(num)
    count += 1
 
b_tree.postorder(b_tree.head)


# 이번엔 이진트리이다.

# 루트와 모든 원소만 알고있다면 트리를 구성할수있다.

# 전위순회의 가장 첫원소는 루트이다.

# 트리를 구한뒤 후위순회를 통해 출력해보자.

# 입력방식은 조금 특이하다. 예외처리를 이용해 처리하자.