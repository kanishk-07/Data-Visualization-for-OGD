from django.shortcuts import render
from collections import OrderedDict
from fusioncharts import FusionCharts
import commonFunctions

serviceUrl = 'https://api.data.gov.in/resource/9fcce189-8a67-485f-8c86-a12b6e64882d?api-key=<< place your api key >>&format=json'

def PollutionAndVehicles(request):
    rawData = commonFunctions.downloadData(serviceUrl)
    js = commonFunctions.loadJson(rawData)
    data = js['records']
    #js = {"records": [
    #    {"states_uts": "Andaman & Nicobar Islands", "Vehicles": "69", "Pollution": "2", "projects": "16"},
    #    {"states_uts": "Andhra Pradesh", "Vehicles": "10189", "Pollution": "19", "projects": "16"},
    #    {"states_uts": "Arunachal Pradesh", "Vehicles": "145", "Pollution": "4", "projects": "1"},
    #    {"states_uts": "Assam", "Vehicles": "1582", "Pollution": "14", "projects": "11"},
    #    {"states_uts": "Bihar", "Vehicles": "2673", "Pollution": "47", "projects": "15"},
    #    {"states_uts": "Chhattisgarh", "Vehicles": "2766", "Pollution": "27", "projects": "7"},
    #    {"states_uts": "Goa", "Vehicles": "790", "Pollution": "18", "projects": "1"},
    #    {"states_uts": "Gujarat", "Vehicles": "12993", "Pollution": "25", "projects": "27"},
    #    {"states_uts": "Haryana", "Vehicles": "5377", "Pollution": "25", "projects": "2"},
    #    {"states_uts": "Himachal Pradesh", "Vehicles": "622", "Pollution": "12", "projects": "36"},
    #    {"states_uts": "Jammu & Kashmir", "Vehicles": "927", "Pollution": "12", "projects": "2"},
    #    {"states_uts": "Jharkhand", "Vehicles": "3113", "Pollution": "39", "projects": "10"},
    #    {"states_uts": "Karnataka", "Vehicles": "9930", "Pollution": "21", "projects": "57"},
    #    {"states_uts": "Kerala", "Vehicles": "6072", "Pollution": "14", "projects": "15"},
    #    {"states_uts": "Madhya Pradesh", "Vehicles": "7356", "Pollution": "18", "projects": "20"},
    #    {"states_uts": "Maharashtra", "Vehicles": "17434", "Pollution": "33", "projects": "102"},
    #    {"states_uts": "Manipur", "Vehicles": "207", "Pollution": "5", "projects": "3"},
    #    {"states_uts": "Meghalaya", "Vehicles": "176", "Pollution": "10", "projects": "2"},
    #    {"states_uts": "Mizoram", "Vehicles": "93", "Pollution": "4", "projects": "2"},
    #    {"states_uts": "Nagaland", "Vehicles": "273", "Pollution": "6", "projects": "2"},
    #    {"states_uts": "Odisha", "Vehicles": "3338", "Pollution": "19", "projects": "5"},
    #    {"states_uts": "Punjab", "Vehicles": "5274", "Pollution": "26", "projects": "13"},
    #    {"states_uts": "Rajasthan", "Vehicles": "7986", "Pollution": "31", "projects": "34"},
    #    {"states_uts": "Sikkim", "Vehicles": "39", "Pollution": "1", "projects": "2"},
    #    {"states_uts": "Tamil Nadu", "Vehicles": "15638", "Pollution": "22", "projects": "53"},
    #    {"states_uts": "Tripura", "Vehicles": "188", "Pollution": "4.5", "projects": "2"},
    #    {"states_uts": "Uttar Pradesh", "Vehicles": "13287", "Pollution": "30", "projects": "11"},
    #    {"states_uts": "Uttarakhand", "Vehicles": "997", "Pollution": "24", "projects": "16"},
    #    {"states_uts": "West Bengal", "Vehicles": "3261", "Pollution": "57", "projects": "10"}]}
    #data = js["records"]

    # *****************************Chloropleth Map*****************************#
    mapConfig = OrderedDict()
    mapConfig["animation"] = "0"
    mapConfig["usehovercolor"] = "1"
    mapConfig["showlegend"] = "1"
    mapConfig["legendposition"] = "BOTTOM"
    mapConfig["legendborderalpha"] = "0"
    mapConfig["legendbordercolor"] = "#FDFDB7"
    mapConfig["legendallowdrag"] = "0"
    mapConfig["legendshadow"] = "0"
    #mapConfig["numbersuffix"] = "crRs."
    mapConfig["caption"] = "Vehicles Registered"
    mapConfig["subcaption"] = "2011"
    mapConfig["connectorcolor"] = "#FDFDB7"
    mapConfig["fillalpha"] = "80"
    mapConfig["entityFillHoverColor"] = "#dddddd"
    mapConfig["theme"] = "fusion"

    colorDataObj = {
        "minvalue": "0",
        "code": "#FFE0B2",
        "gradient": "1",
        "color": [{
            "minValue": "39",
            "maxValue": "2524",
            "code": "#f4fdff"
        },
            {
                "minValue": "2524",
                "maxValue": "5009",
                "code": "#c0dae0"
            },
            {
                "minValue": "5009",
                "maxValue": "7494",
                "code": "#8bc8d6"
            },
            {
                "minValue": "7494",
                "maxValue": "9979",
                "code": "#57b6cc"
            },
            {
                "minValue": "9979",
                "maxValue": "12464",
                "code": "#037db7"
            },
            {
                "minValue": "12464",
                "maxValue": "14949",
                "code": "#0365b7"
            },
            {
                "minValue": "14949",
                "maxValue": "17434",
                "code": "#013159"
            }
        ]
    }

    for i in range(len(data)):
        stateName = data[i]["states_uts"]
        commonFunctions.stateDictionary[stateName][0] = float(data[i]["Pollution"])
        commonFunctions.stateDictionary[stateName][1] = data[i]["Vehicles"]

    mapDataArray = [
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
        ["033", str(commonFunctions.stateDictionary["Uttar Pradesh"][1]), "1"],  # UP
        ["034", str(commonFunctions.stateDictionary["Uttarakhand"][1]), "1"],  # UT
        ["035", str(commonFunctions.stateDictionary["West Bengal"][1]), "1"]  # WB
    ]
    dataSource = OrderedDict()
    dataSource["chart"] = mapConfig
    dataSource["colorrange"] = colorDataObj
    dataSource["data"] = commonFunctions.makeDataSourceForChloroplethMap(mapDataArray)

    fusionMap1 = FusionCharts("maps/india", "demoMap1", "600", "600", "VehiclesMap", "json", dataSource)

    chartObj2 = FusionCharts('scrollcombidy2d', 'graph2', '600', '600', 'PollutionGraph', 'json', """{
                      "chart": {
                        "caption": "Concentration of NO2 in air to vehicles registered",
                        "subcaption": "",
                        "yaxisname": "Annual Average(µg/m³)",
                        "syaxisname": "",
                        "plottooltext": "$dataValue",
                        "labeldisplay": "auto",
                        "numvisibleplot": "6",
                        "drawcrossline": "1",
                        "showvalues":"1",
                        "theme": "fusion",
                        "lineColor": "#f94343"
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
                          "seriesname": "NO2 Concentration",
                          "plottooltext": "$dataValue µg/m³",
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
                              "value": """ + '"' + str(commonFunctions.stateDictionary["Uttar Pradesh"][0]) + '"' + """
                            },
                            {
                              "value": """ + '"' + str(commonFunctions.stateDictionary["Uttarakhand"][0]) + '"' + """
                            },
                            {
                              "value": """ + '"' + str(commonFunctions.stateDictionary["West Bengal"][0]) + '"' + """
                            }
                          ]
                        },
                        {
                            "seriesname": "Vehicles Registered",
                            "parentyaxis": "S",
                            "renderas": "line",
                            "plottooltext": "$dataValue",
                            "showvalues": "0",
                            "data": [
                            {
                                "value": """ + '"' + str(commonFunctions.stateDictionary["Andhra Pradesh"][1]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.stateDictionary["Arunachal Pradesh"][1]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.stateDictionary["Assam"][1]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.stateDictionary["Bihar"][1]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.stateDictionary["Chhattisgarh"][1]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.stateDictionary["Goa"][1]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.stateDictionary["Gujarat"][1]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.stateDictionary["Haryana"][1]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.stateDictionary["Himachal Pradesh"][1]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.stateDictionary["Jammu & Kashmir"][1]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.stateDictionary["Jharkhand"][1]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.stateDictionary["Karnataka"][1]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.stateDictionary["Kerala"][1]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.stateDictionary["Madhya Pradesh"][1]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.stateDictionary["Maharashtra"][1]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.stateDictionary["Manipur"][1]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.stateDictionary["Meghalaya"][1]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.stateDictionary["Mizoram"][1]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.stateDictionary["Nagaland"][1]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.stateDictionary["Odisha"][1]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.stateDictionary["Punjab"][1]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.stateDictionary["Rajasthan"][1]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.stateDictionary["Sikkim"][1]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.stateDictionary["Tamil Nadu"][1]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.stateDictionary["Tripura"][1]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.stateDictionary["Uttar Pradesh"][1]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.stateDictionary["Uttarakhand"][1]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.stateDictionary["West Bengal"][1]) + '"' + """
                }
              ]
            }
                      ]
                }"""
                             )

    return render(request, 'PollutionAndVehicles.html', {'outputVehicles':fusionMap1.render(), 'outputPollution':chartObj2.render()})
