import sqlite3
import os
import csv
from application_logging.logger import App_Logger
import pandas as pd


class DbOperations:

    def __init__(self):
        self.log = App_Logger()
        self.path = "Prediction_Database/"
        self.badFilePath = "Prediction_Raw_files_validation/Bad_Raw/"
        self.goodFilePath = "Prediction_Raw_files_validation/Good_Raw/"

    def DataBaseConnection(self,databasename):
        try:
            conn = sqlite3.connect(self.path + databasename + ".db")
            file = open("Prediction_Logs/DataBaseConnectionLog.txt", "a+")
            self.log.log(file, "Opened %s database successfully" % databasename)
            file.close()


        except ConnectionError as c:
            file = open("Prediction_Logs/DataBaseConnectionLog.txt", "a+")
            self.log.log(file, "Error While Connecting to database %s" % c)
            file.close()
            raise c
        return conn


    def createTableDb(self, DatabaseName):



        try:
            conn = self.DataBaseConnection(DatabaseName)
            cur = conn.cursor()
            cur.execute("create table Good_data('CustomerID' int, 'Age' float, 'TypeofContact' varchar(50), 'CityTier' int,'DurationOfPitch' float, 'Occupation' varchar(50), 'Gender' varchar(10), 'NumberOfPersonVisiting' int,'NumberOfFollowups' float, 'ProductPitched' varchra(50), 'PreferredPropertyStar' float,'MaritalStatus' varchar(50), 'NumberOfTrips' float, 'Passport' int, 'PitchSatisfactionScore' int,'OwnCar' int, 'NumberOfChildrenVisiting' float, 'Designation' varchar(50), 'MonthlyIncome' float)")
            if cur.rowcount == -1:
                conn.close()
                file = open("Prediction_Logs/DataBaseConnectionLog.txt", "a+")
                self.log.log(file,"Tables created successfully!!")
                file.close()

                file = open("Prediction_Logs/DataBaseConnectionLog.txt", "a+")
                self.log.log(file, "%s database closed successfully!!!" %DatabaseName)
                file.close()


        except Exception as e:
            file = open("Prediction_Logs/DataBaseConnectionLog.txt", "a+")
            self.log.log(file,"Error while creating table %s" %e)
            file.close()
            raise e


    def deleteExistingtable(self,DatabaseName):

        try:
            conn = self.DataBaseConnection(DatabaseName)
            cur = conn.cursor()
            cur.execute("drop table Good_data")
            conn.close()
            file = open("Prediction_Logs/DataBaseConnectionLog.txt", "a+")
            self.log.log(file, "Good_data Table droped successfully!!!")
            file.close()

        except Exception as e:
            file = open("Prediction_Logs/DataBaseConnectionLog.txt", "a+")
            self.log.log(file, "Error While droping the table %s" %e)
            file.close()
            raise e

    def insertIntoTableGoodData(self, Database):

        conn = self.DataBaseConnection(Database)
        cur = conn.cursor()
        Good_path = self.goodFilePath

        try:
            data_list = []
            if os.path.isdir(Good_path):
                for file in os.listdir(Good_path):
                    with open(Good_path + file) as f:
                        data = csv.reader(f)
                        for file_data in data:
                            data_list.append(tuple(file_data))
            for insert_data in data_list[1:]:
                # print(insert_data)
                cur.execute('insert into Good_data values {values}'.format(values= insert_data))
                conn.commit()
            if cur.rowcount > 0:
                file = open("Prediction_Logs/DataBaseConnectionLog.txt", "a+")
                self.log.log(file,"Data successfully inserted into Good_data table")
                file.close()


        except Exception as e:
            file = open("Prediction_Logs/DataBaseConnectionLog.txt", "a+")
            self.log.log(file, "Error while inserting data in Good_data table %s" %e)
            file.close()
            raise e
        conn.close()



    def selectingDatafromtableintocsv(self, Database):

        try:
            conn = self.DataBaseConnection(Database)
            data = pd.read_sql_query("select * from Good_data", conn)
            file = open("Prediction_Logs/DataBaseConnectionLog.txt", "a+")
            self.log.log(file, "Data successfully loaded from Good_data table")
            file.close()
            return data


        except Exception as e:
            file = open("Prediction_Logs/DataBaseConnectionLog.txt", "a+")
            self.log.log(file, "Error while loding data from Good_data table %s" % e)
            file.close()
            raise e




