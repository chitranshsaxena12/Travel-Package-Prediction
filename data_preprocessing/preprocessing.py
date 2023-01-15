from application_logging.logger import App_Logger
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectFromModel
from imblearn.over_sampling import RandomOverSampler
from sklearn.ensemble import ExtraTreesClassifier



class  Preprocessor:

    def __init__(self):
        self.log = App_Logger()
        self.file = open("Training_Logs/preprocessinglog.txt", 'a+')


    def encodeCategoricalValues(self,data):
        """
                                                Method Name: encodeCategoricalValues
                                                Description: This method encodes all the categorical values into the numerical values.
                                                Output: return the new data with numerical values.
                                                On Failure: Raise Exception

                                                Written By: Chitransh Saxena
                                                Version: 1.0
                                                Revisions: None
                             """
        try:
            self.log.log(self.file,"Encoding has been started.... ")
            data["TypeofContact"] = data["TypeofContact"].map({"Self Enquiry": 1, "Company Invited": 0})
            data["Occupation"] = data["Occupation"].map({'Salaried': 3, 'Free Lancer': 2, 'Small Business': 1, 'Large Business': 0})
            if "Fe Male" in data["Gender"].unique():
                data["Gender"] = data["Gender"].replace("Fe Male", "Female")
            else:
                pass
            data["Gender"] = data["Gender"].map({"Male": 1, "Female": 0})
            data["ProductPitched"] = data["ProductPitched"].map({'Deluxe': 2, 'Basic': 4, 'Standard': 3, 'Super Deluxe': 1, 'King': 0})
            data["MaritalStatus"] = data["MaritalStatus"].map({'Single': 0, 'Divorced': 3, 'Married': 2, 'Unmarried': 1})
            data["Designation"] = data["Designation"].map({'Manager': 3, 'Executive': 4, 'Senior Manager': 2, 'AVP': 1, 'VP': 0})
            self.log.log(self.file,"Encoding succesfully finished !!!!")
            self.file.close()

        except Exception as e:
            self.log.log(self.file,"Exception while encoding the values %s" %e)
            self.file.close()
            raise e

    def separate_label_feature(self, data, label_column_name):
        """
                        Method Name: separate_label_feature
                        Description: This method separates the features and a Label Coulmns.
                        Output: Returns two separate Dataframes, one containing features and the other containing Labels .
                        On Failure: Raise Exception

                        Written By: Chitransh Saxena
                        Version: 1.0
                        Revisions: None

                """

        try:
            # self.log.log(self.file, 'Entered the separate_label_feature method of the Preprocessor class')
            self.X = data.drop(labels=label_column_name,axis=1) # drop the columns specified and separate the feature columns
            self.Y = data[label_column_name] # Filter the Label columns
            # self.log.log(self.file,'Label Separation Successful. Exited the separate_label_feature method of the Preprocessor class')
            # self.file.close()
            return self.X,self.Y
        except Exception as e:
            self.log.log(self.file,'Exception occured in separate_label_feature method of the Preprocessor class. Exception message:  ' + str(e))
            self.log.log(self.file, 'Label Separation Unsuccessful. Exited the separate_label_feature method of the Preprocessor class')
            self.file.close()
            raise e


    def standardScalingData(self,X):
        """
                                Method Name: standardScalingData
                                Description: This method use for standard scaling.
                                Output: Returns standard values.
                                On Failure: Raise Exception

                                Written By: Chitransh Saxena
                                Version: 1.0
                                Revisions: None

                        """

        try:

            scalar = StandardScaler()
            X_scaled = scalar.fit_transform(X)
            self.log.log(self.file,"Standard scaling is successfully completed!!!")
            self.file.close()
            return X_scaled

        except Exception as e:
            self.log.log(self.file,"Exception While doing standard scaling %s" %e)
            self.file.close()
            raise e

    def OverSampling(self,x,y):
        """
                                        Method Name: OverSampling
                                        Description: This method use for over sampling.
                                        Output: Returns the over sampled values.
                                        On Failure: Raise Exception

                                        Written By: Chitransh Saxena
                                        Version: 1.0
                                        Revisions: None

                                """

        try:

            ros = RandomOverSampler(random_state=0)
            X_resampled, y_resampled = ros.fit_resample(x, y)
            # self.log.log(self.file,"Over sampling is successfully completed !!!")
            # self.file.close()
            return X_resampled , y_resampled

        except Exception as e:
            self.log.log(self.file,"Exception While doing over sampling %s" %e)
            self.file.close()
            raise e

    def FeatureSelection(self):
        """
                                               Method Name: FeatureSelection
                                               Description: This method use for selecting the best features.
                                               Output: Returns the best features name list.
                                               On Failure: Raise Exception

                                               Written By: Chitransh Saxena
                                               Version: 1.0
                                               Revisions: None

                                       """

        try:

            return ["Age","DurationOfPitch","PreferredPropertyStar","MaritalStatus","NumberOfTrips","Passport","PitchSatisfactionScore" ,"MonthlyIncome"]


        except Exception as e:
            self.log.log(self.file,"Exception while seleting the features %s" %e)
            self.file.close()
            raise e

    def dropUnnecessaryColumns(self,data,columnNameList):
        """
                        Method Name: dropUnnecessaryColumns
                        Description: This method drops the unwanted columns as discussed in EDA section.

                        Written By: Chitransh Saxena
                        Version: 1.0
                        Revisions: None

                                """
        try:
            data = data.drop(columnNameList,axis=1)
            return data

        except Exception as e:
            self.log.log(self.file,"Exception While droping the columns...")
            self.file.close()
            raise e