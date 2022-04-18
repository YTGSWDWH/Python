import operator
class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild
    
    def setRootVal(self, obj):
        self.key = obj
    
    def getRootVal(self):
        return self.key
    
def buildParseTree(fpexp):
    fplist = fpexp.split()      # 表达式分解为单词表
    pStack = []                 # 用列表来实现栈
    eTree = BinaryTree('')      # 创建空树
    pStack.append(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')  # 创建左节点
            pStack.append(currentTree)
            currentTree = currentTree.getLeftChild()    # 当前节点下降
        elif i not in ['+', '-', '*', '/', ')']:    # 读入数字
            currentTree.setRootVal(int(i))  # 当前节点设置为读入的数字
            parent = pStack.pop()   # 上升为父节点
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)   # 当前节点设置为操作符
            currentTree.insertRight('') # 创建右节点
            pStack.append(currentTree)
            currentTree = currentTree.getRightChild()   # 当前节点下降
        elif i == ')':
            currentTree = pStack.pop()  # 上升到父节点
        else:
            raise ValueError
    return eTree

def evaluate(parseTree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()
    
    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()

fpexp = "( 5 * ( 2 + 8 ) )"
eTree = buildParseTree(fpexp)
print(evaluate(eTree))