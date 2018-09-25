
def things_i_need(top, bottom, url=[],title=[],index=[]):
	i = 0
	for x in url:
	 	printingdata = open(f"{x}", "w+")
	 	row  = another_thing(top, i, title)
	 	content = indexreader(i, index)
	 	printingdata.write(f"{row}"+"\n"+f"{content}"+"\n"+bottom);
	 	i+=1
	 	printingdata.close();

def another_thing(top,i, title=[]):
	t = title[i]

	row = titlechange(top,t,)
	return row

def titlechange(top, t):
	top = top.replace("{{title}}",f"{t}") 
	return top


def indexreader(i, index=[]):
	content = index[i]
	content = str(content)
	return content


def main():
	base = str(open("/Users/Simonsays/Desktop/BootcampCite/templates/base.html").read())

	
	url = [
	 	"/Users/Simonsays/Desktop/BootcampCite/docs/index.html",
	 	"/Users/Simonsays/Desktop/BootcampCite/docs/blogIndex.html",
		"/Users/Simonsays/Desktop/BootcampCite/docs/relevantIndex.html"
	 ]

	index = [
	 	open("//Users/Simonsays/Desktop/BootcampCite/content/index.html").read(),
	 	open("//Users/Simonsays/Desktop/BootcampCite/content/blogIndex.html").read(),
	 	open("//Users/Simonsays/Desktop/BootcampCite/content/relevantIndex.html").read()
	 ]

	title = [
	 	"Simon Tekeste",
	 	"Blog",
	 	"Relevance"
	 ]

	things_i_need(base title, index, url)
	 
	print("complete")


if __name__ == "__main__":
	main();
