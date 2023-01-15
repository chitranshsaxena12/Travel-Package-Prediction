from application_logging.logger import App_Logger
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score


class Model_Finder:
    """
                This class shall  be used to find the model with best accuracy and AUC score.
                Written By: Chitransh Saxena
                Version: 1.0
                Revisions: None

                """

    def __init__(self):
        self.file = open("Training_logs/best_model_finder.txt","a+")
        self.log = App_Logger()
        self.XG_boost = XGBClassifier()
        self.RandomForestClass = RandomForestClassifier()



    def get_best_params_for_Random_Forest_Classifier(self, train_x, train_y):
        """
                                                Method Name: get_best_params_for_Random_Forest_Classifier
                                                Description: get the parameters for Random_Forest_Classifier Algorithm which give the best accuracy.
                                                             Use Hyper Parameter Tuning.
                                                Output: The model with the best parameters
                                                On Failure: Raise Exception

                                                Written By: Chitransh Saxena
                                                Version: 1.0
                                                Revisions: None

                                        """
        # self.log.log(self.file,'Entered the RandomForestclassifier method of the Model_Finder class')
        try:
            # self.param_grid_Random_forest_Tree = {"n_estimators" :[100,200,300,400,500,600,700,800,900,1000],
            #                                      "max_depth" : [14,15,16,13,18,17]}#,
            #                                      # "bootstrap" : [True,False],
            #                                      # "max_features" : ["sqrt","log2"]
            #                                      #  }
            #
            # self.grid = GridSearchCV(self.RandomForestClass, self.param_grid_Random_forest_Tree, verbose=3, cv=5)
            # # finding the best parameters
            # self.grid.fit(train_x, train_y)
            #
            # self.n_estimators = self.grid.best_params_['n_estimators']
            # self.max_depth = self.grid.best_params_['max_depth']
            # # self.bootstrap = self.grid.best_params_['bootstrap']
            # # self.max_features = self.grid.best_params_['max_features']

            self.random_tree = RandomForestClassifier()#n_estimators = self.n_estimators, max_depth = self.max_depth)#, bootstrap = self.bootstrap, max_features = self.max_features )
            self.random_tree.fit(train_x,train_y)
            # self.log.log(self.file,'RandomForestClass best params: ' + str(self.grid.best_params_) + '. Exited the RandomForestClass method of the Model_Finder class')
            # self.file.close()
            return self.random_tree

        except Exception as e:
            # self.log.log(self.file,'Exception occured in RandomForestReg method of the Model_Finder class. Exception message:  ' + str(e))
            # self.file.close()
            raise e

    def get_best_params_for_XG_Boost_Classifier(self, train_x, train_y):
        """
                                                Method Name: get_best_params_for_XG_Boost_Classifier
                                                Description: get the parameters for XG_Boost_Classifier Algorithm which give the best accuracy.
                                                             Use Hyper Parameter Tuning.
                                                Output: The model with the best parameters
                                                On Failure: Raise Exception

                                                Written By: Chitransh Saxena
                                                Version: 1.0
                                                Revisions: None

                                        """

        try:
            # self.log.log(self.file, 'Entered the XGBOOSTCLASSIFIER method of the Model_Finder class')
            # self.file.close()
            # self.param_grid_XG_Boost_Tree = {
            #                                          "max_depth":[9,10,12,15,16,14,13],
            #                                          "n_estimators":[100,200,300,400,700,1000,800]
            #                                         }
            #
            # self.grid = GridSearchCV(self.XG_boost, self.param_grid_Random_forest_Tree, verbose=3, cv=5)
            # # finding the best parameters
            # self.grid.fit(train_x, train_y)
            #
            # self.n_estimators = self.grid.best_params_['n_estimators']
            # self.max_depth = self.grid.best_params_['max_depth']


            self.XG_Boost_tree = XGBClassifier()#n_estimators=self.n_estimators, max_depth=self.max_depth)
            self.XG_Boost_tree.fit(train_x, train_y)
            # self.log.log(self.file, 'XGBOOST best params: ' + str(self.grid.best_params_) + '. Exited the XGBoostClassifier method of the Model_Finder class')
            # self.file.close()
            return self.XG_Boost_tree

        except Exception as e:
            # self.log.log(self.file, 'Exception occured in XGBoost method of the Model_Finder class. Exception message:  ' + str(e))
            # self.file.close()
            raise e



    def get_best_model(self,train_x,train_y,test_x,test_y):
        """
                                                Method Name: get_best_model
                                                Description: Find out the Model which has the best AUC score.
                                                Output: The best model name and the model object
                                                On Failure: Raise Exception

                                                Written By: Chitransh Saxena
                                                Version: 1.0
                                                Revisions: None

                                        """

        # create best model for Random Forest
        try:
            self.log.log(self.file, 'Entered the get_best_model method of the Model_Finder class')
            self.file.close()

            self.random= self.get_best_params_for_Random_Forest_Classifier(train_x, train_y)
            self.prediction_random = self.random.predict(test_x) # Predictions using the Random Forest Classifier Model
            self.accurancy_value_random = accuracy_score(test_y,self.prediction_random)


         # create best model for XGBoost
            self.XG_Boost = self.get_best_params_for_XG_Boost_Classifier(train_x, train_y)
            self.prediction_XG_Boost = self.XG_Boost.predict(test_x)  # Predictions using the XGBoost Classifier Model
            self.accurancy_value_XG_Boost = accuracy_score(test_y, self.prediction_XG_Boost)
            # self.log.log(self.file, 'Finished the get_best_model method of the Model_Finder class')
            # self.file.close()


            #comparing the two models
            if(self.accurancy_value_random <  self.accurancy_value_XG_Boost):
                return "XG_Boost" , self.XG_Boost
            else:
                return "Random_Forest" , self.random

        except Exception as e:
            # # self.log.log(self.file,'Exception occured in get_best_model method of the Model_Finder class. Exception message:  ' + str(e))
            # self.log.log(self.file,'Model Selection Failed. Exited the get_best_model method of the Model_Finder class')
            # self.file.close()
            raise e


