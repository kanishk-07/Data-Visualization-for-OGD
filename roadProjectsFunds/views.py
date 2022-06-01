from django.shortcuts import render
from collections import OrderedDict
from fusioncharts import FusionCharts
import commonFunctions

urlFunds = "https://api.data.gov.in/resource/8d215449-5b85-4bb9-bda4-b637becd5de3?api-key=<< place api key here >>&format=json&offset=0&limit=100"
urlProjects = "https://api.data.gov.in/resource/f17274ef-4bf3-4390-88ad-4bf80a4d6bd0?api-key=<< place api key here >>&format=json&offset=0&limit=100"
urlLaneWiseLenNH = "https://api.data.gov.in/resource/54864dd4-9e8d-4935-a6fe-aed8c86287b1?api-key=<< place api key here >>&format=json&offset=0&limit=100"

def roadProjectsFunds(request):
    rawData = commonFunctions.downloadData(urlFunds)
    js = commonFunctions.loadJson(rawData)
    data = js['records']
    #js = {"records": [{"states_uts": "Andhra Pradesh", "acq2016-2017": "348.72", "acq2017-2018": "316.45", "projects":"16"},
    #                    {"states_uts": "Arunachal Pradesh", "acq2016-2017": "131.11", "acq2017-2018": "122.47", "projects":"1"},
    #                    {"states_uts": "Assam", "acq2016-2017": "144.08", "acq2017-2018": "134.77", "projects":"11"},
    #                    {"states_uts": "Bihar", "acq2016-2017": "200.46", "acq2017-2018": "190.11", "projects":"15"},
    #                    {"states_uts": "Chhattisgarh", "acq2016-2017": "247.3", "acq2017-2018": "231.16", "projects":"7"},
    #                    {"states_uts": "Goa", "acq2016-2017": "17.08", "acq2017-2018": "16.49", "projects":"1"},
    #                    {"states_uts": "Gujarat", "acq2016-2017": "445.09", "acq2017-2018": "412.84", "projects":"27"},
    #                    {"states_uts": "Haryana", "acq2016-2017": "194.74", "acq2017-2018": "180.11", "projects":"2"},
    #                    {"states_uts": "Himachal Pradesh", "acq2016-2017": "100.91", "acq2017-2018": "94.85", "projects":"36"},
    #                    {"states_uts": "Jammu & Kashmir", "acq2016-2017": "357.32", "acq2017-2018": "332.57", "projects":"2"},
    #                    {"states_uts": "Jharkhand", "acq2016-2017": "164.63", "acq2017-2018": "153.23", "projects":"10"},
    #                    {"states_uts": "Karnataka", "acq2016-2017": "450.95", "acq2017-2018": "430", "projects":"57"},
    #                    {"states_uts": "Kerala", "acq2016-2017": "150.37", "acq2017-2018": "132.69", "projects":"15"},
    #                    {"states_uts": "Madhya Pradesh", "acq2016-2017": "566.39", "acq2017-2018": "525.83", "projects":"20"},
    #                    {"states_uts": "Maharashtra", "acq2016-2017": "717.66", "acq2017-2018": "660.16", "projects":"102"},
    #                    {"states_uts": "Manipur", "acq2016-2017": "37.48", "acq2017-2018": "34.19", "projects":"3"},
    #                    {"states_uts": "Meghalaya", "acq2016-2017": "42.57", "acq2017-2018": "39.05", "projects":"2"},
    #                    {"states_uts": "Mizoram", "acq2016-2017": "34.18", "acq2017-2018": "31.7", "projects":"2"},
    #                    {"states_uts": "Nagaland", "acq2016-2017": "27.42", "acq2017-2018": "29.17", "projects":"2"},
    #                    {"states_uts": "Odisha", "acq2016-2017": "295.71", "acq2017-2018": "279.93", "projects":"5"},
    #                    {"states_uts": "Punjab", "acq2016-2017": "167.04", "acq2017-2018": "156.63", "projects":"13"},
    #                    {"states_uts": "Rajasthan", "acq2016-2017": "663.06", "acq2017-2018": "617.93", "projects":"34"},
    #                    {"states_uts": "Sikkim", "acq2016-2017": "12.63", "acq2017-2018": "11.64", "projects":"2"},
    #                    {"states_uts": "Tamil Nadu", "acq2016-2017": "392.02", "acq2017-2018": "361.19", "projects":"53"},
    #                    {"states_uts": "Telangana", "acq2016-2017": "258.81", "acq2017-2018": "249.13", "projects":"11"},
    #                    {"states_uts": "Tripura", "acq2016-2017": "19.09", "acq2017-2018": "17.54", "projects":"2"},
    #                    {"states_uts": "Uttar Pradesh", "acq2016-2017": "569.23", "acq2017-2018": "587.07", "projects":"11"},
    #                    {"states_uts": "Uttarakhand", "acq2016-2017": "103.68", "acq2017-2018": "96.16", "projects":"16"},
    #                    {"states_uts": "West Bengal", "acq2016-2017": "210.97", "acq2017-2018": "201.66", "projects":"10"} ]}
    #data = js["records"]
    # *****************************Choropleth Map*****************************#

    mapConfig = OrderedDict()
    mapConfig["animation"] = "0"
    mapConfig["usehovercolor"] = "1"
    mapConfig["showlegend"] = "1"
    mapConfig["legendposition"] = "BOTTOM"
    mapConfig["legendborderalpha"] = "0"
    mapConfig["legendbordercolor"] = "#FDFDB7"
    mapConfig["legendallowdrag"] = "0"
    mapConfig["legendshadow"] = "0"
    mapConfig["numbersuffix"] = "cr ₹"
    mapConfig["caption"] = "Budget Acquired For Road Projects"
    mapConfig["subcaption"] = ""
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
            "maxValue": "150",
            "code": "#f4fdff"
        },
            {
                "minValue": "150",
                "maxValue": "300",
                "code": "#c0dae0"
            },
            {
                "minValue": "300",
                "maxValue": "450",
                "code": "#8bc8d6"
            },
            {
                "minValue": "450",
                "maxValue": "600",
                "code": "#57b6cc"
            },
            {
                "minValue": "600",
                "maxValue": "750",
                "code": "#037db7"
            },
            {
                "minValue": "750",
                "maxValue": "900",
                "code": "#0365b7"
            }
        ]
    }

    for i in range(len(data)):
        stateName = data[i]["states_uts"]
        commonFunctions.stateDictionary[stateName][0] = float(data[i]["acq2016-2017"])
        commonFunctions.stateDictionary[stateName][1] = float(data[i]["acq2017-2018"])
        commonFunctions.stateDictionary[stateName][2] = float(data[i]["projects"])
        #commonFunctions.stateDictionary[stateName][3] = float(data[i]["development_of_state_roads_non_rural___ei_isc___alloc_2018_19"])

    # mapDataArray2017_18 = [
    #     ["001", str(commonFunctions.stateDictionary["Andaman & Nicobar Islands"][0] + commonFunctions.stateDictionary["Andaman & Nicobar Islands"][2]), "1"],
    #     ["002", str(commonFunctions.stateDictionary["Andhra Pradesh"][0] + commonFunctions.stateDictionary["Andhra Pradesh"][2]), "1"],  # AP
    #     ["003", str(commonFunctions.stateDictionary["Arunachal Pradesh"][0] + commonFunctions.stateDictionary["Arunachal Pradesh"][2]), "1"],  # AR
    #     ["004", str(commonFunctions.stateDictionary["Assam"][0] + commonFunctions.stateDictionary["Assam"][2]), "1"],  # AS
    #     ["005", str(commonFunctions.stateDictionary["Bihar"][0] + commonFunctions.stateDictionary["Bihar"][2]), "1"],
    #     ["006", str(commonFunctions.stateDictionary["Chandigarh"][0] + commonFunctions.stateDictionary["Chandigarh"][2]), "1"],
    #     ["007", str(commonFunctions.stateDictionary["Chhattisgarh"][0] + commonFunctions.stateDictionary["Chhattisgarh"][2]), "1"],  # CA
    #     ["011", str(commonFunctions.stateDictionary["Goa"][0] + commonFunctions.stateDictionary["Goa"][2]), "1"],  # GO
    #     ["012", str(commonFunctions.stateDictionary["Gujarat"][0] + commonFunctions.stateDictionary["Gujarat"][2]), "1"],  # GU
    #     ["013", str(commonFunctions.stateDictionary["Haryana"][0] + commonFunctions.stateDictionary["Haryana"][2]), "1"],  # HA
    #     ["014", str(commonFunctions.stateDictionary["Himachal Pradesh"][0] + commonFunctions.stateDictionary["Himachal Pradesh"][2]), "1"],  # HP
    #     ["015", str(commonFunctions.stateDictionary["Jammu & Kashmir"][0] + commonFunctions.stateDictionary["Jammu & Kashmir"][2]), "1"],  # JK
    #     ["016", str(commonFunctions.stateDictionary["Jharkhand"][0] + commonFunctions.stateDictionary["Jharkhand"][2]), "1"],  # JH
    #     ["017", str(commonFunctions.stateDictionary["Karnataka"][0] + commonFunctions.stateDictionary["Karnataka"][2]), "1"],  # KA
    #     ["018", str(commonFunctions.stateDictionary["Kerala"][0] + commonFunctions.stateDictionary["Kerala"][2]), "1"],  # KE
    #     ["020", str(commonFunctions.stateDictionary["Madhya Pradesh"][0] + commonFunctions.stateDictionary["Madhya Pradesh"][2]), "1"],  # MP
    #     ["021", str(commonFunctions.stateDictionary["Maharashtra"][0] + commonFunctions.stateDictionary["Maharashtra"][2]), "1"],  # MA
    #     ["022", str(commonFunctions.stateDictionary["Manipur"][0] + commonFunctions.stateDictionary["Manipur"][2]), "1"],  # MN
    #     ["023", str(commonFunctions.stateDictionary["Meghalaya"][0] + commonFunctions.stateDictionary["Meghalaya"][2]), "1"],  # ME
    #     ["024", str(commonFunctions.stateDictionary["Mizoram"][0] + commonFunctions.stateDictionary["Mizoram"][2]), "1"],  # MI
    #     ["025", str(commonFunctions.stateDictionary["Nagaland"][0] + commonFunctions.stateDictionary["Nagaland"][2]), "1"],  # NA
    #     ["026", str(commonFunctions.stateDictionary["Odisha"][0] + commonFunctions.stateDictionary["Odisha"][2]), "1"],  # OR
    #     ["028", str(commonFunctions.stateDictionary["Punjab"][0] + commonFunctions.stateDictionary["Punjab"][2]), "1"],  # PU
    #     ["029", str(commonFunctions.stateDictionary["Rajasthan"][0]  + commonFunctions.stateDictionary["Rajasthan"][2]), "1"],  # RA
    #     ["030", str(commonFunctions.stateDictionary["Sikkim"][0] + commonFunctions.stateDictionary["Sikkim"][2]), "1"],  # SI
    #     ["031", str(commonFunctions.stateDictionary["Tamil Nadu"][0] + commonFunctions.stateDictionary["Tamil Nadu"][2]), "1"],  # TN
    #     ["032", str(commonFunctions.stateDictionary["Tripura"][0] + commonFunctions.stateDictionary["Tripura"][2]), "1"],  # TR
    #     ["036", str(commonFunctions.stateDictionary["Telangana"][0] + commonFunctions.stateDictionary["Telangana"][2]), "1"],  # TG
    #     ["033", str(commonFunctions.stateDictionary["Uttar Pradesh"][0] + commonFunctions.stateDictionary["Uttar Pradesh"][2]), "1"],  # UP
    #     ["034", str(commonFunctions.stateDictionary["Uttarakhand"][0] + commonFunctions.stateDictionary["Uttarakhand"][2]), "1"],  # UT
    #     ["035", str(commonFunctions.stateDictionary["West Bengal"][0] + commonFunctions.stateDictionary["West Bengal"][2]), "1"]  # WB
    # ]
    mapDataArray2017_18 = [
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
        ["031", str(commonFunctions.stateDictionary["Tamil Nadu"][0]), "1"],# TN
        ["032", str(commonFunctions.stateDictionary["Tripura"][0]), "1"],  # TR
        ["036", str(commonFunctions.stateDictionary["Telangana"][0]), "1"],  # TG
        ["033", str(commonFunctions.stateDictionary["Uttar Pradesh"][0]), "1"],  # UP
        ["034", str(commonFunctions.stateDictionary["Uttarakhand"][0]), "1"],  # UT
        ["035", str(commonFunctions.stateDictionary["West Bengal"][0]), "1"]  # WB
    ]
    mapDataArray2018_19 = [
        ["001", str(commonFunctions.stateDictionary["Andaman & Nicobar Islands"][1]), "1"],
        ["002", str(commonFunctions.stateDictionary["Andhra Pradesh"][1]), "1"],  # AP
        ["003", str(commonFunctions.stateDictionary["Arunachal Pradesh"][1]), "1"],  # AR
        ["004", str(commonFunctions.stateDictionary["Assam"][1]), "1"], # AS
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

    # mapDataArray2018_19 = [
    #     ["001", str(commonFunctions.stateDictionary["Andaman & Nicobar Islands"][1] + commonFunctions.stateDictionary["Andaman & Nicobar Islands"][3]), "1"],
    #     ["002", str(commonFunctions.stateDictionary["Andhra Pradesh"][1] + commonFunctions.stateDictionary["Andhra Pradesh"][3]), "1"],  # AP
    #     ["003", str(commonFunctions.stateDictionary["Arunachal Pradesh"][1] + commonFunctions.stateDictionary["Arunachal Pradesh"][3]), "1"],  # AR
    #     ["004", str(commonFunctions.stateDictionary["Assam"][1] + commonFunctions.stateDictionary["Assam"][3]), "1"], # AS
    #     ["005", str(commonFunctions.stateDictionary["Bihar"][1] + commonFunctions.stateDictionary["Bihar"][3]), "1"],
    #     ["006", str(commonFunctions.stateDictionary["Chandigarh"][1] + commonFunctions.stateDictionary["Chandigarh"][3]), "1"],
    #     ["007", str(commonFunctions.stateDictionary["Chhattisgarh"][1] + commonFunctions.stateDictionary["Chhattisgarh"][3]), "1"],  # CA
    #     ["011", str(commonFunctions.stateDictionary["Goa"][1] + commonFunctions.stateDictionary["Goa"][3]), "1"],  # GO
    #     ["012", str(commonFunctions.stateDictionary["Gujarat"][1] + commonFunctions.stateDictionary["Gujarat"][3]), "1"],  # GU
    #     ["013", str(commonFunctions.stateDictionary["Haryana"][1] + commonFunctions.stateDictionary["Haryana"][3]), "1"],  # HA
    #     ["014", str(commonFunctions.stateDictionary["Himachal Pradesh"][1] + commonFunctions.stateDictionary["Himachal Pradesh"][3]), "1"],  # HP
    #     ["015", str(commonFunctions.stateDictionary["Jammu & Kashmir"][ 1] + commonFunctions.stateDictionary["Jammu & Kashmir"][3]), "1"],  # JK
    #     ["016", str(commonFunctions.stateDictionary["Jharkhand"][1] + commonFunctions.stateDictionary["Jharkhand"][3]), "1"],  # JH
    #     ["017", str(commonFunctions.stateDictionary["Karnataka"][1] + commonFunctions.stateDictionary["Karnataka"][3]), "1"],  # KA
    #     ["018", str(commonFunctions.stateDictionary["Kerala"][1] + commonFunctions.stateDictionary["Kerala"][3]), "1"], # KE
    #     ["020", str(commonFunctions.stateDictionary["Madhya Pradesh"][ 1] + commonFunctions.stateDictionary["Madhya Pradesh"][3]), "1"],  # MP
    #     ["021", str(commonFunctions.stateDictionary["Maharashtra"][1] + commonFunctions.stateDictionary["Maharashtra"][3]), "1"],  # MA
    #     ["022", str(commonFunctions.stateDictionary["Manipur"][1] + commonFunctions.stateDictionary["Manipur"][3]), "1"],  # MN
    #     ["023", str(commonFunctions.stateDictionary["Meghalaya"][1] + commonFunctions.stateDictionary["Meghalaya"][3]), "1"],  # ME
    #     ["024", str(commonFunctions.stateDictionary["Mizoram"][1] + commonFunctions.stateDictionary["Mizoram"][3]), "1"],  # MI
    #     ["025", str(commonFunctions.stateDictionary["Nagaland"][1] + commonFunctions.stateDictionary["Nagaland"][3]), "1"],  # NA
    #     ["026", str(commonFunctions.stateDictionary["Odisha"][1] + commonFunctions.stateDictionary["Odisha"][3]), "1"], # OR
    #     ["028", str(commonFunctions.stateDictionary["Punjab"][1] + commonFunctions.stateDictionary["Punjab"][3]), "1"], # PU
    #     ["029", str(commonFunctions.stateDictionary["Rajasthan"][1] + commonFunctions.stateDictionary["Rajasthan"][3]), "1"],  # RA
    #     ["030", str(commonFunctions.stateDictionary["Sikkim"][1] + commonFunctions.stateDictionary["Sikkim"][3]), "1"], # SI
    #     ["031", str(commonFunctions.stateDictionary["Tamil Nadu"][1] + commonFunctions.stateDictionary["Tamil Nadu"][3]), "1"], # TN
    #     ["032", str(commonFunctions.stateDictionary["Tripura"][1] + commonFunctions.stateDictionary["Tripura"][3]), "1"],  # TR
    #     ["036", str(commonFunctions.stateDictionary["Telangana"][1] + commonFunctions.stateDictionary["Telangana"][3]), "1"],  # TG
    #     ["033", str(commonFunctions.stateDictionary["Uttar Pradesh"][1] + commonFunctions.stateDictionary["Uttar Pradesh"][3]), "1"],  # UP
    #     ["034", str(commonFunctions.stateDictionary["Uttarakhand"][1] + commonFunctions.stateDictionary["Uttarakhand"][3]), "1"],  # UT
    #     ["035", str(commonFunctions.stateDictionary["West Bengal"][1] + commonFunctions.stateDictionary["West Bengal"][3]), "1"] # WB
    # ]

    dataSource2017_2018 = OrderedDict()
    dataSource2017_2018["chart"] = mapConfig
    dataSource2017_2018["colorrange"] = colorDataObj
    dataSource2017_2018["data"] = commonFunctions.makeDataSourceForChloroplethMap(mapDataArray2017_18)

    dataSource2018_2019 = OrderedDict()
    dataSource2018_2019["chart"] = mapConfig
    dataSource2018_2019["colorrange"] = colorDataObj
    dataSource2018_2019["data"] = commonFunctions.makeDataSourceForChloroplethMap(mapDataArray2018_19)

    fusionMap2017_18 = FusionCharts("maps/india", "Map1", "600", "600", "fundsChloropleth2017_18", "json", dataSource2017_2018)
    fusionMap2018_19 = FusionCharts("maps/india", "Map2", "600", "600", "fundsChloropleth2018_19", "json", dataSource2018_2019)

    ############
    ###########

    rawData = commonFunctions.downloadData(urlLaneWiseLenNH)
    js = commonFunctions.loadJson(rawData)
    data = js['records']
    
    for i in range(29):
        stateName = data[i]["states_uts"]
        if stateName == "Jammu and Kashmir":
            stateName = "Jammu & Kashmir"
        commonFunctions.stateDictionary[stateName][0] = float(data[i]["total_length"])
        commonFunctions.stateDictionary[stateName][1] = float(data[i]["less_than_2_lane"])
        commonFunctions.stateDictionary[stateName][2] = float(data[i]["two_lane"])
        commonFunctions.stateDictionary[stateName][3] = float(data[i]["four_lane_above"])
    
     mapDataArrayTotalLength = [
         ["002", str(commonFunctions.stateDictionary["Andhra Pradesh"][0]), "1"],  # AP
         ["003", str(commonFunctions.stateDictionary["Arunachal Pradesh"][0]), "1"],  # AR
         ["004", str(commonFunctions.stateDictionary["Assam"][0]), "1"], # AS
         ["005", str(commonFunctions.stateDictionary["Bihar"][0]), "1"],
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
    
     colorDataObj = {
         "minvalue": "0",
         "code": "#FFE0B2",
         "gradient": "1",
         "color": [{
             "minValue": "0",
             "maxValue": "260",
             "code": "#f4fdff"
         },
             {
                 "minValue": "260",
                 "maxValue": "1500",
                 "code": "#c0dae0"
             },
             {
                 "minValue": "1500",
                 "maxValue": "3000",
                 "code": "#8bc8d6"
             },
             {
                 "minValue": "3000",
                 "maxValue": "4500",
                 "code": "#57b6cc"
             },
             {
                 "minValue": "4500",
                 "maxValue": "6000",
                 "code": "#037db7"
             },
             {
                 "minValue": "6000",
                 "maxValue": "7500",
                 "code": "#0365b7"
             },
             {
                 "minValue": "7500",
                 "maxValue": "9000",
                 "code": "#033fb7"
             }
         ]
     }
    
     mapConfig1 = OrderedDict()
     mapConfig1["animation"] = "0"
     mapConfig1["usehovercolor"] = "1"
     mapConfig1["showlegend"] = "1"
     mapConfig1["legendposition"] = "BOTTOM"
     mapConfig1["legendborderalpha"] = "0"
     mapConfig1["legendbordercolor"] = "#FDFDB7"
     mapConfig1["legendallowdrag"] = "0"
     mapConfig1["legendshadow"] = "0"
     mapConfig1["numbersuffix"] = " km"
     mapConfig1["caption"] = "Data of March 2015"
     mapConfig1["subcaption"] = ""
     mapConfig1["connectorcolor"] = "#FDFDB7"
     mapConfig1["fillalpha"] = "80"
     mapConfig1["entityFillHoverColor"] = "#dddddd"
     mapConfig1["theme"] = "fusion"
    
    dataSourceRoadLength = OrderedDict()
    dataSourceRoadLength["chart"] = mapConfig1
    dataSourceRoadLength["colorrange"] = colorDataObj
    dataSourceRoadLength["data"] = commonFunctions.makeDataSourceForChloroplethMap(mapDataArrayTotalLength)
    
    fusionMapRoadLength = FusionCharts("maps/india", "Map3", "600", "600", "RoadLengthStates", "json", dataSourceRoadLength)

    # ********************************************************************#

    rawData = commonFunctions.downloadData(urlProjects)
    js = commonFunctions.loadJson(rawData)
    data = js['records']

    for key in commonFunctions.stateDictionary.keys():
        commonFunctions.stateDictionary[key][0] = 0

    for i in range(len(data)):
        stateName = data[i]["states_uts"]
        if stateName in commonFunctions.stateDictionary.keys():
            commonFunctions.stateDictionary[stateName][0] = float(data[i]["numbers_of_projects"])
        elif stateName not in commonFunctions.stateDictionary.keys():
            for state in commonFunctions.stateDictionary.keys():
                for j in range(len(data)):
                    if state in data[j]["states_uts"] and data[j]["states_uts"] == stateName:
                        commonFunctions.stateDictionary[state][0] = commonFunctions.stateDictionary[state][0] + float(data[j]["numbers_of_projects"])

    chartObj1 = FusionCharts('scrollcombidy2d', 'ex1', '600', '600', 'populationDensityProjects', 'json', """{
          "chart": {
            "caption": "Population Density and No of Projects",
            "subcaption": "",
            "yaxisname": "Density by census 2011",
            "syaxisname": "Number of Projects",
            "labeldisplay": "rotate",
            "snumbersuffix": "",
            "scrollheight": "10",
            "numvisibleplot": "9",
            "drawcrossline": "1",
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
              "seriesname": "Pouplation Density of States",
              "plottooltext": "Population Density: $dataValue /sq km",
              "data": [
                {
                  "value": """ + '"' + str(commonFunctions.populationOfStates["Andhra Pradesh"]/commonFunctions.landAreaStates["Andhra Pradesh"]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.populationOfStates["Arunachal Pradesh"]/commonFunctions.landAreaStates["Arunachal Pradesh"]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.populationOfStates["Assam"]/commonFunctions.landAreaStates["Assam"]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.populationOfStates["Bihar"]/commonFunctions.landAreaStates["Bihar"]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.populationOfStates["Chhattisgarh"]/commonFunctions.landAreaStates["Chhattisgarh"]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.populationOfStates["Goa"]/commonFunctions.landAreaStates["Goa"]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.populationOfStates["Gujarat"]/commonFunctions.landAreaStates["Gujarat"]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.populationOfStates["Haryana"]/commonFunctions.landAreaStates["Haryana"]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.populationOfStates["Himachal Pradesh"]/commonFunctions.landAreaStates["Himachal Pradesh"]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.populationOfStates["Jammu & Kashmir"]/commonFunctions.landAreaStates["Jammu & Kashmir"]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.populationOfStates["Jharkhand"]/commonFunctions.landAreaStates["Jharkhand"]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.populationOfStates["Karnataka"]/commonFunctions.landAreaStates["Karnataka"]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.populationOfStates["Kerala"]/commonFunctions.landAreaStates["Kerala"]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.populationOfStates["Madhya Pradesh"]/commonFunctions.landAreaStates["Madhya Pradesh"]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.populationOfStates["Maharashtra"]/commonFunctions.landAreaStates["Maharashtra"]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.populationOfStates["Manipur"]/commonFunctions.landAreaStates["Manipur"]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.populationOfStates["Meghalaya"]/commonFunctions.landAreaStates["Meghalaya"]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.populationOfStates["Mizoram"]/commonFunctions.landAreaStates["Mizoram"]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.populationOfStates["Nagaland"]/commonFunctions.landAreaStates["Nagaland"]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.populationOfStates["Odisha"]/commonFunctions.landAreaStates["Odisha"]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.populationOfStates["Punjab"]/commonFunctions.landAreaStates["Punjab"]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.populationOfStates["Rajasthan"]/commonFunctions.landAreaStates["Rajasthan"]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.populationOfStates["Sikkim"]/commonFunctions.landAreaStates["Sikkim"]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.populationOfStates["Tamil Nadu"]/commonFunctions.landAreaStates["Tamil Nadu"]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.populationOfStates["Tripura"]/commonFunctions.landAreaStates["Tripura"]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.populationOfStates["Telangana"]/commonFunctions.landAreaStates["Telangana"]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.populationOfStates["Uttar Pradesh"]/commonFunctions.landAreaStates["Uttar Pradesh"]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.populationOfStates["Uttarakhand"]/commonFunctions.landAreaStates["Uttarakhand"]) + '"' + """
                },
                {
                  "value": """ + '"' + str(commonFunctions.populationOfStates["West Bengal"]/commonFunctions.landAreaStates["West Bengal"]) + '"' + """
                }
              ]
            },
            {
              "seriesname": "No. of major projects about to be completed by March 2019",
              "parentyaxis": "S",
              "renderas": "line",
              "plottooltext": "$dataValue",
              "showvalues": "0",
              "data": [
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

    chartObj = FusionCharts('scrollcombidy2d', 'ex2', '600', '600', 'barChartForProjects', 'json', """{
      "chart": {
        "caption": "Population Land Area and No of Projects",
        "subcaption": "",
        "yaxisname": "Population by census 2011",
        "syaxisname": "Number of Projects",
        "labeldisplay": "rotate",
        "snumbersuffix": "",
        "scrollheight": "10",
        "numvisibleplot": "9",
        "drawcrossline": "1",
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
          "seriesname": "Pouplation of States",
          "plottooltext": "Population: $dataValue",
          "data": [
            {
              "value": """ + '"' + str(commonFunctions.populationOfStates["Andhra Pradesh"]) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.populationOfStates["Arunachal Pradesh"]) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.populationOfStates["Assam"]) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.populationOfStates["Bihar"]) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.populationOfStates["Chhattisgarh"]) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.populationOfStates["Goa"]) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.populationOfStates["Gujarat"]) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.populationOfStates["Haryana"]) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.populationOfStates["Himachal Pradesh"]) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.populationOfStates["Jammu & Kashmir"]) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.populationOfStates["Jharkhand"]) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.populationOfStates["Karnataka"]) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.populationOfStates["Kerala"]) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.populationOfStates["Madhya Pradesh"]) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.populationOfStates["Maharashtra"]) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.populationOfStates["Manipur"]) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.populationOfStates["Meghalaya"]) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.populationOfStates["Mizoram"]) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.populationOfStates["Nagaland"]) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.populationOfStates["Odisha"]) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.populationOfStates["Punjab"]) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.populationOfStates["Rajasthan"]) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.populationOfStates["Sikkim"]) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.populationOfStates["Tamil Nadu"]) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.populationOfStates["Tripura"]) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.populationOfStates["Telangana"]) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.populationOfStates["Uttar Pradesh"]) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.populationOfStates["Uttarakhand"]) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.populationOfStates["West Bengal"]) + '"' + """
            }
          ]
        },
        {
          "seriesname": "Land Area in sq km(multiplied by 100 for a better graph)",
          "renderas": "area",
          "showanchors": "0",
          "plottooltext": "Land Area: $dataValue*100",
          "data": [
            {
              "value": """ + '"' + str(commonFunctions.landAreaStates["Andhra Pradesh"]*100) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.landAreaStates["Arunachal Pradesh"]*100) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.landAreaStates["Assam"]*100) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.landAreaStates["Bihar"]*100) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.landAreaStates["Chhattisgarh"]*100) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.landAreaStates["Goa"]*100) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.landAreaStates["Gujarat"]*100) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.landAreaStates["Haryana"]*100) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.landAreaStates["Himachal Pradesh"]*100) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.landAreaStates["Jammu & Kashmir"]*100) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.landAreaStates["Jharkhand"]*100) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.landAreaStates["Karnataka"]*100) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.landAreaStates["Kerala"]*100) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.landAreaStates["Madhya Pradesh"]*100) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.landAreaStates["Maharashtra"]*100) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.landAreaStates["Manipur"]*100) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.landAreaStates["Meghalaya"]*100) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.landAreaStates["Mizoram"]*100) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.landAreaStates["Nagaland"]*100) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.landAreaStates["Odisha"]*100) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.landAreaStates["Punjab"]*100) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.landAreaStates["Rajasthan"]*100) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.landAreaStates["Sikkim"]*100) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.landAreaStates["Tamil Nadu"]*100) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.landAreaStates["Tripura"]*100) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.landAreaStates["Telangana"]*100) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.landAreaStates["Uttar Pradesh"]*100) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.landAreaStates["Uttarakhand"]*100) + '"' + """
            },
            {
              "value": """ + '"' + str(commonFunctions.landAreaStates["West Bengal"]*100) + '"' + """
            }
          ]
        },
        {
          "seriesname": "No. of major projects about to be completed by March 2019",
          "parentyaxis": "S",
          "renderas": "line",
          "plottooltext": "$dataValue",
          "showvalues": "0",
          "data": [
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
    }""")

    return render(request, 'roadProjectsFunds.html',
                  {'output2017_2018': fusionMap2017_18.render(), 'output2018_2019': fusionMap2018_19.render(),
                   'projects': chartObj.render(), 'outputPopulationDensityProjects': chartObj1.render()})
