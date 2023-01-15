from Prediction_validation_insertion import prediction_validation
from predictionModel import predictModel
import os
import shutil
from DataTypeValidation_insertion_Prediction.DataTypeValidation import DbOperations
from datetime import datetime
from flask import send_file


class Download:
    def __init__(self):
        self.predictdb = prediction_validation()
        self.predict = predictModel()
        self.dboperation = DbOperations()
        self.path = "SaveDownloadedFile/"

    def save_file(self):
        date_time = datetime.now()
        date = date_time.date()
        time = date_time.strftime("%H%M%S")
        try:
            data = self.dboperation.selectingDatafromtableintocsv("Prediction")
            prediction = self.predict.predictionModel()
            data["prediction"] = prediction
            data.to_csv("SaveDownloadedFile/DownloadFile"+str(date)+str(time)+".csv",index=False)
            self.dboperation.deleteExistingtable("Prediction")

        except Exception as e:
            raise e

    def MoveSaveDownloadFileToSaveFiles(self):
        movefiledest = "SaveFile/"
        try:
            for file in os.listdir(self.path):
                if file in os.listdir(self.path):
                    return shutil.move(self.path+ file,movefiledest)
                else:
                    pass
        except Exception as e:
            raise e

    def downloadfile(self):
        # destinationfilepath = "SaveFile/"
        try:
            for files in os.listdir(self.path):
                return send_file(self.path+files,as_attachment=True)
        except Exception as e:
            raise e




