
def things_i_need(top, bottom):
	print("this will work!")
	i = 0

	url = [
 		"/Users/Simonsays/Desktop/BootcampCite/docs/index.html",
 		"/Users/Simonsays/Desktop/BootcampCite/docs/blogIndex.html",
		"/Users/Simonsays/Desktop/BootcampCite/docs/relevantIndex.html"
	 ]

	for x in url:
	 	printingdata = open(f"{x}", "w+")
	 	row  = another_thing(top, i)
	 	content = indexreader(i)
	 	printingdata.write(f"{row}"+"\n"+f"{content}"+"\n"+bottom);
	 	i+=1
	 	printingdata.close();

def another_thing(top,i):
	title = [
	 	"Simon Tekeste",
	 	"Blog",
	 	"Relevance"
	 ]

	t = title[i]

	row = titlechange(top,t)
	return row

def titlechange(top, t):
	# title = "Simon Tekeste"
	top = top.replace("{{title}}",f"{t}") 
	return top


def indexreader(i):
	index = [
	 	open("//Users/Simonsays/Desktop/BootcampCite/content/index.html").read(),
	 	open("//Users/Simonsays/Desktop/BootcampCite/content/blogIndex.html").read(),
	 	open("//Users/Simonsays/Desktop/BootcampCite/content/relevantIndex.html").read()
	 ]

	content = index[i]
	content = str(content)
	return content


def main():
	top = str(open("/Users/Simonsays/Desktop/BootcampCite/templates/top.html").read())
	bottom = str(open("/Users/Simonsays/Desktop/BootcampCite/templates/bottom.html").read())

	# webpage = [
	# 	indexPage(top),
	#  	blogPage(top),
	#  	relevancePage(top),
	#  ]

	# url = [
	#  	"/Users/Simonsays/Desktop/BootcampCite/docs/index.html",
	#  	"/Users/Simonsays/Desktop/BootcampCite/docs/blogIndex.html",
	# 	"/Users/Simonsays/Desktop/BootcampCite/docs/relevantIndex.html"
	#  ]

	# index = [
	#  	open("//Users/Simonsays/Desktop/BootcampCite/content/index.html").read(),
	#  	open("//Users/Simonsays/Desktop/BootcampCite/content/blogIndex.html").read(),
	#  	open("//Users/Simonsays/Desktop/BootcampCite/content/relevantIndex.html").read()
	#  ]

	 # title = [
	 # 	"Simon Tekeste",
	 # 	"Blog",
	 # 	"Relevance"
	 # ]

	things_i_need(top, bottom)
	 # row  = another_thing()
	 # content = indexreader()


	# i = 0
	# for x in url:
	# 	printingdata = open(f"{x}", "w+")
	# 	row = webpage[i]
	# 	content = index[i]
	# 	//content = str(content)
	# 	printingdata.write(f"{row}"+"\n"+f"{content}"+"\n"+bottom);
	# i+=1
	# printingdata.close();

	print("complete")


if __name__ == "__main__":
	main();
