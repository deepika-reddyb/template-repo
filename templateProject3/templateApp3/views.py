from django.shortcuts import render

# Create your views here.
def dateTimeView(request):
	dt=datetime.datetime.now()
	h1=dt.strftime('%H')
	h=int(h1)
	if(h<12):
		msg="Good Morning"
	elif(h<15):
		msg="Good afternoon"
	else:
		msg="Good Night"
	d={'datetime':dt,'message':msg }
	return render(request,'templateApp3/1.html',d)