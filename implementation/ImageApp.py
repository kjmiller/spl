import re
import APIExample

class ImageExample(APIExample.Example):
	def __init__(self, inputFileLine, params,id):
		self.params = params
		self.h = []
		self.psiCache = ()
		self.id = id
		self.processFile(inputFileLine)
		#self.load(inputfile)

	def findMVC(self,w, givenY, givenH):
		maxScore= 0
		bestH = givenH
		bestY = givenY
		for labelY in self.params.ylabels:
			(h, score, vec) = self.highestScoringLV(w,label)
			totalScore = self.delta(givenY, labelY) + score
			if totalScore> maxScore:
				bestH = h
				eestY = labelY
		const = self.delta(givenY, labelY)
		vec = self.psi(bestY, bestH).minus(psi(givenY, givenH))
		return (const,vec)
	
	def findScoreAllClasses(self, w):
		results = {}
		for label in self.params.ylabels:
			(h, score, vec) = self.highestScoringLV(w, label)
			results[label] = score
		return results

	def processFile(self, inputFileLine):
		objects  = inputFileLine.split()
		self.fileUUID= objects[0]
		self.width = objects[2]
		self.height = objects[1]

		self.xs = []
		self.ys = []
		self.values = []

		for kernelName in self.params.kernelIndices:
			self.loadData(kernelNum)

	def loadData(self, kernelName):
		index = len(self.xs)
		assert(index == self.ys)
		assert(index == self.values)

		self.xs.append([])
		self.ys.append([])
		self.values.append([])
		inputFile = open("/afs/cs.stanford.edu/u/rwitten/scratch/mkl_features/%s/%s_spquantized_1000_%s.mat"%(kernelName,self.fileUUId, kernelName),"r")
		
		inputFile.next() #we don't care how many indices are in the file		
		inputFile.next() #we already know the image size
		for line in inputFile:
			data = re.match('\((\d+),(\d+)\):(\d+)', line).groups()
			self.ys[index].append(int(data[0]))
			self.xs[index].append(int(data[1]))
			self.values[index].append(int(data[2]-1))

 
	# this returns a psi object
	def psi(self, y,h):
		if (y,h) in self.psiCache:
			return self.psiCache[(y,h)]

		result = PsiObject(self.params)
		for kernelNum in range(params.numKernels):
			for index in range(self.xs[kernelNum]):
				result.setEntry(y,kernelNum,self.values(index))
		
		self.psiCache[(y,h)] = result
		return result

	def highestScoringLV(self,w, labelY):
		maxScore = -Inf
		for latentH in self.hlabels:
			score= w.dot(psi(labelY,latentH))
			if score> maxScore:
				bestH= latentH

		return (bestH, score, psi(labelY, bestH))