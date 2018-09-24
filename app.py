from bottle import route, run, get, static_file,template,request,redirect
import sqlite3

@get('/static/css/<filePath:path>')
def index(filePath):
    return static_file(filePath, root='./static/css')    

@route("/")
def index():
    return "<head><link rel = 'stylesheet' href = '/static/css/style.css'></head><h1>Welcome to Python</h1>"

@route("/top")
def top():
    return template("top_tmpl")

@route("/list")
def view_list():
    conn = sqlite3.connect('items.db')
    c = conn.cursor()
    c.execute(u"select date,id,system,task from items order by date")
    item_list = []

    for row in c.fetchall():
        item_list.append({"date": row[0],"id": row[1],"system": row[2],"task": row[3]})

    conn.close()

    return template("list_tmpl", item_list=item_list)

@route("/add", method=["GET","POST"])
def add_item():
    if request.method == "POST":
        item_system = request.POST.getunicode("item_system")
        item_date = request.POST.getunicode("item_date")
        item_task = request.POST.getunicode("item_task")
        
        conn = sqlite3.connect('items.db')
        c = conn.cursor()

        item = (item_system, item_date, item_task)
        c.execute('insert into items (system, date, task) values (?,?,?)', item)
        
        conn.commit()
        conn.close()
        return "SUCCESS <br> <a href='list'>return to list</a>"
    else:
        return template("add_tmpl")
    
@route("/summary")
def view_summary():
    conn = sqlite3.connect('items.db')
    c = conn.cursor()
    c.execute(u"select date, group_concat(case when system is 'OTC' THEN task ELSE NULL END,'\n') as 'OTC',group_concat(case when system is '2nd' THEN task ELSE NULL END) as '2nd',group_concat(case when system is 'RTC' THEN task ELSE NULL END) as 'RTC'from items group by date")
    item_list = []

    for row in c.fetchall():
        item_list.append({"date": row[0],"OTC": row[1],"2nd": row[2],"RTC": row[3]})
    conn.close()
    return template("summary_tmpl", item_list=item_list)


@route("/del/<item_id:int>")
def del_item(item_id):
    conn = sqlite3.connect('items.db')
    c = conn.cursor()
    c.execute("delete from items where id=?", (item_id,))
    conn.commit()
    conn.close()
    
    return redirect("/list")

run(reloader=True, port=9999)
