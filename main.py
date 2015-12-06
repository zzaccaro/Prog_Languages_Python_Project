### PYTHON FAMILY TREE PROJECT ###

### PERSON CLASS ###
class Person:
	def __init__(self, name, parents = []):
		self.name = name
		self.parents = parents
		self.children = []
		self.spouse = []

	def addChild(self, child):
		self.children.append(child)

	def addParent(self, parent):
		self.parents.append(parent)

	def setParents(self, parent1, parent2):
		self.parents = []
		self.parents.append(parent1)
		self.parents.append(parent2)

	def addSpouse(self, spouse):
		if spouse not in self.spouse:
			self.spouse.append(spouse)


### MAIN ###

# Helper method for comparing strings
def eqIgnoreCase(s1, s2):
    return s1.lower() == s2.lower()

familytree = {}

# E query
def E(name1, name2, name3):
    checkOrAddToGraph(name1, name1, name1)
    checkOrAddToGraph(name2, name2, name2)
    checkOrAddToGraph(name3, name1, name2)

    familytree.get(name1).addSpouse(name2)
    familytree.get(name2).addSpouse(name1)

def checkOrAddToGraph(nodeName, parent1, parent2):
    if nodeName not in familytree.keys():
        familytree[nodeName] = Person(nodeName, parent1, parent2)
    elif isAdamAndEve(nodeName):
        familytree[nodeName].setParents(parent1, parent2)

    if not eqIgnoreCase(parent1, parent2):
        familytree.get(parent1).addChild(nodeName)
        familytree.get(parent2).addChild(nodeName)

def isAdamAndEve(name):
    if name in familytree.get(name).parents:
        return True
    else:
        return False

# R query
def R(name1, name2):
    person1 = familytree.get(name1)
    person2 = familytree.get(name2)

    if person1 == None or person2 == None:
        return 'Person not in family tree'
    elif isSpouse(person1, person2):
        return 'Spouse'
    elif isParent(person1, person2):
        return 'Parent'
    elif isSibling(person1, person2):
        return 'Sibling'
    elif isAncestor(person1, person2):
        return 'Ancestor'
    elif isRelative(person1, person2):
        return 'Relative'
    else:
        return 'Unrelated'

# boolean for spouse
def isSpouse(person1, person2):
    if person1.name in person2.spouse:
        return True
    else:
        return False

# boolean for parent
def isParent(person1, person2):
    if eqIgnoreCase(person1.name, person2.name):
        return False
    if person1.name in person2.parents:
        return True
    else:
        return False

# boolean for sibling
def isSibling(person1, person2):
    if isAdamAndEve(person1.name):
        return False
    if isAdamAndEve(person2.name):
        return False

    p1parents = person1.parents
    p2parents = person2.parents
    p1parents.sort()
    p2parents.sort()
    return p1parents == p2parents

# boolean for ancestor
def isAncestor(person1, person2):
    return True

# recursive method for isAncestor
def checkParents(target, p):
    return True

# boolean for cousin
def isCousin(person1, person2):
    return True

# collects all cousins of particular person
def getCousins(person, numCousin, numRemoved):
    return True

# boolean for relative
def isRelative(person1, person2):
    return True

# main method
def main():
    adam = Person('Adam')
    eve = Person('Eve')
    bob = Person('Bob', ['Adam', 'Eve'])

    familytree['Adam'] = adam
    familytree['Eve'] = eve
    familytree['Bob'] = bob

    s1 = 'Adam'
    s2 = 'adam'

    list1 = ['Adam', 'Eve']
    list2 = ['Eve', 'Adam']
    list1.sort()
    list2.sort()
    print(list1 == list2)


if  __name__ =='__main__':main()