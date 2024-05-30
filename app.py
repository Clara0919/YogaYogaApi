from flask import Flask, request
import getYogaData
from flask_cors import CORS

app = Flask(__name__)


CORS(app)  # 啟用 CORS
@app.route("/getAllBranch", methods=['GET'])
def getAllBranch():
    result =getYogaData.formatted_branchData
    return result

@app.route("/getFilterData", methods=['GET'])
def getFilterData():
    branchId = request.args.get('branchId')
    tab= request.args.get('tab')
    date= request.args.get('date')
    view = request.args.get('view')
    result=getYogaData.getFilterClassData(branchId,tab,date,view)

    return result 