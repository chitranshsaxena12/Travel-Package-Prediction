import json
from datetime import datetime
import pandas as pd
import shutil
from application_logging.logger import App_Logger
import os

class raw_data_validation:

    def __init__(self):
        # self.file_path = path
        self.schema_path = "schema_prediction.json"
        self.log = App_Logger()

    def valuefromschema(self):
        try:
            with open(self.schema_path,"r") as f:
                data = json.load(f)
                f.close()
            column_number = data["NumberofColumns"]
            column_name = data["ColName"]

            file = open("Prediction_Logs/valuesfromSchemaValidationLog.txt","a+")
            message = "Column_number :: %s" %column_number + "\t" + "Column_names :: %s" % column_name
            self.log.log(file,message)

            file.close()

        except Exception as e:
            file = open("Prediction_Logs/valuesfromSchemaValidationLog.txt", "a+")
            self.log.log(file, str(e))

            file.close()
            raise e

        return column_number , column_name

    def createDirectoryForGoodBadRawData(self):

        try:
            path = os.path.join("Prediction_Raw_files_validation/", "Good_Raw/")
            if not os.path.isdir(path):
                os.makedirs(path)

            path  = os.path.join("Prediction_Raw_files_validation/", "Bad_Raw/")
            if not os.path.isdir(path):
                os.makedirs(path)
            file = open("Prediction_Logs/GeneralLog.txt", 'a+')
            self.log.log(file, "Good and Bad directory has been successfully created" )
            file.close()

        except OSError as ex:
            file = open("Prediction_Logs/GeneralLog.txt", 'a+')
            self.log.log(file, "Error while creating Directory %s:" % ex)
            file.close()
            raise ex

    def validateMissingValuesInWholeColumn(self):

        try:
            f = open("Prediction_Logs/missingValuesInColumn.txt", 'a+')
            self.log.log(f, "Missing Values Validation Started!!")

            for file in os.listdir("Prediction_Raw_files_validation/Good_Raw/"):
                data = pd.read_csv("Prediction_Raw_files_validation/Good_Raw/"+file)
                count = 0
                for column in data:
                    if len(data[column]) - data[column].count() > 0 :
                        count += 1
                if count!=0:
                    shutil.move("Prediction_Raw_files_validation/Good_Raw/"+file,"Prediction_Raw_files_validation/Bad_Raw/")
                else:
                    pass
        except OSError as s:
            f = open("Prediction_Logs/missingValuesInColumn.txt", 'a+')
            self.log.log(f, "Error Occured while moving the file :: %s" % s)
            f.close()
            raise s
        except Exception as e:
            f = open("Prediction_Logs/missingValuesInColumn.txt", 'a+')
            self.log.log(f, "Error Occured:: %s" % e)
            f.close()
            raise e
        f.close()

    def deleteExistingGoodDataTrainingFolder(self):

        try:
            path = "Prediction_Raw_files_validation/"
            if os.path.isdir(path+"Good_Raw/"):
                shutil.rmtree(path + "Good_Raw/")
                file = open("Prediction_Logs/GeneralLog.txt", 'a+')
                self.log.log(file,"Good Raw directory deleted successfully!!!")
                file.close()

        except OSError as s:
            file = open("Prediction_Logs/GeneralLog.txt", 'a+')
            self.log.log(file,"Error While Deleting Directory : %s " %s)
            file.close()
            raise s

    def deleteExistingBadDataTrainingFolder(self):

        try:
            path= "Prediction_Raw_files_validation/"
            if os.path.isdir(path + "Bad_Raw/"):
                shutil.rmtree(path + "Bad_Raw/")
                file = open("Prediction_Logs/GeneralLog.txt", 'a+')
                self.log.log(file,"Bad Raw Directory deleted successfully!!!")
                file.close()

        except OSError as s:
            file = open("Prediction_Logs/GeneralLog.txt", 'a+')
            self.log.log(file,"Error While Deleting Directory : %s" %s)
            file.close()
            raise s

    def moveBadFilesToArchiveBad(self):

        date_time = datetime.now()
        date = date_time.date()
        time = date_time.strftime("%H%M%S")

        try:
            valid_path = "Prediction_Raw_files_validation/Bad_Raw/"
            if os.path.isdir(valid_path):
                archive_path = "Bad_archived_data_prediction/Bad_Raw_"+ str(date)+ "_" + str(time)
                if not os.path.isdir(archive_path):
                    os.makedirs(archive_path)
                for file in os.listdir(valid_path):
                    shutil.move(valid_path + file, archive_path)


                file = open("Prediction_Logs/GeneralLog.txt", 'a+')
                self.log.log(file,"Bad Raw data successfully transfer to bad archive folder")
                file.close()

        except OSError as oe:
            file = open("Prediction_Logs/GeneralLog.txt", 'a+')
            self.log.log(file,"Error while creating directory %s" %oe)
            file.close()
            raise oe

        except Exception as e:
            file = open("Prediction_Logs/GeneralLog.txt", 'a+')
            self.log.log(file,"Error while transfering file bad raw to bad archive folder %s" %e)
            file.close()
            raise e