#DATABASE testdb")
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

# mycursor.execute("SHOW DATABASES")
#
# for db in mycursor:
#     print(db)

#mycursor.execute("DROP TABLE Animals")
#mycursor.execute("CREATE TABLE Animals (ID VARCHAR(100), Experimentator VARCHAR(100) , Sex VARCHAR(10), Age   INTEGER(10), Species  VARCHAR(100),Histology_images_path VARCHAR(100), Description_text VARCHAR(100))")

#mycursor.execute("DROP TABLE Sessions")
#mycursor.execute("CREATE TABLE Sessions (ID VARCHAR(100), AnimalID INTEGER(100) , Behavioral_test VARCHAR(100), Video_file_path   VARCHAR(100), Electrophysiology_data_file_path  VARCHAR(100), Description_text VARCHAR(100))") #FOREIGN KEY (AnimalID) REFERENCES animals(ID))


mycursor.execute("CREATE TABLE Cells (ID VARCHAR(100), Session_ID VARCHAR(100) , Electrode_ID VARCHAR(10), Type   VARCHAR(4), Quality  VARCHAR(10), Nspikes INT(100))")
#

sqlFormula1 = "INSERT INTO animals (ID, Experimentator, Sex, Age, Species, Histology_images_path, Description_text) VALUES (%s, %s, %s, %s, %s, %s, %s)"
sqlFormula2 = "INSERT INTO sessions (ID, AnimalID, Behavioral_test, Video_file_path, Electrophysiology_data_file_path, Description_text) VALUES (%s, %s, %s, %s, %s, %s)"
animal_1 = (1, "Georgiy", "male", 1, "rat", "C:\Histology_images_path1", "It's a record of some neurons activity" )
animal_2 = (2, "Ivan   ", "male", 2, "rat", "C:\Histology_images_path2", "It's a record of some neurons activity" )
animal_3 = (3, "Artem  ", "male", 2, "rat", "C:\Histology_images_path3", "It's a record of some neurons activity" )
animal_4 = (4, "Sergey ", "male", 4, "rat", "C:\Histology_images_path4", "It's a record of some neurons activity" )


session_1 = ('ec01', 1, "mWheel", "C:\Video_path1", "C:\El_Phys_data_path1", "It's a data on some experiment" )
session_2 = ('ec02', 1, "Square", "C:\Video_path2", "C:\El_Phys_data_path2", "It's a data on some experiment" )
session_3 = ('ec03', 1, "Labirint", "C:\Video_path3", "C:\El_Phys_data_path3", "It's a data on some experiment" )
session_4 = ('ec04', 1, "mWheel", "C:\Video_path4", "C:\El_Phys_data_path4", "It's a data on some experiment" )



mycursor.execute(sqlFormula1, animal_1)
mycursor.execute(sqlFormula1, animal_2)
mycursor.execute(sqlFormula1, animal_3)
mycursor.execute(sqlFormula1, animal_4)


mycursor.execute(sqlFormula2, session_1)
mycursor.execute(sqlFormula2, session_2)
mycursor.execute(sqlFormula2, session_3)
mycursor.execute(sqlFormula2, session_4)


mycursor.execute("SELECT * FROM animals")

result = mycursor.fetchall()

print("ID   Experimentator   Sex    Age   Species   Histology_images_path       Description_text")
#print(result)
for row in result:
    print(row[0],'  ', row[1],'        ', row[2],' ', row[3],'   ', row[4],'     ', row[5],' ', row[6])


print('\n\n')
#mycursor.execute("SELECT * FROM sessions")
#mycursor.execute("SELECT ID FROM animals WHERE Experimentator == 'Sergey' ")

result = mycursor.fetchall()

#print("ID AnimalID  Behavioral_test   Video_file_path   Electrophysiology_data_file_path   Description_text")
print(result)
#for row in result:
#    print(row[0],'  ', row[1],'           ', row[2],' ', row[3],'   ', row[4],'     ', row[5])
