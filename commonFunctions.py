import urllib.request, urllib.error
import json

statesWithId = {"Andaman and Nicobar Islands":"001", "Andhra Pradesh":"002", "Arunachal Pradesh":"003", "Assam":"004",
                "Bihar":"005", "Chandigarh":"006", "Chhattisgarh":"007", "Dadra and Nagar Haveli":"008", "Daman and Diu":"009",
                "Delhi":"010", "Goa":"011", "Gujarat":"012", "Haryana":"013", "Himachal Pradesh":"014", "Jammu and Kashmir":"015",
                "Jharkhand":"016", "Karnataka":"017", "Kerala":"018", "Lakshadweep":"019", "Madhya Pradesh":"020",
                "Maharashtra":"021", "Manipur":"022", "Meghalaya":"023", "Mizoram":"024", "Nagaland":"025", "Odisha":"026",
                "Puducherry":"027", "Punjab":"028", "Rajasthan":"029", "Sikkim":"030", "Tamil Nadu":"031", "Tripura":"032",
                "Uttar Pradesh":"033", "Uttarakhand":"034", "West Bengal":"035", "Telangana":"036"}

populationOfStates = {"Andaman & Nicobar Islands":379944, "Andhra Pradesh":49634314, "Arunachal Pradesh":1382611,
              "Assam":31169272, "Bihar":103804637, "Chandigarh":1054686, "Chhattisgarh":25540196,
              "Dadar & Nagar Haveli":342853, "Daman & Diu":242911, "NCT of Delhi":16753235, "Goa":1457723,
              "Gujarat":60383628, "Haryana":25353081, "Himachal Pradesh":6856509, "Jammu & Kashmir":12548926,
              "Jharkhand":32966238, "Karnataka":61130704, "Kerala":33387677, "Lakshadweep":64429,
              "Madhya Pradesh":72597565, "Maharashtra":112372972, "Manipur":2721756, "Meghalaya":2964007,
              "Mizoram":1091014, "Nagaland":1980602, "Odisha":41947358, "Puducherry":1244464, "Punjab":27704236,
              "Rajasthan":68621012, "Sikkim":607688, "Tamil Nadu":72138958, "Tripura":3671032,
              "Uttar Pradesh":199581477, "Uttarakhand":10116752, "West Bengal":91347736, "Telangana":39644000}

stateDictionary = {"Andaman & Nicobar Islands":[-1, -1, -1, -1], "Andhra Pradesh":[-1, -1, -1, -1], "Arunachal Pradesh":[-1, -1, -1, -1], "Assam":[-1, -1, -1, -1], "Bihar":[-1, -1, -1, -1],
                   "Chandigarh":[-1, -1, -1, -1], "Chhattisgarh":[-1, -1, -1, -1], "Dadar & Nagar Haveli":[-1, -1, -1, -1], "Daman & Diu":[-1, -1, -1, -1], "Delhi":[-1, -1, -1, -1],
                   "Goa":[-1, -1, -1, -1], "Gujarat":[-1, -1, -1, -1], "Haryana":[-1, -1, -1, -1], "Himachal Pradesh":[-1, -1, -1, -1], "Jammu & Kashmir":[-1, -1, -1, -1],
                   "Jharkhand":[-1, -1, -1, -1], "Karnataka":[-1, -1, -1, -1], "Kerala":[-1, -1, -1, -1], "Lakshadweep":[-1, -1, -1, -1], "Madhya Pradesh":[-1, -1, -1, -1], "Maharashtra":[-1, -1, -1, -1],
                   "Manipur":[-1, -1, -1, -1], "Meghalaya":[-1, -1, -1, -1], "Mizoram":[-1, -1, -1, -1], "Nagaland":[-1, -1, -1, -1], "Odisha":[-1, -1, -1, -1], "Puducherry":[-1, -1, -1, -1], "Punjab":[-1, -1, -1, -1],
                   "Rajasthan":[-1, -1, -1, -1], "Sikkim":[-1, -1, -1, -1], "Tamil Nadu":[-1, -1, -1, -1], "Tripura":[-1, -1, -1, -1], "Uttar Pradesh":[-1, -1, -1, -1], "Uttarakhand":[-1, -1, -1, -1],
                   "West Bengal":[-1, -1, -1, -1], "Telangana":[-1, -1, -1, -1]}

landAreaStates = {"Andaman & Nicobar Islands":379944, "Andhra Pradesh":160205, "Arunachal Pradesh":83743,
              "Assam":78438, "Bihar":94163, "Chandigarh":-1, "Chhattisgarh":135192,
              "Dadar & Nagar Haveli":-1, "Daman & Diu":-1, "NCT of Delhi":-1, "Goa":3702,
              "Gujarat":196244, "Haryana":44212, "Himachal Pradesh":55673, "Jammu & Kashmir":222236,
              "Jharkhand":79716, "Karnataka":191791, "Kerala":38852, "Lakshadweep":-1,
              "Madhya Pradesh":308252, "Maharashtra":307713, "Manipur":22327, "Meghalaya":22429,
              "Mizoram":21081, "Nagaland":16579, "Odisha":155707, "Puducherry":-1, "Punjab":50362,
              "Rajasthan":342239, "Sikkim":7096, "Tamil Nadu":130060, "Tripura":10486,
              "Uttar Pradesh":240928, "Uttarakhand":53483, "West Bengal":88752, "Telangana":112077}

def downloadData(serviceUrl):
    try:
        response = urllib.request.urlopen(serviceUrl)
    except:
        response = ""
    data = response.read().decode()
    return data

def loadJson(rawData):
    try:
        js = json.loads(rawData)
    except:
        js = None
    return js

def makeMapDataArray(str):
    return str

def makeDataSourceForChloroplethMap(mapDataArray):
    list = []
    for i in range(len(mapDataArray)):
        list.append({
            "id": mapDataArray[i][0],
            "value": mapDataArray[i][1],
            "showLabel": mapDataArray[i][2]})
    return list