<head>
    <link rel = 'stylesheet' href = '/static/css/style.css'>
</head>
<body>
    <h1>Registrated List and Add/Delete item</h1>
        <h2>Add</h2>
            <form action="add" method='POST'>
                <input type='text' name='item_system' placeholder='システム名'/>
                <input type='text' name='item_date' placeholder='日付(yyyymmdd))'/>
                <input type='text' name='item_task' placeholder='タスク(hh:mm-hh:mm xxxxxxxx)'/>
                <input type='submit' value='登録'/>
            </form>
        <h2>List and Delete</h1>
            <table>
                <tr>
                    <th>date</th>
                    <th>id</th>
                    <th>system</th>
                    <th>task</th>
                    <th>delete</th>
                </tr>
                %for item in item_list:
                    <tr>
                        <td>{{item["date"]}}</td>
                        <td class="id">{{item["id"]}}</td>
                        <td class="id">{{item["system"]}}</td>
                        <td class="long">{{item["task"]}}</td>
                        <td><a href="/del/{{item['id']}}">delete</a></td>
                    </tr>
                %end
            </table>
        <a href="./summary">go to summary</a>
</body>
