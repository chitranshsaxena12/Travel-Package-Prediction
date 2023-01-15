from Prediction_Raw_Data_Validation.predictionDataValidation import raw_data_validation
from application_logging.logger import App_Logger
from DataTypeValidation_insertion_Prediction.DataTypeValidation import DbOperations
import pandas as pd



class prediction_validation:

    def __init__(self):
        self.log = App_Logger()
        self.valid = raw_data_validation()
        self.data_ingestion = DbOperations()
        self.file_object = open("Prediction_Logs/Prediction_Main_Log.txt", 'a+')


    def prediction_validation(self,data):
        try:
            self.log.log(self.file_object,"Data Validation started")
            if self.valid.valuefromschema()[0] == len(data[0]):
                new_data = pd.DataFrame(data[1:], columns=data[0])
                self.log.log(self.file_object," Directory creation is started!!!")
                self.valid.createDirectoryForGoodBadRawData()
                self.log.log(self.file_object," Directory Successfully Created!!!")
                new_data.to_csv("Prediction_Raw_files_validation/Good_Raw/mydata.csv", index=False)
                self.valid.validateMissingValuesInWholeColumn()
                self.data_ingestion.createTableDb("Prediction")
                self.log.log(self.file_object,"Table is Created Successfully")
                self.data_ingestion.insertIntoTableGoodData("Prediction")
                self.log.log(self.file_object,"Data Successfully Inserted!!!")
                self.valid.deleteExistingGoodDataTrainingFolder()
                self.log.log(self.file_object,"Good Data Folder is successfully Deleted....")
                self.valid.moveBadFilesToArchiveBad()
                self.log.log(self.file_object,"Bad Data Successfully Transfer to Bad Archive data folder!!!!")
                self.valid.deleteExistingBadDataTrainingFolder()
                self.log.log(self.file_object,"Bad Data Folder is Successfully Deleted...")
                # self.log.log(self.file_object,"Data is Started to convert into Data Frame...")
                # data = self.data_ingestion.selectingDatafromtableintocsv("training")
                # self.log.log(self.file_object,"Data Successfully converted into Data Frame !!!!")
                self.file_object.close()

            else:
                return "please enter valid data!!"

        except Exception as e:
            raise e