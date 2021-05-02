import csv
import math
import json
import pickle
import os, os.path 
from collections import defaultdict

def colorForVector(collisionRate):
    if(collisionRate <= 0):
        return "Wozniak"
    if((collisionRate > 0) and (collisionRate < 0.1)):
        return "Torvalds"
    if(collisionRate > 0.1):
        return "Jobs"


ORBSlam_dir = 'ORBSlam/'
ShortestPath_dir = 'ShortestPath/'

CSV_Output = 'data.csv'

file_in_ORBSlam = sum(len(files) for _, _, files in os.walk(ORBSlam_dir))

json_data = open('val.json')
data = json.load(json_data)

r = file_in_ORBSlam - 2

scene = []
sceneKeyword = ['Cantwell', 'Denmark', 'Eastville', 'Edgemere', 'Elmira', 'Eudora', 'Greigsville' , 'Mosquito', 'Pablo', 'Ribera', 'Sands', 'Scioto', 'Sisters', 'Swormville']
sceneDict = {}
dataPerScene = {'Cantwell' : [], 'Denmark' : [], 'Eastville' : [], 'Edgemere' : [], 'Elmira' : [], 'Eudora' : [], 'Greigsville' : [], 'Mosquito' : [], 'Pablo' : [], 'Ribera' : [], 'Sands' : [], 'Scioto' : [], 'Sisters' : [], 'Swormville' : []}

episode_id = 0

#Extract data with episode_id and the corresponding scene from JSON file
for episode in data['episodes']:
    if(episode['episode_id'] not in scene):
        sceneDict.update({episode['episode_id'] : episode['scene_id']})

dataPerScene = defaultdict(list)

#Calculating SPL, collision_rate and succes_rate  
while episode_id < r:

    li = 0
    pi = 0
    si = 0
    SPL = 0
    collision_rate = 0
    success_rate = 0
    nb_episodeInScene = 0

    while(sceneKeyword[0] in sceneDict[episode_id]):
        #Load Data from episodes
        episode_ORBSlam = pickle.load(open( ORBSlam_dir +"episodeStats"+str(episode_id)+".p", "rb" ))
        episode_ShortestPath = pickle.load(open( ShortestPath_dir +"episodeStats"+str(episode_id)+".p", "rb" ))

        collisions = episode_ORBSlam["collisions"]
        success = episode_ORBSlam["success"]
        pose_env_ORBSlam = episode_ORBSlam["pose_env"]
        pose_env_ShortestPath = episode_ShortestPath["pose_env"] 


        li = len(pose_env_ORBSlam)
        pi = len(pose_env_ShortestPath)
        si = int(success == True)

        SPL += si*(li/max(pi,li))

        success_rate += int(success == True)

        collision_rate = sum(collisions)

        episode_id += 1
        nb_episodeInScene += 1
    
    #Calculate all the data and append them in a list contained in a dictionary
    SPL *= 1/nb_episodeInScene
    success_rate /= nb_episodeInScene
    collision_rate /= nb_episodeInScene
    dataPerScene[sceneKeyword[0]].append(SPL)
    dataPerScene[sceneKeyword[0]].append(success_rate)
    dataPerScene[sceneKeyword[0]].append(collision_rate)
    print(dataPerScene[sceneKeyword[0]])

    #Reset variables
    li = 0
    pi = 0
    si = 0
    SPL = 0
    collision_rate = 0
    success_rate = 0
    nb_episodeInScene = 0

    while(sceneKeyword[1] in sceneDict[episode_id]):
        #Load Data from episodes
        episode_ORBSlam = pickle.load(open( ORBSlam_dir +"episodeStats"+str(episode_id)+".p", "rb" ))
        episode_ShortestPath = pickle.load(open( ShortestPath_dir +"episodeStats"+str(episode_id)+".p", "rb" ))

        collisions = episode_ORBSlam["collisions"]
        success = episode_ORBSlam["success"]
        pose_env_ORBSlam = episode_ORBSlam["pose_env"]
        pose_env_ShortestPath = episode_ShortestPath["pose_env"] 


        li = len(pose_env_ORBSlam)
        pi = len(pose_env_ShortestPath)
        si = int(success == True)

        SPL += si*(li/max(pi,li))

        success_rate += int(success == True)

        collision_rate = sum(collisions)

        episode_id += 1
        nb_episodeInScene += 1
    
    SPL *= 1/nb_episodeInScene
    success_rate /= nb_episodeInScene
    collision_rate /= nb_episodeInScene
    dataPerScene[sceneKeyword[1]].append(SPL)
    dataPerScene[sceneKeyword[1]].append(success_rate)
    dataPerScene[sceneKeyword[1]].append(collision_rate)
    print(dataPerScene[sceneKeyword[1]])

    #Reset variables
    li = 0
    pi = 0
    si = 0
    SPL = 0
    collision_rate = 0
    success_rate = 0
    nb_episodeInScene = 0

    while(sceneKeyword[2] in sceneDict[episode_id]):
        #Load Data from episodes
        episode_ORBSlam = pickle.load(open( ORBSlam_dir +"episodeStats"+str(episode_id)+".p", "rb" ))
        episode_ShortestPath = pickle.load(open( ShortestPath_dir +"episodeStats"+str(episode_id)+".p", "rb" ))

        collisions = episode_ORBSlam["collisions"]
        success = episode_ORBSlam["success"]
        pose_env_ORBSlam = episode_ORBSlam["pose_env"]
        pose_env_ShortestPath = episode_ShortestPath["pose_env"] 


        li = len(pose_env_ORBSlam)
        pi = len(pose_env_ShortestPath)
        si = int(success == True)

        SPL += si*(li/max(pi,li))

        success_rate += int(success == True)

        collision_rate = sum(collisions)

        episode_id += 1
        nb_episodeInScene += 1
    
    SPL *= 1/nb_episodeInScene
    success_rate /= nb_episodeInScene
    collision_rate /= nb_episodeInScene
    dataPerScene[sceneKeyword[2]].append(SPL)
    dataPerScene[sceneKeyword[2]].append(success_rate)
    dataPerScene[sceneKeyword[2]].append(collision_rate)
    print(dataPerScene[sceneKeyword[2]])

    #Reset variables
    li = 0
    pi = 0
    si = 0
    SPL = 0
    collision_rate = 0
    success_rate = 0
    nb_episodeInScene = 0

    while(sceneKeyword[3] in sceneDict[episode_id]):
        #Load Data from episodes
        episode_ORBSlam = pickle.load(open( ORBSlam_dir +"episodeStats"+str(episode_id)+".p", "rb" ))
        episode_ShortestPath = pickle.load(open( ShortestPath_dir +"episodeStats"+str(episode_id)+".p", "rb" ))

        collisions = episode_ORBSlam["collisions"]
        success = episode_ORBSlam["success"]
        pose_env_ORBSlam = episode_ORBSlam["pose_env"]
        pose_env_ShortestPath = episode_ShortestPath["pose_env"] 


        li = len(pose_env_ORBSlam)
        pi = len(pose_env_ShortestPath)
        si = int(success == True)

        SPL += si*(li/max(pi,li))

        success_rate += int(success == True)

        collision_rate = sum(collisions)

        episode_id += 1
        nb_episodeInScene += 1
    
    SPL *= 1/nb_episodeInScene
    success_rate /= nb_episodeInScene
    collision_rate /= nb_episodeInScene
    dataPerScene[sceneKeyword[3]].append(SPL)
    dataPerScene[sceneKeyword[3]].append(success_rate)
    dataPerScene[sceneKeyword[3]].append(collision_rate)
    print(dataPerScene[sceneKeyword[3]])

    #Reset variables
    li = 0
    pi = 0
    si = 0
    SPL = 0
    collision_rate = 0
    success_rate = 0
    nb_episodeInScene = 0

    while(sceneKeyword[4] in sceneDict[episode_id]):
        #Load Data from episodes
        episode_ORBSlam = pickle.load(open( ORBSlam_dir +"episodeStats"+str(episode_id)+".p", "rb" ))
        episode_ShortestPath = pickle.load(open( ShortestPath_dir +"episodeStats"+str(episode_id)+".p", "rb" ))

        collisions = episode_ORBSlam["collisions"]
        success = episode_ORBSlam["success"]
        pose_env_ORBSlam = episode_ORBSlam["pose_env"]
        pose_env_ShortestPath = episode_ShortestPath["pose_env"] 


        li = len(pose_env_ORBSlam)
        pi = len(pose_env_ShortestPath)
        si = int(success == True)

        SPL += si*(li/max(pi,li))

        success_rate += int(success == True)

        collision_rate = sum(collisions)

        episode_id += 1
        nb_episodeInScene += 1
    
    SPL *= 1/nb_episodeInScene
    success_rate /= nb_episodeInScene
    collision_rate /= nb_episodeInScene
    dataPerScene[sceneKeyword[4]].append(SPL)
    dataPerScene[sceneKeyword[4]].append(success_rate)
    dataPerScene[sceneKeyword[4]].append(collision_rate)
    print(dataPerScene[sceneKeyword[4]])

    #Reset variables
    li = 0
    pi = 0
    si = 0
    SPL = 0
    collision_rate = 0
    success_rate = 0
    nb_episodeInScene = 0

    while(sceneKeyword[5] in sceneDict[episode_id]):
        #Load Data from episodes
        episode_ORBSlam = pickle.load(open( ORBSlam_dir +"episodeStats"+str(episode_id)+".p", "rb" ))
        episode_ShortestPath = pickle.load(open( ShortestPath_dir +"episodeStats"+str(episode_id)+".p", "rb" ))

        collisions = episode_ORBSlam["collisions"]
        success = episode_ORBSlam["success"]
        pose_env_ORBSlam = episode_ORBSlam["pose_env"]
        pose_env_ShortestPath = episode_ShortestPath["pose_env"] 


        li = len(pose_env_ORBSlam)
        pi = len(pose_env_ShortestPath)
        si = int(success == True)

        SPL += si*(li/max(pi,li))

        success_rate += int(success == True)

        collision_rate = sum(collisions)

        episode_id += 1
        nb_episodeInScene += 1
    
    SPL *= 1/nb_episodeInScene
    success_rate /= nb_episodeInScene
    collision_rate /= nb_episodeInScene
    dataPerScene[sceneKeyword[5]].append(SPL)
    dataPerScene[sceneKeyword[5]].append(success_rate)
    dataPerScene[sceneKeyword[5]].append(collision_rate)
    print(dataPerScene[sceneKeyword[5]])

    #Reset variables
    li = 0
    pi = 0
    si = 0
    SPL = 0
    collision_rate = 0
    success_rate = 0
    nb_episodeInScene = 0

    while(sceneKeyword[6] in sceneDict[episode_id]):
        #Load Data from episodes
        episode_ORBSlam = pickle.load(open( ORBSlam_dir +"episodeStats"+str(episode_id)+".p", "rb" ))
        episode_ShortestPath = pickle.load(open( ShortestPath_dir +"episodeStats"+str(episode_id)+".p", "rb" ))

        collisions = episode_ORBSlam["collisions"]
        success = episode_ORBSlam["success"]
        pose_env_ORBSlam = episode_ORBSlam["pose_env"]
        pose_env_ShortestPath = episode_ShortestPath["pose_env"] 


        li = len(pose_env_ORBSlam)
        pi = len(pose_env_ShortestPath)
        si = int(success == True)

        SPL += si*(li/max(pi,li))

        success_rate += int(success == True)

        collision_rate = sum(collisions)

        episode_id += 1
        nb_episodeInScene += 1
    
    SPL *= 1/nb_episodeInScene
    success_rate /= nb_episodeInScene
    collision_rate /= nb_episodeInScene
    dataPerScene[sceneKeyword[6]].append(SPL)
    dataPerScene[sceneKeyword[6]].append(success_rate)
    dataPerScene[sceneKeyword[6]].append(collision_rate)
    print(dataPerScene[sceneKeyword[6]])

    #Reset variables
    li = 0
    pi = 0
    si = 0
    SPL = 0
    collision_rate = 0
    success_rate = 0
    nb_episodeInScene = 0

    while(sceneKeyword[7] in sceneDict[episode_id]):
        #Load Data from episodes
        episode_ORBSlam = pickle.load(open( ORBSlam_dir +"episodeStats"+str(episode_id)+".p", "rb" ))
        episode_ShortestPath = pickle.load(open( ShortestPath_dir +"episodeStats"+str(episode_id)+".p", "rb" ))

        collisions = episode_ORBSlam["collisions"]
        success = episode_ORBSlam["success"]
        pose_env_ORBSlam = episode_ORBSlam["pose_env"]
        pose_env_ShortestPath = episode_ShortestPath["pose_env"] 


        li = len(pose_env_ORBSlam)
        pi = len(pose_env_ShortestPath)
        si = int(success == True)

        SPL += si*(li/max(pi,li))

        success_rate += int(success == True)

        collision_rate = sum(collisions)

        episode_id += 1
        nb_episodeInScene += 1
    
    SPL *= 1/nb_episodeInScene
    success_rate /= nb_episodeInScene
    collision_rate /= nb_episodeInScene
    dataPerScene[sceneKeyword[7]].append(SPL)
    dataPerScene[sceneKeyword[7]].append(success_rate)
    dataPerScene[sceneKeyword[7]].append(collision_rate)
    print(dataPerScene[sceneKeyword[7]])

    #Reset variables
    li = 0
    pi = 0
    si = 0
    SPL = 0
    collision_rate = 0
    success_rate = 0
    nb_episodeInScene = 0

    while(sceneKeyword[8] in sceneDict[episode_id]):
        #Load Data from episodes
        episode_ORBSlam = pickle.load(open( ORBSlam_dir +"episodeStats"+str(episode_id)+".p", "rb" ))
        episode_ShortestPath = pickle.load(open( ShortestPath_dir +"episodeStats"+str(episode_id)+".p", "rb" ))

        collisions = episode_ORBSlam["collisions"]
        success = episode_ORBSlam["success"]
        pose_env_ORBSlam = episode_ORBSlam["pose_env"]
        pose_env_ShortestPath = episode_ShortestPath["pose_env"] 


        li = len(pose_env_ORBSlam)
        pi = len(pose_env_ShortestPath)
        si = int(success == True)

        SPL += si*(li/max(pi,li))

        success_rate += int(success == True)

        collision_rate = sum(collisions)

        episode_id += 1
        nb_episodeInScene += 1
    
    SPL *= 1/nb_episodeInScene
    success_rate /= nb_episodeInScene
    collision_rate /= nb_episodeInScene
    dataPerScene[sceneKeyword[8]].append(SPL)
    dataPerScene[sceneKeyword[8]].append(success_rate)
    dataPerScene[sceneKeyword[8]].append(collision_rate)
    print(dataPerScene[sceneKeyword[8]])

    #Reset variables
    li = 0
    pi = 0
    si = 0
    SPL = 0
    collision_rate = 0
    success_rate = 0
    nb_episodeInScene = 0

    while(sceneKeyword[9] in sceneDict[episode_id]):
        #Load Data from episodes
        episode_ORBSlam = pickle.load(open( ORBSlam_dir +"episodeStats"+str(episode_id)+".p", "rb" ))
        episode_ShortestPath = pickle.load(open( ShortestPath_dir +"episodeStats"+str(episode_id)+".p", "rb" ))

        collisions = episode_ORBSlam["collisions"]
        success = episode_ORBSlam["success"]
        pose_env_ORBSlam = episode_ORBSlam["pose_env"]
        pose_env_ShortestPath = episode_ShortestPath["pose_env"] 


        li = len(pose_env_ORBSlam)
        pi = len(pose_env_ShortestPath)
        si = int(success == True)

        SPL += si*(li/max(pi,li))

        success_rate += int(success == True)

        collision_rate = sum(collisions)

        episode_id += 1
        nb_episodeInScene += 1
    
    SPL *= 1/nb_episodeInScene
    success_rate /= nb_episodeInScene
    collision_rate /= nb_episodeInScene
    dataPerScene[sceneKeyword[9]].append(SPL)
    dataPerScene[sceneKeyword[9]].append(success_rate)
    dataPerScene[sceneKeyword[9]].append(collision_rate)
    print(dataPerScene[sceneKeyword[9]])

    #Reset variables
    li = 0
    pi = 0
    si = 0
    SPL = 0
    collision_rate = 0
    success_rate = 0
    nb_episodeInScene = 0

    while(sceneKeyword[10] in sceneDict[episode_id]):
        #Load Data from episodes
        episode_ORBSlam = pickle.load(open( ORBSlam_dir +"episodeStats"+str(episode_id)+".p", "rb" ))
        episode_ShortestPath = pickle.load(open( ShortestPath_dir +"episodeStats"+str(episode_id)+".p", "rb" ))

        collisions = episode_ORBSlam["collisions"]
        success = episode_ORBSlam["success"]
        pose_env_ORBSlam = episode_ORBSlam["pose_env"]
        pose_env_ShortestPath = episode_ShortestPath["pose_env"] 


        li = len(pose_env_ORBSlam)
        pi = len(pose_env_ShortestPath)
        si = int(success == True)

        SPL += si*(li/max(pi,li))

        success_rate += int(success == True)

        collision_rate = sum(collisions)

        episode_id += 1
        nb_episodeInScene += 1
    
    SPL *= 1/nb_episodeInScene
    success_rate /= nb_episodeInScene
    collision_rate /= nb_episodeInScene
    dataPerScene[sceneKeyword[10]].append(SPL)
    dataPerScene[sceneKeyword[10]].append(success_rate)
    dataPerScene[sceneKeyword[10]].append(collision_rate)
    print(dataPerScene[sceneKeyword[10]])

    #Reset variables
    li = 0
    pi = 0
    si = 0
    SPL = 0
    collision_rate = 0
    success_rate = 0
    nb_episodeInScene = 0

    while(sceneKeyword[11] in sceneDict[episode_id]):
        #Load Data from episodes
        episode_ORBSlam = pickle.load(open( ORBSlam_dir +"episodeStats"+str(episode_id)+".p", "rb" ))
        episode_ShortestPath = pickle.load(open( ShortestPath_dir +"episodeStats"+str(episode_id)+".p", "rb" ))

        collisions = episode_ORBSlam["collisions"]
        success = episode_ORBSlam["success"]
        pose_env_ORBSlam = episode_ORBSlam["pose_env"]
        pose_env_ShortestPath = episode_ShortestPath["pose_env"] 


        li = len(pose_env_ORBSlam)
        pi = len(pose_env_ShortestPath)
        si = int(success == True)

        SPL += si*(li/max(pi,li))

        success_rate += int(success == True)

        collision_rate = sum(collisions)

        episode_id += 1
        nb_episodeInScene += 1
    
    SPL *= 1/nb_episodeInScene
    success_rate /= nb_episodeInScene
    collision_rate /= nb_episodeInScene
    dataPerScene[sceneKeyword[11]].append(SPL)
    dataPerScene[sceneKeyword[11]].append(success_rate)
    dataPerScene[sceneKeyword[11]].append(collision_rate)
    print(dataPerScene[sceneKeyword[11]])

    #Reset variables
    li = 0
    pi = 0
    si = 0
    SPL = 0
    collision_rate = 0
    success_rate = 0
    nb_episodeInScene = 0

    while(sceneKeyword[12] in sceneDict[episode_id]):
        #Load Data from episodes
        episode_ORBSlam = pickle.load(open( ORBSlam_dir +"episodeStats"+str(episode_id)+".p", "rb" ))
        episode_ShortestPath = pickle.load(open( ShortestPath_dir +"episodeStats"+str(episode_id)+".p", "rb" ))

        collisions = episode_ORBSlam["collisions"]
        success = episode_ORBSlam["success"]
        pose_env_ORBSlam = episode_ORBSlam["pose_env"]
        pose_env_ShortestPath = episode_ShortestPath["pose_env"] 


        li = len(pose_env_ORBSlam)
        pi = len(pose_env_ShortestPath)
        si = int(success == True)

        SPL += si*(li/max(pi,li))

        success_rate += int(success == True)

        collision_rate = sum(collisions)

        episode_id += 1
        nb_episodeInScene += 1
    
    SPL *= 1/nb_episodeInScene
    success_rate /= nb_episodeInScene
    collision_rate /= nb_episodeInScene
    dataPerScene[sceneKeyword[12]].append(SPL)
    dataPerScene[sceneKeyword[12]].append(success_rate)
    dataPerScene[sceneKeyword[12]].append(collision_rate)
    print(dataPerScene[sceneKeyword[12]])

    #Reset variables
    li = 0
    pi = 0
    si = 0
    SPL = 0
    collision_rate = 0
    success_rate = 0
    nb_episodeInScene = 0

    while((sceneKeyword[13] in sceneDict[episode_id]) and (episode_id < 993)):
        #Load Data from episodes
        episode_ORBSlam = pickle.load(open( ORBSlam_dir +"episodeStats"+str(episode_id)+".p", "rb" ))
        episode_ShortestPath = pickle.load(open( ShortestPath_dir +"episodeStats"+str(episode_id)+".p", "rb" ))

        collisions = episode_ORBSlam["collisions"]
        success = episode_ORBSlam["success"]
        pose_env_ORBSlam = episode_ORBSlam["pose_env"]
        pose_env_ShortestPath = episode_ShortestPath["pose_env"] 


        li = len(pose_env_ORBSlam)
        pi = len(pose_env_ShortestPath)
        si = int(success == True)

        SPL += si*(li/max(pi,li))

        success_rate += int(success == True)

        collision_rate = sum(collisions)

        episode_id += 1
        nb_episodeInScene += 1
        print(episode_id)
    
    SPL *= 1/nb_episodeInScene
    success_rate /= nb_episodeInScene
    collision_rate /= nb_episodeInScene
    dataPerScene[sceneKeyword[13]].append(SPL)
    dataPerScene[sceneKeyword[13]].append(success_rate)
    dataPerScene[sceneKeyword[13]].append(collision_rate)
    print(dataPerScene[sceneKeyword[13]])

    #Reset variables
    li = 0
    pi = 0
    si = 0
    SPL = 0
    collision_rate = 0
    success_rate = 0
    nb_episodeInScene = 0

with open('data.csv', 'w') as csv_file:
        fieldnames = ['SPL', 'Success_Rate', 'Collisions_rate', 'Species']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',')
        csv_writer.writeheader()
        csv_writer.writerow({'SPL' : str(dataPerScene[sceneKeyword[0]][0]), 'Success_Rate' : str(dataPerScene[sceneKeyword[0]][1]), 'Collisions_rate' : str(dataPerScene[sceneKeyword[0]][2]), 'Species' : colorForVector(dataPerScene[sceneKeyword[0]][2])})
        csv_writer.writerow({'SPL' : str(dataPerScene[sceneKeyword[1]][0]), 'Success_Rate' : str(dataPerScene[sceneKeyword[1]][1]), 'Collisions_rate' : str(dataPerScene[sceneKeyword[1]][2]), 'Species' : colorForVector(dataPerScene[sceneKeyword[1]][2])})
        csv_writer.writerow({'SPL' : str(dataPerScene[sceneKeyword[2]][0]), 'Success_Rate' : str(dataPerScene[sceneKeyword[2]][1]), 'Collisions_rate' : str(dataPerScene[sceneKeyword[2]][2]), 'Species' : colorForVector(dataPerScene[sceneKeyword[2]][2])})
        csv_writer.writerow({'SPL' : str(dataPerScene[sceneKeyword[3]][0]), 'Success_Rate' : str(dataPerScene[sceneKeyword[3]][1]), 'Collisions_rate' : str(dataPerScene[sceneKeyword[3]][2]), 'Species' : colorForVector(dataPerScene[sceneKeyword[3]][2])})
        csv_writer.writerow({'SPL' : str(dataPerScene[sceneKeyword[4]][0]), 'Success_Rate' : str(dataPerScene[sceneKeyword[4]][1]), 'Collisions_rate' : str(dataPerScene[sceneKeyword[4]][2]), 'Species' : colorForVector(dataPerScene[sceneKeyword[4]][2])})
        csv_writer.writerow({'SPL' : str(dataPerScene[sceneKeyword[5]][0]), 'Success_Rate' : str(dataPerScene[sceneKeyword[5]][1]), 'Collisions_rate' : str(dataPerScene[sceneKeyword[5]][2]), 'Species' : colorForVector(dataPerScene[sceneKeyword[5]][2])})
        csv_writer.writerow({'SPL' : str(dataPerScene[sceneKeyword[6]][0]), 'Success_Rate' : str(dataPerScene[sceneKeyword[6]][1]), 'Collisions_rate' : str(dataPerScene[sceneKeyword[6]][2]), 'Species' : colorForVector(dataPerScene[sceneKeyword[6]][2])})
        csv_writer.writerow({'SPL' : str(dataPerScene[sceneKeyword[7]][0]), 'Success_Rate' : str(dataPerScene[sceneKeyword[7]][1]), 'Collisions_rate' : str(dataPerScene[sceneKeyword[7]][2]), 'Species' : colorForVector(dataPerScene[sceneKeyword[7]][2])})
        csv_writer.writerow({'SPL' : str(dataPerScene[sceneKeyword[8]][0]), 'Success_Rate' : str(dataPerScene[sceneKeyword[8]][1]), 'Collisions_rate' : str(dataPerScene[sceneKeyword[8]][2]), 'Species' : colorForVector(dataPerScene[sceneKeyword[8]][2])})
        csv_writer.writerow({'SPL' : str(dataPerScene[sceneKeyword[9]][0]), 'Success_Rate' : str(dataPerScene[sceneKeyword[9]][1]), 'Collisions_rate' : str(dataPerScene[sceneKeyword[9]][2]), 'Species' : colorForVector(dataPerScene[sceneKeyword[9]][2])})
        csv_writer.writerow({'SPL' : str(dataPerScene[sceneKeyword[10]][0]), 'Success_Rate' : str(dataPerScene[sceneKeyword[10]][1]), 'Collisions_rate' : str(dataPerScene[sceneKeyword[10]][2]), 'Species' : colorForVector(dataPerScene[sceneKeyword[10]][2])})
        csv_writer.writerow({'SPL' : str(dataPerScene[sceneKeyword[11]][0]), 'Success_Rate' : str(dataPerScene[sceneKeyword[11]][1]), 'Collisions_rate' : str(dataPerScene[sceneKeyword[11]][2]), 'Species' : colorForVector(dataPerScene[sceneKeyword[11]][2])})
        csv_writer.writerow({'SPL' : str(dataPerScene[sceneKeyword[12]][0]), 'Success_Rate' : str(dataPerScene[sceneKeyword[12]][1]), 'Collisions_rate' : str(dataPerScene[sceneKeyword[12]][2]), 'Species' : colorForVector(dataPerScene[sceneKeyword[12]][2])})
        csv_writer.writerow({'SPL' : str(dataPerScene[sceneKeyword[13]][0]), 'Success_Rate' : str(dataPerScene[sceneKeyword[13]][1]), 'Collisions_rate' : str(dataPerScene[sceneKeyword[13]][2]), 'Species' : colorForVector(dataPerScene[sceneKeyword[13]][2])})
