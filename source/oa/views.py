from django.db.models import F
from django.shortcuts import render
from .models import Sensors
import sys
from django.utils import timezone
import csv

# Create your views here.
from django.http import HttpResponse
sys.path.insert(0,'/home/oa-user/openAquaponics/oa/helperScripts/')
import getSensorReadings
from getSensorReadings import HelperScripts
from plug import growLamp 


    #instance variables
temp=0
tds=0
pH=0
    #mins and maxs for formatting/alerts
tempMin=0 
tempMax=0
tdsMin=0 
tdsMax=0
pHMin=0
pHMax=0


helper = getSensorReadings.HelperScripts()
    #helper methods
def tempInRange():
    if tempMin <temp and temp<tempMax:
        return True
    else: 
        return False

def tdsInRange():
    if float(tdsMin) <float(tds) and float(tds)<float(tdsMax):
        return True
    else: 
        return False

def pHInRange():
    if float(pHMin) <float(pH) and float(pH)<float(pHMax):
        return True
    else: 
        return False
    #views
def index(request):
        #pass a variable to the html like this vvv
    global temp, tds, pH
    r = helper.getSensorReading()
    
    readings = Sensors(waterLevel=r[0], thermo=r[1], tds=r[2], pH=r[3], timestamp=timezone.now())
    readings.save()
    readings.waterLevel = r[0] 
    readings.thermo = r[1]
    temp = r[1]
    readings.tds = r[2]
    tds = r[2]
    readings.pH = r[3]
    pH = r[3]
    readings.timestamp =timezone.now()
        #need most recent sensor reading here
    tempIR = tempInRange()
    tdsIR = tdsInRange()
    pHIR = pHInRange()
    #have to import from Helper Scripts
    light_status = helper.lightStatus()
    context = {"sensor_reading":readings, "tempIR":tempIR, "tdsIR":tdsIR, "pHIR":pHIR, "lightStatus":light_status}

    return render(request, "oa/index.html", context)

def settings(request):
        # Default values
    light_status = False
    global tempMin, tempMax, tdsMin, tdsMax, pHMin, pHMax
      

    if request.method == 'POST':
            # Handle light toggle
        if request.POST.get('light_status') == 'on':
            print("Light ON")
            light_status = True
            growLamp()  # Activate grow lamp
        else:
            print("Light OFF")
            light_status = False

            # Get numeric form values (safe cast with fallback to None or 0)
        try:
      
            tempMin = float(request.POST.get('tempMin', 0))
            tempMax = float(request.POST.get('tempMax', 0))
            tdsMin = float(request.POST.get('tdsMin', 0))
            tdsMax = float(request.POST.get('tdsMax', 0))
            pHMin = float(request.POST.get('pHMin', 0))
            pHMax = float(request.POST.get('pHMax', 0))
        except ValueError:
            print("Invalid input encountered.")

            # Optional: Save these to a database or config file if needed
        print("Temperature Min/Max:", tempMin, tempMax)
        print("TDS Min/Max:", tdsMin, tdsMax)
        print("pH Min/Max:", pHMin, pHMax)

        # Pass back current values to prefill form if needed
    context = {
            "light_status": light_status,
            "tempMin": tempMin,
            "tempMax": tempMax,
            "tdsMin": tdsMin,
            "tdsMax": tdsMax,
            "pHMin": pHMin,
            "pHMax": pHMax
    }

    return render(request, "oa/settings.html", context)

def download_csv(request):
    response =HttpResponse(content_type='text/csv') 

    writer = csv.writer(response)
    response.write(u'\ufeff'.encode('utf8'))
    
    writer.writerow(["Time & Date","Current Status","Temperature","TDS","PH"])
    for row in Sensors.objects.all():
        List = [row.timestamp,row.waterLevel,row.thermo,row.tds,row.pH]
        writer.writerow(List)

    return response


def logs(request):
    if request.GET.get('download') == 'csv':
            # Create the HttpResponse object with CSV headers.
        responce = download_csv(request)
        return responce
           
    # regular logs rendering
    #need most recent sensor reading here
    
    times = Sensors.objects.order_by('-id').values_list("timestamp",flat=True)
    waterlevels = Sensors.objects.order_by('-id').values_list("waterLevel",flat=True)
    temps = Sensors.objects.order_by('-id').values_list("thermo",flat=True)
    tds = Sensors.objects.order_by('-id').values_list("tds",flat=True)
    pHs = Sensors.objects.order_by('-id').values_list("pH",flat=True)
    
    context = {"timestamp":times,"waterlevels":waterlevels,"temps":temps,"tds":tds,"pHs":pHs,"tempInRange":tempInRange(),"tdsInRange":tdsInRange(),"phInRange":pHInRange()}
    
    return render(request, "oa/logs.html", context)

