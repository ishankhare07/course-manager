function initialize() {
    for(var x in data) {
        var div = document.createElement('div');
        var unit = document.createTextNode(x);
        div.appendChild(unit);
        div.setAttribute('class','units');
        div.appendChild(document.createTextNode("Unit " + x));
        
        var course = document.createElement('div');
        course.setAttribute('class','courseContainer');
        //course.appendChild(div);
        document.body.appendChild(course);
        
        for(var y in data[x]) {
            var itemContainer = document.createElement('span');
            itemContainer.setAttribute('class','itemContainer');
            itemContainer.classList.add('unchecked');
            
            var content = document.createTextNode(data[x][y]["content"]);
            itemContainer.appendChild(content);
            itemContainer.setAttribute('onclick','clicked(this)');
            
            course.appendChild(itemContainer);
        }
    }
}

function clicked(button) {
    if(button.classList.contains("unchecked")) {
        button.classList.remove("unchecked");
        button.classList.add("checked");
    }
    else if(button.classList.contains("checked")){
        button.classList.remove("checked");
        button.classList.add("unchecked");
    }
}