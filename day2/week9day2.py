"""
#2.)


class Node:
	
	def __init__(self, x):
		
		self.data = x
		self.left = None
		self.right = None

def buildUtil(inn, post, innStrt, innEnd):
	
	global mp, index
	
	if (innStrt > innEnd):
		return None

	
	curr = post[index]
	node = Node(curr)
	index -= 1

	
	if (innStrt == innEnd):
		return node

	
	iIndex = mp[curr]

	
	node.right = buildUtil(inn, post,
						iIndex + 1, innEnd)
	node.left = buildUtil(inn, post, innStrt,
						iIndex - 1)

	return node


def buildTree(inn, post, lenn):
	
	global index
	
	
	
	for i in range(lenn):
		mp[inn[i]] = i
		
	
	index = lenn - 1
	return buildUtil(inn, post, 0, lenn - 1)


def preOrder(node):
	
	if (node == None):
		return
		
	print(node.data, end = " ")
	preOrder(node.left)
	preOrder(node.right)


if __name__ == '__main__':
	
	inn = [ 5,4,4,3.5,7 ]
	post = [7,5,4,4,3,5 ]
	n = len(inn)
	mp, index = {}, 0

	root = buildTree(inn, post, n)

	print("Preorder of the constructed tree :")
	preOrder(root)

"""
#3.)


class GFG:
	
	
	class Node:
		def __init__(self,n,data):
			
			self.children = [None]*n
			self.data = data
	
	
	def inorder(self, node):
		if node == None:
			return
		
		
		total = len(node.children)
		
		
		for i in range(total-1):
			self.inorder(node.children[i])
		
		
		print(node.data,end=" ")
		
		
		self.inorder(node.children[total-1])
	
	
	def main(self):
		
		
		n = 3
		root = self.Node(n, 1)
		root.children[0] = self.Node(n, 2)
		root.children[1] = self.Node(n, 3)
		root.children[2] = self.Node(n, 4)
		root.children[0].children[0] = self.Node(n, 5)
		root.children[0].children[1] = self.Node(n, 6)
		root.children[0].children[2] = self.Node(n, 7)
		
		self.inorder(root)
		
ob = GFG() 
ob.main() 






