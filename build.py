
def things_i_need(base, url=[],title=[],index=[]):
	i = 0
	for x in url:
	 	printingdata = open(f"{x}", "w+")
	 	row  = another_thing(base, i, title)
	 	content_insert = indexplug(row, i, index)
	 	printingdata.write(f"{content_insert}")
	 	i+=1
	 	printingdata.close();

def another_thing(base,i, title=[]):
	t = title[i]
	row = base.replace("{{title}}",f"{t}")
	return row


def indexplug(row, i, index =[]):
	c = index[i]
	c = open(c).read()
	c = str(c)
	con = row.replace("{{content_insert}}",f"{c}")
	return con


def main():
	base = str(open("templates/base.html").read())

	url =[]
	title =[]
	index =[]

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
		 index.append(page["filename"])
		 url.append(page['output'])
		 title.append(page["title"])
	
	things_i_need(base, url,title,index)

	print("complete")


if __name__ == "__main__":
	main();
