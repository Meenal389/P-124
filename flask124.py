from flask import Flask,jsonify,request

app=Flask(__name__)

data = [
    {
        'contact':9543434535,
        'name':'Raju',
        'done':false,
        'id':1
    },
    {
        'contact':9543856948,
        'name':'Rahul',
        'done':false,
        'id':2
    }
]

@app.route("/add-data",methods=["POST"])

def add_task():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'please provide the data'
        },400)

    contact= {
        'id': tasks[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }

    tasks.append(contact)

    return jsonify({
            "status":"success",
            "message": "Task added succesfully!"
    })
    
@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    }) 

if(__name__== "__main__"):
    app.run(debug=True)
