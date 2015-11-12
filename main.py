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
	emp = open("temp.txt")

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


