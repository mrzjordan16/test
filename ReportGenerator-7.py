#!/usr/bin/env python3

import json
import sys


JobName=sys.argv[1]
Team=sys.argv[2]
JenkinUser=sys.argv[3]
Date=sys.argv[4]
print ("DATE:"+str(Date))
#JenkinUser="xyz@@stc.com.sa"

path="/var/lib/jenkins/scripts/linting/Tenant/"+Team+"/"+JobName+"/output.json"

f= open(path, "r")
listofJson=json.load(f)
f.close()

def type_identifier(input):
    if input=="error":
        return "error"  
    elif input =="information":
        return "info"
    else: 
        return "warning"



output='<!DOCTYPE html><head> <title>STC Linting Report</title> <style>/*Common CSS*/ *{padding: 0; margin: 0;}body{font-family: "Roboto",Arial, Helvetica, sans-serif; background-color: #F2F2F2; padding-top:100px;}/*REUSABLE*/ /*icon*/ .icon-list ul{list-style: none; /* height:50px; */ /* background-color: gold; */}.icon-list ul li{display:inline-block; height:90%; /* background-color: red; */ /* border:2px solid white; */}.span-icon{/* background-color: #12B0FB; */ margin-top:10px;}.error-color{color: #F54336;}.info-color{color: #12B0FB;}.warning-color{color: #FFB258 ;}.{color: white; font-weight: 100;}.{color: #37474F;}.font-lightweight{font-weight: 100;}/*NAV BAR*/ .title_body{background-color: #37474F; padding:10px; color:white; text-shadow: 1px 1px 10px black; border-bottom: 4px solid #4CAF50; display: flex; position:fixed; width: 100%; top:0;}.Title_text{flex: 2;}.Title_info{flex:1;}.tool_title_body{margin-top:2px; letter-spacing: 0.5px; font-weight: 100;}.Title_info .status_box{font-size:20px;}.status_box{background-color: black; padding:5px 10px; /* text-shadow: 2px 2px 10px white; */ box-shadow: 2px solid black; font-weight: bold; border-radius: 5px; color:white; margin-left:5px;}.pass{background-color:#469749; font-size:60px;}.total{background-color: #37474F; text-shadow: 2px 2px 10px transparent;}.info{background-color: #12B0FB;}.warn{background-color: #FFB258;}.error{background-color: #F54336;}/*Card*/ .card{background-color: #FFFFFF; width:50vw; margin:40px auto; padding-top: 10px; /* text-shadow: 1px 1px 10px black; */ box-shadow: 1px 5px 10px rgb(151, 151, 151,0.7); border-radius:5px; padding-bottom: 10px;}.card_title,.card_info{margin:10px 20px;}.card_heading{font-size: 25px; font-weight: 600; font-family:Arial, Helvetica, sans-serif;}.card_subheading{font-size: 15px; color: grey;}.card_border{border:0.5px solid #e6e6e6; margin: 20px 0;}.card-table{width:100%; border-collapse: collapse; height:auto;table-layout:fixed;}.card-table thead tr{padding-bottom: 10px;word-wrap:break-word;}.card-table tbody tr:nth-child(even){background-color: #d4d4d4;word-wrap:break-word;}.card-table tbody tr:nth-child(odd){background-color: #FFFFFF;word-wrap:break-word}.card-table-cell-middle{/* background-color: red; */ padding:10px;}.card-table-type{width:10vh; text-align: center;}.card-table-line{width:10%; text-align: left;}.card-table-message{width:80%; text-align: left;}.td-icon{padding-bottom: 15px;word-wrap:normal}.icon_thumb_up{width:100%; height:auto;}.thumb_div{color:white; width:max-content; font-size:125px; margin: 0px auto; margin-bottom: 20px;}</style></head><body> <div class="main_body"> <div class="title_body"> <div class="Title_text"> <h3>STC Linting Report&nbsp;&nbsp;|&nbsp;&nbsp;'+JenkinUser+'</h3> <div class="tool_title_body"> <p>By <span> STC </span></p></div></div>'
output=output+'<div class="Title_info"><div class="icon-list"><ul><li><div class="span-icon"><div class="status_box total">Total:&nbsp;&nbsp;<span class="">'+str(listofJson["total"])+'</span>&nbsp;</div></div></li><li><div class="span-icon"><div class="status_box info">Info:&nbsp;&nbsp;<span class="">'+str(listofJson["info"])+'</span>&nbsp;</div></div></li><li><div class="span-icon"><div class="status_box warn">Warning:&nbsp;&nbsp;<span class="">'+str(listofJson["warning"])+'</span>&nbsp;</div></div></li><li><div class="span-icon"><div class="status_box error">Error:&nbsp;&nbsp;<span class="">'+str(listofJson["error"])+'</span>&nbsp;</div></div></li></ul></div></div></div>'
output=output+'<div class="report">'

if(len(listofJson["result"])>0):
    for i in range(len(listofJson["result"])):
        #CARD
        output=output+' <div class="card"> <div class="card_title"> <div class="card_heading_box"> <p class="card_heading">'+str(listofJson["result"][i]["filename"])+'</p></div><div class="card_subheading_box"> <p class="card_subheading"></p></div></div>';
        output=output+'<div class="card_info"> <div class="icon-list"> <ul> <li> <div class="span-icon"> <div class="status_box total">Total:&nbsp;&nbsp;<span class=" font-lightweight">'+str(listofJson["result"][i]["total"])+'</span>&nbsp;</div> </div></li><li> <div class="span-icon"> <div class="status_box info">Info:&nbsp;&nbsp;<span class=" font-lightweight">'+str(listofJson["result"][i]["info"])+'</span>&nbsp;</div> </div></li><li> <div class="span-icon"> <div class="status_box warn">Warning:&nbsp;&nbsp;<span class=" font-lightweight">'+str(listofJson["result"][i]["warning"])+'</span>&nbsp;</div> </div></li><li> <div class="span-icon"> <div class="status_box error">Error:&nbsp;&nbsp;<span class=" font-lightweight">'+str(listofJson["result"][i]["error"])+'</span>&nbsp;</i> </div></li></ul> </div></div>'
        output=output+' <div class="card_border"></div><div class="card_description">'
        if(len(listofJson["result"][i]["table"])>0):
            output=output+'<div class="logs-table"> <table class="card-table"> <thead> <tr> <th class="card-table-type">Type</th> <th class="card-table-line">Line</th> <th class="card-table-message">Message</th> </tr></thead> <tbody>'
            for j in range(len(listofJson["result"][i]["table"])): 
            #CARD TABLE
                output=output+' <tr> <td class="card-table-cell-middle td-icon"> <div class="span-icon"> <div class="status_box '+type_identifier(str(listofJson["result"][i]["table"][j]["type"]))+'">'+type_identifier(str(listofJson["result"][i]["table"][j]["type"]))+'</div> </div></td><td> <p>'+str(listofJson["result"][i]["table"][j]["line"])+'</p></td><td> <p>'+str(listofJson["result"][i]["table"][j]["message"])+'</p></td></tr>'
            output=output+'</tbody> </table></div>'
        else:
            output=output+'<div class="icon_thumb_up"> <div class="thumb_div"> <div class="status_box pass">Passed</div> </div></div>'
        output=output+'</div></div></div>'
else:
    output=output+'<div class="icon_thumb_up"> <div class="thumb_div"> <i class="fa-regular fa-thumbs-up"></i> </div></div>'
output=output+'</div></body></html>'
#print(output)



path="/var/lib/jenkins/scripts/linting/Tenant/"+Team+"/"+JobName+"/Report.html"

f= open(path, "w")
f.write(output)
f.close()
