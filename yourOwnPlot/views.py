from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponse
from collections import OrderedDict
from fusioncharts import FusionCharts
import commonFunctions
import json
import logging

logger = logging.getLogger(__name__)

# https://api.data.gov.in/resource/4256d3dd-5e4a-4e0b-9d35-17fd1bdc83f7?api-key=579b464db66ec23bdd000001c8e6c9d6daf34e65556dabe447fd0c35&format=json&offset=0&limit=100
# 579b464db66ec23bdd000001c8e6c9d6daf34e65556dabe447fd0c35
def yourOwnPlot(request):
    if request.method == "POST":
        str1 = request.POST.get('handle')
        rawData = commonFunctions.downloadData(str1)
        rawData = check_sr_no(rawData)
        loadJson = commonFunctions.loadJson(rawData)
        mainKey = ""
        #if "records" in loadJson:
        mainKey = "records"
        #elif "data" in loadJson:
         #   mainKey = "data"
        #data = loadJson[mainKey]
        i = 0
        start = rawData.find(mainKey)
        start = rawData.find("[", start)
        end = rawData.find("]", start)
        dataString = rawData[start:end + 1]
        labels = []
        dataString = dataString.split('},')
        for x in range(len(dataString)):
            labels.append(dataString[x].split(',')[1].split(":")[1].split("\"")[1])
        i = 0
        count = 0
        dataString = rawData[start:end + 1]
        dataString = dataString.replace("\r", "").replace(" ", "")
        dataString = dataString.replace("\r", "").replace("\n", "")
        dataString = dataString.replace("\r", "").replace("\t", "")
        while dataString[i] != '}':
            if dataString[i] == ',':
                count += 1
            i += 1
        count -= 1

        dataString = dataString.split('},')
        # impData = {}
        # list = []
        # # for i in range(len(labels)):
        # #     list.append({})
        # impData[mainKey] = []
        # for i in range(len(labels)):
        #     impData[mainKey] = impData[mainKey].append({"label":labels[i]})
        # print(impData)

        listOfAttributes = []
        commaCount = 0
        quote = 0
        s = dataString[0]
        s = s.replace("\r", "").replace(" ", "")
        s = s.replace("\r", "").replace("\n", "")
        s = s.replace("\r", "").replace("\t", "")
        s = s[2:]
        s = s.split(",")
        attr = ""
        for i in range(2, len(s)):
            v = s[i][1:]
            for j in range(0, len(v)):
                if(v[j]=='"'):
                    break
                attr = attr + v[j]
            listOfAttributes.append(attr)
            attr = ""

        impData = {}
        impData[mainKey] = []
        for i in range(len(labels)):
            dict = {}
            dict["labels"] = labels[i]
            list = impData[mainKey]
            list.append(dict)
            impData[mainKey] = list

        string = ''
        i=0
        for i in range(len(labels)):
            string = dataString[i]
            l = len(string)
            if i==0:
                string = string[1:len(string)-1]
            if i==(len(labels)-1):
                string = string[0:len(string)-3]
            string = string[1:l-1]
            array = string.split(',')
            for j in range(2, len(array)):
                stray = array[j]
                #print(stray)
                stray = stray.split(':"')[1]
                stray = stray[0:len(stray)]
                list = impData[mainKey]
                dict = {}
                if(j != len(array)-1):
                    list[i][listOfAttributes[j-2]] = stray[0:len(stray)-1]
                else:
                    list[i][listOfAttributes[j - 2]] = stray
                impData[mainKey] = list

        maximumValues = []
        for i in range(count):
            maximumValues.append(impData[mainKey][0][listOfAttributes[i]])
        #print("The maxi is ",maximumValues,"\n\n\n")
        for i in range(len(labels)):
            for j in range(count):
                if float(impData[mainKey][i][listOfAttributes[j]]) > float(maximumValues[j]):
                    maximumValues[j] = impData[mainKey][i][listOfAttributes[j]]
        units = []
        unitsList = loadJson["field"]
        for i in range(count):
            st = unitsList[i+2]["name"]
            if(st.find('(')!=-1):
                st = st.split(')')[0].split('(')[1]
            units.append(st)
            print(units)


        string1 = '''{"chart": {
        "caption": "''' + str(loadJson["title"]) + '''",
        "showvalues": "0",
        "labeldisplay": "ROTATE",
        "rotatelabels": "0",
        "allowAxisShift": "1",
        "numvisibleplot": "12",
        "plothighlighteffect": "fadeout",
        "plottooltext": "$seriesName in $label : <b>$dataValue</b>",
        "theme": "fusion"
        },'''

        string2 = """ "axis": ["""
        string3 = ""
        mid = (count+1)/2
        for i in range(count):
            if i<=mid:
                pos = "left"
            else:
                pos = "right"
            s = ""
            s = '''{ "title": "''' + listOfAttributes[i] + '''",
                    "titlepos": "''' + pos + ''' ",
                    "numberprefix": "''' + units[i] + ''' ",
                    "divlineisdashed": "1",
                    "maxvalue": "''' + maximumValues[i] + '''",
                    "dataset": [
                                    {
                                        "seriesname": "''' + listOfAttributes[i] + '''",
                                        "linethickness": "3",
                                        "data": ['''
            for j in range(len(labels)):
                s = s + '''{
                                "value": "''' + impData[mainKey][j][listOfAttributes[i]] + '''"},'''
            s = s[0:len(s)-1]
            string3 = string3 + s + """]}]},"""
        string3 = string3[0:len(string3)-1]
        string3 = string3 + """],"""

        category = """ "categories": [
                            {
                                "category": ["""
        for i in range(len(labels)):
            category = category + '''{"label": "''' + labels[i] + '''"},'''
        category = category[0:len(category)-1]
        category = category +  ''']}]}'''
        final = string1 + string2 + string3 + category

        jjssoonn = commonFunctions.loadJson(final)
        scr = 0
        cunt = count
        while cunt>0:
            cunt-=2
            scr+=1200
        scroll = str(scr)

        chartObj = FusionCharts('multiaxisline', 'ex1', scroll, '600', 'yourOwnPlotGraph', 'json', final)
        return render(request, 'yourOwnPlot.html', {'outputYourOwnPlotGraph':chartObj.render()})

    return render(request, 'yourOwnPlot.html', {})

def check_sr_no(rawData):

    if rawData.find('"sr_no": ')==-1 and rawData.find('s_no')==-1 and rawData.find('"id":')==-1:
        index = rawData.find("records")
        i=1
        l=len(rawData)
        while(index<len(rawData)):
            while(index<len(rawData) and rawData[index]!='{'):
                index+=1
            if index>=len(rawData):
                break
            index+=1
            rawData = rawData[0:index] + '"sr_no": "' + str(i) + '",' + rawData[index:]
            i += 1

        index = rawData.find("field")
        i=1
        while(rawData[index]!='['):
            index+=1
        index+=1
        rawData = rawData[0:index] + '{},' + rawData[index:]



    return rawData
