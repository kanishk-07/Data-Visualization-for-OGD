from django.shortcuts import render
from collections import OrderedDict
from fusioncharts import FusionCharts
import commonFunctions

serviceUrl = 'https://api.data.gov.in/resource/1fa8f9d2-c88e-4908-81b9-f6edca4b7799?api-key=<< api key >>&format=json'

def WaterBornDisease(request):
    rawData = commonFunctions.downloadData(serviceUrl)
    js = commonFunctions.loadJson(rawData)
    data = js['records']
    #js = {"records": [
    #    {"states_uts": "Andaman & Nicobar Islands", "Expenditure": "0.43", "Cases": "15.357", "projects": "16"},
    #    {"states_uts": "Andhra Pradesh", "Expenditure": "159.51", "Cases": "1163.707", "projects": "16"},
    #    {"states_uts": "Arunachal Pradesh", "Expenditure": "77.51", "Cases": "23.888", "projects": "1"},
    #    {"states_uts": "Assam", "Expenditure": "524.1", "Cases": "165.347", "projects": "11"},
    #    {"states_uts": "Bihar", "Expenditure": "394.53", "Cases": "309.289", "projects": "15"},
    #    {"states_uts": "Chhattisgarh", "Expenditure": "64.33", "Cases": "180.398", "projects": "7"},
    #    {"states_uts": "Goa", "Expenditure": "2.32", "Cases": "20.706", "projects": "1"},
    #    {"states_uts": "Gujarat", "Expenditure": "231.62", "Cases": "667.459", "projects": "27"},
    #    {"states_uts": "Haryana", "Expenditure": "118.95", "Cases": "236.752", "projects": "2"},
    #    {"states_uts": "Himachal Pradesh", "Expenditure": "66.02", "Cases": "314.463", "projects": "36"},
    #    {"states_uts": "Jammu & Kashmir", "Expenditure": "222.26", "Cases": "512.376", "projects": "2"},
    #    {"states_uts": "Jharkhand", "Expenditure": "172.68", "Cases": "91.326", "projects": "10"},
    #    {"states_uts": "Karnataka", "Expenditure": "290.86", "Cases": "917.488", "projects": "57"},
    #    {"states_uts": "Kerala", "Expenditure": "56.88", "Cases": "452.859", "projects": "15"},
    #    {"states_uts": "Madhya Pradesh", "Expenditure": "195.67", "Cases": "698.396", "projects": "20"},
    #    {"states_uts": "Maharashtra", "Expenditure": "338.13", "Cases": "611.920", "projects": "102"},
    #    {"states_uts": "Manipur", "Expenditure": "32.2", "Cases": "32.085", "projects": "3"},
    #    {"states_uts": "Meghalaya", "Expenditure": "41.86", "Cases": "124.461", "projects": "2"},
    #    {"states_uts": "Mizoram", "Expenditure": "22.4", "Cases": "15.885", "projects": "2"},
    #    {"states_uts": "Nagaland", "Expenditure": "27.66", "Cases": "14.638", "projects": "2"},
    #    {"states_uts": "Odisha", "Expenditure": "102.69", "Cases": "626.421", "projects": "5"},
    #    {"states_uts": "Punjab", "Expenditure": "115.25", "Cases": "203.510", "projects": "13"},
    #    {"states_uts": "Rajasthan", "Expenditure": "891.95", "Cases": "971.113", "projects": "34"},
    #    {"states_uts": "Sikkim", "Expenditure": "9.3", "Cases": "39.624", "projects": "2"},
    #    {"states_uts": "Tamil Nadu", "Expenditure": "121.67", "Cases": "407.678", "projects": "53"},
    #    {"states_uts": "Telangana", "Expenditure": "775.01", "Cases": "487.099", "projects": "11"},
    #    {"states_uts": "Tripura", "Expenditure": "32.26", "Cases": "77.434", "projects": "2"},
    #    {"states_uts": "Uttar Pradesh", "Expenditure": "539.09", "Cases": "1219.071", "projects": "11"},
    #    {"states_uts": "Uttarakhand", "Expenditure": "68.42", "Cases": "98.780", "projects": "16"},
    #    {"states_uts": "West Bengal", "Expenditure": "810.48", "Cases": "1888.794", "projects": "10"}]}
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
    mapConfig["numberprefix"] = "$"
    mapConfig["caption"] = "Funds Allocated for Drinking Water"
    mapConfig["subcaption"] = "2017-18 (in billions)"
    mapConfig["connectorcolor"] = "#FDFDB7"
    mapConfig["fillalpha"] = "80"
    mapConfig["entityFillHoverColor"] = "#dddddd"
    mapConfig["theme"] = "fusion"

    colorDataObj = {
        "minvalue": "0",
        "code": "#FFE0B2",
        "gradient": "1",
        "color": [{
            "minValue": "0",
            "maxValue": "128",
            "code": "#f4fdff"
        },
            {
                "minValue": "128",
                "maxValue": "256",
                "code": "#c0dae0"
            },
            {
                "minValue": "256",
                "maxValue": "384",
                "code": "#8bc8d6"
            },
            {
                "minValue": "384",
                "maxValue": "512",
                "code": "#57b6cc"
            },
            {
                "minValue": "512",
                "maxValue": "640",
                "code": "#037db7"
            },
            {
                "minValue": "640",
                "maxValue": "768",
                "code": "#0365b7"
            },
            {
                "minValue": "768",
                "maxValue": "896",
                "code": "#013159"
            }
        ]
    }

    for i in range(len(data)):
        stateName = data[i]["states_uts"]
        commonFunctions.stateDictionary[stateName][0] = float(data[i]["Cases"])
        commonFunctions.stateDictionary[stateName][1] = data[i]["Expenditure"]

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
        ["036", str(commonFunctions.stateDictionary["Telangana"][1]), "1"],  # TG
        ["033", str(commonFunctions.stateDictionary["Uttar Pradesh"][1]), "1"],  # UP
        ["034", str(commonFunctions.stateDictionary["Uttarakhand"][1]), "1"],  # UT
        ["035", str(commonFunctions.stateDictionary["West Bengal"][1]), "1"]  # WB
    ]
    dataSource = OrderedDict()
    dataSource["chart"] = mapConfig
    dataSource["colorrange"] = colorDataObj
    dataSource["data"] = commonFunctions.makeDataSourceForChloroplethMap(mapDataArray)

    fusionMap1 = FusionCharts("maps/india", "demoMap1", "600", "600", "AllocatedBudgetMap", "json", dataSource)

    chartObj2 = FusionCharts('scrollcombidy2d', 'graph2', '600', '600', 'CasesGraph', 'json', """{
                      "chart": {
                        "caption": "Budget and Cases registered for diarrhoea",
                        "subcaption": "",
                        "yaxisname": "Cases per thousand",
                        "syaxisname": "Billion",
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
                          "seriesname": "Cases Registered per thousand",
                          "plottooltext": "Value: $dataValue",
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
                        },
                        {
                            "seriesname": "Budget Allocated",
                            "parentyaxis": "S",
                            "renderas": "line",
                            "plottooltext": "$dataValue$",
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
                  "value": """ + '"' + str(commonFunctions.stateDictionary["Telangana"][1]) + '"' + """
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

    return render(request, 'WaterBornDisease.html', {'outputAllocatedBudget':fusionMap1.render(), 'outputCases':chartObj2.render()})
