import sys,fileinputimport random as rimport mathtau=0.01InputSize=2OutputSizeX=4OutputSizeY=4InitialLR=0.1LRDecay=0.001#1-math.exp(-1/tau)InitialNbdWidth=0.1#0.1NbdWidthDecay=0.001#1-math.exp(-1/tau)debug=0#read filef = open('data24.txt')inputVec=[[float(i) for i in line.strip().split()] for line in f]f.close()#set neuron output settingsneuronW=4neuronH=2neuronN=neuronW*neuronH#init weight matrixweight=[[0,0]]*neuronN#for i in xrange(len(weight)):#	weight[i]=[[0,0]]*len(inputVec)#initalizing weights between -1.0 and 1.0for i in xrange(neuronN):	#for j in xrange(len(inputVec)):	weight[i]=[r.uniform(-0.1,0.1),r.uniform(-0.1,0.1)]smallestVal=100000000000smallestJ=0m=[]LR=InitialLRh=1nbdwidth=InitialNbdWidthdecayC=0.1f=open('neurondebug.txt','w')#print weightfor k in xrange(1,5000):	r.shuffle(inputVec)	if debug==1:				f.write("Epoch: "+str(k)+"\n")		print "Epoch: ",k	for i in xrange(len(inputVec)):		if debug==1:			f.write("ith vector: "+str(i)+"\n")			print "ith vector: ",i		#competition		m=[]		for j in xrange(neuronN):			#print (weight[j][0]-(inputVec[i][0])**2)			m.append(math.sqrt(((weight[j][0]-inputVec[i][0])**2) + (weight[j][1]-inputVec[i][1])**2))			#print m			if(m[-1]<smallestVal):				smallestJ=j				smallestVal=m[-1]										for j in xrange(neuronN):			#check if weightj is in the neighoubhood of winning neuron			#print smallestJ			#print (weight[smallestJ][0])			d=math.sqrt(((weight[smallestJ][0]-weight[j][0])**2) + ((weight[smallestJ][1]-weight[j][1])**2))			if debug==1:				f.write("j: "+str(j)+" d: "+str(d)+" wsmallest: "+str(weight[smallestJ][0])+" wj: "+str(weight[j][0])+" j: "+str(j)+" smallej: "+str(smallestJ)+"\n")				print "j: ",j,"d: ",d, weight[smallestJ][0],weight[j][0],j,smallestJ			#print math.sqrt(((weight[smallestJ][0]-weight[j][0])**2) + ((weight[smallestJ][1]-weight[j][1])**2))			if(d<nbdwidth and smallestJ!=j):				#cal d												#cal h				h=math.exp(-(d**2)/(2*(nbdwidth**2)))								#cal LR				#print h				#adjust weights				weight[j][0]=weight[j][0]+(LR*h*(inputVec[i][0]-weight[j][0]))				weight[j][1]=weight[j][1]+(LR*h*(inputVec[i][1]-weight[j][1]))				#print weight[j]			print LR		#update winners weight		weight[smallestJ][0]=weight[smallestJ][0]+(LR*h*(inputVec[i][0]-weight[smallestJ][0]))		weight[smallestJ][1]=weight[smallestJ][1]+(LR*h*(inputVec[i][1]-weight[smallestJ][1]))				#reset winner		smallestVal=100000000000		smallestJ=0					#change LR	LR=LR*(1-LRDecay)			#change nbdwidth	nbdwidth=nbdwidth*(1-NbdWidthDecay)	if nbdwidth <= 0.000000000000000001:		nbdwidth=0.000000000000000000001		#change LRdecay	#LRDecay=1-math.exp(-1/decayC)	#change nbdwidthDecay	#NbdWidthDecay=1-math.exp(-1/decayC)	f.close()	#outputf=open('neuron.txt','w')for j in xrange(neuronN):	f.write(str(weight[j][0])+" "+str(weight[j][1])+"\n")f.close()#print smallestJ,smallestVal#smallestVal=100000000000#smallestJ=0	#adjust weights