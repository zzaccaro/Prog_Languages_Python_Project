### PYTHON FAMILY TREE PROJECT ###

### PERSON CLASS ###
class Person:
	def __init__(self, name, parent1, parent2):
		self.name = name
		self.parents = [parent1, parent2]
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
def E(name1, name2, name3 = ''):
    name1 = name1.lower()
    name2 = name2.lower()
    name3 = name3.lower()
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
    name1 = name1.lower()
    name2 = name2.lower()
    person1 = familytree.get(name1)
    person2 = familytree.get(name2)

    if person1 == None or person2 == None:
        return 'Person not in family tree'
    elif isSpouse(person1, person2):
        return 'spouse'
    elif isParent(person1, person2):
        return 'parent'
    elif isSibling(person1, person2):
        return 'sibling'
    elif isAncestor(person1, person2):
        return 'ancestor'
    elif isRelative(person1, person2):
        return 'relative'
    else:
        return 'unrelated'

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
    if eqIgnoreCase(person1.name, person2.name) and isAdamAndEve(person1.name):
        return True
    if checkParents(person1, person2):
        return True
    else:
        return False

# recursive method for isAncestor
def checkParents(target, p):
    if isAdamAndEve(p.name):
        return False
    elif eqIgnoreCase(p.parents[0], target.name):
        return True
    elif eqIgnoreCase(p.parents[1], target.name):
        return True
    elif checkParents(target, familytree.get(p.parents[0])):
        return True
    elif checkParents(target, familytree.get(p.parents[1])):
        return True
    else:
        return False

# boolean for cousin
def isCousin(person1, person2, cuzNum, remNum):
    if person1 in getCousins(person2, cuzNum, remNum):
        return True
    else:
        return False

# collects all cousins of particular person
def getCousins(person, numCousin, numRemoved):
    pList1 = [person]
    pList2 = []
    for i in range(numCousin):
        pList2 = []
        for x in pList1:
            pList2.extend(list(set(familytree.get(x).parents)))
        pList1 = []
        pList1.extend(pList2)

    pList2 = []
    for x in pList1:
        pList2.extend(list(set(getSiblings(familytree.get(x)))))
    pList1 = []
    pList1.extend(pList2)

    for j in range(numCousin + numRemoved):
        pList2 = []
        for x in pList1:
            pList2.extend(list(set(familytree.get(x).children)))
        pList1 = []
        pList1.extend(pList2)

    pList1 = list(set(pList1))
    return pList1


# boolean for relative
def isRelative(person1, person2):
    p1Rels = getAncestors(person1)
    p2Rels = getAncestors(person2)
    for p1 in p1Rels:
        for p2 in p2Rels:
            if eqIgnoreCase(p1, p2):
                return True
    return False

# X query
def X(name1, relation, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    person1 = familytree.get(name1)
    person2 = familytree.get(name2)

    if person1 == None or person2 == None:
        return 'Person not in family tree.'

    if type(relation) is list:
        if isCousin(name1, name2, relation[1], relation[2]):
            return 'Yes'
        else:
            return 'No'

    def spouse():
        if isSpouse(person1, person2):
            return 'Yes'
        else:
            return 'No'

    def parent():
        if isParent(person1, person2):
            return 'Yes'
        else:
            return 'No'

    def sibling():
        if isSibling(person1, person2):
            return 'Yes'
        else:
            return 'No'

    def ancestor():
        if isAncestor(person1, person2):
            return 'Yes'
        else:
            return 'No'

    def relative():
        if isRelative(person1, person2):
            return 'Yes'
        else:
            return 'No'

    def unrelated():
        if not isRelative(person1, person2):
            return 'Yes'
        else:
            return 'No'

    options = {'spouse': spouse,
             'parent': parent,
             'sibling': sibling,
             'ancestor': ancestor,
             'relative': relative,
             'unrelated': unrelated}

    for key, value in options.items():
        if eqIgnoreCase(key, relation):
            return value()

    return 'Invalid input.'

# W query
def W(relation, name):
    name = name.lower()
    p = familytree.get(name)
    allPeople = []

    if p == None:
        return 'Person not in family tree.'

    if type(relation) is list:
        allPeople = getCousins(name, relation[1], relation[2])
        allPeople.sort()
        allPeople = [x.capitalize() for x in allPeople]
        return allPeople

    def spouse():
        return p.spouse

    def parent():
        people = []
        if isAdamAndEve(p.name):
            people.append(p.name)
        else:
            people = p.parents
        return people

    def sibling():
        return getSiblings(p)

    def ancestor():
        return getAncestors(p)

    def relative():
        return getRelatives(p)

    def unrelated():
        return getStrangers(p)

    options = {'spouse': spouse,
               'parent': parent,
               'sibling': sibling,
               'ancestor': ancestor,
               'relative': relative,
               'unrelated': unrelated}

    for key, value in options.items():
        if eqIgnoreCase(key, relation):
            allPeople = value()

    allPeople.sort()
    allPeople = [x.capitalize() for x in allPeople]

    return allPeople

# collects all siblings of particular person
def getSiblings(p):
    siblings = []
    for key, value in familytree.items():
        if isSibling(p, value):
            siblings.append(key)
    return siblings

# collects all ancestors of particular person
def getAncestors(p):
    ancestors = []
    for key, value in familytree.items():
        if checkParents(value, p):
            ancestors.append(key)
    if ancestors.__sizeof__() == 0:
        ancestors.append(p.name)
    return ancestors

# collects all relatives of particular person
def getRelatives(p):
    relatives = []
    for key, value in familytree.items():
        if isRelative(value, p):
            relatives.append(key)
    return relatives

# collects all people who are unrelated to particular person
def getStrangers(p):
    strangers = []
    for key, value in familytree.items():
        if not isRelative(value, p) and not isSpouse(value, p):
            strangers.append(key)
    return strangers

# main method
def main():
    E('Adam', 'Eve', 'Bob')
    E('Adam', 'Eve', 'Stacy')
    E('Bob', 'Mary', 'Zach')
    E('Stacy', 'Andrew', 'Matt')
    E('Matt', 'Liz', 'Danny')
    E('Steve', 'Taylor', 'Greg')
    E('Chris', 'Becky')

    print(R('Adam', 'Eve'))
    print(R('Adam', 'Bob'))
    print(R('Adam', 'zach'))
    print(W('spouse', 'Adam'))
    print(W('parent', 'Bob'))
    print(X('Steve', 'spouse', 'mary'))
    print(X('Adam', 'ancestor', 'zach'))
    print(R('adam', 'greg'))
    print(W(['cousin', 1, 1], 'zach'))
    print(W('spouse', 'becky'))



if  __name__ =='__main__':main()