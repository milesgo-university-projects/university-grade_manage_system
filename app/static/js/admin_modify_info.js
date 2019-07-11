//修改学生信息
function modifystudent() {
    var id = document.getElementById("id").value;
    var name = document.getElementById("name").value;

    var obj1 = document.getElementById("sexes");
    var index1 = obj1.selectedIndex;
    var sex = obj1.options[index1].value;

    var birth_year =  document.getElementById("birth_year").value;
    var province =  document.getElementById("province").value;
    var enter_year =  document.getElementById("enter_year").value;

    var obj2 = document.getElementById("major_ids");
    var index2 = obj2.selectedIndex;
    var major_id = obj2.options[index2].value;
    major_id = major_id.split('/')[0];

    var url = "http://localhost:6060/admin/student/update?student_id="+id+"&student_name="+name+"&sex="+sex+"&birth_year="+birth_year+"&province="+province+"&enter_year="+enter_year+"&major_id="+major_id;
    var ajaxObj = new XMLHttpRequest();
    ajaxObj.open('post', url);
    ajaxObj.send();
    ajaxObj.onreadystatechange = function () {
        if (ajaxObj.readyState == 4 && ajaxObj.status == 200) {
            console.log('数据返回成功');
            console.log(ajaxObj.responseText);
            alert("修改成功");
        }
        else if(ajaxObj.readyState == 4 && ajaxObj.status == 404) {
            var last=ajaxObj.responseText; //将JSON对象转化为JSON字符
            var obj = JSON.parse(last);
            alert("修改失败: " + obj.error);
        }
    }
}
//修改教师信息
function modifyteacher() {
    var id = document.getElementById("id").value;
    var name = document.getElementById("name").value;

    var obj1 = document.getElementById("sexes"); //定位id
    var index1 = obj1.selectedIndex; // 选中索引
    var sex = obj1.options[index1].value; // 选中值

    var birth_year =  document.getElementById("birth_year").value;

    var url = "http://localhost:6060/admin/teacher/update?teacher_id="+id+"&teacher_name="+name+"&sex="+sex+"&birth_year="+birth_year;
    var ajaxObj = new XMLHttpRequest();
    ajaxObj.open('post', url);
    ajaxObj.send();
    ajaxObj.onreadystatechange = function () {
        if (ajaxObj.readyState == 4 && ajaxObj.status == 200) {
            console.log('数据返回成功');
            console.log(ajaxObj.responseText);
            alert("修改成功");
        }
        else if(ajaxObj.readyState == 4 && ajaxObj.status == 404) {
            var last=ajaxObj.responseText; //将JSON对象转化为JSON字符
            var obj = JSON.parse(last);
            alert("修改失败: " + obj.error);
        }
    }
}
//修改课程信息
function modifycourse() {
    var id = document.getElementById("id").value;
    var name = document.getElementById("name").value;
    var year = document.getElementById("year").value;

    var obj1 = document.getElementById("semester"); //定位id
    var index1 = obj1.selectedIndex; // 选中索引
    var semester = obj1.options[index1].value; // 选中值

    var obj2 = document.getElementById("teacher_ids"); //定位id
    var index2 = obj2.selectedIndex; // 选中索引
    var teacher_id = obj2.options[index2].value; // 选中值
    teacher_id = teacher_id.split("/")[0];

    var credit = document.getElementById("credit").value;
    
    var url = "http://localhost:6060/admin/course/update?course_id="+id+"&course_name="+name+"&year="+year+"&semester="+semester+"&teacher_id="+teacher_id+"&credit="+credit;
    var ajaxObj = new XMLHttpRequest();
    ajaxObj.open('post', url);
    ajaxObj.send();
    ajaxObj.onreadystatechange = function () {
        if (ajaxObj.readyState == 4 && ajaxObj.status == 200){
            console.log('数据返回成功');
            console.log(ajaxObj.responseText);
            alert("修改成功");
        }
        else if(ajaxObj.readyState == 4 && ajaxObj.status == 404) {
            var last=ajaxObj.responseText; //将JSON对象转化为JSON字符
            var obj = JSON.parse(last);
            alert("修改失败: " + obj.error);
        }
    }
}
//修改专业信息
function modifymajor() {
    var id = document.getElementById("id").value;
    var name = document.getElementById("name").value;
    
    var url = "http://localhost:6060/admin/major/update?major_id="+id+"&major_name="+name;
    var ajaxObj = new XMLHttpRequest();
    ajaxObj.open('post', url);
    ajaxObj.send();
    ajaxObj.onreadystatechange = function () {
        if (ajaxObj.readyState == 4 && ajaxObj.status == 200){
            console.log('数据返回成功');
            console.log(ajaxObj.responseText);
            alert("修改成功");
        }
        else if(ajaxObj.readyState == 4 && ajaxObj.status == 404) {
            var last=ajaxObj.responseText; //将JSON对象转化为JSON字符
            var obj = JSON.parse(last);
            alert("修改失败: " + obj.error);
        }
    }
}

