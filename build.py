def relevancePage():
	top = open("/Users/Simonsays/Desktop/BootcampCite/templates/top.html").read();
	index = open("//Users/Simonsays/Desktop/BootcampCite/content/relevantIndex.html").read();
	bottom = open("/Users/Simonsays/Desktop/BootcampCite/templates/bottom.html").read();

	top = str(top);
	index = str(index);
	bottom = str(bottom);

	title = "Relevance"
	printingdata = open("/Users/Simonsays/Desktop/BootcampCite/docs/relevancePythonIndex.html", "w+");
	top = top.replace("{{title}}",f"{title}") 
	printingdata.write(top+"\n"+index+"\n"+bottom);
	printingdata.close();

def blogPage():
	top = open("/Users/Simonsays/Desktop/BootcampCite/templates/top.html").read();
	index = open("//Users/Simonsays/Desktop/BootcampCite/content/blogIndex.html").read();
	bottom = open("/Users/Simonsays/Desktop/BootcampCite/templates/bottom.html").read();

	top = str(top);
	index = str(index);
	bottom = str(bottom);

	title = "Blog"
	printingdata = open("/Users/Simonsays/Desktop/BootcampCite/docs/blogPythonIndex.html", "w+");
	top = top.replace("{{title}}",f"{title}") 
	printingdata.write(top+"\n"+index+"\n"+bottom);
	printingdata.close();


def indexPage():
	top = open("/Users/Simonsays/Desktop/BootcampCite/templates/top.html").read();
	index = open("//Users/Simonsays/Desktop/BootcampCite/content/index.html").read();
	bottom = open("/Users/Simonsays/Desktop/BootcampCite/templates/bottom.html").read();

	top = str(top);
	index = str(index);
	bottom = str(bottom);

	title = "Simon Tekeste"
	printingdata = open("/Users/Simonsays/Desktop/BootcampCite/docs/pythonIndex.html", "w+");
	top = top.replace("{{title}}",f"{title}") 
	printingdata.write(top+"\n"+index+"\n"+bottom);
	printingdata.close();

def main():
	indexPage();
	blogPage();
	relevancePage();

main();
