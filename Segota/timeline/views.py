from django.shortcuts import render
import sys
import json 

# Create your views here.

def index(request):
    print sys.path

    event_dict = {
    "events":
    [
    {
        "date": "16 May, 2008" ,
        "summary" :"Aarushi Talwar found dead with her throat slit in the bedroom of her home in Noida. Domestic help Hemraj, a Nepali, suspected of murder. "
    },
    {
        "date": "17 May, 2008" ,
        "summary" :"Hemraj's body found on the terrace of Talwar's residence. "
    },
    {
        "date": "18 May, 2008" ,
        "summary" :"Aarushi Talwar found dead with her throat slit in the bedroom of her home in Noida. Domestic help Hemraj, a Nepali, suspected of murder. "
    }
    
    ]


}

    context_dict = event_dict


    return render(request,'timeline/index.html' , context_dict)