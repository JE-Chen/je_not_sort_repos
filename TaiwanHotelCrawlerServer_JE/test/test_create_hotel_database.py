import datetime

from je_database import sqlite_core
from je_taiwan_open_data_core import GovernmentOpenDataCore

print(datetime.datetime.now())

sql = sqlite_core(r"Hotel.sqlite", table_name="Hotel")
sql.create_table("CREATE TABLE IF NOT EXISTS Hotel("
                 "Id VARCHAR (20) PRIMARY KEY,"
                 "Hotel_Name VARCHAR (20),"
                 "Description VARCHAR (500),"
                 "Grade VARCHAR (10),"
                 "Address VARCHAR (10),"
                 "Region VARCHAR (20),"
                 "Town VARCHAR(15),"
                 "Tel VARCHAR (20),"
                 "Website VARCHAR (100),"
                 "Picture1 VARCHAR (30),"
                 "Picdescribe1 VARCHAR (50),"
                 "Picture2 VARCHAR (50),"
                 "Picdescribe2 VARCHAR (50),"
                 "Picture3 VARCHAR (50),"
                 "Picdescribe3 VARCHAR (50),"
                 "Px VARCHAR (15),"
                 "Py VARCHAR (15),"
                 "Serviceinfo VARCHAR (100),"
                 "Parkinginfo VARCHAR (30),"
                 "TotalNumberofRooms VARCHAR (5),"
                 "LowestPrice VARCHAR (6),"
                 "CeilingPrice VARCHAR (6),"
                 "IndustryEmail VARCHAR (50),"
                 "TotalNumberofPeople VARCHAR (5),"
                 "AccessibilityRooms VARCHAR (5),"
                 "PublicToilets VARCHAR (5),"
                 "LiftingEquipment VARCHAR (20),"
                 "ParkingSpace VARCHAR (20))")

core = GovernmentOpenDataCore("Not Need Key")
core.parse_url = "https://gis.taiwan.net.tw/XMLReleaseALL_public/hotel_C_f.json"
data = core.parse_response_content(is_utf8_sig=True)['XML_Head'].get('Infos').get('Info')
for i in range(len(data)):
    sql.insert_into_replace(data[i].get("Id"),
                            data[i].get("Name"),
                            data[i].get("Description"),
                            data[i].get("Grade"),
                            data[i].get("Add"),
                            data[i].get("Region"),
                            data[i].get("Town"),
                            data[i].get("Tel"),
                            data[i].get("Website"),
                            data[i].get("Picture1"),
                            data[i].get("Picdescribe1"),
                            data[i].get('Picture2'),
                            data[i].get('Picdescribe2'),
                            data[i].get('Picture3'),
                            data[i].get('Picdescribe3'),
                            data[i].get('Px'),
                            data[i].get('Py'),
                            data[i].get('Serviceinfo'),
                            data[i].get('Parkinginfo'),
                            data[i].get('TotalNumberofRooms'),
                            data[i].get('LowestPrice'),
                            data[i].get('CeilingPrice'),
                            data[i].get('IndustryEmail'),
                            data[i].get('TotalNumberofPeople'),
                            data[i].get('AccessibilityRooms'),
                            data[i].get('PublicToilets'),
                            data[i].get('LiftingEquipment'),
                            data[i].get('ParkingSpace'))
print(datetime.datetime.now())

result = sql.select_where('Region', '高雄市')
for i in range(len(result)):
    print(result[i])
