let table = document.createElement("table");
table.id = "menu_tbl";
let tbody = document.createElement("tbody");
tbody.appendChild(create_table_row("meaning", "Meaning"));
tbody.appendChild(create_table_row(null, ["meaning_m", "Multiple-Choice"]));
tbody.appendChild(create_table_row(null, ["meaning_i", "Input"]));
tbody.appendChild(create_table_row("pronunciation", "Pronunciation"));
tbody.appendChild(create_table_row(null, ["pronunciation_m", "Multiple-Choice"]));
tbody.appendChild(create_table_row(null, ["pronunciation_i", "Input"]));
table.appendChild(tbody);

let menu_details = document.getElementById('menu_details');
menu_details.appendChild(table);

//optionaler Bestätigungsbutton, sonst neue Einstellungen bei jedem Change-Ereignis ändern:
let submit = document.createElement("button");
submit.id = "submit_button";
submit.textContent = "Choose";
menu_details.appendChild(submit);
document.getElementById("submit_button").addEventListener("click", function(){
    return; //Einstellungen übernehmen
});
//

if (localStorage.getItem("selection") != null) {
    let selection = localStorage.getItem("selection");
    setting(selection);
}
else {
    setting("meaning_m");
}

let menu_checkbox = document.getElementsByClassName("menu_checkbox");
for (let i = 0; i < menu_checkbox.length; i++) {
    menu_checkbox[i].addEventListener("change", function() {
        let id = menu_checkbox[i].id;
        if (this.checked) {
            if (!id.includes("_")) {
                id = id += "_m"
            }
            setting(id);
            localStorage.setItem("selection", id);
        }
        else {
            if (id.includes("_m") ) {
                id = id.replace("_m", "_i");
                setting(id);
                localStorage.setItem("selection", id);
            }
            else if (id.includes("_i") ) {
                id = id.replace("_i", "_m");
                setting(id);
                localStorage.setItem("selection", id);
            }
            else if (id.includes("meaning")) {
                setting("pronunciation_m");
                localStorage.setItem("selection", "pronunciation_m");
            }
            else {
                setting("meaning_m");
                localStorage.setItem("selection", "meaning_m");
            }
        }
    })
}

function create_table_row(a, b){
    let tr = document.createElement("tr");
    if (a == null){
        tr.appendChild(create_td());
        let id = b[0];
        let text = b[1]; 
        tr.appendChild(create_td(id, text));
    }
    else {
        tr.appendChild(create_td(a, null));
        tr.appendChild(create_td(null, b));
    }
    return tr;
}

function create_td (id, text) {
    let td = document.createElement("td");
    if (id != null) {
        td.appendChild(create_checkbox(id));
    }
    if (text != null) {
        td.appendChild(document.createTextNode(text));
    }
    return td;
}

function create_checkbox(id){
    let checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.id = id;
    checkbox.className = "menu_checkbox";
    return checkbox;
}

function uncheck(ids) {
    for (let i = 0; i < ids.length; i++) {
        document.getElementById(ids[i]).checked = false;
    }
}

function check(ids) {
    for (let i = 0; i < ids.length; i++) {
        document.getElementById(ids[i]).checked = true;
    }
}

function setting(option) {
    if (option === "pronunciation_m") {
        uncheck(["meaning", "meaning_m", "meaning_i", "pronunciation_i"]);
        check(["pronunciation", "pronunciation_m"]);
    }
    else if (option === "pronunciation_i") {
        uncheck(["meaning", "meaning_m", "meaning_i", "pronunciation_m"]);
        check(["pronunciation", "pronunciation_i"]);
    }
    else if (option === "meaning_m") {
        uncheck(["pronunciation", "pronunciation_m", "pronunciation_i", "meaning_i"]);
        check(["meaning", "meaning_m"]);
    }
    else if (option === "meaning_i") {
        uncheck(["pronunciation", "pronunciation_m", "pronunciation_i", "meaning_m"]);
        check(["meaning", "meaning_i"]);
    }
}