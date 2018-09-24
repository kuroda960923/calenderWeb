<head>
    <link rel = 'stylesheet' href = '/static/css/style.css'>
</head>
<body>
    <h1>Schedule Summary of Clearing System</h1>
    <table>
        <tr>
            <th>date</th>
            <th>OTC</th>
            <th>2nd</th>
            <th>RTC</th>
        </tr>
        %for item in item_list:
            <tr>
                <td>{{item["date"]}}</td>
                <td>{{item["OTC"]}}</td>
                <td>{{item["2nd"]}}</td>
                <td>{{item["RTC"]}}</td>
            </tr>
        %end
    </table>
    <a href="./add">go to add request</a>
</body>
