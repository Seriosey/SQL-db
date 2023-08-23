import pandas as pd
import h5py
import os
from os import walk
import numpy as np

# print(os.listdir(path = '/media/usb/Data/Data_from_CRCNS/hc-3/'))
# f = []
# for (dirpath, dirnames, filenames) in walk('/media/usb/Data/Data_from_CRCNS/hc-3/docs/hc3-metadata-tables/'):
#     f.extend(filenames)
    
# print(f)


def get_all(name):
    
    print(name)
    for key_ in name.keys():
        print(name.key_)

sourses_path = '/media/usb/Data/Transformed_CRCNC/hc-3/'
i=0
n=0

Animals = pd.DataFrame({
 'ID': [],
 'Experimentator': [],
 'Sex': [],
 'Age': [],
 'Species': [],
 'Histology Images Path': [],
 'Description Text': []})


Sessions = pd.DataFrame({
 'SID': [],
 'SAnimal_ID': [],
 'Behavioral test': [],
 'Video_file_path': [],
 'Electrophysiology_data_file_path': [],
 'Description Text': []})


Electrodes = pd.DataFrame({
 'EID': [],
 'EAnimal_ID': [],
 'Brain_zone': [],
 'Stereotaxic_coordinates': [],
 'Type': []})


Cells = pd.DataFrame({
 'ID': [],
 'Session_ID': [],
 'Electrode_ID': [],
 'Type': [],
 'Quality': [],
 'NSpikes': []})

EID = 0
CID = 0
c=0

for path, _, files in os.walk(sourses_path):
    
    c+=1
    print(c)
    if c == 5: 
        break
    
    for file in files:
        
        
        if file.find(".hdf5"): 
            try:
                SID = SAnimalID = BTest = Video = EPData = DTExt = None
                SID = file[:-5]
                #AnimalID = sourse_hdf5.attrs.items()['animal']
                
                print(file)
                sourse_hdf5 = h5py.File(path + '/' + file, "r")
                #attrs = np.array([])
                #print(attrs)
                #AnimalID = attrs[0]
                for data in sourse_hdf5.attrs.items():
                                                                             #attrs = np.append(attrs, data)
                        print(data)
                        if data[0] == 'animal': SAnimalID = data[1]
                        if data[0] == 'session': SID = data[1]
                        if data[0] == 'behavior_test': BTest = data[1]
                        #if data[0] == 'animal': AnimalID = data[1]
                        #if data[0] == 'animal': AnimalID = data[1]
                        #if data[0] == 'animal': AnimalID = data[1]
                                                                                #if print(data[1])
                                                                             #print(attrs)
#                                                                           sourse_hdf5.visit(get_all)
                
                for key in sourse_hdf5.keys():
#                                                                               data = sourse_hdf5['default'][:]
#                                                                                 print(data)
                    print('   ', key)
                    
                        
                    for item in sourse_hdf5[key].attrs.items():
                        BZone = EAID = Scoordinates = etype = None
                        
                        if item[0] == 'brainZone': BZone = item[1]
                        #if item[0] == 'type': etype = item[1]
                        print('   ', item)
                        EID += 1
                        Electrodes.loc[ len(Electrodes.index )] = [EID, SAnimalID ,BZone, Scoordinates, etype]
    
                    for dset in sourse_hdf5[key].keys():
                        
#                        pass
                        print ('   ',dset)
                        if dset == 'spikes':
                            for group in sourse_hdf5[key][dset].keys():
                                    print('      ',group)
                                    for cluster in sourse_hdf5[key][dset][group].attrs.items():
                                        CQuality = CType = NSpikes = None
                                        CID += 1
                                        print('      ',cluster)
                                        if cluster[0] == 'quality': CQuality = cluster[1]
                                        if cluster[0] == 'Type': CType = cluster[1]
                                        Cells.loc[ len(Cells.index )] = [CID, SID ,EID, CType, CQuality, NSpikes]
                        

                        #ds_data = sourse_hdf5[key][dset] # returns HDF5 dataset object
                    
                        for group in sourse_hdf5[key][dset].attrs.items():
#                            pass
                            print('   ', group)
#                             print (ds_data)
                Sessions.loc[ len(Sessions.index )] = [SID, SAnimalID, BTest, Video, EPData, DTExt]

            except OSError:
                continue
        
            
print('\n Sessions: \n', Sessions)

print('\n Electrodes: \n', Electrodes)

print('\n Cells: \n', Cells)

import sys
!{sys.executable} -m pip install mysql
!{sys.executable} -m pip install mysql-connector-python



import mysql
import mysql.connector

#print(dir(mysql))

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    passwd = "Msql_2023",
    database = "testdb"
    )


mycursor = mydb.cursor()
#mycursor.execute("CREATE
# mycursor.execute("SHOW DATABASES")
#
# for db in mycursor:
#     print(db)

mycursor.execute("CREATE TABLE Sessions (ID INTEGER(100), AnimalID INTEGER(100), Bevavioral_test VARCHAR(100), Video_file_path VARCHAR(100), Electrophysiology_data_file_path VARCHAR(100), Description_text VARCHAR(255))")

#

sqlFormula = "INSERT INTO animals (ID, Experimentator, Sex, Age, Species, Histology_images_path, Description_text) VALUES (%s, %s, %s, %s, %s, %s, %s)"
animal_i = (1, "Georgiy", "male", 1, "rat", "C:\Histology_images_path", "It's a record of some neurons activity" )
mycursor.execute(sqlFormula, animal_i)


sqlFormula = "INSERT INTO sessions (ID, AnimalID, Bevavioral_test, Video_file_path, Electrophysiology_data_file_path, Description_text) VALUES (%s, %s, %s, %s, %s, %s, %s)"
#animal_i = (1, "Georgiy", "male", 1, "rat", "C:\Histology_images_path", "It's a record of some neurons activity" )
for i, row in Sessions.iterrows():
    mycursor.execute(sqlFormula, row)