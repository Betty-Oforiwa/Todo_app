import sqlite3
DB_PATH = './todoapp.db'
NOTSTARTED = 'Not Started'
INPROGRESS = 'In Progress'
COMPLETED = 'Completed'

   



def add_to_list(item,status):
    try:
        connection = sqlite3.connect(DB_PATH)
        print ("Opened database successfully")
        c = connection.cursor()
        c.execute('insert into todolist(item,status) values(?,?)',( item, status))
        connection.commit()
        connection.close()
        return "Added"
    except Exception as e:
        print ('Error ', e)
        return None
    
todo_list = {}
    
    
def get_all_items():
    try:
        connection = sqlite3.connect(DB_PATH)
        print ("All Items in Database")
        c = connection.cursor()
        c.execute('select * from todolist')
        rows = c.fetchall()
        connection.close()
        return {"count": len(rows), "items": rows }
    except Exception as e:
        print ('Error: ', e)
        return None


def get_item(item):
    try:
        connection = sqlite3.connect(DB_PATH)
        c = connection.cursor()
        c.execute("select status from todolist where item='%s'" % item) 
        status = c.fetchone()[0]
        return status
    except Exception as e:
        print ('Error: ', e)
        return None
    
    
def update_status(item, status):
    
    if(status.lower().strip() == 'not started'):
            status = NOTSTARTED
    elif(status.lower().strip() == 'in progress'):
            status = INPROGRESS
    elif(status.lower(). strip() == 'completed'):
            status = COMPLETED
    else:
            print("Invalid Status - " + status)
            return None
            
    try:
        connection = sqlite3.connect(DB_PATH)
        c = connection.cursor()
        c.execute('update items set status=? where item=?', (status, item))
        connection.commit()
        return {item:status}
    except Exception as e:
        print('Error: ', e)
        return None 
    
    
def delete_item(item, status):
    try:
        connection = sqlite3.connect(DB_PATH)
        c = connection.cursor()
        c.execute('delete from todolist where item=? where item=?', (item, status))
        connection.commit()
        
        return {'item': item}
    except Exception as e:
        print('Error: ', e)
        return None  
        
        
        