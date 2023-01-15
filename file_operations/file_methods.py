import pickle
import os
import shutil
from application_logging.logger import App_Logger




class File_Operation:
    """
                This class shall be used to save the model after training
                and load the saved model for prediction.

                Written By:
                Version: 1.0
                Revisions: None

                """
    def __init__(self):
        self.file = open("Training_logs/file_operation.txt","a+")
        self.log = App_Logger()
        self.model_directory = 'models/'


    def save_model(self,model,filename):

        self.log.log(self.file,"Save_model is started")
        self.file.close()
        try:
            path = os.path.join(self.model_directory,filename)
            if os.path.isdir(path):
                shutil.rmtree(self.model_directory)
                os.makedirs(path)
            else:
                os.makedirs(path)

            with open(path + "/" + filename + ".pickle","wb") as f:
                pickle.dump(model, f)
                # self.log.log(self.file , 'Model File ' + filename + ' saved. Exited the save_model method of the Model_Finder class')
                # self.file.close()

                return 'success'

        except Exception as e:
            # self.log.log(self.file,'Exception occured in save_model method of the Model_Finder class. Exception message:  %s' %e)
            # self.file.close()
            raise e

    def load_model(self, filename):

        self.log.log(self.file, "load_model is started...")
        self.file.close()
        try:
            path = os.path.join(self.model_directory,filename)
            with open(path + "/" + filename + ".pickle", "rb") as f:
                # self.log.log(self.file,'Model File ' + filename + ' loaded. Exited the load_model method of the Model_Finder class')
                return pickle.load(f)

        except Exception as e:
            # self.log.log(self.file, 'Exception occured in load_model method of the Model_Finder class. Exception message: %s' %e)
            # self.file.close()
            raise e



