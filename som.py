import sys,fileinputimport random as rimport math#read filef = open('data24.txt')inputVec=[[float(i) for i in line.strip().split()] for line in f]f.close()#set neuron output settingsneuronW=4neuronH=4neuronN=neuronW*neuronH#init weight matrixweight=[[0,0]]*neuronN#for i in xrange(len(weight)):#	weight[i]=[[0,0]]*len(inputVec)#initalizing weights between -1.0 and 1.0for i in xrange(neuronN):	#for j in xrange(len(inputVec)):	weight[i]=[r.uniform(-1.0,1.0),r.uniform(-1.0,1.0)]smallestVal=100000000000smallestJ=0m=[]LR=1h=1nbdwidth=1LRDECAY=0.2NbdWidthDecay=0.2for k in xrange(5000):	r.shuffle(inputVec)	for i in xrange(len(inputVec)):		#competition		for j in xrange(neuronN):			#print (weight[j][0]-(inputVec[i][0])**2)			m.append(math.sqrt(((weight[j][0]-inputVec[i][0])**2) + (weight[j][1]-inputVec[i][1])**2))			#print m			if(m[-1]<smallestVal):				smallestJ=j				smallestVal=m[-1]												d=math.sqrt(((weight[smallestJ][0]-inputVec[i][0])**2) + (weight[smallestJ][1]-inputVec[i][1])**2)				for j in xrange(neuronN):			#cal d									#cal h			h=math.exp((-d**2)/(2*nbdwidth**2))			#cal LR			#print h			#adjust weights			weight[j][0]=weight[j][0]+(LR*h*(inputVec[i][0]-weight[j][0]))			weight[j][1]=weight[j][1]+(LR*h*(inputVec[i][1]-weight[j][1]))			#change LR	LR=LR*(1-LRDECAY)			#change nbdwidth	nbdwidth=nbdwidth*(1-NbdWidthDecay)	#outputf=open('neuron.txt','w')for i in xrange(len(inputVec)):	for j in xrange(neuronN):		f.write(str(weight[j][0])+" "+str(weight[j][1])+"\n")f.close()#print smallestJ,smallestVal#smallestVal=100000000000#smallestJ=0	#adjust weights