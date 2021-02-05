
from bs4 import BeautifulSoup as b
import requests as r

def MCQScraper(link):
      page_title=link.split("/")[3]
      heading="<!DOCTYPE html>\n<html>\n<head>\n<title>"+page_title+"</title>\n</head>\n<link rel='stylesheet' type='text/css' href='./style.css'>\n<body>";

      file=open("../cse/"+page_title+".html","w")
      file.write(heading)

      p=r.get(link).text
      soup=b(p,features="html.parser")

      links=[]
      
      table_data=soup.find_all("td");
      
      for data in table_data:
      	href=data.a["href"]
      	# text=data.a.text;
      	if(href):
      		#title.append(text)
      		links.append(href)
      
      k=0
      
      for i in links:
      	p=r.get(i).text
      	soup=b(p,features="html.parser")
      	questions=soup.find("div",{"class":"entry-content","itemprop":"text"})
      	file.write(str(questions))

      ending="</body>\n<script src='./script.js'></script>\n</html>"
      file.write(ending)


# Add your link here 
links=["https://www.sanfoundry.com/c-interview-questions-answers/"]
index_file=open("../index.html","a")


for link in links:
      MCQScraper(link)
      href=link.split("/")[3]
      text="<li>\n<a href=./cse/"+href+">"+href+"</a>\n</li>"
      index_file.write(text)

end_text="</ol>\n</div>\n</body>\n</html>"
index_file.write(end_text);



# Add the link it generate the html file 
#  "https://www.sanfoundry.com/1000-basic-electrical-engineering-questions-answers/",
#  "https://www.sanfoundry.com/computer-network-questions-answers/",
#  "https://www.sanfoundry.com/microprocessors-questions-answers/",
#  "https://www.sanfoundry.com/1000-data-structure-questions-answers/",
#  "https://www.sanfoundry.com/1000-microcontroller-questions-answers/",
#  "https://www.sanfoundry.com/1000-discrete-mathematics-questions-answers/",
#  "https://www.sanfoundry.com/1000-object-oriented-programming-oops-questions-answers/",
# "https://www.sanfoundry.com/software-engineering-questions-answers/",
# "https://www.sanfoundry.com/artificial-intelligence-questions-answers/",
# "https://www.sanfoundry.com/1000-database-management-system-questions-answers/"

# global file;
# def OOADScraper(link,isfirst=1):
#       global file
#       if(isfirst):
#             page_title=link.split("/")[3]
#             heading="<!DOCTYPE html>\n<html>\n<head>\n<title>"+page_title+"</title>\n</head>\n<link rel='stylesheet' type='text/css' href='./style.css'>\n<body>";

#             file=open("../cse/"+page_title+".html","w")
#             file.write(heading)

#       p=r.get(link).text
#       soup=b(p,features="html.parser")

#       links=[]
      
#       next_link=soup.find("a",{"rel":"next"});
#       print(next_link["href"],next_link.text)
#       if(next_link and next_link.text=="Next"):
#             questions=soup.find("div",{"class":"entry-content","itemprop":"text"})
#             file.write(str(questions))
#             OOADScraper(next_link["href"],0)
#       else:
#             ending="</body>\n<script src='./script.js'></script>\n</html>"
#             file.write(ending)
#             print("finished")



