//删除学生
function deletestudent() {
    var id = document.getElementById("id").value;
    var url = "http://localhost:6060/admin/student/delete?student_id="+id;
    var ajaxObj = new XMLHttpRequest();
    ajaxObj.open('post', url);
    ajaxObj.send();
    ajaxObj.onreadystatechange = function () {
        if (ajaxObj.readyState == 4 && ajaxObj.status == 200){
            console.log('数据返回成功');
            console.log(ajaxObj.responseText);
            alert("删除成功");
            localStorage.setItem("current_type", "student_info");
            window.location.href = "Admin_Info.html";
        }
        else if(ajaxObj.readyState == 4 && ajaxObj.status == 404) {
            var last=ajaxObj.responseText; //将JSON对象转化为JSON字符
            var obj = JSON.parse(last);
            alert("删除失败: " + obj.error);
        }
    }
}
//删除教师信息
function deleteteacher() {
    var id = document.getElementById("id").value;
    var url = "http://localhost:6060/admin/teacher/delete?teacher_id="+id;
    var ajaxObj = new XMLHttpRequest();
    ajaxObj.open('post', url);
    ajaxObj.send();
    ajaxObj.onreadystatechange = function () {
        if (ajaxObj.readyState == 4 && ajaxObj.status == 200){
            console.log('数据返回成功');
            console.log(ajaxObj.responseText);
            alert("删除成功");
            localStorage.setItem("current_type", "teacher_info");
            window.location.href = "Admin_Info.html";
        }
        else if(ajaxObj.readyState == 4 && ajaxObj.status == 404) {
            var last=ajaxObj.responseText; //将JSON对象转化为JSON字符
            var obj = JSON.parse(last);
            alert("删除失败: " + obj.error);
        }
    }
}
//删除课程
function deletecourse() {
    var id = document.getElementById("id").value;
    var url = "http://localhost:6060/admin/course/delete?course_id="+id;
    var ajaxObj = new XMLHttpRequest();
    ajaxObj.open('post', url);
    ajaxObj.send();
    ajaxObj.onreadystatechange = function () {
        if (ajaxObj.readyState == 4 && ajaxObj.status == 200){
            console.log('数据返回成功');
            console.log(ajaxObj.responseText);
            alert("删除成功");
            localStorage("current_type", "course_info");
            window.location.href = "Admin_Info.html";
        }
        else if(ajaxObj.readyState == 4 && ajaxObj.status == 404) {
            var last=ajaxObj.responseText; //将JSON对象转化为JSON字符
            var obj = JSON.parse(last);
            alert("删除失败: " + obj.error);
        }
    }
}
//删除专业
function deletemajor() {
    var id = document.getElementById("id").value;
    var url = "http://localhost:6060/admin/major/delete?major_id="+id;
    var ajaxObj = new XMLHttpRequest();
    ajaxObj.open('post', url);
    ajaxObj.send();
    ajaxObj.onreadystatechange = function () {
        if (ajaxObj.readyState == 4 && ajaxObj.status == 200){
            console.log('数据返回成功');
            console.log(ajaxObj.responseText);
            alert("删除成功");
            localStorage("current_type", "major_info");
            window.location.href = "Admin_Info.html";
        }
        else if(ajaxObj.readyState == 4 && ajaxObj.status == 404) {
            var last=ajaxObj.responseText; //将JSON对象转化为JSON字符
            var obj = JSON.parse(last);
            alert("删除失败: " + obj.error);
        }
    }
}

//删除专业选课
function deletemajorcourse() {
    var major_id = document.getElementById("major_id").value;
    var course_id = document.getElementById("course_id").value;
    var url = "http://localhost:6060/admin/major_course/delete?major_id="+major_id+"&course_id="+course_id;
    var ajaxObj = new XMLHttpRequest();
    ajaxObj.open('post', url);
    ajaxObj.send();
    ajaxObj.onreadystatechange = function () {
        if (ajaxObj.readyState == 4 && ajaxObj.status == 200){
            console.log('数据返回成功');
            console.log(ajaxObj.responseText);
            alert("删除成功");
            localStorage("current_type", "major_course_info");
            window.location.href = "Admin_Info.html";
        }
        else if(ajaxObj.readyState == 4 && ajaxObj.status == 404) {
            var last=ajaxObj.responseText; //将JSON对象转化为JSON字符
            var obj = JSON.parse(last);
            alert("删除失败: " + obj.error);
        }
    }
}