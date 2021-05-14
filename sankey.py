import csv
import math
import json
import pickle
import os, os.path

ORBSlam_dir = 'ORBSlam/'
ShortestPath_dir = 'ShortestPath/'

sceneKeyword = ['Cantwell', 'Denmark', 'Eastville', 'Edgemere', 'Elmira', 'Eudora', 'Greigsville' , 'Mosquito', 'Pablo', 'Ribera', 'Sands', 'Scioto', 'Sisters', 'Swormville']
dataPerScene = {'Cantwell' : [{'True' : [], 'False' : []}], 'Denmark' : [{'True' : [], 'False' : []}], 'Eastville' : [{'True' : [], 'False' : []}], 'Edgemere' : [{'True' : [], 'False' : []}], 'Elmira' : [{'True' : [], 'False' : []}], 'Eudora' : [{'True' : [], 'False' : []}], 'Greigsville' : [{'True' : [], 'False' : []}], 'Mosquito' : [{'True' : [], 'False' : []}], 'Pablo' : [{'True' : [], 'False' : []}], 'Ribera' : [{'True' : [], 'False' : []}], 'Sands' : [{'True' : [], 'False' : []}], 'Scioto' : [{'True' : [], 'False' : []}], 'Sisters' : [{'True' : [], 'False' : []}], 'Swormville' : [{'True' : [], 'False' : []}]}


def episodeLevel(scene_id):
    print()

def sceneLevel():
    episode_id = 0

    #Load the JSON file where scene_id is located
    json_data = open('val.json')
    data = json.load(json_data)

    #Store the episode number and is corresponding scene
    for episode in data['episodes']:

        #We only load the agent episode because the perfect one will be a success
        episode_ORBSlam = pickle.load(open( ORBSlam_dir +"episodeStats"+str(episode_id)+".p", "rb" ))
        #Loading if the episode has failed or not
        success = episode_ORBSlam["success"]

        #Cantwell case
        if sceneKeyword[0] in episode['scene_id']:
            if success == True:
                #Accessing the Dictionnary of episode who succeed in Cantwell Scene and writting the episode_id
                #(Cantwell = [First element in list sceneKeyword] is the key of the first dictionnary who's value is a list which contain two dictionnary True and False, who contain the episodes who have failed or succeed)
                dataPerScene[sceneKeyword[0]][0]['True'].append(episode_id)

            else:
                #Accessing the Dictionnary of episode who failed in Cantwell Scene and writting the episode_id
                #(Cantwell = [First element in list sceneKeyword] is the key of the first dictionnary who's value is a list which contain two dictionnary True and False, who contain the episodes who have failed or succeed)
                dataPerScene[sceneKeyword[0]][0]['False'].append(episode_id)

        #Denmark case
        if sceneKeyword[1] in episode['scene_id']:
            if success == True:
                dataPerScene[sceneKeyword[1]][0]['True'].append(episode_id)
            else:
                dataPerScene[sceneKeyword[1]][0]['False'].append(episode_id)
        #Eastville case
        if sceneKeyword[2] in episode['scene_id']:
            if success == True:
                dataPerScene[sceneKeyword[2]][0]['True'].append(episode_id)
            else:
                dataPerScene[sceneKeyword[2]][0]['False'].append(episode_id)
        #Edgemere case
        if sceneKeyword[3] in episode['scene_id']:
            if success == True:
                dataPerScene[sceneKeyword[3]][0]['True'].append(episode_id)
            else:
                dataPerScene[sceneKeyword[3]][0]['False'].append(episode_id)
        #Elmira case
        if sceneKeyword[4] in episode['scene_id']:
            if success == True:
                dataPerScene[sceneKeyword[4]][0]['True'].append(episode_id)
            else:
                dataPerScene[sceneKeyword[4]][0]['False'].append(episode_id)
        #Eudora case
        if sceneKeyword[5] in episode['scene_id']:
            if success == True:
                dataPerScene[sceneKeyword[5]][0]['True'].append(episode_id)
            else:
                dataPerScene[sceneKeyword[5]][0]['False'].append(episode_id)
        #Greigsville case
        if sceneKeyword[6] in episode['scene_id']:
            if success == True:
                dataPerScene[sceneKeyword[6]][0]['True'].append(episode_id)
            else:
                dataPerScene[sceneKeyword[6]][0]['False'].append(episode_id)
        #Mosquito case
        if sceneKeyword[7] in episode['scene_id']:
            if success == True:
                dataPerScene[sceneKeyword[7]][0]['True'].append(episode_id)
            else:
                dataPerScene[sceneKeyword[7]][0]['False'].append(episode_id)
        #Pablo case
        if sceneKeyword[8] in episode['scene_id']:
            if success == True:
                dataPerScene[sceneKeyword[8]][0]['True'].append(episode_id)
            else:
                dataPerScene[sceneKeyword[8]][0]['False'].append(episode_id)
        #Ribera case
        if sceneKeyword[9] in episode['scene_id']:
            if success == True:
                dataPerScene[sceneKeyword[9]][0]['True'].append(episode_id)
            else:
                dataPerScene[sceneKeyword[9]][0]['False'].append(episode_id)
        #Sands case
        if sceneKeyword[10] in episode['scene_id']:
            if success == True:
                dataPerScene[sceneKeyword[10]][0]['True'].append(episode_id)
            else:
                dataPerScene[sceneKeyword[10]][0]['False'].append(episode_id)
        #Scioto case
        if sceneKeyword[11] in episode['scene_id']:
            if success == True:
                dataPerScene[sceneKeyword[11]][0]['True'].append(episode_id)
            else:
                dataPerScene[sceneKeyword[12]][0]['False'].append(episode_id)
        #Sisters case
        if sceneKeyword[12] in episode['scene_id']:
            if success == True:
                dataPerScene[sceneKeyword[12]][0]['True'].append(episode_id)
            else:
                dataPerScene[sceneKeyword[12]][0]['False'].append(episode_id)
        #Swormville case
        if sceneKeyword[13] in episode['scene_id']:
            if success == True:
                dataPerScene[sceneKeyword[13]][0]['True'].append(episode_id)
            else:
                dataPerScene[sceneKeyword[13]][0]['False'].append(episode_id)

        episode_id += 1
        print(episode_id)        

def storeInJson():
    dumped = {
        #Define the links between nodes with value, Links is a list of dictionnary
        "Links" : [
            {"source" : "Success", "target" : sceneKeyword[0],"value" : len(dataPerScene[sceneKeyword[0]][0]['True'])},
            {"source" : "Failed", "target" : sceneKeyword[0],"value" : len(dataPerScene[sceneKeyword[0]][0]['False'])},
            {"source" : "Success", "target" : sceneKeyword[1],"value" : len(dataPerScene[sceneKeyword[1]][0]['True'])},
            {"source" : "Failed", "target" : sceneKeyword[1],"value" : len(dataPerScene[sceneKeyword[1]][0]['False'])},
            {"source" : "Success", "target" : sceneKeyword[2],"value" : len(dataPerScene[sceneKeyword[2]][0]['True'])},
            {"source" : "Failed", "target" : sceneKeyword[2],"value" : len(dataPerScene[sceneKeyword[2]][0]['False'])},
            {"source" : "Success", "target" : sceneKeyword[3],"value" : len(dataPerScene[sceneKeyword[3]][0]['True'])},
            {"source" : "Failed", "target" : sceneKeyword[3],"value" : len(dataPerScene[sceneKeyword[3]][0]['False'])},
            {"source" : "Success", "target" : sceneKeyword[4],"value" : len(dataPerScene[sceneKeyword[4]][0]['True'])},
            {"source" : "Failed", "target" : sceneKeyword[4],"value" : len(dataPerScene[sceneKeyword[4]][0]['False'])},
            {"source" : "Success", "target" : sceneKeyword[5],"value" : len(dataPerScene[sceneKeyword[5]][0]['True'])},
            {"source" : "Failed", "target" : sceneKeyword[5],"value" : len(dataPerScene[sceneKeyword[5]][0]['False'])},
            {"source" : "Success", "target" : sceneKeyword[6],"value" : len(dataPerScene[sceneKeyword[6]][0]['True'])},
            {"source" : "Failed", "target" : sceneKeyword[6],"value" : len(dataPerScene[sceneKeyword[6]][0]['False'])},
            {"source" : "Success", "target" : sceneKeyword[7],"value" : len(dataPerScene[sceneKeyword[7]][0]['True'])},
            {"source" : "Failed", "target" : sceneKeyword[7],"value" : len(dataPerScene[sceneKeyword[7]][0]['False'])},
            {"source" : "Success", "target" : sceneKeyword[8],"value" : len(dataPerScene[sceneKeyword[8]][0]['True'])},
            {"source" : "Failed", "target" : sceneKeyword[8],"value" : len(dataPerScene[sceneKeyword[8]][0]['False'])},
            {"source" : "Success", "target" : sceneKeyword[9],"value" : len(dataPerScene[sceneKeyword[9]][0]['True'])},
            {"source" : "Failed", "target" : sceneKeyword[9],"value" : len(dataPerScene[sceneKeyword[9]][0]['False'])},
            {"source" : "Success", "target" : sceneKeyword[10],"value" : len(dataPerScene[sceneKeyword[10]][0]['True'])},
            {"source" : "Failed", "target" : sceneKeyword[10],"value" : len(dataPerScene[sceneKeyword[10]][0]['False'])},
            {"source" : "Success", "target" : sceneKeyword[11],"value" : len(dataPerScene[sceneKeyword[11]][0]['True'])},
            {"source" : "Failed", "target" : sceneKeyword[11],"value" : len(dataPerScene[sceneKeyword[11]][0]['False'])},
            {"source" : "Success", "target" : sceneKeyword[12],"value" : len(dataPerScene[sceneKeyword[12]][0]['True'])},
            {"source" : "Failed", "target" : sceneKeyword[12],"value" : len(dataPerScene[sceneKeyword[12]][0]['False'])},
            {"source" : "Success", "target" : sceneKeyword[13],"value" : len(dataPerScene[sceneKeyword[13]][0]['True'])},
            {"source" : "Failed", "target" : sceneKeyword[13],"value" : len(dataPerScene[sceneKeyword[13]][0]['False'])}        
        ],
        "Nodes" : [
            {"name" : "Success"},
            {"name" : "Failed"},
            {"name" : sceneKeyword[0]},
            {"name" : sceneKeyword[1]},
            {"name" : sceneKeyword[2]},
            {"name" : sceneKeyword[3]},
            {"name" : sceneKeyword[4]},
            {"name" : sceneKeyword[5]},
            {"name" : sceneKeyword[6]},
            {"name" : sceneKeyword[7]},
            {"name" : sceneKeyword[8]},
            {"name" : sceneKeyword[9]},
            {"name" : sceneKeyword[10]},
            {"name" : sceneKeyword[11]},
            {"name" : sceneKeyword[12]},
            {"name" : sceneKeyword[13]}
        ]
    }
    dumped = str(dumped)
    dumped = dumped.replace("'",'"')
    with open("sankeyData.json", "w") as outfile:
        outfile.write(dumped)


#Calling the function to process the date and store them in dataPerScene
print("Start Parsing")
sceneLevel()
print("End Parsing and Start Writing")
storeInJson()
print("End Writing")