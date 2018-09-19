top = open("/Users/Simonsays/Desktop/BootcampCite/templates/top.html").read();
index = open("//Users/Simonsays/Desktop/BootcampCite/content/index.html").read();
bottom = open("/Users/Simonsays/Desktop/BootcampCite/templates/bottom.html").read();

top = str(top);
index = str(index);
bottom = str(bottom);

title = "simmy"
printingdata = open("/Users/Simonsays/Desktop/BootcampCite/docs/pythonIndex.html", "w+");
html_text =  "<title>" + top.replace("{{title}}","{title}") + "</title>"
printingdata.write(top+"\n"+index+"\n"+bottom);

printingdata.close();


printingdata = open("/Users/Simonsays/Desktop/BootcampCite/docs/pythonIndex.html").read();
print(printingdata);