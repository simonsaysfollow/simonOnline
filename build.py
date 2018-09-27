
def writing_content(base, filename, output, title):	
	printingdata = open(f"{output}", "w+")
	row  = another_thing(base, title)
	content_insert = indexplug(row,filename )
	printingdata.write(f"{content_insert}")
	printingdata.close();

def another_thing(base,title):
	t = title
	row = base.replace("{{title}}",f"{t}")
	return row


def indexplug(row,filename):
	
	c = open(filename).read()
	c = str(c)
	con = row.replace("{{content_insert}}",f"{c}")
	return con


def main():
	base = str(open("templates/base.html").read())


	pages = [
		
		{
			"filename":"content/index.html",
			"output": "docs/index.html",
			"title":"Simon Tekeste",
		},
		{
			"filename":"content/blogIndex.html",
			"output": "docs/blogIndex.html",
			"title":"Blog",
		},
		{
			"filename":"content/relevantIndex.html",
			"output": "docs/relevantIndex.html",
			"title":"Relevance",
		}

	]

	for page in pages:
		filename = page['filename']
		output = page['output']
		title = page['title']
		writing_content(base, filename, output, title)

	print("complete")


if __name__ == "__main__":
	main();
