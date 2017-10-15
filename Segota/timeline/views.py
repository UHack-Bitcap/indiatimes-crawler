from django.shortcuts import render
import sys
import json 
import requests


# Create your views here.

def index(request):

    name = request.GET.get('name')
    print name
    print sys.path
    
    #request for json 

    r = requests.get('http://172.20.10.2:1970/check?keyword=' + name)

    q = json.loads(r.text)
    # responseobj = json.dumps(q)
    # print responseobj


    event_dict = {
    "events": q
   


}   
    
    print event_dict

    context_dict = event_dict


    return render(request,'timeline/index.html' , context_dict)

    # 172.120.10.2:1970/check?keyword=arushi+talwar