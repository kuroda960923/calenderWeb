<head>
    <link rel = 'stylesheet' href = '/static/css/style.css'>
</head>
<body>
    <h1>Add new item</h1>
        <form action="add" method='POST'>
            <input type='text' name='item_system' placeholder='システム名'/>
            <input type='text' name='item_date' placeholder='日付'/>
            <input type='text' name='item_task' placeholder='タスク'/>
            <input type='submit' value='登録'/>
        </form>
</body>
