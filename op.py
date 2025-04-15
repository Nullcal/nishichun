import requests
import os
import gtfs_realtime_pb2 as gtfs_realtime_pb2
import json

#------------------------------#
# Request data from ODPT API.
#------------------------------#

def odpt_request(url):
    token = os.getenv("ODPT_TOKEN")
    response = requests.get(url + token)
    return response.content

# List of URLs for API requests
url = {
    "busstop"   : "https://api.odpt.org/api/v4/odpt:BusstopPole?odpt:operator=odpt.Operator:NishiTokyoBus&acl:consumerKey=",
    "route"     : "https://api.odpt.org/api/v4/odpt:BusroutePattern?odpt:operator=odpt.Operator:NishiTokyoBus&acl:consumerKey=",
    "timetable" : "https://api.odpt.org/api/v4/odpt:BusTimetable?odpt:operator=odpt.Operator:NishiTokyoBus&acl:consumerKey=",
    "realtime"  : "https://api.odpt.org/api/v4/gtfs/realtime/odpt_NishiTokyoBus_NTBus_vehicle?acl:consumerKey="
}


#------------------------------#
# Parse protocol buffer data.
#------------------------------#

def odpt_parse(data):
    protoStr = gtfs_realtime_pb2.FeedMessage()
    protoStr.ParseFromString(data)
    return protoStr


#------------------------------#
# Print filtered data.
#------------------------------#

feed = odpt_parse(odpt_request(url["realtime"]))

for entity in feed.entity:
    route_id = entity.vehicle.trip.route_id
    if route_id == "10112" or route_id == "10113":
        print(entity)
