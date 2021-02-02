""" my mini project to scrap the content inna specific website """
from bs4 import BeautifulSoup as b
import requests as r


def QuestionScraper(link):
      page_title=link.split("/")[3]
      heading="<!DOCTYPE html><html><head><title>"+page_title+"</title></head><link rel='stylesheet' type='text/css' href='./style.css'><body>";

      file=open(page_title+".html","w")
      file.write(heading)

      p=r.get(link).text
      soup=b(p,features="html.parser")

      title=[]
      links=[]
      
      table_data=soup.find_all("td");
      
      for data in table_data:
      	href=data.a["href"]
      	text=data.a.text;
      	if(href and text):
      		title.append(text)
      		links.append(href)
      
      k=0
      
      for i in links:
      	p=r.get(i).text
      	soup=b(p,features="html.parser")
      	questions=soup.find("div",{"class":"entry-content","itemprop":"text"})
      	file.write(str(questions))

      ending="</body><script src='./script.js'></script></html>"
      file.write(ending)


      

#QuestionScraper(pass the link)
#QuestionScraper("https://www.sanfoundry.com/1000-basic-electrical-engineering-questions-answers/");
# QuestionScraper("https://www.sanfoundry.com/computer-network-questions-answers/");
# QuestionScraper("https://www.sanfoundry.com/computer-network-questions-answers/");
# QuestionScraper("https://www.sanfoundry.com/computer-network-questions-answers/");