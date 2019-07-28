from peep import peepy

class Pod :
    '''to hold a person and allow the pod to point to other pods'''

    def __init__(self, person = peepy(), A = None, B = None, id = 0):
        self.ID = id
        self.myPeep = person
        self.exitA = A
        self.exitB = B
        self.priorPods = []
        self.availableExits = []
        if self.myPeep == None:
            self.full = False
        else:
            self.full = True
        '''if self.exitA == None:
            exitA_ID = -1
        else:
            exitA_ID = self.exitA.ID
        if self.exitB == None:
            exitB_ID = -1
        else:
            exitB_ID = self.exitB.ID
        print("exit A = " + str(exitA_ID) + ", exit B = " + str(exitB_ID))'''

    def isFull(self):
        return self.full

    def addPriorPod(self, pod):
        self.priorPods.append(pod)

    def deliverPriors(self):
        return self.priorPods

    def alertPriors(self):
        if self.full == True:
            # remove self from the available list in each of my priors
        else:
            for pod in self.priorPods:
            pod.availableExits.append(self)     # append if i'm empty


    def describePod(self):
        if self.exitA == None:
            exitAID = "non-existant"
        else:
            exitAID = self.exitA.ID
        if self.exitB == None:
            exitBID = "non-existant"
        else:
            exitBID = self.exitB.ID
        if self.myPeep == None:
            mypeep = "V A C A N T"
        else:
            mypeep = self.myPeep.displayPeep()

        return "ID = " +str(self.ID)+ ",\texitA's ID = " +str(exitAID)+ ", \texitB's ID = " + str(exitBID) + ",\t\tperson = " + mypeep

class office:
    '''to hold lots of pods'''

    def __init__(self, name):
        self.name = name
        self.allPods = []

    def describeOffice(self):
        print("The office with name = <" + self.name + "> has the following pods:")
        for pod in self.allPods:
            print("\t" + pod.describePod())

    def addPod(self, pod):
        self.allPods.append(pod)



print("about to make a pod")

human = "chris"
little_pod = Pod(None, Pod(), Pod(), 27)
bigger_pod = Pod(peepy("efrain",982), little_pod, Pod(), 16)

bureaucrat = office("the tower")

bureaucrat.addPod(little_pod)
bureaucrat.addPod(bigger_pod)

bureaucrat.describeOffice()

print("little_pod is full?? ... " + str(little_pod.isFull()))
