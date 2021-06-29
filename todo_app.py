import helper
import json
from flask import Flask, request, Response
import sqlite3
  

app = Flask(__name__)



@app.route('/')
def Welcome_todolist():
    return 'welcome to Todolist. Add, Delete and Update your todo list for effective workflow!!'


@app.route('/item/new', methods=['GET'])
def add_item():
    req_item = request.args.get('item')
    req_status = request.args.get('status')
    print(req_item)
    
    helper.add_to_list(req_item,req_status)
    
    # if res_data is None:
    #     response = Response("{'error':'Item not add - " + item + "'}", status=400 , mimetype='application/json')
    #     return response
    
    response = Response(json.dumps(req_item), mimetype='application/json')
    return response 
@app.route('/items/all')
def get_all_items():
    res_item = helper.get_all_items()
    response = r=Response(json.dumps(res_item), mimetype='application/json')
    return response


@app.route('/item/status', methods=['GET'])
def get_item():
   item_name = request.args.get('name')
   status = helper.get_item(item_name)
   if status is None:
      response = Response("{'error': 'Item Not Found - '}"  + item_name, status=404 , mimetype='application/json')
      return response
   res_item = {
      'status': status
   }

   response = Response(json.dumps(res_item), status=200, mimetype='application/json')
   return response


@app.route('/item/update', methods = ['PUT'])
def update_status():
   req_item = request.get_json()
   item = req_item['item']
   status = req_item['status']
   res_item = helper.update_status(item, status)
   if res_item is None:
      response = Response("{'error': 'Error updating item - '" + item + ", " + status   +  "}", status=400 , mimetype='application/json')
      return response

   response = Response(json.dumps(res_item), mimetype='application/json')
   
   return response

@app.route('/item/remove', methods = ['DELETE'])
def delete_item():
   #Get item from the POST body
   req_item = request.get_json()
   item = req_item['item']
   
   #Delete item from the list
   res_item = helper.delete_item(item)
   if res_item is None:
      response = Response("{'error': 'Error deleting item - '" + item +  "}", status=400 , mimetype='application/json')
      return response
   
   #Return response
   response = Response(json.dumps(res_item), mimetype='application/json')
   
   return response



if __name__ == "__main__":
    app.run(debug=True)
