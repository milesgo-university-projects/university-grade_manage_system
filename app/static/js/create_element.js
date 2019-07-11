function createDivWithInput(label_html, input_id, read_only, input_value) {
    var div = document.createElement("div");
    div.className = "alert alert-success";
    var label = document.createElement("label");
    label.innerHTML = label_html;
    div.appendChild(label);

    var input = document.createElement("input");
    input.className="form-control";
    input.id = input_id;
    if (read_only == "true") {
        input.setAttribute("readOnly", read_only);
    }
    input.value = input_value;
    div.appendChild(input);

    return div;
}

function createDivWithSelection(label_html, select_id, default_value, value_list) {
    var div = document.createElement("div");
    div.className = "alert alert-success";

    var label = document.createElement("label");
    label.innerHTML = label_html;
    div.appendChild(label);

    var select = document.createElement("select");
    select.id = select_id;
    select.className = "form-control";
    for(var i = 0; i < value_list.length; i ++) {
        var op = document.createElement("option");
        op.innerHTML = value_list[i];
        if (op.innerHTML == default_value) {
            op.selected = "selected";
        }
        select.add(op, null);
    }
    div.appendChild(select);
    return div;
}

function createButton(button_name, margin_right, onclick_callback) {
    var div = document.createElement("div");
    var button = document.createElement("button");
    button.className = "btn btn-success btn-lg";
    button.innerHTML = button_name;
    button.style.marginRight = margin_right;
    button.onclick = onclick_callback;
    div.appendChild(button);
    return div;
}

function createButtonWithoutDiv(button_name, margin_right, onclick_callback) {
    var button = document.createElement("button");
    button.className = "btn btn-success btn-lg";
    button.innerHTML = button_name;
    button.style.marginRight = margin_right;
    button.onclick = onclick_callback;
    return button;
}