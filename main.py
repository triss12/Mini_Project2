class Review:
	"""
	Because why the fuck not?

	Now without the tags inside of the attributes!
	Or trailing newlines!
	"""
	def __init__(self, attributes):
		self.pid = attributes[0].split(' ', 1)[1].rstrip('\n')
		self.ptitle = attributes[1].split(' ', 1)[1].rstrip('\n')
		self.price = attributes[2].split(' ', 1)[1].rstrip('\n')
		self.userid = attributes[3].split(' ', 1)[1].rstrip('\n')
		self.username = attributes[4].split(' ', 1)[1].rstrip('\n')
		self.helpful = attributes[5].split(' ', 1)[1].rstrip('\n')
		self.rscore = attributes[6].split(' ', 1)[1].rstrip('\n')
		self.rtime = attributes[7].split(' ', 1)[1].rstrip('\n')
		self.summary = attributes[8].split(' ', 1)[1].rstrip('\n')
		self.ftext = attributes[9].split(' ', 1)[1].rstrip('\n')


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
	single_r = []
	for line in temp.readlines():
		if line == '\n':
			reviews_list.append(Review(single_r))
			single_r = []
		else:
			single_r.append(line)
		
	print(len(reviews_list))

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


