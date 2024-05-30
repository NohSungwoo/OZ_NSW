from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_feed(request):
    return HttpResponse("show feed")

def one_feed(request, feed_id, feed_content) : 
    return HttpResponse(f"feed_id : {feed_id}, feed_content : {feed_content}")
def all_feed(request) :
    return HttpResponse("all_feed")
