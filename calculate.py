import math
import csv
import json
import pickle
import os, os.path
import threading

ORBSlam_dir = 'ORBSlam/'
ShortestPath_dir = 'ShortestPath/'

sceneKeyword = ['Cantwell', 'Denmark', 'Eastville', 'Edgemere', 'Elmira', 'Eudora', 'Greigsville' , 'Mosquito', 'Pablo', 'Ribera', 'Sands', 'Scioto', 'Sisters', 'Swormville']
dataPerScene = {'Cantwell' : [{'True' : [], 'False' : [], 'SPL' : '', 'Success_rate' : ''}], 'Denmark' : [{'True' : [], 'False' : [], 'SPL' : '', 'Success_rate' : ''}], 'Eastville' : [{'True' : [], 'False' : [], 'SPL' : '', 'Success_rate' : ''}], 'Edgemere' : [{'True' : [], 'False' : [], 'SPL' : '', 'Success_rate' : ''}], 'Elmira' : [{'True' : [], 'False' : [], 'SPL' : '', 'Success_rate' : ''}], 'Eudora' : [{'True' : [], 'False' : [], 'SPL' : '', 'Success_rate' : ''}], 'Greigsville' : [{'True' : [], 'False' : [], 'SPL' : '', 'Success_rate' : ''}], 'Mosquito' : [{'True' : [], 'False' : [], 'SPL' : '', 'Success_rate' : ''}], 'Pablo' : [{'True' : [], 'False' : [], 'SPL' : '', 'Success_rate' : ''}], 'Ribera' : [{'True' : [], 'False' : [], 'SPL' : '', 'Success_rate' : ''}], 'Sands' : [{'True' : [], 'False' : [], 'SPL' : '', 'Success_rate' : ''}], 'Scioto' : [{'True' : [], 'False' : [], 'SPL' : '', 'Success_rate' : ''}], 'Sisters' : [{'True' : [], 'False' : [], 'SPL' : '', 'Success_rate' : ''}], 'Swormville' : [{'True' : [], 'False' : [], 'SPL' : '', 'Success_rate' : ''}]}

#Calculate the Euclidian Distance between point A and point B (note : the two parameters need to be an array of at least two values)
def eucldianValue(point_xA, point_xB, point_yA, point_yB):
    return math.sqrt((point_xA-point_xB)**2+(point_yA-point_yB)**2)

def episodeLevel(scene_id):
    euclidianDistance_StartToEnd = []
    lengthShortestPath = []
    lengthORBSlamPath = []
    euclidianDistance_StopPointToEnd = []
    numberOfCollisions = []

    sceneDict = {}

    episode_id = 0
    episodePerScene = 0

    json_data = open('val.json')
    data = json.load(json_data)

    file_in_ORBSlam = sum(len(files) for _, _, files in os.walk(ORBSlam_dir))

    for episode in data['episodes']:
        if(episode['episode_id'] not in sceneDict):
            sceneDict.update({episode['episode_id'] : episode['scene_id']})

    for episode_id in range(file_in_ORBSlam-1):
        if(scene_id in sceneDict[episode_id]):
            #We load both episode
            episode_ORBSlam = pickle.load(open( ORBSlam_dir +"episodeStats"+str(episode_id)+".p", "rb" ))
            episode_ShortestPath = pickle.load(open( ShortestPath_dir +"episodeStats"+str(episode_id)+".p", "rb" ))

            collisions = episode_ORBSlam["collisions"]
            pose_env_ORBSlam = episode_ORBSlam["pose_env"]
            pose_env_ShortestPath = episode_ShortestPath["pose_env"]

            euclidianDistance_StartToEnd.append(eucldianValue(pose_env_ShortestPath[0][0,3], pose_env_ShortestPath[len(pose_env_ShortestPath)-1][0,3], pose_env_ShortestPath[0][2,3], pose_env_ShortestPath[len(pose_env_ShortestPath)-1][2,3]))
            lengthShortestPath.append(len(pose_env_ShortestPath))
            lengthORBSlamPath.append(len(pose_env_ORBSlam))
            euclidianDistance_StopPointToEnd.append(eucldianValue(pose_env_ORBSlam[0][0,3], pose_env_ORBSlam[len(pose_env_ORBSlam)-1][0,3], pose_env_ORBSlam[0][2,3], pose_env_ORBSlam[len(pose_env_ORBSlam)-1][2,3]))
            numberOfCollisions.append(sum(collisions))
            episodePerScene += 1

    print(episodePerScene)        
    print(len(euclidianDistance_StartToEnd))
    print(len(lengthShortestPath))
    print(len(lengthORBSlamPath))
    print(len(euclidianDistance_StopPointToEnd))
    print(len(numberOfCollisions))

    with open('Swormville.csv', 'w') as csv_file:
        fieldnames = ['Start_to_End', 'Length_ShortestPath', 'Length_ORBSlamPath', 'Stop_to_End', 'Number_of_collisions']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',')
        csv_writer.writeheader()
        for i in range(episodePerScene):
            csv_writer.writerow({'Start_to_End' : euclidianDistance_StartToEnd[i], 'Length_ShortestPath' : lengthShortestPath[i], 'Length_ORBSlamPath' : lengthORBSlamPath[i], 'Stop_to_End' : euclidianDistance_StopPointToEnd[i], 'Number_of_collisions': numberOfCollisions[i]})

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
            SPL = 0
            success_rate = 0
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

def calculateSPL_SuccessRate():
    print("Starting to calcule SPL and Success Rate")
    #Load the JSON file where scene_id is located
    json_data = open('val.json')
    data = json.load(json_data)

    #A temporary sceneDict will only be usefull in this Dictionnary
    sceneDict = {}

    #The two variables that will be append in the main Dictionnary
    SPL = 0
    Success_rate = 0

    #Getting some data to calulcate the SPL
    li = 0
    pi = 0
    si = 0

    #Will be usefull as an index to sceneDict and to divide the SPL and the SuccessRate in the end
    episode_id = 0

    #Parsing the data from val.json to get the scene_id as a value and the episode_id as a key
    for episode in data['episodes']:
        if(episode['episode_id'] not in sceneDict):
            sceneDict.update({episode['episode_id'] : episode['scene_id']})

    while(sceneKeyword[0] in sceneDict[episode_id]):
        #Load Data from episodes
        episode_ORBSlam = pickle.load(open( ORBSlam_dir +"episodeStats"+str(episode_id)+".p", "rb" ))
        episode_ShortestPath = pickle.load(open( ShortestPath_dir +"episodeStats"+str(episode_id)+".p", "rb" ))

        success = episode_ORBSlam["success"]
        pose_env_ORBSlam = episode_ORBSlam["pose_env"]
        pose_env_ShortestPath = episode_ShortestPath["pose_env"] 


        li = len(pose_env_ORBSlam)
        pi = len(pose_env_ShortestPath)
        si = int(success == True)

        SPL += si*(li/max(pi,li))

        Success_rate += int(success == True)

        episode_id += 1

    #episode_id correspond to the number of episode too, so we don't need a value to store the number of episode that we pass during the loop
    SPL *= (1/episode_id)
    Success_rate /= episode_id
    dataPerScene[sceneKeyword[0]][0]['SPL'] = SPL
    dataPerScene[sceneKeyword[0]][0]['Success_rate'] = Success_rate  

    SPL, Success_rate = resetValue(SPL, Success_rate)

    while(sceneKeyword[1] in sceneDict[episode_id]):
        #Load Data from episodes
        episode_ORBSlam = pickle.load(open( ORBSlam_dir +"episodeStats"+str(episode_id)+".p", "rb" ))
        episode_ShortestPath = pickle.load(open( ShortestPath_dir +"episodeStats"+str(episode_id)+".p", "rb" ))

        success = episode_ORBSlam["success"]
        pose_env_ORBSlam = episode_ORBSlam["pose_env"]
        pose_env_ShortestPath = episode_ShortestPath["pose_env"] 


        li = len(pose_env_ORBSlam)
        pi = len(pose_env_ShortestPath)
        si = int(success == True)

        SPL += si*(li/max(pi,li))

        Success_rate += int(success == True)

        episode_id += 1

    #episode_id correspond to the number of episode too, so we don't need a value to store the number of episode that we pass during the loop
    SPL *= (1/episode_id)
    Success_rate /= episode_id
    dataPerScene[sceneKeyword[1]][0]['SPL'] = SPL
    dataPerScene[sceneKeyword[1]][0]['Success_rate'] = Success_rate  

    SPL, Success_rate = resetValue(SPL, Success_rate)

    while(sceneKeyword[2] in sceneDict[episode_id]):
        #Load Data from episodes
        episode_ORBSlam = pickle.load(open( ORBSlam_dir +"episodeStats"+str(episode_id)+".p", "rb" ))
        episode_ShortestPath = pickle.load(open( ShortestPath_dir +"episodeStats"+str(episode_id)+".p", "rb" ))

        success = episode_ORBSlam["success"]
        pose_env_ORBSlam = episode_ORBSlam["pose_env"]
        pose_env_ShortestPath = episode_ShortestPath["pose_env"] 


        li = len(pose_env_ORBSlam)
        pi = len(pose_env_ShortestPath)
        si = int(success == True)

        SPL += si*(li/max(pi,li))

        Success_rate += int(success == True)

        episode_id += 1

    #episode_id correspond to the number of episode too, so we don't need a value to store the number of episode that we pass during the loop
    SPL *= (1/episode_id)
    Success_rate /= episode_id
    dataPerScene[sceneKeyword[2]][0]['SPL'] = SPL
    dataPerScene[sceneKeyword[2]][0]['Success_rate'] = Success_rate  

    SPL, Success_rate = resetValue(SPL, Success_rate)

    while(sceneKeyword[3] in sceneDict[episode_id]):
        #Load Data from episodes
        episode_ORBSlam = pickle.load(open( ORBSlam_dir +"episodeStats"+str(episode_id)+".p", "rb" ))
        episode_ShortestPath = pickle.load(open( ShortestPath_dir +"episodeStats"+str(episode_id)+".p", "rb" ))

        success = episode_ORBSlam["success"]
        pose_env_ORBSlam = episode_ORBSlam["pose_env"]
        pose_env_ShortestPath = episode_ShortestPath["pose_env"] 


        li = len(pose_env_ORBSlam)
        pi = len(pose_env_ShortestPath)
        si = int(success == True)

        SPL += si*(li/max(pi,li))

        Success_rate += int(success == True)

        episode_id += 1

    #episode_id correspond to the number of episode too, so we don't need a value to store the number of episode that we pass during the loop
    SPL *= (1/episode_id)
    Success_rate /= episode_id
    dataPerScene[sceneKeyword[3]][0]['SPL'] = SPL
    dataPerScene[sceneKeyword[3]][0]['Success_rate'] = Success_rate  

    SPL, Success_rate = resetValue(SPL, Success_rate)

    while(sceneKeyword[4] in sceneDict[episode_id]):
        #Load Data from episodes
        episode_ORBSlam = pickle.load(open( ORBSlam_dir +"episodeStats"+str(episode_id)+".p", "rb" ))
        episode_ShortestPath = pickle.load(open( ShortestPath_dir +"episodeStats"+str(episode_id)+".p", "rb" ))

        success = episode_ORBSlam["success"]
        pose_env_ORBSlam = episode_ORBSlam["pose_env"]
        pose_env_ShortestPath = episode_ShortestPath["pose_env"] 


        li = len(pose_env_ORBSlam)
        pi = len(pose_env_ShortestPath)
        si = int(success == True)

        SPL += si*(li/max(pi,li))

        Success_rate += int(success == True)

        episode_id += 1

    #episode_id correspond to the number of episode too, so we don't need a value to store the number of episode that we pass during the loop
    SPL *= (1/episode_id)
    Success_rate /= episode_id
    dataPerScene[sceneKeyword[4]][0]['SPL'] = SPL
    dataPerScene[sceneKeyword[4]][0]['Success_rate'] = Success_rate  

    SPL, Success_rate = resetValue(SPL, Success_rate)

    while(sceneKeyword[5] in sceneDict[episode_id]):
        #Load Data from episodes
        episode_ORBSlam = pickle.load(open( ORBSlam_dir +"episodeStats"+str(episode_id)+".p", "rb" ))
        episode_ShortestPath = pickle.load(open( ShortestPath_dir +"episodeStats"+str(episode_id)+".p", "rb" ))

        success = episode_ORBSlam["success"]
        pose_env_ORBSlam = episode_ORBSlam["pose_env"]
        pose_env_ShortestPath = episode_ShortestPath["pose_env"] 


        li = len(pose_env_ORBSlam)
        pi = len(pose_env_ShortestPath)
        si = int(success == True)

        SPL += si*(li/max(pi,li))

        Success_rate += int(success == True)

        episode_id += 1

    #episode_id correspond to the number of episode too, so we don't need a value to store the number of episode that we pass during the loop
    SPL *= (1/episode_id)
    Success_rate /= episode_id
    dataPerScene[sceneKeyword[5]][0]['SPL'] = SPL
    dataPerScene[sceneKeyword[5]][0]['Success_rate'] = Success_rate  

    SPL, Success_rate = resetValue(SPL, Success_rate)

    while(sceneKeyword[6] in sceneDict[episode_id]):
        #Load Data from episodes
        episode_ORBSlam = pickle.load(open( ORBSlam_dir +"episodeStats"+str(episode_id)+".p", "rb" ))
        episode_ShortestPath = pickle.load(open( ShortestPath_dir +"episodeStats"+str(episode_id)+".p", "rb" ))

        success = episode_ORBSlam["success"]
        pose_env_ORBSlam = episode_ORBSlam["pose_env"]
        pose_env_ShortestPath = episode_ShortestPath["pose_env"] 


        li = len(pose_env_ORBSlam)
        pi = len(pose_env_ShortestPath)
        si = int(success == True)

        SPL += si*(li/max(pi,li))

        Success_rate += int(success == True)

        episode_id += 1

    #episode_id correspond to the number of episode too, so we don't need a value to store the number of episode that we pass during the loop
    SPL *= (1/episode_id)
    Success_rate /= episode_id
    dataPerScene[sceneKeyword[6]][0]['SPL'] = SPL
    dataPerScene[sceneKeyword[6]][0]['Success_rate'] = Success_rate  

    SPL, Success_rate = resetValue(SPL, Success_rate)

    while(sceneKeyword[7] in sceneDict[episode_id]):
        #Load Data from episodes
        episode_ORBSlam = pickle.load(open( ORBSlam_dir +"episodeStats"+str(episode_id)+".p", "rb" ))
        episode_ShortestPath = pickle.load(open( ShortestPath_dir +"episodeStats"+str(episode_id)+".p", "rb" ))

        success = episode_ORBSlam["success"]
        pose_env_ORBSlam = episode_ORBSlam["pose_env"]
        pose_env_ShortestPath = episode_ShortestPath["pose_env"] 


        li = len(pose_env_ORBSlam)
        pi = len(pose_env_ShortestPath)
        si = int(success == True)

        SPL += si*(li/max(pi,li))

        Success_rate += int(success == True)

        episode_id += 1

    #episode_id correspond to the number of episode too, so we don't need a value to store the number of episode that we pass during the loop
    SPL *= (1/episode_id)
    Success_rate /= episode_id
    dataPerScene[sceneKeyword[7]][0]['SPL'] = SPL
    dataPerScene[sceneKeyword[7]][0]['Success_rate'] = Success_rate  

    SPL, Success_rate = resetValue(SPL, Success_rate)

    while(sceneKeyword[8] in sceneDict[episode_id]):
        #Load Data from episodes
        episode_ORBSlam = pickle.load(open( ORBSlam_dir +"episodeStats"+str(episode_id)+".p", "rb" ))
        episode_ShortestPath = pickle.load(open( ShortestPath_dir +"episodeStats"+str(episode_id)+".p", "rb" ))

        success = episode_ORBSlam["success"]
        pose_env_ORBSlam = episode_ORBSlam["pose_env"]
        pose_env_ShortestPath = episode_ShortestPath["pose_env"] 


        li = len(pose_env_ORBSlam)
        pi = len(pose_env_ShortestPath)
        si = int(success == True)

        SPL += si*(li/max(pi,li))

        Success_rate += int(success == True)

        episode_id += 1

    #episode_id correspond to the number of episode too, so we don't need a value to store the number of episode that we pass during the loop
    SPL *= (1/episode_id)
    Success_rate /= episode_id
    dataPerScene[sceneKeyword[8]][0]['SPL'] = SPL
    dataPerScene[sceneKeyword[8]][0]['Success_rate'] = Success_rate  

    SPL, Success_rate = resetValue(SPL, Success_rate)

    while(sceneKeyword[9] in sceneDict[episode_id]):
        #Load Data from episodes
        episode_ORBSlam = pickle.load(open( ORBSlam_dir +"episodeStats"+str(episode_id)+".p", "rb" ))
        episode_ShortestPath = pickle.load(open( ShortestPath_dir +"episodeStats"+str(episode_id)+".p", "rb" ))

        success = episode_ORBSlam["success"]
        pose_env_ORBSlam = episode_ORBSlam["pose_env"]
        pose_env_ShortestPath = episode_ShortestPath["pose_env"] 


        li = len(pose_env_ORBSlam)
        pi = len(pose_env_ShortestPath)
        si = int(success == True)

        SPL += si*(li/max(pi,li))

        Success_rate += int(success == True)

        episode_id += 1

    #episode_id correspond to the number of episode too, so we don't need a value to store the number of episode that we pass during the loop
    SPL *= (1/episode_id)
    Success_rate /= episode_id
    dataPerScene[sceneKeyword[9]][0]['SPL'] = SPL
    dataPerScene[sceneKeyword[9]][0]['Success_rate'] = Success_rate  

    SPL, Success_rate = resetValue(SPL, Success_rate)

    while(sceneKeyword[10] in sceneDict[episode_id]):
        #Load Data from episodes
        episode_ORBSlam = pickle.load(open( ORBSlam_dir +"episodeStats"+str(episode_id)+".p", "rb" ))
        episode_ShortestPath = pickle.load(open( ShortestPath_dir +"episodeStats"+str(episode_id)+".p", "rb" ))

        success = episode_ORBSlam["success"]
        pose_env_ORBSlam = episode_ORBSlam["pose_env"]
        pose_env_ShortestPath = episode_ShortestPath["pose_env"] 


        li = len(pose_env_ORBSlam)
        pi = len(pose_env_ShortestPath)
        si = int(success == True)

        SPL += si*(li/max(pi,li))

        Success_rate += int(success == True)

        episode_id += 1

    #episode_id correspond to the number of episode too, so we don't need a value to store the number of episode that we pass during the loop
    SPL *= (1/episode_id)
    Success_rate /= episode_id
    dataPerScene[sceneKeyword[10]][0]['SPL'] = SPL
    dataPerScene[sceneKeyword[10]][0]['Success_rate'] = Success_rate  

    SPL, Success_rate = resetValue(SPL, Success_rate)

    while(sceneKeyword[11] in sceneDict[episode_id]):
        #Load Data from episodes
        episode_ORBSlam = pickle.load(open( ORBSlam_dir +"episodeStats"+str(episode_id)+".p", "rb" ))
        episode_ShortestPath = pickle.load(open( ShortestPath_dir +"episodeStats"+str(episode_id)+".p", "rb" ))

        success = episode_ORBSlam["success"]
        pose_env_ORBSlam = episode_ORBSlam["pose_env"]
        pose_env_ShortestPath = episode_ShortestPath["pose_env"] 


        li = len(pose_env_ORBSlam)
        pi = len(pose_env_ShortestPath)
        si = int(success == True)

        SPL += si*(li/max(pi,li))

        Success_rate += int(success == True)

        episode_id += 1

    #episode_id correspond to the number of episode too, so we don't need a value to store the number of episode that we pass during the loop
    SPL *= (1/episode_id)
    Success_rate /= episode_id
    dataPerScene[sceneKeyword[11]][0]['SPL'] = SPL
    dataPerScene[sceneKeyword[11]][0]['Success_rate'] = Success_rate  

    SPL, Success_rate = resetValue(SPL, Success_rate)

    while(sceneKeyword[12] in sceneDict[episode_id]):
        #Load Data from episodes
        episode_ORBSlam = pickle.load(open( ORBSlam_dir +"episodeStats"+str(episode_id)+".p", "rb" ))
        episode_ShortestPath = pickle.load(open( ShortestPath_dir +"episodeStats"+str(episode_id)+".p", "rb" ))

        success = episode_ORBSlam["success"]
        pose_env_ORBSlam = episode_ORBSlam["pose_env"]
        pose_env_ShortestPath = episode_ShortestPath["pose_env"] 


        li = len(pose_env_ORBSlam)
        pi = len(pose_env_ShortestPath)
        si = int(success == True)

        SPL += si*(li/max(pi,li))

        Success_rate += int(success == True)

        episode_id += 1

    #episode_id correspond to the number of episode too, so we don't need a value to store the number of episode that we pass during the loop
    SPL += (1/episode_id)
    Success_rate /= episode_id
    dataPerScene[sceneKeyword[12]][0]['SPL'] = SPL
    dataPerScene[sceneKeyword[12]][0]['Success_rate'] = Success_rate

    SPL, Success_rate = resetValue(SPL, Success_rate)

    while(sceneKeyword[13] in sceneDict[episode_id] and (episode_id < 993)):
        #Load Data from episodes
        episode_ORBSlam = pickle.load(open( ORBSlam_dir +"episodeStats"+str(episode_id)+".p", "rb" ))
        episode_ShortestPath = pickle.load(open( ShortestPath_dir +"episodeStats"+str(episode_id)+".p", "rb" ))

        success = episode_ORBSlam["success"]
        pose_env_ORBSlam = episode_ORBSlam["pose_env"]
        pose_env_ShortestPath = episode_ShortestPath["pose_env"] 


        li = len(pose_env_ORBSlam)
        pi = len(pose_env_ShortestPath)
        si = int(success == True)

        SPL += si*(li/max(pi,li))

        Success_rate += int(success == True)

        episode_id += 1

    #episode_id correspond to the number of episode too, so we don't need a value to store the number of episode that we pass during the loop
    SPL *= (1/episode_id)
    Success_rate /= episode_id
    dataPerScene[sceneKeyword[13]][0]['SPL'] = SPL
    dataPerScene[sceneKeyword[13]][0]['Success_rate'] = Success_rate  

    SPL, Success_rate = resetValue(SPL, Success_rate) 

def resetValue(SPL, Success_rate):
    SPL = 0
    Success_rate = 0
    return SPL, Success_rate

def storeInJson():
    dumped = {
        #Define the links between nodes with value, Links is a list of dictionnary
        "Links" : [
            {"source" : "0", "target" : "2","value" : len(dataPerScene[sceneKeyword[0]][0]['True']), "SPL" : dataPerScene[sceneKeyword[0]][0]['SPL'], "Success_Rate" : dataPerScene[sceneKeyword[0]][0]['Success_rate']},
            {"source" : "1", "target" : "2","value" : len(dataPerScene[sceneKeyword[0]][0]['False'])},
            {"source" : "0", "target" : "3","value" : len(dataPerScene[sceneKeyword[1]][0]['True']), "SPL" : dataPerScene[sceneKeyword[1]][0]['SPL'], "Success_Rate" : dataPerScene[sceneKeyword[1]][0]['Success_rate']},
            {"source" : "1", "target" : "3","value" : len(dataPerScene[sceneKeyword[1]][0]['False'])},
            {"source" : "0", "target" : "4","value" : len(dataPerScene[sceneKeyword[2]][0]['True']), "SPL" : dataPerScene[sceneKeyword[2]][0]['SPL'], "Success_Rate" : dataPerScene[sceneKeyword[2]][0]['Success_rate']},
            {"source" : "1", "target" : "4","value" : len(dataPerScene[sceneKeyword[2]][0]['False'])},
            {"source" : "0", "target" : "5","value" : len(dataPerScene[sceneKeyword[3]][0]['True']), "SPL" : dataPerScene[sceneKeyword[3]][0]['SPL'], "Success_Rate" : dataPerScene[sceneKeyword[3]][0]['Success_rate']},
            {"source" : "1", "target" : "5","value" : len(dataPerScene[sceneKeyword[3]][0]['False'])},
            {"source" : "0", "target" : "6","value" : len(dataPerScene[sceneKeyword[4]][0]['True']), "SPL" : dataPerScene[sceneKeyword[4]][0]['SPL'], "Success_Rate" : dataPerScene[sceneKeyword[4]][0]['Success_rate']},
            {"source" : "1", "target" : "6","value" : len(dataPerScene[sceneKeyword[4]][0]['False'])},
            {"source" : "0", "target" : "7","value" : len(dataPerScene[sceneKeyword[5]][0]['True']), "SPL" : dataPerScene[sceneKeyword[5]][0]['SPL'], "Success_Rate" : dataPerScene[sceneKeyword[5]][0]['Success_rate']},
            {"source" : "1", "target" : "7","value" : len(dataPerScene[sceneKeyword[5]][0]['False'])},
            {"source" : "0", "target" : "8","value" : len(dataPerScene[sceneKeyword[6]][0]['True']), "SPL" : dataPerScene[sceneKeyword[6]][0]['SPL'], "Success_Rate" : dataPerScene[sceneKeyword[6]][0]['Success_rate']},
            {"source" : "1", "target" : "8","value" : len(dataPerScene[sceneKeyword[6]][0]['False'])},
            {"source" : "0", "target" : "9","value" : len(dataPerScene[sceneKeyword[7]][0]['True']), "SPL" : dataPerScene[sceneKeyword[7]][0]['SPL'], "Success_Rate" : dataPerScene[sceneKeyword[7]][0]['Success_rate']},
            {"source" : "1", "target" : "9","value" : len(dataPerScene[sceneKeyword[7]][0]['False'])},
            {"source" : "0", "target" : "10","value" : len(dataPerScene[sceneKeyword[8]][0]['True']), "SPL" : dataPerScene[sceneKeyword[8]][0]['SPL'], "Success_Rate" : dataPerScene[sceneKeyword[8]][0]['Success_rate']},
            {"source" : "1", "target" : "10","value" : len(dataPerScene[sceneKeyword[8]][0]['False'])},
            {"source" : "0", "target" : "11","value" : len(dataPerScene[sceneKeyword[9]][0]['True']), "SPL" : dataPerScene[sceneKeyword[9]][0]['SPL'], "Success_Rate" : dataPerScene[sceneKeyword[9]][0]['Success_rate']},
            {"source" : "1", "target" : "11","value" : len(dataPerScene[sceneKeyword[9]][0]['False'])},
            {"source" : "0", "target" : "12","value" : len(dataPerScene[sceneKeyword[10]][0]['True']), "SPL" : dataPerScene[sceneKeyword[10]][0]['SPL'], "Success_Rate" : dataPerScene[sceneKeyword[10]][0]['Success_rate']},
            {"source" : "1", "target" : "12","value" : len(dataPerScene[sceneKeyword[10]][0]['False'])},
            {"source" : "0", "target" : "13","value" : len(dataPerScene[sceneKeyword[11]][0]['True']), "SPL" : dataPerScene[sceneKeyword[11]][0]['SPL'], "Success_Rate" : dataPerScene[sceneKeyword[11]][0]['Success_rate']},
            {"source" : "1", "target" : "13","value" : len(dataPerScene[sceneKeyword[11]][0]['False'])},
            {"source" : "0", "target" : "14","value" : len(dataPerScene[sceneKeyword[12]][0]['True']), "SPL" : dataPerScene[sceneKeyword[12]][0]['SPL'], "Success_Rate" : dataPerScene[sceneKeyword[12]][0]['Success_rate']},
            {"source" : "1", "target" : "14","value" : len(dataPerScene[sceneKeyword[12]][0]['False'])},
            {"source" : "0", "target" : "15","value" : len(dataPerScene[sceneKeyword[13]][0]['True']), "SPL" : dataPerScene[sceneKeyword[13]][0]['SPL'], "Success_Rate" : dataPerScene[sceneKeyword[13]][0]['Success_rate']},
            {"source" : "1", "target" : "15","value" : len(dataPerScene[sceneKeyword[13]][0]['False'])}        
        ],
        "Nodes" : [
            {   "node" : 0,
                "name" : "Success"},
            {   "node" : 1,
                "name" : "Failed"},
            {   "node" : 2,
                "name" : sceneKeyword[0]},
            {   "node" : 3,
                "name" : sceneKeyword[1]},
            {   "node" : 4,
                "name" : sceneKeyword[2]},
            {   "node" : 5,
                "name" : sceneKeyword[3]},
            {   "node" : 6,
                "name" : sceneKeyword[4]},
            {   "node" : 7,
                "name" : sceneKeyword[5]},
            {   "node" : 8,
                "name" : sceneKeyword[6]},
            {   "node" : 9,
                "name" : sceneKeyword[7]},
            {   "node" : 10,
                "name" : sceneKeyword[8]},
            {   "node" : 11,
                "name" : sceneKeyword[9]},
            {   "node" : 12,
                "name" : sceneKeyword[10]},
            {   "node" : 13,
                "name" : sceneKeyword[11]},
            {   "node" : 14,
                "name" : sceneKeyword[12]},
            {   "node" : 15,
                "name" : sceneKeyword[13]}
        ]
    }
    dumped = str(dumped)
    dumped = dumped.replace("'",'"')
    with open("sankeyData.json", "w") as outfile:
        outfile.write(dumped)

#Calling the function to process the date and store them in dataPerScene

# print("Start Parsing")
# taskSceneLevel = threading.Thread(target = sceneLevel())
# taskSPL_SuccessRate = threading.Thread(target =calculateSPL_SuccessRate())
# taskSceneLevel.start()
# taskSPL_SuccessRate.start()
# print("End Parsing and Start Writing")

# storeInJson()
# print("End Writing")

episodeLevel('Swormville')