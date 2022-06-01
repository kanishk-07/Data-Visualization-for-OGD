from django.shortcuts import render
from collections import OrderedDict
from fusioncharts import FusionCharts
import commonFunctions

serviceUrl = ''

def crimeandliteracy(request):
    #rawData = commonFunctions.downloadData(serviceUrl)
    #js = commonFunctions.loadJson(rawData)
    #data = js['records']
    js = {"records": [
        {"states_uts": "Andaman & Nicobar Islands", "crimeRates": "452.9", "literacyRates": "86.27", "projects": "16"},
        {"states_uts": "Andhra Pradesh", "crimeRates": "250.1", "literacyRates": "67.35", "projects": "16"},
        {"states_uts": "Arunachal Pradesh", "crimeRates": "204.5", "literacyRates": "66.95", "projects": "1"},
        {"states_uts": "Assam", "crimeRates": "328.5", "literacyRates": "73.18", "projects": "11"},
        {"states_uts": "Bihar", "crimeRates": "181.9", "literacyRates": "63.82", "projects": "15"},
        {"states_uts": "Chhattisgarh", "crimeRates": "323.9", "literacyRates": "71.04", "projects": "7"},
        {"states_uts": "Goa", "crimeRates": "186.2", "literacyRates": "87.40", "projects": "1"},
        {"states_uts": "Gujarat", "crimeRates": "690.3", "literacyRates": "79.31", "projects": "27"},
        {"states_uts": "Haryana", "crimeRates": "518.3", "literacyRates": "76.64", "projects": "2"},
        {"states_uts": "Himachal Pradesh", "crimeRates": "242.3", "literacyRates": "83.78", "projects": "36"},
        {"states_uts": "Jammu & Kashmir", "crimeRates": "213.7", "literacyRates": "68.74", "projects": "2"},
        {"states_uts": "Jharkhand", "crimeRates": "141.5", "literacyRates": "67.63", "projects": "10"},
        {"states_uts": "Karnataka", "crimeRates": "286.8", "literacyRates": "75.60", "projects": "57"},
        {"states_uts": "Kerala", "crimeRates": "893.4", "literacyRates": "93.91", "projects": "15"},
        {"states_uts": "Madhya Pradesh", "crimeRates": "466.6", "literacyRates": "70.63", "projects": "20"},
        {"states_uts": "Maharashtra", "crimeRates": "357.4", "literacyRates": "82.91", "projects": "102"},
        {"states_uts": "Manipur", "crimeRates": "157.6", "literacyRates": "79.85", "projects": "3"},
        {"states_uts": "Meghalaya", "crimeRates": "128.8", "literacyRates": "75.48", "projects": "2"},
        {"states_uts": "Mizoram", "crimeRates": "261.7", "literacyRates": "91.58", "projects": "2"},
        {"states_uts": "Nagaland", "crimeRates": "79.8", "literacyRates": "80.11", "projects": "2"},
        {"states_uts": "Odisha", "crimeRates": "243.2", "literacyRates": "73.45", "projects": "5"},
        {"states_uts": "Punjab", "crimeRates": "197.7", "literacyRates": "76.68", "projects": "13"},
        {"states_uts": "Rajasthan", "crimeRates": "342.7", "literacyRates": "67.06", "projects": "34"},
        {"states_uts": "Sikkim", "crimeRates": "156.9", "literacyRates": "82.20", "projects": "2"},
        {"states_uts": "Tamil Nadu", "crimeRates": "672.3", "literacyRates": "80.33", "projects": "53"},
        {"states_uts": "Telangana", "crimeRates": "326.4", "literacyRates": "66.5", "projects": "11"},
        {"states_uts": "Tripura", "crimeRates": "106.3", "literacyRates": "87.75", "projects": "2"},
        {"states_uts": "Uttar Pradesh", "crimeRates": "225.3", "literacyRates": "69.72", "projects": "11"},
        {"states_uts": "Uttarakhand", "crimeRates": "150.5", "literacyRates": "79.63", "projects": "16"},
        {"states_uts": "West Bengal", "crimeRates": "217.8", "literacyRates": "77.08", "projects": "10"}]}
    data = js["records"]

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
    mapConfig["caption"] = "Crime Rates of States"
    mapConfig["subcaption"] = "2017"
    mapConfig["connectorcolor"] = "#FDFDB7"
    mapConfig["fillalpha"] = "80"
    mapConfig["entityFillHoverColor"] = "#dddddd"
    mapConfig["theme"] = "fusion"

    colorDataObj = {
        "minvalue": "0",
        "code": "#FFE0B2",
        "gradient": "1",
        "color": [{
            "minValue": "70",
            "maxValue": "170",
            "code": "#f4fdff"
        },
            {
                "minValue": "170",
                "maxValue": "270",
                "code": "#c0dae0"
            },
            {
                "minValue": "270",
                "maxValue": "370",
                "code": "#8bc8d6"
            },
            {
                "minValue": "370",
                "maxValue": "470",
                "code": "#57b6cc"
            },
            {
                "minValue": "470",
                "maxValue": "570",
                "code": "#037db7"
            },
            {
                "minValue": "570",
                "maxValue": "700",
                "code": "#0365b7"
            },
            {
                "minValue": "700",
                "maxValue": "900",
                "code": "#013159"
            }
        ]
    }

    for i in range(len(data)):
        stateName = data[i]["states_uts"]
        commonFunctions.stateDictionary[stateName][0] = float(data[i]["crimeRates"])
        commonFunctions.stateDictionary[stateName][1] = data[i]["literacyRates"]

    mapDataArray = [
        ["001", str(commonFunctions.stateDictionary["Andaman & Nicobar Islands"][0]), "1"],
        ["002", str(commonFunctions.stateDictionary["Andhra Pradesh"][0]), "1"],  # AP
        ["003", str(commonFunctions.stateDictionary["Arunachal Pradesh"][0]), "1"],  # AR
        ["004", str(commonFunctions.stateDictionary["Assam"][0]), "1"],  # AS
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
        ["018", str(commonFunctions.stateDictionary["Kerala"][0]), "1"],  # KE
        ["020", str(commonFunctions.stateDictionary["Madhya Pradesh"][0]), "1"],  # MP
        ["021", str(commonFunctions.stateDictionary["Maharashtra"][0]), "1"],  # MA
        ["022", str(commonFunctions.stateDictionary["Manipur"][0]), "1"],  # MN
        ["023", str(commonFunctions.stateDictionary["Meghalaya"][0]), "1"],  # ME
        ["024", str(commonFunctions.stateDictionary["Mizoram"][0]), "1"],  # MI
        ["025", str(commonFunctions.stateDictionary["Nagaland"][0]), "1"],  # NA
        ["026", str(commonFunctions.stateDictionary["Odisha"][0]), "1"],  # OR
        ["028", str(commonFunctions.stateDictionary["Punjab"][0]), "1"],  # PU
        ["029", str(commonFunctions.stateDictionary["Rajasthan"][0]), "1"],  # RA
        ["030", str(commonFunctions.stateDictionary["Sikkim"][0]), "1"],  # SI
        ["031", str(commonFunctions.stateDictionary["Tamil Nadu"][0]), "1"],  # TN
        ["032", str(commonFunctions.stateDictionary["Tripura"][0]), "1"],  # TR
        ["036", str(commonFunctions.stateDictionary["Telangana"][0]), "1"],  # TG
        ["033", str(commonFunctions.stateDictionary["Uttar Pradesh"][0]), "1"],  # UP
        ["034", str(commonFunctions.stateDictionary["Uttarakhand"][0]), "1"],  # UT
        ["035", str(commonFunctions.stateDictionary["West Bengal"][0]), "1"]  # WB
    ]
    dataSource = OrderedDict()
    dataSource["chart"] = mapConfig
    dataSource["colorrange"] = colorDataObj
    dataSource["data"] = commonFunctions.makeDataSourceForChloroplethMap(mapDataArray)

    fusionMap1 = FusionCharts("maps/india", "demoMap1", "600", "600", "crimeRateMap", "json", dataSource)

    chartObj2 = FusionCharts('scrollcombidy2d', 'graph2', '600', '600', 'literacyRateGraph', 'json', """{
                      "chart": {
                        "caption": "Literacy Rates from 2011",
                        "subcaption": "",
                        "yaxisname": "Percentage(%)",
                        "syaxisname": "Crime Rate",
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
                          "seriesname": "Literacy Rate",
                          "plottooltext": "Value: $dataValue%",
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
                        },
                        {
                            "seriesname": "Crime Rates of States",
                            "parentyaxis": "S",
                            "renderas": "line",
                            "plottooltext": "$dataValue",
                            "showvalues": "0",
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

    return render(request, 'crimeAndLitearcy.html', {'outputCrimeRate':fusionMap1.render(), 'outputLiteracy':chartObj2.render()})