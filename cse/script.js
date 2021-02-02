link_tag=document.querySelectorAll("a")
for(let i=0;i<link_tag.length;i++)
{
	//checking chilldren because it has img mean it is question else not 
	if(link_tag[i].parentNode.parentNode.nodeName==="P" && !(link_tag[i].children[0]))
	{
		link_tag[i].parentNode.parentNode.style.display="none";
	}
	if(link_tag[i].parentNode.nodeName==="P" && !(link_tag[i].children[0]))
	{
		link_tag[i].parentNode.style.display="none";
	}
}