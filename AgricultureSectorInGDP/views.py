from django.shortcuts import render
from collections import OrderedDict
from fusioncharts import FusionCharts
import commonFunctions

serviceUrl = ''

def AgricultureSectorInGDP(request):
    #rawData = commonFunctions.downloadData(serviceUrl)
    #js = commonFunctions.loadJson(rawData)
    #data = js['records']
    js = {"records": [
        {"states_uts": "Andaman & Nicobar Islands", "AgricultureSector": "7.9731", "GDP": "60.32", "projects": "16"},
        {"states_uts": "Andhra Pradesh", "AgricultureSector": "1353.9974", "GDP": "6042.29", "projects": "16"},
        {"states_uts": "Arunachal Pradesh", "AgricultureSector": "60.2349", "GDP": "185.09", "projects": "1"},
        {"states_uts": "Assam", "AgricultureSector": "425.8146", "GDP": "2279.59", "projects": "11"},
        {"states_uts": "Bihar", "AgricultureSector": "824.8625", "GDP": "3716.02", "projects": "15"},
        {"states_uts": "Chhattisgarh", "AgricultureSector": "411.5278", "GDP": "2273.83", "projects": "7"},
        {"states_uts": "Goa", "AgricultureSector": "23.0043", "GDP": "550.54", "projects": "1"},
        {"states_uts": "Gujarat", "AgricultureSector": "1507.9057", "GDP": "10290.10", "projects": "27"},
        {"states_uts": "Haryana", "AgricultureSector": "808.1831", "GDP": "4952.49", "projects": "2"},
        {"states_uts": "Himachal Pradesh", "AgricultureSector": "191.4882", "GDP": "1142.39", "projects": "36"},
        {"states_uts": "Jammu & Kashmir", "AgricultureSector": "185.5851", "GDP": "1171.68", "projects": "2"},
        {"states_uts": "Jharkhand", "AgricultureSector": "299.7585", "GDP": "2066.13", "projects": "10"},
        {"states_uts": "Karnataka", "AgricultureSector": "937.0741", "GDP": "10451.68", "projects": "57"},
        {"states_uts": "Kerala", "AgricultureSector": "521.8703", "GDP": "5619.94", "projects": "15"},
        {"states_uts": "Madhya Pradesh", "AgricultureSector": "1540.6542", "GDP": "5411.89", "projects": "20"},
        {"states_uts": "Maharashtra", "AgricultureSector": "1751.5724", "GDP": "19661.47", "projects": "102"},
        {"states_uts": "Manipur", "AgricultureSector": "41.7052", "GDP": "195.31", "projects": "3"},
        {"states_uts": "Meghalaya", "AgricultureSector": "39.3499", "GDP": "251.17", "projects": "2"},
        {"states_uts": "Mizoram", "AgricultureSector": "40.4820", "GDP": "151.39", "projects": "2"},
        {"states_uts": "Nagaland", "AgricultureSector": "48.0242", "GDP": "195.24", "projects": "2"},
        {"states_uts": "Odisha", "AgricultureSector": "516.9092", "GDP": "3285.50", "projects": "5"},
        {"states_uts": "Punjab", "AgricultureSector": "975.9027", "GDP": "3900.87", "projects": "13"},
        {"states_uts": "Rajasthan", "AgricultureSector": "1866.8612", "GDP": "6814.85", "projects": "34"},
        {"states_uts": "Sikkim", "AgricultureSector": "11.6426", "GDP": "180.34", "projects": "2"},
        {"states_uts": "Tamil Nadu", "AgricultureSector": "1240.4932", "GDP": "11765.00", "projects": "53"},
        {"states_uts": "Telangana", "AgricultureSector": "636.6387", "GDP": "5779.02", "projects": "11"},
        {"states_uts": "Tripura", "AgricultureSector": "73.9076", "GDP": "359.38", "projects": "2"},
        {"states_uts": "Uttar Pradesh", "AgricultureSector": "2657.0057", "GDP": "11372.10", "projects": "11"},
        {"states_uts": "Uttarakhand", "AgricultureSector": "162.2398", "GDP": "1771.63", "projects": "16"},
        {"states_uts": "West Bengal", "AgricultureSector": "1503.3150", "GDP": "7973.00", "projects": "10"}]}
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
    mapConfig["numberprefix"] = "$"
    mapConfig["caption"] = "Value Output through Agriculture Sector (in billions)"
    mapConfig["subcaption"] = "2015-16"
    mapConfig["connectorcolor"] = "#FDFDB7"
    mapConfig["fillalpha"] = "80"
    mapConfig["entityFillHoverColor"] = "#dddddd"
    mapConfig["theme"] = "fusion"

    colorDataObj = {
        "minvalue": "0",
        "code": "#FFE0B2",
        "gradient": "1",
        "color": [{
            "minValue": "8",
            "maxValue": "387",
            "code": "#f4fdff"
        },
            {
                "minValue": "387",
                "maxValue": "766",
                "code": "#c0dae0"
            },
            {
                "minValue": "766",
                "maxValue": "1145",
                "code": "#8bc8d6"
            },
            {
                "minValue": "1145",
                "maxValue": "1524",
                "code": "#57b6cc"
            },
            {
                "minValue": "1524",
                "maxValue": "1903",
                "code": "#037db7"
            },
            {
                "minValue": "1903",
                "maxValue": "2282",
                "code": "#0365b7"
            },
            {
                "minValue": "2282",
                "maxValue": "2661",
                "code": "#013159"
            }
        ]
    }

    for i in range(len(data)):
        stateName = data[i]["states_uts"]
        commonFunctions.stateDictionary[stateName][0] = float(data[i]["GDP"])
        commonFunctions.stateDictionary[stateName][1] = data[i]["AgricultureSector"]

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

    fusionMap1 = FusionCharts("maps/india", "demoMap1", "600", "600", "AgricultureSectorMap", "json", dataSource)

    chartObj2 = FusionCharts('scrollcombidy2d', 'graph2', '600', '600', 'GDPGraph', 'json', """{
                      "chart": {
                        "caption": "Contribution of Agriculture Sector in GDP",
                        "subcaption": "",
                        "yaxisname": "billions",
                        "syaxisname": "billions",
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
                          "seriesname": "State wise GDP",
                          "plottooltext": "$dataValue",
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
                            "seriesname": "Agriculture Sector Output",
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

    return render(request, 'AgricultureSectorInGDP.html', {'outputAgricultureSector':fusionMap1.render(), 'outputGDP':chartObj2.render()})