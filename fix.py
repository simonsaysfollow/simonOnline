def relevancePage(top, bottom):
	index = open("//Users/Simonsays/Desktop/BootcampCite/content/relevantIndex.html").read();
	index = str(index);


	title = "Relevance"
	# printingdata = open("/Users/Simonsays/Desktop/BootcampCite/docs/relevantIndex.html", "w+");
	top = top.replace("{{title}}",f"{title}") 
	# printingdata.write(top+"\n"+index+"\n"+bottom);
	# printingdata.close();
	return top

def blogPage(top, bottom):
	index = open("//Users/Simonsays/Desktop/BootcampCite/content/blogIndex.html").read();
	index = str(index);

	title = "Blog"
	# printingdata = open("/Users/Simonsays/Desktop/BootcampCite/docs/blogIndex.html", "w+");
	top = top.replace("{{title}}",f"{title}") 
	# printingdata.write(top+"\n"+index+"\n"+bottom);
	# printingdata.close();
	return top


def indexPage(top, bottom):
	index = open(f"//Users/Simonsays/Desktop/BootcampCite/content/index.html").read();
	index = str(index);

	title = "Simon Tekeste"
	# printingdata = open(f"{url}", "w+")
	top = top.replace("{{title}}",f"{title}") 
	# printingdata.write(top+"\n"+index+"\n"+bottom);
	# printingdata.close();
	return top

def main():
	top = open("/Users/Simonsays/Desktop/BootcampCite/templates/top.html").read();
	bottom = open("/Users/Simonsays/Desktop/BootcampCite/templates/bottom.html").read();
	top = str(top);
	bottom = str(bottom);

	webpage = [
		indexPage(top, bottom),
	 	blogPage(top, bottom),
	 	relevancePage(top, bottom),
	 ]

	url = [
	 	"/Users/Simonsays/Desktop/BootcampCite/docs/index.html",
	 	"/Users/Simonsays/Desktop/BootcampCite/docs/blogIndex.html",
		"/Users/Simonsays/Desktop/BootcampCite/docs/relevantIndex.html"
	 ]

	i = 0

	for x in url:
		printingdata = open(f"{x}", "w+")
		row = webpage[i]
		printingdata.write(f"{row}"+"\n") #+index+"\n"+bottom);
		i+=1
	printingdata.close();

	print("complete")


if __name__ == "__main__":
	main();
