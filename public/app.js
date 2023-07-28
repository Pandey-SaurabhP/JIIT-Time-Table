function postData() {
    var inp = document.getElementById('inp');
    var day = document.getElementById('day');

    
    const url = 'http://127.0.0.1:5000/';
    const data = {
        input: inp.value,
        day: day.value
    };

    const jsonData = JSON.stringify(data);

    console.log(jsonData);

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: jsonData
    })
    .then(response => response.text())
    .then(text => {
        dataArray = convertToLL(text)
        generate(dataArray)

    })
    .catch(error => console.error('Error:', error));
}

function autoDetect(){

    var today = new Date();
    var dayOfWeek = today.getDay();
    var daysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    var todayDayName = daysOfWeek[dayOfWeek];
    var selectElement = document.getElementById('day');
    var optionIndex = Array.from(selectElement.options).findIndex(option => option.value === todayDayName);
    selectElement.selectedIndex = optionIndex;
}

function convertToLL(text){
    dataString = text;
    dataString = "[" + dataString.replace(/\]\s*,\s*\[/g, "],[") + "]";

    return JSON.parse(dataString);
}


function generate(data){
    var table = document.getElementById('myTable');
    table.innerHTML = ""

    data.forEach(rowData => {
        var row = document.createElement('tbody');

        rowData.forEach(cellData => {
            var cell = document.createElement('tr');

            if (typeof cellData === 'string') {
                cell.textContent = cellData;
            } else if (Array.isArray(cellData)) {
                cellData.forEach(cellValue => {
                    var x = document.createElement('td');
                    x.textContent = cellValue;
                    cell.appendChild(x);
                });
            }

            row.appendChild(cell);
        });

        table.appendChild(row);
    });

    document.body.appendChild(table);
}


  