from flask import Flask
from flask import request,jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/IDE_Task"
mongo = PyMongo(app)
CORS(app)
@app.route('/save_code',methods=['POST'])
def code_save():
    data=request.json
   
    if data['code'] and data['code']!='':
        save_id=mongo.db.code.insert(data)
        return jsonify({'response':'1','message':str(save_id)})
    else:
        return jsonify({'response':'0','message':'Please write a code to save.'})

@app.route('/remove_code/<id>',methods=['GET'])
def code_remove(id):
    if id!='':
        remove_id=mongo.db.code.delete_one({'_id':ObjectId(id)})
        return jsonify({'response':'1','message':str(remove_id)})
    else:
        return jsonify({'response':'0','message':'Sorry! Cannot find the code to be deleted.'})

@app.route('/get_code',methods=['GET'])
def code_get():
    code_list=[]
   
    for cod in mongo.db.code.find({},{"code":1,"_id":1}):
        cod['_id']=str(cod['_id'])
        code_list.append(cod)
       
    return jsonify({'list':code_list})
    

    
    