import re

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
	temp = open("temp.txt", 'r')
	


	# Read the lines in temp
	#line = str(temp.readline()).rstrip('\n')
	#line = (line + ",")
	#while line:
	#	review = []
	#	for i in range(11):
	#		review.append(line)
			#line = (str(temp.readline()).rstrip('\n') + ",")
	#		line = temp.readline()
	#		line = str(line)
	#		line = line.rstrip('\n')
			#line = line + ","
	#	reviews.writelines(review)
		#for i in range(11):

	#	reviews.writelines("\n")
	#reviews.close()


	# create the review objects
	reviews_list = []
	single_r = []
	for line in temp.readlines():
		if line == '\n':
			reviews_list.append(Review(single_r))
			single_r = []
		else:
			single_r.append(line)
		
	# create "reviews.txt"	
	reviews = open("reviews.txt", 'w')
	j = 0
	for i in reviews_list:
		j = j + 1
		reviews.write(str(j)+","+i.pid +',"'+i.ptitle+'",'+i.price+","+i.userid+',"'+i.username+'",'+i.helpful+","+i.rscore+","+i.rtime+',"'+i.summary+'","'+i.ftext+'"\n')
	reviews.close()

	#pterms.txt: This file includes terms of length 3 or more characters 
	#extracted from product titles; a term is a consecutive sequence of 
	#alphanumeric and underscore '_' characters, i.e [0-9a-zA-Z_] or the 
	#character class \w in Perl or Python. The format of the file is as 
	#follows: for every term T in a product title of a review with id I, 
	#there is a row in this file of the form T',I where T' is the lowercase 
	#form of T. That means, terms must be converted to all lowercase before
	#writing them in this file. Here is the respective file for our sample 
	#file with 10 records.
	pterms = open("pterms.txt", 'w')
	j = 0
	for i in reviews_list:
		# for every product title:
		j =  j + 1
		product_title = i.ptitle
		# find every pterm:
		product_title = product_title.split(" ")
		for words in product_title:
			# take out non-alphanumeric characters
			# re.sub(r'\W+', '', your_string)
			words = words.lower()
			words = re.sub(r'\W+', ' ', words).split(" ")
			for word in words:
			# if it's long enough, write it to the file
				if len(word) > 2:
					# and write them to the file
					pterms.write(word+","+str(j)+"\n")
		
	pterms.close()


	# rterms.txt: This file includes terms of length 3 or more characters 
	# extracted from the fields review summary and review text. The file 
	# format and the way a term is defined is the as given above for the
	# file pterms.txt. 
	rterms = open("rterms.txt", 'w')
	j = 0
	for i in reviews_list:
		# for every product title:
		j =  j + 1
		summary = i.summary
		ftext = i.ftext
		# find every pterm:
		summary = summary.split(" ")
		ftext = ftext.split(" ")
		for words in summary:
			# take out non-alphanumeric characters
			words = words.lower()
			words = re.sub(r'\W+', ' ', words).split(" ")
			for word in words:
			# if it's long enough, write it to the file
				if len(word) > 2:
					# and write them to the file
					print(word+","+str(j))
					rterms.write(word+","+str(j)+"\n")
		
		for words in ftext:
			# take out non-alphanumeric characters
			words = words.lower()
			words = re.sub(r'\W+', ' ', words).split(" ")
			for word in words:
			# if it's long enough, write it to the file
				if len(word) > 2:
					# and write them to the file
					print(word+","+str(j))
					rterms.write(word+","+str(j)+"\n")

	rterms.close()


	# scores.txt: This file includes one line for each review record in the form 
	# of sc:I where sc is the review score and I is the review id. 
	scores = open("scores.txt", 'w')
	j = 0
	for i in reviews_list:
		j = j + 1
		scores.write(str(j)+":"+i.rscore+'\n')

	scores.close()



	

	# open the rest of the files to write to them

	# close our files
	txt.close()
	temp.close()

phase_one()

