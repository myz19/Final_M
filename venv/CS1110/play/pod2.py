from peep import peepy

class Pod :
    '''to hold a person and allow the pod to point to other pods'''

    numMade = 0 ## a class variable

    def __init__(self, person = None, A = None, B = None):
        self.myPeep = person
        self.exitA = A
        self.exitB = B
        self.priorPods = [ ]
        self.availableExits = [ ]
        if self.myPeep == None:     # can modify this later on if we have a list of peeps in a pod
            self.Full = False
            self.Empty = True
        else:
            self.Full = True
            self.Empty = False

        self.ID = Pod.numMade
        Pod.numMade += 1

    def isFull(self ):
        return self.Full

    def setPeep(self, human):
        self.myPeep = human
        self.alertPriors()

    def emptyPeep(self):
        self.myPeep = None
        self.alertPriors()

    def addPriorPod(self, pod):
        self.priorPods.append(pod)

    def deliverPriorPods(self):
        return self.priorPods

    def alertPriors(self):
        for pod in self.priorPods:
            if self.Full:  ### remove self from the available list in each of my priors
                if self in pod.availableExits: ## don't remove if it's not there!!!
                    pod.availableExits.remove(self)
            else: ### append self to the available list in each of my priors
                if self not in pod.availableExits: ## don't append it if it's already there!!
                    pod.availableExits.append(self)

    '''def pickRandomExit(self):
        use randint to pick from the lsit of available exits
        # use randint inside range(len(self.availableExits)) to return the pod corresponding to that exit -- note that exits are pods'''

    def pickExit(self):
        '''pick the first one from the list of available Exits'''
        if len(self.availableExits) == 0:
            return None     # check for this if called since we have no exceptions
        else:
            return self.availbleExits[0]

    def movePeep(self):
        '''if self has a peep, move them to a chosen new pod'''
        # first check that self has a peep
        # use pickExit to pick a pod (say X) from available exits to move peep to
        # use X.setPeep to set that pod's peep to be self's peep
        # change setPeep so that it automatically calls alertPriors (now occupied)
        # use self.emptyPeep to remove self.peep
        # write self.emptyPeep, and make it include alertPriors

        if self.Empty:
            return
        P = self.myPeep
        X = self.pickExit()
        if X == None:
            return
        # at this stage we have a peep P to move and a pod X to move them to
        X.setPeep(P)
        self.emptyPeep()

    def describePod(self):
        if self.exitA == None:
            exitAID = "-1"
        else:
            exitAID = self.exitA.ID
        if self.exitB == None:
            exitBID = "-1"
        else:
            exitBID = self.exitB.ID
        if self.myPeep == None:
            mypeep = "V A C A N T"
        else:
            mypeep = self.myPeep.displayPeep()
        return "ID = " +str(self.ID)+ ", \texitA's ID = " +str(exitAID)+ \
               ", \texitB's ID = " +str(exitBID)+ ", \t\tperson = " +mypeep


class universe:
    '''to hold lots of pods'''

    def __init__(self, name):
        self.name = name
        self.allPods = [ ]

    def describeUniverse(self):
        print("The universe with name = <" + self.name + "> has the following pods:")
        for pod in self.allPods:
            print("\t" + pod.describePod())

    def addPod(self, pod):
        self.allPods.append(pod)

    def findPod(self, id):
        '''given the integer id return the pod with that id'''
        notFound = True
        p = 0
        while notFound and p < len(self.allPods):
            if self.allPods[p].ID == id:
                notFound = False
            else:
                p+=1
        if notFound:
            return None     # didn't find it
        else:
            return self.allPods[p]

    def createlinks(self, fromID, toID):
        '''IF the pod with fromID has any available exits, ie exitA and exitB aren't already set
            THEN make the pod with toID to be an exit from the pod with fromID
            If no availble exits, complain'''
        # use findPod twice to get the FROM pod and the TO pod, check if either == None, complain if so
        # choose the first of exitA and exitB that hasn't been set, if non available, complain
        # set the TO pod as that exit (found above) for the FROM pod
        # add the FROM pod as a prior of the TO pod using addPriorPod
        # call the TO pod's alertPriors to ensure that the FROM pod's available exits list is correct


    def deleteLinks(self, fromID):
        '''deletes all exits from the pod found using findPod (fromID)
            useful in case of messing up when using createLinks'''
        # don't just delte the links, there might be an effect on lists of priors for these exits
        # make sure to fix the list of available exits
###+++++++++++++++++++++++++++++++++++++++++++++

print("\nAbout to make lots of pods -- note that an ID = -1 means it doesn't exist\n")

allPods = []
for i in range(20):
    allPods.append(Pod())

bureaucrat = universe("the tower")
for pod in allPods:
    bureaucrat.addPod(pod)

# bureaucrat.describeUniverse()
# print("\tThat was the universe before anything happened!!\n")

print("\nAbout to make lots of peeps\n")
allPeeps = []
for human in range(30):
    allPeeps.append(peepy())

for i in range( len(bureaucrat.allPods) ):
    bureaucrat.allPods[i].setPeep(allPeeps[i])

theirName = allPeeps[3].getName()
directName = allPeeps[3].myname

print(">>>>>> that name = " + theirName + ", and direct name = " + directName)
# bureaucrat.describeUniverse()
# print("\tThat was the universe after adding people!!\n")

### on Monday we'll play with moving people around ....