from django.shortcuts import render
from django.http import HttpResponse
from collections import OrderedDict
from fusioncharts import FusionCharts
import commonFunctions
import logging
# 579b464db66ec23bdd000001c8e6c9d6daf34e65556dabe447fd0c35

urlLiteracy = "https://api.data.gov.in/resource/f7d34594-f40d-42a3-990e-fd9a5fe2b7f5?api-key=579b464db66ec23bdd000001c8e6c9d6daf34e65556dabe447fd0c35&format=json&offset=0&limit=100"
#http://www.jsonmate.com/permalink/5cd5708f85da04b10bcf81b7

logger = logging.getLogger(__name__)
def literacyRatesStates(request):
    rawData = commonFunctions.downloadData(urlLiteracy)
    js = commonFunctions.loadJson(rawData)
    data = js['records']

    # *****************************Chloropleth Map*****************************#

    mapConfig = OrderedDict()
    mapConfig["animation"] = "1"
    mapConfig["usehovercolor"] = "1"
    mapConfig["showlegend"] = "1"
    mapConfig["legendposition"] = "BOTTOM"
    mapConfig["legendborderalpha"] = "0"
    mapConfig["legendbordercolor"] = "#FDFDB7"
    mapConfig["legendallowdrag"] = "0"
    mapConfig["legendshadow"] = "0"
    mapConfig["numbersuffix"] = "%"
    mapConfig["caption"] = "Literacy Rates of States"
    mapConfig["subcaption"] = "Open Census Data"
    mapConfig["connectorcolor"] = "#FDFDB7"
    mapConfig["fillalpha"] = "80"
    mapConfig["entityFillHoverColor"] = "#dddddd"
    mapConfig["theme"] = "fusion"

    colorDataObj = {
        "minvalue": "50",
        "code": "#FFE0B2",
        "gradient": "1",
        "color": [{
            "minValue": "50",
            "maxValue": "58",
            "code": "#f4fdff"
        },
            {
                "minValue": "58",
                "maxValue": "66",
                "code": "#c0dae0"
            },
            {
                "minValue": "66",
                "maxValue": "74",
                "code": "#8bc8d6"
            },
            {
                "minValue": "74",
                "maxValue": "82",
                "code": "#57b6cc"
            },
            {
                "minValue": "82",
                "maxValue": "90",
                "code": "#037db7"
            },
            {
                "minValue": "90",
                "maxValue": "100",
                "code": "#0365b7"
            }
        ]
    }

    for i in range(len(data)):
        stateName = data[i]["india_states_uts"]
        if stateName == "Uttrakhand":
            commonFunctions.stateDictionary["Uttarakhand"][0] = float(data[i]["literacy_rates_percentage___total___2011"])
            commonFunctions.stateDictionary["Uttarakhand"][1] = float(data[i]["literacy_rates_percentage___total___2001"])
            commonFunctions.stateDictionary["Uttarakhand"][2] = float(data[i]["increase_in_literacy_rates2001_2011_percentage_points_total___2001_2011"])
        elif stateName in commonFunctions.stateDictionary.keys():
            commonFunctions.stateDictionary[stateName][0] = float(data[i]["literacy_rates_percentage___total___2011"])
            commonFunctions.stateDictionary[stateName][1] = float(data[i]["literacy_rates_percentage___total___2001"])
            commonFunctions.stateDictionary[stateName][2] = float(data[i]["increase_in_literacy_rates2001_2011_percentage_points_total___2001_2011"])
    commonFunctions.stateDictionary["Telangana"][0] = 66.67
    commonFunctions.stateDictionary["Telangana"][1] = 58.89
    commonFunctions.stateDictionary["Telangana"][2] = 8.87

    mapDataArray2011 = [
        ["001", str(commonFunctions.stateDictionary["Andaman & Nicobar Islands"][0]), "1"],
        ["002", str(commonFunctions.stateDictionary["Andhra Pradesh"][0]), "1"],  # AP
        ["003", str(commonFunctions.stateDictionary["Arunachal Pradesh"][0]), "1"],  # AR
        ["004", str(commonFunctions.stateDictionary["Assam"][0]), "1"], # AS
        ["005", str(commonFunctions.stateDictionary["Bihar"][0]), "1"],
        ["006", str(commonFunctions.stateDictionary["Chandigarh"][0]), "1"],
        ["007", str(commonFunctions.stateDictionary["Chhattisgarh"][0]), "1"],  # CA
        ["011", str(commonFunctions.stateDictionary["Goa"][0]), "1"],  # GO
        ["012", str(commonFunctions.stateDictionary["Gujarat"][0]), "1"],  # GU
        ["013", str(commonFunctions.stateDictionary["Haryana"][0]), "1"],  # HA
        ["014", str(commonFunctions.stateDictionary["Himachal Pradesh"][0]), "1"],  # HP
        ["015", str(commonFunctions.stateDictionary["Jammu & Kashmir"][0]), "1"],  # JK
        ["016", str(commonFunctions.stateDictionary["Jharkhand"][0]), "1"],  # JH
        ["017", str(commonFunctions.stateDictionary["Karnataka"][0]), "1"],  # KA
        ["018", str(commonFunctions.stateDictionary["Kerala"][0]), "1"], # KE
        ["020", str(commonFunctions.stateDictionary["Madhya Pradesh"][0]), "1"],  # MP
        ["021", str(commonFunctions.stateDictionary["Maharashtra"][0]), "1"],  # MA
        ["022", str(commonFunctions.stateDictionary["Manipur"][0]), "1"],  # MN
        ["023", str(commonFunctions.stateDictionary["Meghalaya"][0]), "1"],  # ME
        ["024", str(commonFunctions.stateDictionary["Mizoram"][0]), "1"],  # MI
        ["025", str(commonFunctions.stateDictionary["Nagaland"][0]), "1"],  # NA
        ["026", str(commonFunctions.stateDictionary["Odisha"][0]), "1"], # OR
        ["028", str(commonFunctions.stateDictionary["Punjab"][0]), "1"], # PU
        ["029", str(commonFunctions.stateDictionary["Rajasthan"][0]), "1"],  # RA
        ["030", str(commonFunctions.stateDictionary["Sikkim"][0]), "1"], # SI
        ["031", str(commonFunctions.stateDictionary["Tamil Nadu"][0]), "1"], # TN
        ["032", str(commonFunctions.stateDictionary["Tripura"][0]), "1"],  # TR
        ["036", str(commonFunctions.stateDictionary["Telangana"][0]), "1"],  # TG
        ["033", str(commonFunctions.stateDictionary["Uttar Pradesh"][0]), "1"],  # UP
        ["034", str(commonFunctions.stateDictionary["Uttarakhand"][0]), "1"],  # UT
        ["035", str(commonFunctions.stateDictionary["West Bengal"][0]), "1"]  # WB
    ]

    mapDataArray2001 = [
        ["001", str(commonFunctions.stateDictionary["Andaman & Nicobar Islands"][1]), "1"],
        ["002", str(commonFunctions.stateDictionary["Andhra Pradesh"][1]), "1"],  # AP
        ["003", str(commonFunctions.stateDictionary["Arunachal Pradesh"][1]), "1"],  # AR
        ["004", str(commonFunctions.stateDictionary["Assam"][1]), "1"],  # AS
        ["005", str(commonFunctions.stateDictionary["Bihar"][1]), "1"],
        ["006", str(commonFunctions.stateDictionary["Chandigarh"][1]), "1"],
        ["007", str(commonFunctions.stateDictionary["Chhattisgarh"][1]), "1"],  # CA
        ["011", str(commonFunctions.stateDictionary["Goa"][1]), "1"],  # GO
        ["012", str(commonFunctions.stateDictionary["Gujarat"][1]), "1"],  # GU
        ["013", str(commonFunctions.stateDictionary["Haryana"][1]), "1"],  # HA
        ["014", str(commonFunctions.stateDictionary["Himachal Pradesh"][1]), "1"],  # HP
        ["015", str(commonFunctions.stateDictionary["Jammu & Kashmir"][1]), "1"],  # JK
        ["016", str(commonFunctions.stateDictionary["Jharkhand"][1]), "1"],  # JH
        ["017", str(commonFunctions.stateDictionary["Karnataka"][1]), "1"],  # KA
        ["018", str(commonFunctions.stateDictionary["Kerala"][1]), "1"],  # KE
        ["020", str(commonFunctions.stateDictionary["Madhya Pradesh"][1]), "1"],  # MP
        ["021", str(commonFunctions.stateDictionary["Maharashtra"][1]), "1"],  # MA
        ["022", str(commonFunctions.stateDictionary["Manipur"][1]), "1"],  # MN
        ["023", str(commonFunctions.stateDictionary["Meghalaya"][1]), "1"],  # ME
        ["024", str(commonFunctions.stateDictionary["Mizoram"][1]), "1"],  # MI
        ["025", str(commonFunctions.stateDictionary["Nagaland"][1]), "1"],  # NA
        ["026", str(commonFunctions.stateDictionary["Odisha"][1]), "1"],  # OR
        ["028", str(commonFunctions.stateDictionary["Punjab"][1]), "1"],  # PU
        ["029", str(commonFunctions.stateDictionary["Rajasthan"][1]), "1"],  # RA
        ["030", str(commonFunctions.stateDictionary["Sikkim"][1]), "1"],  # SI
        ["031", str(commonFunctions.stateDictionary["Tamil Nadu"][1]), "1"],  # TN
        ["032", str(commonFunctions.stateDictionary["Tripura"][1]), "1"],  # TR
        ["036", str(commonFunctions.stateDictionary["Telangana"][1]), "1"],  # TG
        ["033", str(commonFunctions.stateDictionary["Uttar Pradesh"][1]), "1"],  # UP
        ["034", str(commonFunctions.stateDictionary["Uttarakhand"][1]), "1"],  # UT
        ["035", str(commonFunctions.stateDictionary["West Bengal"][1]), "1"]  # WB
    ]

    dataSource2011 = OrderedDict()
    dataSource2011["chart"] = mapConfig
    dataSource2011["colorrange"] = colorDataObj
    dataSource2011["data"] = commonFunctions.makeDataSourceForChloroplethMap(mapDataArray2011)

    dataSource2001 = OrderedDict()
    dataSource2001["chart"] = mapConfig
    dataSource2001["colorrange"] = colorDataObj
    dataSource2001["data"] = commonFunctions.makeDataSourceForChloroplethMap(mapDataArray2001)

    fusionMap2011 = FusionCharts("maps/india", "Map1", "600", "600", "literacyChloropleth2011", "json", dataSource2011)
    fusionMap2001 = FusionCharts("maps/india", "Map2", "600", "600", "literacyChloropleth2001", "json", dataSource2001)

    chartObj1 = FusionCharts('scrollcolumn2d', 'graph1', '600', '600', 'literacyGraph', 'json', """{
              "chart": {
                "caption": "Increase in Literacy Rates from 2001-2011",
                "subcaption": "",
                "yaxisname": "Percentage(%)",
                "plottooltext": "$dataValue",
                "labeldisplay": "auto",
                "numvisibleplot": "6",
                "drawcrossline": "1",
                "showvalues":"1",
                "theme": "fusion"
              },
              "categories": [
                {
                  "category": [
                    {
                        "label": "Andaman & Nicobar Islands"
                    },
                    {
                        "label": "Andhra Pradesh"
                    },
                    {
                        "label": "Arunachal Pradesh"
                    },
                    {
                        "label": "Assam"
                    },
                    {
                        "label": "Bihar"
                    },
                    {
                        "label": "Chattisgarh"
                    },
                    {
                        "label": "Delhi"
                    },
                    {
                        "label": "Goa"
                    },
                    {
                        "label": "Gujarat"
                    },
                    {
                        "label": "Haryana"
                    },
                    {
                        "label": "Himachal Pradesh"
                    },
                    {
                        "label": "Jammu & Kashmir"
                    },
                    {
                        "label": "Jharkhand"
                    },
                    {
                        "label": "Karnataka"
                    },
                    {
                        "label": "Kerala"
                    },
                    {
                        "label": "Lakshadweep"
                    },
                    {
                        "label": "Madhya Pradesh"
                    },
                    {
                        "label": "Maharashtra"
                    },
                    {
                        "label": "Manipur"
                    },
                    {
                        "label": "Meghalaya"
                    },
                    {
                        "label": "Mizoram"
                    },
                    {
                        "label": "Nagaland"
                    },
                    {
                        "label": "Odisha"
                    },
                    {
                        "label": "Punjab"
                    },
                    {
                        "label": "Rajasthan"
                    },
                    {
                        "label": "Sikkim"
                    },
                    {
                        "label": "Tamil Nadu"
                    },
                    {
                        "label": "Tripura"
                    },
                    {
                        "label": "Telangana"
                    },
                    {
                        "label": "Uttar Pradesh"
                    },
                    {
                        "label": "Uttrakhand"
                    },
                    {
                        "label": "West Bengal"
                    }
                  ]
                }
              ],
              "dataset": [
                {
                  "seriesname": "Increase in literacy Rate",
                  "plottooltext": "Increase: $dataValue%",
                  "data": [
                    {
                      "value": """ + '"' + str(commonFunctions.stateDictionary["Andaman & Nicobar Islands"][2]) + '"' + """
                    },
                    {
                      "value": """ + '"' + str(commonFunctions.stateDictionary["Andhra Pradesh"][2]) + '"' + """
                    },
                    {
                      "value": """ + '"' + str(commonFunctions.stateDictionary["Arunachal Pradesh"][2]) + '"' + """
                    },
                    {
                      "value": """ + '"' + str(commonFunctions.stateDictionary["Assam"][2]) + '"' + """
                    },
                    {
                      "value": """ + '"' + str(commonFunctions.stateDictionary["Bihar"][2]) + '"' + """
                    },
                    {
                      "value": """ + '"' + str(commonFunctions.stateDictionary["Chhattisgarh"][2]) + '"' + """
                    },
                    {
                      "value": """ + '"' + str(commonFunctions.stateDictionary["Delhi"][2]) + '"' + """
                    },
                    {
                      "value": """ + '"' + str(commonFunctions.stateDictionary["Goa"][2]) + '"' + """
                    },
                    {
                      "value": """ + '"' + str(commonFunctions.stateDictionary["Gujarat"][2]) + '"' + """
                    },
                    {
                      "value": """ + '"' + str(commonFunctions.stateDictionary["Haryana"][2]) + '"' + """
                    },
                    {
                      "value": """ + '"' + str(commonFunctions.stateDictionary["Himachal Pradesh"][2]) + '"' + """
                    },
                    {
                      "value": """ + '"' + str(commonFunctions.stateDictionary["Jammu & Kashmir"][2]) + '"' + """
                    },
                    {
                      "value": """ + '"' + str(commonFunctions.stateDictionary["Jharkhand"][2]) + '"' + """
                    },
                    {
                      "value": """ + '"' + str(commonFunctions.stateDictionary["Karnataka"][2]) + '"' + """
                    },
                    {
                      "value": """ + '"' + str(commonFunctions.stateDictionary["Kerala"][2]) + '"' + """
                    },
                    {
                      "value": """ + '"' + str(commonFunctions.stateDictionary["Lakshadweep"][2]) + '"' + """
                    },
                    {
                      "value": """ + '"' + str(commonFunctions.stateDictionary["Madhya Pradesh"][2]) + '"' + """
                    },
                    {
                      "value": """ + '"' + str(commonFunctions.stateDictionary["Maharashtra"][2]) + '"' + """
                    },
                    {
                      "value": """ + '"' + str(commonFunctions.stateDictionary["Manipur"][2]) + '"' + """
                    },
                    {
                      "value": """ + '"' + str(commonFunctions.stateDictionary["Meghalaya"][2]) + '"' + """
                    },
                    {
                      "value": """ + '"' + str(commonFunctions.stateDictionary["Mizoram"][2]) + '"' + """
                    },
                    {
                      "value": """ + '"' + str(commonFunctions.stateDictionary["Nagaland"][2]) + '"' + """
                    },
                    {
                      "value": """ + '"' + str(commonFunctions.stateDictionary["Odisha"][2]) + '"' + """
                    },
                    {
                      "value": """ + '"' + str(commonFunctions.stateDictionary["Punjab"][2]) + '"' + """
                    },
                    {
                      "value": """ + '"' + str(commonFunctions.stateDictionary["Rajasthan"][2]) + '"' + """
                    },
                    {
                      "value": """ + '"' + str(commonFunctions.stateDictionary["Sikkim"][2]) + '"' + """
                    },
                    {
                      "value": """ + '"' + str(commonFunctions.stateDictionary["Tamil Nadu"][2]) + '"' + """
                    },
                    {
                      "value": """ + '"' + str(commonFunctions.stateDictionary["Tripura"][2]) + '"' + """
                    },
                    {
                      "value": """ + '"' + str(commonFunctions.stateDictionary["Telangana"][2]) + '"' + """
                    },
                    {
                      "value": """ + '"' + str(commonFunctions.stateDictionary["Uttar Pradesh"][2]) + '"' + """
                    },
                    {
                      "value": """ + '"' + str(commonFunctions.stateDictionary["Uttarakhand"][2]) + '"' + """
                    },
                    {
                      "value": """ + '"' + str(commonFunctions.stateDictionary["West Bengal"][2]) + '"' + """
                    }
                  ]
                }
              ]
        }"""
    )

    chartObj2 = FusionCharts('scrollcolumn2d', 'graph2', '600', '600', 'literacyGraph2011', 'json', """{
                  "chart": {
                    "caption": "Literacy Rates from 2011",
                    "subcaption": "",
                    "yaxisname": "Percentage(%)",
                    "plottooltext": "$dataValue",
                    "labeldisplay": "auto",
                    "numvisibleplot": "6",
                    "drawcrossline": "1",
                    "showvalues":"1",
                    "theme": "fusion"
                  },
                  "categories": [
                    {
                      "category": [
                        {
                            "label": "Andhra Pradesh"
                        },
                        {
                            "label": "Arunachal Pradesh"
                        },
                        {
                            "label": "Assam"
                        },
                        {
                            "label": "Bihar"
                        },
                        {
                            "label": "Chattisgarh"
                        },
                        {
                            "label": "Goa"
                        },
                        {
                            "label": "Gujarat"
                        },
                        {
                            "label": "Haryana"
                        },
                        {
                            "label": "Himachal Pradesh"
                        },
                        {
                            "label": "Jammu & Kashmir"
                        },
                        {
                            "label": "Jharkhand"
                        },
                        {
                            "label": "Karnataka"
                        },
                        {
                            "label": "Kerala"
                        },
                        {
                            "label": "Madhya Pradesh"
                        },
                        {
                            "label": "Maharashtra"
                        },
                        {
                            "label": "Manipur"
                        },
                        {
                            "label": "Meghalaya"
                        },
                        {
                            "label": "Mizoram"
                        },
                        {
                            "label": "Nagaland"
                        },
                        {
                            "label": "Odisha"
                        },
                        {
                            "label": "Punjab"
                        },
                        {
                            "label": "Rajasthan"
                        },
                        {
                            "label": "Sikkim"
                        },
                        {
                            "label": "Tamil Nadu"
                        },
                        {
                            "label": "Tripura"
                        },
                        {
                            "label": "Telangana"
                        },
                        {
                            "label": "Uttar Pradesh"
                        },
                        {
                            "label": "Uttrakhand"
                        },
                        {
                            "label": "West Bengal"
                        }
                      ]
                    }
                  ],
                  "dataset": [
                    {
                      "seriesname": "Literacy Rate",
                      "plottooltext": "Value: $dataValue%",
                      "data": [
                        {
                          "value": """ + '"' + str(commonFunctions.stateDictionary["Andhra Pradesh"][0]) + '"' + """
                        },
                        {
                          "value": """ + '"' + str(commonFunctions.stateDictionary["Arunachal Pradesh"][0]) + '"' + """
                        },
                        {
                          "value": """ + '"' + str(commonFunctions.stateDictionary["Assam"][0]) + '"' + """
                        },
                        {
                          "value": """ + '"' + str(commonFunctions.stateDictionary["Bihar"][0]) + '"' + """
                        },
                        {
                          "value": """ + '"' + str(commonFunctions.stateDictionary["Chhattisgarh"][0]) + '"' + """
                        },
                        {
                          "value": """ + '"' + str(commonFunctions.stateDictionary["Goa"][0]) + '"' + """
                        },
                        {
                          "value": """ + '"' + str(commonFunctions.stateDictionary["Gujarat"][0]) + '"' + """
                        },
                        {
                          "value": """ + '"' + str(commonFunctions.stateDictionary["Haryana"][0]) + '"' + """
                        },
                        {
                          "value": """ + '"' + str(commonFunctions.stateDictionary["Himachal Pradesh"][0]) + '"' + """
                        },
                        {
                          "value": """ + '"' + str(commonFunctions.stateDictionary["Jammu & Kashmir"][0]) + '"' + """
                        },
                        {
                          "value": """ + '"' + str(commonFunctions.stateDictionary["Jharkhand"][0]) + '"' + """
                        },
                        {
                          "value": """ + '"' + str(commonFunctions.stateDictionary["Karnataka"][0]) + '"' + """
                        },
                        {
                          "value": """ + '"' + str(commonFunctions.stateDictionary["Kerala"][0]) + '"' + """
                        },
                        {
                          "value": """ + '"' + str(commonFunctions.stateDictionary["Madhya Pradesh"][0]) + '"' + """
                        },
                        {
                          "value": """ + '"' + str(commonFunctions.stateDictionary["Maharashtra"][0]) + '"' + """
                        },
                        {
                          "value": """ + '"' + str(commonFunctions.stateDictionary["Manipur"][0]) + '"' + """
                        },
                        {
                          "value": """ + '"' + str(commonFunctions.stateDictionary["Meghalaya"][0]) + '"' + """
                        },
                        {
                          "value": """ + '"' + str(commonFunctions.stateDictionary["Mizoram"][0]) + '"' + """
                        },
                        {
                          "value": """ + '"' + str(commonFunctions.stateDictionary["Nagaland"][0]) + '"' + """
                        },
                        {
                          "value": """ + '"' + str(commonFunctions.stateDictionary["Odisha"][0]) + '"' + """
                        },
                        {
                          "value": """ + '"' + str(commonFunctions.stateDictionary["Punjab"][0]) + '"' + """
                        },
                        {
                          "value": """ + '"' + str(commonFunctions.stateDictionary["Rajasthan"][0]) + '"' + """
                        },
                        {
                          "value": """ + '"' + str(commonFunctions.stateDictionary["Sikkim"][0]) + '"' + """
                        },
                        {
                          "value": """ + '"' + str(commonFunctions.stateDictionary["Tamil Nadu"][0]) + '"' + """
                        },
                        {
                          "value": """ + '"' + str(commonFunctions.stateDictionary["Tripura"][0]) + '"' + """
                        },
                        {
                          "value": """ + '"' + str(commonFunctions.stateDictionary["Telangana"][0]) + '"' + """
                        },
                        {
                          "value": """ + '"' + str(commonFunctions.stateDictionary["Uttar Pradesh"][0]) + '"' + """
                        },
                        {
                          "value": """ + '"' + str(commonFunctions.stateDictionary["Uttarakhand"][0]) + '"' + """
                        },
                        {
                          "value": """ + '"' + str(commonFunctions.stateDictionary["West Bengal"][0]) + '"' + """
                        }
                      ]
                    }
                  ]
            }"""
    )

    list = []
    i = len(list)
    for key, value in commonFunctions.stateDictionary.items():
        if value[0] != -1:
            list.append([key, value[0], i])
            i=i-1
    list = Sort(list)
    list.reverse()
    #logger.error(str(list))
    string1 = """{
                      "chart": {
                        "caption": "Literacy Rates from 2011 and Predicted Ranks of Health Indexes",
                        "subcaption": "",
                        "yaxisname": "Percentage(%)",
                        "syaxisname": "Rank",
                        "plottooltext": "$dataValue",
                        "labeldisplay": "auto",
                        "numvisibleplot": "8",
                        "drawcrossline": "1",
                        "showvalues":"1",
                        "theme": "fusion",
                        "lineColor": "#f94343"
                      },
                      "categories": [
                        {
                          "category": ["""
    string2 = ""
    for i in range(len(list)):
        string2 = string2 + ''' { "label": "''' + list[i][0] + '''"},'''
    string2 = string2[:-1]
    string3 = """]
                        }
                      ],
                      "dataset": [
                        {
                          "seriesname": "Literacy Rate",
                          "plottooltext": "Increase: $dataValue%",
                          "data": ["""

    string4 = ""
    for i in range(len(list)):
        string4 = string4 + '''{
                              "value": "''' + str(list[i][1]) + '''"},'''
    string4 = string4 + """]}"""
    string5 = string1+string2+string3+string4

    string6 = """,{
              "seriesname": "Predicted rank of health indexes",
              "parentyaxis": "S",
              "renderas": "line",
              "plottooltext": "$dataValue",
              "showvalues": "0",
              "data": ["""
    string7 = ""
    l=len(list)
    for i in range(l):
        string7 = string7 + """{
                  "value": """ + '"' + str(i+1) + '"' + """
                },"""
    string7 = string7 + """]
            }
          ]
        }"""
    string8 = string5+string6+string7
    #logger.error(string8)

    chartObj3 = FusionCharts('scrollcombidy2d', 'graph3', '1170', '600', 'literacyGraph2011Sorted', 'json', string8)

    # listSorted = []
    # for i in range(len(list)):
    #     listSorted.append(list[i][0])
    return render(request, 'literacyRatesStates.html',
                  {'outputliteracyChloropleth2011': fusionMap2011.render(), 'outputliteracyChloropleth2001': fusionMap2001.render(),
                   'outputliteracyGraph': chartObj1.render(), 'outputliteracyGraph2011': chartObj2.render(), 'outputliteracyGraph2011Sorted': chartObj3.render(),}) #'listSortedPredicted':listSorted.render()})


def Sort(sub_li):
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of
    # sublist lambda has been used
    sub_li.sort(key=lambda x: x[1])
    return sub_li