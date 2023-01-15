from data_preprocessing.preprocessing import Preprocessor
from application_logging.logger import App_Logger
# from best_model_finder.tuner import Model_Finder
import os
from file_operations.file_methods import File_Operation
from DataTypeValidation_insertion_Prediction.DataTypeValidation import DbOperations
# from sklearn.model_selection import train_test_split


class predictModel:

    def __init__(self):
        self.log = App_Logger()
        self.file = open("Prediction_logs/ModelPredictionlog.txt","a+")
        self.data = DbOperations()
        self.preprocess = Preprocessor()
        # self.model_train = Model_Finder()
        self.file_operation = File_Operation()
        self.model_directory = 'models/'


    def predictionModel(self):
        self.log.log(self.file, 'Start of Prediction')
        try:
            data = self.data.selectingDatafromtableintocsv("Prediction")
            self.preprocess.encodeCategoricalValues(data)
            new_data = self.preprocess.dropUnnecessaryColumns(data,"CustomerID")
            feature_data = self.preprocess.FeatureSelection()
            selected_data = new_data[feature_data]
            for i in os.listdir(self.model_directory):
                predict_ = self.file_operation.load_model(i)
                return predict_.predict(selected_data)
                # prediction = predict_.predict(selected_data)
                # return prediction


        except Exception as e:
            self.log.log(self.file, 'Unsuccessful End of Prediction')
            self.file.close()
            raise e






