from django.shortcuts import render
from collections import OrderedDict
from fusioncharts import FusionCharts
import commonFunctions

serviceUrl = 'https://api.data.gov.in/resource/023681b2-24e1-41e1-a34b-8f6bfaa29b94?api-key=<< place api key here >>&format=json'

def UnemploymentandEconomicOutput(request):
    rawData = commonFunctions.downloadData(serviceUrl)
    js = commonFunctions.loadJson(rawData)
    data = js['records']
    #js = {"records": [
    #    {"states_uts": "Andaman & Nicobar Islands", "UnemploymentRates": "15.8", "EconomicOutput": "20.71", "projects": "16"},
    #    {"states_uts": "Andhra Pradesh", "UnemploymentRates": "4.5", "EconomicOutput": "16.31", "projects": "16"},
    #    {"states_uts": "Arunachal Pradesh", "UnemploymentRates": "5.9", "EconomicOutput": "15.94", "projects": "1"},
    #    {"states_uts": "Assam", "UnemploymentRates": "8.1", "EconomicOutput": "9.25", "projects": "11"},
    #   {"states_uts": "Bihar", "UnemploymentRates": "7.2", "EconomicOutput": "4.66", "projects": "15"},
    #    {"states_uts": "Chhattisgarh", "UnemploymentRates": "3.3", "EconomicOutput": "11.12", "projects": "7"},
    #    {"states_uts": "Goa", "UnemploymentRates": "13.9", "EconomicOutput": "48.35", "projects": "1"},
    #    {"states_uts": "Gujarat", "UnemploymentRates": "4.8", "EconomicOutput": "21.7", "projects": "27"},
    #    {"states_uts": "Haryana", "UnemploymentRates": "8.6", "EconomicOutput": "24.69", "projects": "2"},
    #    {"states_uts": "Himachal Pradesh", "UnemploymentRates": "5.5", "EconomicOutput": "20.5", "projects": "36"},
    #    {"states_uts": "Jammu & Kashmir", "UnemploymentRates": "5.3", "EconomicOutput": "11.00", "projects": "2"},
    #    {"states_uts": "Jharkhand", "UnemploymentRates": "7.7", "EconomicOutput": "8.37", "projects": "10"},
    #    {"states_uts": "Karnataka", "UnemploymentRates": "4.8", "EconomicOutput": "22.08", "projects": "57"},
    #    {"states_uts": "Kerala", "UnemploymentRates": "11.4", "EconomicOutput": "20.9", "projects": "15"},
    #    {"states_uts": "Madhya Pradesh", "UnemploymentRates": "4.5", "EconomicOutput": "10.03", "projects": "20"},
    #    {"states_uts": "Maharashtra", "UnemploymentRates": "4.9", "EconomicOutput": "21.4", "projects": "102"},
    #    {"states_uts": "Manipur", "UnemploymentRates": "11.6", "EconomicOutput": "8.8", "projects": "3"},
    #    {"states_uts": "Meghalaya", "UnemploymentRates": "1.5", "EconomicOutput": "10.3", "projects": "2"},
    #    {"states_uts": "Mizoram", "UnemploymentRates": "10.1", "EconomicOutput": "17.8", "projects": "2"},
    #    {"states_uts": "Nagaland", "UnemploymentRates": "21.4", "EconomicOutput": "12.2", "projects": "2"},
    #    {"states_uts": "Odisha", "UnemploymentRates": "7.1", "EconomicOutput": "10.4", "projects": "5"},
    #    {"states_uts": "Punjab", "UnemploymentRates": "7.8", "EconomicOutput": "17.2", "projects": "13"},
    #    {"states_uts": "Rajasthan", "UnemploymentRates": "5.0", "EconomicOutput": "12.17", "projects": "34"},
    #    {"states_uts": "Sikkim", "UnemploymentRates": "3.5", "EconomicOutput": "38.6", "projects": "2"},
    #    {"states_uts": "Tamil Nadu", "UnemploymentRates": "7.6", "EconomicOutput": "20.2", "projects": "53"},
    #   {"states_uts": "Telangana", "UnemploymentRates": "7.6", "EconomicOutput": "19.01", "projects": "11"},
    #    {"states_uts": "Tripura", "UnemploymentRates": "6.8", "EconomicOutput": "12.5", "projects": "2"},
    #    {"states_uts": "Uttar Pradesh", "UnemploymentRates": "6.4", "EconomicOutput": "6.8", "projects": "11"},
    #    {"states_uts": "Uttarakhand", "UnemploymentRates": "7.6", "EconomicOutput": "22.02", "projects": "16"},
    #    {"states_uts": "West Bengal", "UnemploymentRates": "4.6", "EconomicOutput": "10.9", "projects": "10"}]}
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
    mapConfig["caption"] = "Economic Output of States 2017-18"
    mapConfig["subcaption"] = "Percent GDP(in hundred million)"
    mapConfig["connectorcolor"] = "#FDFDB7"
    mapConfig["fillalpha"] = "80"
    mapConfig["entityFillHoverColor"] = "#dddddd"
    mapConfig["theme"] = "fusion"

    colorDataObj = {
        "minvalue": "0",
        "code": "#FFE0B2",
        "gradient": "1",
        "color": [{
            "minValue": "6",
            "maxValue": "12",
            "code": "#f4fdff"
        },
            {
                "minValue": "12",
                "maxValue": "18",
                "code": "#c0dae0"
            },
            {
                "minValue": "18",
                "maxValue": "24",
                "code": "#8bc8d6"
            },
            {
                "minValue": "24",
                "maxValue": "30",
                "code": "#57b6cc"
            },
            {
                "minValue": "30",
                "maxValue": "36",
                "code": "#037db7"
            },
            {
                "minValue": "36",
                "maxValue": "42",
                "code": "#0365b7"
            },
            {
                "minValue": "42",
                "maxValue": "49",
                "code": "#013159"
            }
        ]
    }

    for i in range(len(data)):
        stateName = data[i]["states_uts"]
        commonFunctions.stateDictionary[stateName][0] = float(data[i]["UnemploymentRates"])
        commonFunctions.stateDictionary[stateName][1] = data[i]["EconomicOutput"]

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

    fusionMap1 = FusionCharts("maps/india", "demoMap1", "600", "600", "EconomicOutputMap", "json", dataSource)

    chartObj2 = FusionCharts('scrollcombidy2d', 'graph2', '600', '600', 'UnemploymentRateGraph', 'json', """{
                      "chart": {
                        "caption": "Unemployment Rate and Economic Output",
                        "subcaption": "",
                        "yaxisname": "Percentage(%)",
                        "syaxisname": "Percentage (GDP( in hundred million) / Population)",
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
                          "seriesname": "Unemployment Rate",
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
                        },
                        {
                            "seriesname": "Economic Output Percentage",
                            "parentyaxis": "S",
                            "renderas": "line",
                            "plottooltext": "$dataValue%",
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

    return render(request, 'UnemploymentandEconomicOutput.html', {'outputEconomicOutput':fusionMap1.render(), 'outputUnemploymentRate':chartObj2.render()})
