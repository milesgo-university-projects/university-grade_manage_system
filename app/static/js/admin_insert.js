//添加学生后提交到服务器
function insertstudent() {
    var name = document.getElementById("name").value;

    var obj1 = document.getElementById("sexes"); 
    var index1 = obj1.selectedIndex;
    var sex = obj1.options[index1].value;

    var birth_year =  parseInt(document.getElementById("birth_year").value);
    var province =  document.getElementById("province").value;
    var enter_year = document.getElementById("enter_year").value;

    var obj2 = document.getElementById("major_ids");
    var index2 = obj2.selectedIndex;
    var major_id = obj2.options[index2].value;
    
    var url = "http://localhost:6060/admin/student/insert?student_name="+name+"&sex="+sex+"&birth_year="+birth_year+"&province="+province+"&enter_year="+enter_year+"&major_id="+major_id;
    var ajaxObj = new XMLHttpRequest();
    ajaxObj.open('post', url);
    ajaxObj.send();
    ajaxObj.onreadystatechange = function () {
        if (ajaxObj.readyState == 4 && ajaxObj.status == 200){
            console.log('数据返回成功');
            console.log(ajaxObj.responseText);
            alert("添加成功");
        }
        else if(ajaxObj.readyState == 4 && ajaxObj.status == 404) {
            var last=ajaxObj.responseText; //将JSON对象转化为JSON字符
            var obj = JSON.parse(last);
            alert("添加失败: " + obj.error);
        }
    }
}
//添加教师后提交到服务器
function insertteacher() {
    var name = document.getElementById("name").value;

    var obj1 = document.getElementById("sexes"); 
    var index1 = obj1.selectedIndex;
    var sex = obj1.options[index1].value;

    var birth_year =  parseInt(document.getElementById("birth_year").value);
    
    var url = "http://localhost:6060/admin/teacher/insert?teacher_name="+name+"&sex="+sex+"&birth_year="+birth_year;
    var ajaxObj = new XMLHttpRequest();
    ajaxObj.open('post', url);
    ajaxObj.send();
    ajaxObj.onreadystatechange = function () {
        if (ajaxObj.readyState == 4 && ajaxObj.status == 200){
            console.log('数据返回成功');
            console.log(ajaxObj.responseText);
            alert("添加成功");
        }
        else if(ajaxObj.readyState == 4 && ajaxObj.status == 404) {
            var last=ajaxObj.responseText; //将JSON对象转化为JSON字符
            var obj = JSON.parse(last);
            alert("添加失败:" + obj.error);
        }
    }
}

//添加课程后提交到服务器
function insertcourse() {
    var name = document.getElementById("name").value;
    var year = document.getElementById("year").value;

    var obj1 = document.getElementById("semester"); 
    var index1 = obj1.selectedIndex;
    var semester = obj1.options[index1].value;

    var credit = document.getElementById("credit").value;

    var obj2 = document.getElementById("teacher_ids");
    var index2 = obj2.selectedIndex;
    var teacher_id = obj2.options[index2].value;
    
    var url = "http://localhost:6060/admin/course/insert?course_name="+name+"&year="+year+"&semester="+semester+"&credit="+credit+"&teacher_id="+teacher_id;
    var ajaxObj = new XMLHttpRequest();
    ajaxObj.open('post', url);
    ajaxObj.send();
    ajaxObj.onreadystatechange = function () {
        if (ajaxObj.readyState == 4 && ajaxObj.status == 200){
            console.log('数据返回成功');
            console.log(ajaxObj.responseText);
            alert("添加成功");
        }
        else if(ajaxObj.readyState == 4 && ajaxObj.status == 404) {
            var last=ajaxObj.responseText; //将JSON对象转化为JSON字符
            var obj = JSON.parse(last);
            alert("添加失败: " + obj.error);
        }
    }
}

//添加专业后提交到服务器
function insertmajor() {
    var name = document.getElementById("name").value;

    var url = "http://localhost:6060/admin/major/insert?major_name="+name;
    var ajaxObj = new XMLHttpRequest();
    ajaxObj.open('post', url);
    ajaxObj.send();
    ajaxObj.onreadystatechange = function () {
        if (ajaxObj.readyState == 4 && ajaxObj.status == 200){
            console.log('数据返回成功');
            console.log(ajaxObj.responseText);
            alert("添加成功");
        }
        else if(ajaxObj.readyState == 4 && ajaxObj.status == 404) {
            var last=ajaxObj.responseText; //将JSON对象转化为JSON字符
            var obj = JSON.parse(last);
            alert("添加失败: " + obj.error);
        }
    }
}

//添加专业选课后提交到服务器
function insertstudent() {
    var name = document.getElementById("name").value;

    var obj1 = document.getElementById("sexes"); 
    var index1 = obj1.selectedIndex;
    var sex = obj1.options[index1].value;

    var birth_year =  parseInt(document.getElementById("birth_year").value);
    var province =  document.getElementById("province").value;
    var enter_year = document.getElementById("enter_year").value;

    var obj2 = document.getElementById("major_ids");
    var index2 = obj2.selectedIndex;
    var major_id = obj2.options[index2].value;
    
    var url = "http://localhost:6060/admin/student/insert?student_name="+name+"&sex="+sex+"&birth_year="+birth_year+"&province="+province+"&enter_year="+enter_year+"&major_id="+major_id;
    var ajaxObj = new XMLHttpRequest();
    ajaxObj.open('post', url);
    ajaxObj.send();
    ajaxObj.onreadystatechange = function () {
        if (ajaxObj.readyState == 4 && ajaxObj.status == 200){
            console.log('数据返回成功');
            console.log(ajaxObj.responseText);
            alert("添加成功");
        }
        else if(ajaxObj.readyState == 4 && ajaxObj.status == 404) {
            var last=ajaxObj.responseText; //将JSON对象转化为JSON字符
            var obj = JSON.parse(last);
            alert(obj.error);
            alert("添加失败");
        }
    }
}