//添加学生前的准备工作
function addstudent() {
    var title = document.getElementById("title");
    title.innerHTML = "添加学生";
    var ajaxObj = new XMLHttpRequest();
    ajaxObj.open('get', "http://localhost:6060/admin/student/insert");
    ajaxObj.send();
    ajaxObj.onreadystatechange = function () {
        if (ajaxObj.readyState == 4 && ajaxObj.status == 200) {
            console.log('数据返回成功');
            console.log(ajaxObj.responseText);

            var last=ajaxObj.responseText; //将JSON对象转化为JSON字符
            var obj = JSON.parse(last);
            var container = document.getElementById("container");

            while(container.hasChildNodes()) {
                container.removeChild(container.firstChild);
            }

            var major_list = new Array();
            for (var i = 0; i < obj.majors.length; i ++) {
                major_list[i] = obj.majors[i].major_id + "/" + obj.majors[i].major_name;
            }

            container.appendChild(createDivWithInput("姓名", "name", "false", ""));
            container.appendChild(createDivWithSelection("性别", "sexes", "", new Array("男","女")));
            container.appendChild(createDivWithInput("出生年份", "birth_year", "false", ""));
            container.appendChild(createDivWithInput("籍贯", "province", "false", ""));
            container.appendChild(createDivWithInput("入学年份", "enter_year", "false", ""));
            container.appendChild(createDivWithSelection("专业编号/名称", "majors", "", major_list));
            container.appendChild(createButton("添加", "0px", insertstudent));
        }
        else if(ajaxObj.readyState == 4 && ajaxObj.status == 404) {
            var last=ajaxObj.responseText; //将JSON对象转化为JSON字符
            var obj = JSON.parse(last);
            alert("添加失败: " + obj.error);
        }
    }
}

//添加教师前的准备工作
function addteacher() {
    var title = document.getElementById("title");
    title.innerHTML = "添加教师";

    var container = document.getElementById("container");
    while(container.hasChildNodes()) {
        container.removeChild(container.firstChild);
    }

    container.appendChild(createDivWithInput("姓名", "name", "false", ""));
    container.appendChild(createDivWithSelection("性别", "sexes", "", new Array("男","女")));
    container.appendChild(createDivWithInput("出生年份", "birth_year", "false", ""));
    container.appendChild(createButton("添加", "0px", insertteacher));
}

//添加课程前的准备工作
function addcourse() {
    var title = document.getElementById("title");
    title.innerHTML = "添加课程";
    var ajaxObj = new XMLHttpRequest();
    ajaxObj.open('get', "http://localhost:6060/admin/course/insert");
    ajaxObj.send();
    ajaxObj.onreadystatechange = function () {
        if (ajaxObj.readyState == 4 && ajaxObj.status == 200) {
            console.log('数据返回成功');
            console.log(ajaxObj.responseText);

            var last=ajaxObj.responseText; //将JSON对象转化为JSON字符
            var obj = JSON.parse(last);
            var container = document.getElementById("container");
            while(container.hasChildNodes()) {
                container.removeChild(container.firstChild);
            }

            var teacher_list = new Array();
            for (var i = 0; i < obj.teachers.length; i ++) {
                teacher_list[i] = obj.teachers[i].teacher_id + "/" + obj.teachers[i].teacher_name;
            }
            
            container.appendChild(createDivWithInput("课程名称", "name", "false", ""));
            container.appendChild(createDivWithInput("开课学年", "year", "false", ""));
            container.appendChild(createDivWithSelection("开课学期", "semester", "", new Array("春","秋")));
            container.appendChild(createDivWithInput("学分", "credit", "false", ""));
            container.appendChild(createDivWithSelection("授课教师id", "teachers", "", teacher_list));
            container.appendChild(createButton("添加", "0px", insertcourse));
        }
        else if(ajaxObj.readyState == 4 && ajaxObj.status == 404) {
            var last=ajaxObj.responseText; //将JSON对象转化为JSON字符
            var obj = JSON.parse(last);
            alert("添加失败: " + obj.error);
        }
    }
}

//添加专业前的准备工作
function addmajor() {
    var title = document.getElementById("title");
    title.innerHTML = "添加专业";

    var container = document.getElementById("container");
    while(container.hasChildNodes()) {
        container.removeChild(container.firstChild);
    }

    container.appendChild(createDivWithInput("专业名称", "name", "false", ""));
    container.appendChild(createButton("添加", "0px", insertmajor));
}

//添加专业选课前的准备工作
function addmajorcourse() {
    var title = document.getElementById("title");
    title.innerHTML = "添加专业选课";
    var ajaxObj = new XMLHttpRequest();
    ajaxObj.open('get', "http://localhost:6060/admin/major_course/insert");
    ajaxObj.send();
    ajaxObj.onreadystatechange = function () {
        if (ajaxObj.readyState == 4 && ajaxObj.status == 200) {
            console.log('数据返回成功');
            console.log(ajaxObj.responseText);

            var last=ajaxObj.responseText; //将JSON对象转化为JSON字符
            var obj = JSON.parse(last);
            var container = document.getElementById("container");
            while(container.hasChildNodes()) {
                container.removeChild(container.firstChild);
            }

            major_list = new Array();
            for (var i = 0; i < obj.majors.length; i ++) {
                major_list[i] = obj.majors[i].major_id + "/" + obj.majors[i].major_name;
            }
            course_list = new Array();
            for (var i = 0; i < obj.courses.length; i ++) {
                course_list[i] = obj.courses[i].course_id + "/" + obj.courses[i].course_name;
            }
            container.appendChild(createDivWithSelection("专业编号/名称", "major", "false", major_list));
            container.appendChild(createDivWithSelection("课程编号/名称", "course", "false", course_list));
            container.appendChild(createButton("添加", "0px", insertmajorcourse));
        }
        else if(ajaxObj.readyState == 4 && ajaxObj.status == 404) {
            var last=ajaxObj.responseText; //将JSON对象转化为JSON字符
            var obj = JSON.parse(last);
            alert("添加失败: " + obj.error);
        }
    }
}