from flask import Flask, render_template, request, Response
import csv
from training_validation_insertion import train_validation
from Prediction_validation_insertion import prediction_validation
from trainingModel import trainModel
from predictionModel import predictModel
from downloadedfile.download import Download





app = Flask(__name__)

@app.route("/",methods=["GET","POST"])

def index():
    move = Download()
    move.MoveSaveDownloadFileToSaveFiles()
    return render_template("home.html")

@app.route("/training",methods=["GET","POST"])

def training():
    try:
        if request.method == "POST":
            f = request.form["csvfile"]
            data = []
            with open(f) as file:
                csv_file = csv.reader(file)
                for row in csv_file:
                    data.append(row)
                train_valObj = train_validation()
                train_valObj.train_validation(data)
                train_model = trainModel()
                train_model.trainingModel()
                return "Model Has Been Successfully Trained"

    except ValueError:
        return Response("Error Occurred! %s " % ValueError)

    except KeyError:
        return Response("Error Occurred! %s " % KeyError)

    except Exception as e:
        return Response("Error Occurred! %s or enter valid data" % e)




@app.route("/prediction", methods=["GET", "POST"])
def prediction():
    if request.method == "POST":
        f = request.form["csvfile"]
        data = []
        with open(f) as file:
            csv_file = csv.reader(file)
            for row in csv_file:
                data.append(row)
        prediction_obj = prediction_validation()
        prediction_obj.prediction_validation(data)

        prediction_model = predictModel()
        prediction_model.predictionModel()

        savefile = Download()
        savefile.save_file()
        return Response("Model Has Been Successfully Predicted Now You Can Download Your Predicted File")


@app.route('/download')
def download_file():
    downfile = Download()
    return downfile.downloadfile()










if __name__=="__main__":
    app.run(debug=True)