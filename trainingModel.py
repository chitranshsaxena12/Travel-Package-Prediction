from data_preprocessing.preprocessing import Preprocessor
from application_logging.logger import App_Logger
from best_model_finder.tuner import Model_Finder
from file_operations.file_methods import File_Operation
from DataTypeValidation_Insertion_Training.DataTypeValidation import DbOperations
from sklearn.model_selection import train_test_split


class trainModel:

    def __init__(self):
        self.log = App_Logger()
        self.file = open("Training_logs/ModelTraininglog.txt","a+")
        self.data = DbOperations()
        self.preprocess = Preprocessor()
        self.model_train = Model_Finder()
        self.file_operation = File_Operation()


    def trainingModel(self):
        self.log.log(self.file, 'Start of Training')
        try:
            data = self.data.selectingDatafromtableintocsv("training")
            self.preprocess.encodeCategoricalValues(data)
            new_data = self.preprocess.dropUnnecessaryColumns(data,"CustomerID")
            X , Y = self.preprocess.separate_label_feature(new_data,"ProdTaken")
            X_resampled, y_resampled = self.preprocess.OverSampling(X,Y)
            feature_data = self.preprocess.FeatureSelection()
            selected_data = X_resampled[feature_data]
            x_train, x_test, y_train, y_test = train_test_split(selected_data , y_resampled, test_size=0.20, random_state=0)
            best_model_name,best_model = self.model_train.get_best_model(x_train , y_train, x_test, y_test)
            self.file_operation.save_model(best_model,best_model_name)
            self.data.deleteExistingtable("training")
            self.log.log(self.file, 'Successful End of Training')
            self.file.close()
        except Exception as e:
            self.log.log(self.file, 'Unsuccessful End of Training')
            self.file.close()
            raise e






