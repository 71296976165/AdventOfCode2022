print("Enter a source file:")
loc = input()
f = open(loc, "r")

# To represent this structure, I need a data structure which can act like a directory
# The ideal is if I have some sort of tree structure I can build
# Y'know what, let's just make a tree object.

class Tree:
    def __init__(self, name, data = 0,parent = None):
        self.children = []
        self.parent = parent
        self.name = name
        self.data = data
    
    def print(self):
        for x in self.children:
            x.print()
        if self.parent != None:
            print(self.isDirectory(),self.name, self.data, self.parent.name)
        else:
            print(self.isDirectory(), self.name, self.data, "root")
    
    def getVal(self):
        return self.data
    
    def getTotalVals(self):
        val = 0
        for x in self.children:
            val += x.getVal()
        val += self.data
        return val
    
    def addChild(self, other):
        self.children.append(other)
        other.parent = self
    
    def getParent(self):
        return self.parent
    
    def getChild(self, name):
        for x in self.children:
            if(x.name == name):
                return x
        print("child not found")
        return self
    
    def isDirectory(self):
        if len(self.children) == 0:
            return "file"
        return "dir"
        

root = Tree("root")
root.addChild(Tree("/"))
currentTree = root

for line in f:
    line = line.strip('\n')
    commands = line.split()
    if commands[0] == '$':
        # this is a command - we need to figure out if this is entering a child leaf, or listing
        if commands[1] == "cd":
            if commands[2] == "..":
                currentTree.data = currentTree.getTotalVals()
                currentTree = currentTree.getParent()
            else:
                currentTree = currentTree.getChild(commands[2])
    else:
        if commands[0] == "dir":
            currentTree.addChild(Tree(commands[1],0,currentTree))
        else:
            currentTree.addChild(Tree(commands[1],int(commands[0]),currentTree))

while currentTree != root:
    currentTree.data = currentTree.getTotalVals()
    currentTree = currentTree.getParent()

finalChild = currentTree.getChild('/')
val = 0
for x in finalChild.children:
    val += x.data

finalChild.data = val

f.close()

import sys

stdout_origin = sys.stdout

treefile = loc.strip(".txt") + "tw.txt"
w = open(treefile, "w")

sys.stdout = w

currentTree.print()

w.close()

sys.stdout = stdout_origin

file = open(treefile, "r")

directorySize = 0

for line in file:
    line = line.strip('\n')
    dir = line.split()
    if dir[0] == "dir":
        dirsize = int(dir[2])
        if dirsize < 100000:
            directorySize += dirsize

print(directorySize)

file.close()
# just to clean up after ourselves