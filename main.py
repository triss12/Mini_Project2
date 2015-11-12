class Review:
	"""
	Because why the fuck not?
	"""
	def __init__(self, attributes):
		self.pid = attributes[0]
		self.ptitle = attributes[1]
		self.price = attributes[2]
		self.userid = attributes[3]
		self.username = attributes[4]
		self.helpful = attributes[5]
		self.rscore = attributes[6]
		self.rtime = attributes[7]
		self.summary = attributes[8]
		self.ftext = attributes[9]

def phase_one():
	"""
	 Read the file "small-date.txt" and write it into 
	 the four files described in the assignment spec
	 """

	#filename = input("Enter the name of the file: ")
	# or no!

	txt = open("small-data.txt")
	
	# Create a new file, replacing " with &quot
	# and \ with \\
	temp = open("temp.txt", 'w')
	temp.write(txt.read().replace('"', '&quot').replace("\\", "\\\\"))
	temp.close()
	temp = open("temp.txt")

	# create the review objects
	reviews_list = []
	for line in temp.readlines():
		review = []
		for i in range(10):
			review.append(line)
		reviews_list.append(Review(review))

	# Open reviews to write to it

	# We probably want to open it in buffering mode, 
	# If we're going to change the input around
	# Actually I have no idea what buffering mode is
	reviews = open("reviews.txt", 'w')
	reviews.write(temp.read())
	

	# open the rest of the files to write to them
	pterms = open("pterms.txt", 'w')
	rterms = open("rterms.txt", 'w')
	scores = open("scores.txt", 'w')

	# close our files
	txt.close()
	temp.close()
	reviews.close()
	pterms.close()
	rterms.close()
	scores.close()

phase_one()


