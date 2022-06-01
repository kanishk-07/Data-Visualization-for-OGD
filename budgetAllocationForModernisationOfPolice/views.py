from django.shortcuts import render
from collections import OrderedDict
from fusioncharts import FusionCharts
import commonFunctions

serviceUrl = '''https://api.data.gov.in/resource/1ee05646-e255-49fb-a6f2-5b4ce69b0aec?api-key=579b464db66ec23bdd000001c8e6c9d6daf34e65556dabe447fd0c35&format=json&offset=0&limit=100'''
#http://www.jsonmate.com/permalink/5cd5701185da04b10bcf81b6

def budgetAllocationPolice(request):
    rawData = commonFunctions.downloadData(serviceUrl)
    js = commonFunctions.loadJson(rawData)
    data = js['records']

    #*****************************Chloropleth Map*****************************#
    mapConfig = OrderedDict()
    mapConfig["animation"] = "0"
    mapConfig["usehovercolor"] = "1"
    mapConfig["showlegend"] = "1"
    mapConfig["legendposition"] = "BOTTOM"
    mapConfig["legendborderalpha"] = "0"
    mapConfig["legendbordercolor"] = "#FDFDB7"
    mapConfig["legendallowdrag"] = "0"
    mapConfig["legendshadow"] = "0"
    mapConfig["numbersuffix"] = "crRs."
    mapConfig["caption"] = "Budget Allocation for Modernisation of Police"
    mapConfig["subcaption"] = "2017-2018"
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
            "maxValue": "15",
            "code": "#f4fdff"
        },
            {
                "minValue": "15",
                "maxValue": "30",
                "code": "#c0dae0"
            },
            {
                "minValue": "30",
                "maxValue": "45",
                "code": "#8bc8d6"
            },
            {
                "minValue": "45",
                "maxValue": "60",
                "code": "#57b6cc"
            },
            {
                "minValue": "60",
                "maxValue": "75",
                "code": "#037db7"
            },
            {
                "minValue": "75",
                "maxValue": "90",
                "code": "#0365b7"
            }
        ]
    }
    # mapDataArray = [
    #     ["002", (str)(((float)(data[0]["current_financial_year_2017_18_allocation_rs_in_crore_"])*10000000)/commonFunctions.populationOfStates["Andhra Pradesh"]), "1"],     #AP
    #     ["003", (str)(((float)(data[1]["current_financial_year_2017_18_allocation_rs_in_crore_"])*10000000)/commonFunctions.populationOfStates["Arunachal Pradesh"]), "1"],     #AR
    #     ["004", (str)(((float)(data[2]["current_financial_year_2017_18_allocation_rs_in_crore_"])*10000000)/commonFunctions.populationOfStates["Assam"]), "1"],     #AS
    #     ["005", (str)(((float)(data[3]["current_financial_year_2017_18_allocation_rs_in_crore_"])*10000000)/commonFunctions.populationOfStates["Bihar"]), "1"],     #BI
    #     ["007", (str)(((float)(data[4]["current_financial_year_2017_18_allocation_rs_in_crore_"])*10000000)/commonFunctions.populationOfStates["Chhattisgarh"]), "1"],     #CA
    #     ["011", (str)(((float)(data[5]["current_financial_year_2017_18_allocation_rs_in_crore_"])*10000000)/commonFunctions.populationOfStates["Goa"]), "1"],     #GO
    #     ["012", (str)(((float)(data[6]["current_financial_year_2017_18_allocation_rs_in_crore_"])*10000000)/commonFunctions.populationOfStates["Gujarat"]), "1"],     #GU
    #     ["013", (str)(((float)(data[7]["current_financial_year_2017_18_allocation_rs_in_crore_"])*10000000)/commonFunctions.populationOfStates["Haryana"]), "1"],     #HA
    #     ["014", (str)(((float)(data[8]["current_financial_year_2017_18_allocation_rs_in_crore_"])*10000000)/commonFunctions.populationOfStates["Himachal Pradesh"]), "1"],     #HP
    #     ["015", (str)(((float)(data[9]["current_financial_year_2017_18_allocation_rs_in_crore_"])*10000000)/commonFunctions.populationOfStates["Jammu & Kashmir"]), "1"],     #JK
    #     ["016", (str)(((float)(data[10]["current_financial_year_2017_18_allocation_rs_in_crore_"])*10000000)/commonFunctions.populationOfStates["Jharkhand"]), "1"],    #JH
    #     ["017", (str)(((float)(data[11]["current_financial_year_2017_18_allocation_rs_in_crore_"])*10000000)/commonFunctions.populationOfStates["Karnataka"]), "1"],    #KA
    #     ["018", (str)(((float)(data[12]["current_financial_year_2017_18_allocation_rs_in_crore_"])*10000000)/commonFunctions.populationOfStates["Kerala"]), "1"],    #KE
    #     ["020", (str)(((float)(data[13]["current_financial_year_2017_18_allocation_rs_in_crore_"])*10000000)/commonFunctions.populationOfStates["Madhya Pradesh"]), "1"],    #MP
    #     ["021", (str)(((float)(data[14]["current_financial_year_2017_18_allocation_rs_in_crore_"])*10000000)/commonFunctions.populationOfStates["Maharashtra"]), "1"],    #MA
    #     ["022", (str)(((float)(data[15]["current_financial_year_2017_18_allocation_rs_in_crore_"])*10000000)/commonFunctions.populationOfStates["Manipur"]), "1"],    #MN
    #     ["023", (str)(((float)(data[16]["current_financial_year_2017_18_allocation_rs_in_crore_"])*10000000)/commonFunctions.populationOfStates["Meghalaya"]), "1"],    #ME
    #     ["024", (str)(((float)(data[17]["current_financial_year_2017_18_allocation_rs_in_crore_"])*10000000)/commonFunctions.populationOfStates["Mizoram"]), "1"],    #MI
    #     ["025", (str)(((float)(data[18]["current_financial_year_2017_18_allocation_rs_in_crore_"])*10000000)/commonFunctions.populationOfStates["Nagaland"]), "1"],    #NA
    #     ["026", (str)(((float)(data[19]["current_financial_year_2017_18_allocation_rs_in_crore_"])*10000000)/commonFunctions.populationOfStates["Odisha"]), "1"],    #OR
    #     ["028", (str)(((float)(data[20]["current_financial_year_2017_18_allocation_rs_in_crore_"])*10000000)/commonFunctions.populationOfStates["Punjab"]), "1"],    #PU
    #     ["029", (str)(((float)(data[21]["current_financial_year_2017_18_allocation_rs_in_crore_"])*10000000)/commonFunctions.populationOfStates["Rajasthan"]), "1"],    #RA
    #     ["030", (str)(((float)(data[22]["current_financial_year_2017_18_allocation_rs_in_crore_"])*10000000)/commonFunctions.populationOfStates["Sikkim"]), "1"],    #SI
    #     ["031", (str)(((float)(data[23]["current_financial_year_2017_18_allocation_rs_in_crore_"])*10000000)/commonFunctions.populationOfStates["Tamil Nadu"]), "1"],    #TN
    #     ["032", (str)(((float)(data[24]["current_financial_year_2017_18_allocation_rs_in_crore_"])*10000000)/commonFunctions.populationOfStates["Tripura"]), "1"],    #TR
    #     ["036", (str)(((float)(data[25]["current_financial_year_2017_18_allocation_rs_in_crore_"])*10000000)/commonFunctions.populationOfStates["Telangana"]), "1"],    #TG
    #     ["033", (str)(((float)(data[26]["current_financial_year_2017_18_allocation_rs_in_crore_"])*10000000)/commonFunctions.populationOfStates["Uttar Pradesh"]), "1"],    #UP
    #     ["034", (str)(((float)(data[27]["current_financial_year_2017_18_allocation_rs_in_crore_"])*10000000)/commonFunctions.populationOfStates["Uttarakhand"]), "1"],    #UT
    #     ["035", (str)(((float)(data[28]["current_financial_year_2017_18_allocation_rs_in_crore_"])*10000000)/commonFunctions.populationOfStates["West Bengal"]), "1"],    #WB
    # ]

    mapDataArray = [
        ["002", data[0]["current_financial_year_2017_18_allocation_rs_in_crore_"], "1"],  # AP
        ["003", data[1]["current_financial_year_2017_18_allocation_rs_in_crore_"], "1"],  # AR
        ["004", data[2]["current_financial_year_2017_18_allocation_rs_in_crore_"], "1"],  # AS
        ["005", data[3]["current_financial_year_2017_18_allocation_rs_in_crore_"], "1"],  # BI
        ["007", data[4]["current_financial_year_2017_18_allocation_rs_in_crore_"], "1"],  # CA
        ["011", data[5]["current_financial_year_2017_18_allocation_rs_in_crore_"], "1"],  # GO
        ["012", data[6]["current_financial_year_2017_18_allocation_rs_in_crore_"], "1"],  # GU
        ["013", data[7]["current_financial_year_2017_18_allocation_rs_in_crore_"], "1"],  # HA
        ["014", data[8]["current_financial_year_2017_18_allocation_rs_in_crore_"], "1"],  # HP
        ["015", data[9]["current_financial_year_2017_18_allocation_rs_in_crore_"], "1"],  # JK
        ["016", data[10]["current_financial_year_2017_18_allocation_rs_in_crore_"], "1"],  # JH
        ["017", data[11]["current_financial_year_2017_18_allocation_rs_in_crore_"], "1"],  # KA
        ["018", data[12]["current_financial_year_2017_18_allocation_rs_in_crore_"], "1"],  # KE
        ["020", data[13]["current_financial_year_2017_18_allocation_rs_in_crore_"], "1"],  # MP
        ["021", data[14]["current_financial_year_2017_18_allocation_rs_in_crore_"], "1"],  # MA
        ["022", data[15]["current_financial_year_2017_18_allocation_rs_in_crore_"], "1"],  # MN
        ["023", data[16]["current_financial_year_2017_18_allocation_rs_in_crore_"], "1"],  # ME
        ["024", data[17]["current_financial_year_2017_18_allocation_rs_in_crore_"], "1"],  # MI
        ["025", data[18]["current_financial_year_2017_18_allocation_rs_in_crore_"], "1"],  # NA
        ["026", data[19]["current_financial_year_2017_18_allocation_rs_in_crore_"], "1"],  # OR
        ["028", data[20]["current_financial_year_2017_18_allocation_rs_in_crore_"], "1"],  # PU
        ["029", data[21]["current_financial_year_2017_18_allocation_rs_in_crore_"], "1"],  # RA
        ["030", data[22]["current_financial_year_2017_18_allocation_rs_in_crore_"], "1"],  # SI
        ["031", data[23]["current_financial_year_2017_18_allocation_rs_in_crore_"], "1"],  # TN
        ["032", data[24]["current_financial_year_2017_18_allocation_rs_in_crore_"], "1"],  # TR
        ["036", data[25]["current_financial_year_2017_18_allocation_rs_in_crore_"], "1"],  # TG
        ["033", data[26]["current_financial_year_2017_18_allocation_rs_in_crore_"], "1"],  # UP
        ["034", data[27]["current_financial_year_2017_18_allocation_rs_in_crore_"], "1"],  # UT
        ["035", data[28]["current_financial_year_2017_18_allocation_rs_in_crore_"], "1"]  # WB
    ]

    dataSource = OrderedDict()
    dataSource["chart"] = mapConfig
    dataSource["colorrange"] = colorDataObj
    dataSource["data"] = commonFunctions.makeDataSourceForChloroplethMap(mapDataArray)

    fusionMap = FusionCharts("maps/india", "demoMap1", "600", "600", "myFirstchart-container", "json", dataSource)

    #********************************Bar Chart******************************#
    listData = []
    for i in range(len(mapDataArray)):
        listData.append({"value": mapDataArray[i][1]})
    string1 = """{
          "chart": {
            "caption": "Budget for Modernisation of Police and Crime Rates in 2017",
            "subcaption": "By States",
            "yaxisname": "Count",
            "labeldisplay": "auto",
            "theme": "fusion",
            "numvisibleplot": "8"
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
                  "label": "Chhattisgarh"
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
                  "label": "Uttarakhand"
                },
                {
                  "label": "West Bengal"
                }
              ]
            }
          ],
          "dataset": [
            {
              "seriesname": "Budget Allocated",
              "data": """
    string2 = str(listData)
    string3 = """},
            {
              "seriesname": "Crime Rate per 10 thousand people in population",
              "data": [
                {
                  "value": "22.4"
                },
                {
                  "value": "19.2"
                },
                {
                  "value": "25.0"
                },
                {
                  "value": "12.7"
                },
                {
                  "value": "22.1"
                },
                {
                  "value": "19.6"
                },
                {
                  "value": "21.6"
                },
                {
                  "value": "24.0"
                },
                {
                  "value": "18.2"
                },
                {
                  "value": "20.6"
                },
                {
                  "value": "14.7"
                },
                {
                  "value": "22.2"
                },
                {
                  "value": "45.5"
                },
                {
                  "value": "29.8"
                },
                {
                  "value": "17.6"
                },
                {
                  "value": "15.0"
                },
                {
                  "value": "9.6"
                },
                {
                  "value": "17.6"
                },
                {
                  "value": "4.7"
                },
                {
                  "value": "16.4"
                },
                {
                  "value": "12.7"
                },
                {
                  "value": "24.6"
                },
                {
                  "value": "8.4"
                },
                {
                  "value": "29.4"
                },
                {
                  "value": "17.0"
                },
                {
                  "value": "8.9"
                },
                {
                  "value": "9.6"
                },
                {
                  "value": "8.7"
                },
                {
                  "value": "17.8"
                }
              ]
            }
          ]
        }"""
    chartObj = FusionCharts('scrollcolumn2d', 'ex1', '600', '600', 'myBarChart-container', 'json', string1+string2+string3)

    return render(request, 'budgetAllocationPolice.html', {'output': fusionMap.render(), 'output1':chartObj.render()})