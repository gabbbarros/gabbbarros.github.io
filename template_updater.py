""""
This function creates a project page for each game in the games.yml
file, using the template provided.
"""

f  = open("pages/template.html", "r")
template = f.read().split("\r\n")
f.close();

f = open("_data/games.yml")
projects = f.read().split("\r\n")
f.close()

st = len("- tag: ");

for line in projects:
	if "tag:" in line and "#" not in line:
		name = line[st:]
		file = open("pages/projects/"+name+".html","w")
		for base in template:
			file.write(base.replace("!TAG!",name)+"\r\n") 
		
		file.close()
		print ("Created file for "+name)

