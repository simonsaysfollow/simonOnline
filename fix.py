def relevancePage(top, bottom):
	# top = open("/Users/Simonsays/Desktop/BootcampCite/templates/top.html").read();
	index = open("//Users/Simonsays/Desktop/BootcampCite/content/relevantIndex.html").read();
	# bottom = open("/Users/Simonsays/Desktop/BootcampCite/templates/bottom.html").read();

	# top = str(top);
	index = str(index);
	# bottom = str(bottom);

	title = "Relevance"
	printingdata = open("/Users/Simonsays/Desktop/BootcampCite/docs/relevantIndex.html", "w+");
	top = top.replace("{{title}}",f"{title}") 
	printingdata.write(top+"\n"+index+"\n"+bottom);
	printingdata.close();

def blogPage(top, bottom):
	# top = open("/Users/Simonsays/Desktop/BootcampCite/templates/top.html").read();
	index = open("//Users/Simonsays/Desktop/BootcampCite/content/blogIndex.html").read();
	# bottom = open("/Users/Simonsays/Desktop/BootcampCite/templates/bottom.html").read();

	# top = str(top);
	index = str(index);
	# bottom = str(bottom);

	title = "Blog"
	printingdata = open("/Users/Simonsays/Desktop/BootcampCite/docs/blogIndex.html", "w+");
	top = top.replace("{{title}}",f"{title}") 
	printingdata.write(top+"\n"+index+"\n"+bottom);
	printingdata.close();


def indexPage(top, bottom):
	# top = open("/Users/Simonsays/Desktop/BootcampCite/templates/top.html").read();
	index = open("//Users/Simonsays/Desktop/BootcampCite/content/index.html").read();
	# bottom = open("/Users/Simonsays/Desktop/BootcampCite/templates/bottom.html").read();

	# top = str(top);
	index = str(index);
	# bottom = str(bottom);

	title = "Simon Tekeste"
	printingdata = open("/Users/Simonsays/Desktop/BootcampCite/docs/index.html", "w+")
	top = top.replace("{{title}}",f"{title}") 
	printingdata.write(top+"\n"+index+"\n"+bottom);
	printingdata.close();

def main():
	top = open("/Users/Simonsays/Desktop/BootcampCite/templates/top.html").read();
	bottom = open("/Users/Simonsays/Desktop/BootcampCite/templates/bottom.html").read();
	top = str(top);
	bottom = str(bottom);


	indexPage(top, bottom);
	blogPage(top, bottom);
	relevancePage(top, bottom);
	print("complete")

if __name__ == "__main__":
	main();
