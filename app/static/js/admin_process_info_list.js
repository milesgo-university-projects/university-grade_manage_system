function process_student_info() {
    var ajaxObj = new XMLHttpRequest();
    ajaxObj.open('get', 'http://localhost:6060/admin/student/select');
    ajaxObj.send();
    ajaxObj.onreadystatechange = function () {
        if (ajaxObj.readyState == 4 && ajaxObj.status == 200) {
            console.log('数据返回成功');
            console.log(ajaxObj.responseText);
            var last=ajaxObj.responseText; //将JSON对象转化为JSON字符
            var obj = JSON.parse(last);
            var students = obj.students;

            var tablecontainer = document.getElementById("tablecontainer");
            while(tablecontainer.hasChildNodes()) {
                tablecontainer.removeChild(tablecontainer.firstChild);
            }

            var table=document.createElement("table");
            table.style.width = "1000px";
            table.style.borderCollapse = "collapse";
            table.border = 1;
            table.className = "table table-striped table-bordered table-hover";

            var thead=document.createElement("thead");

            var row = document.createElement('tr');
            var student_id = document.createElement('td');
            var student_name = document.createElement('td');
            var sex = document.createElement('td');
            var birth_year = document.createElement('td');
            var province = document.createElement('td');
            var major_name = document.createElement('td');
            var credits = document.createElement('td');
            var number_of_courses = document.createElement('td');
            var average_grade = document.createElement('td');
            var detail = document.createElement("td");

            student_id.innerHTML = "学生编号";
            student_name.innerHTML = "学生姓名";
            sex.innerHTML = "性别";
            birth_year.innerHTML = "出生年份";
            province.innerHTML = "籍贯";
            major_name.innerHTML = "专业编号/名称";
            credits.innerHTML = "已获学分";
            number_of_courses.innerHTML = "课程数";
            average_grade.innerHTML = "加权平均分";
            detail.innerHTML = "查看详情";

            row.appendChild(student_id);
            row.appendChild(student_name);
            row.appendChild(sex);
            row.appendChild(birth_year);
            row.appendChild(province);
            row.appendChild(major_name);
            row.appendChild(credits);
            row.appendChild(number_of_courses);
            row.appendChild(average_grade);
            row.appendChild(detail);

            thead.appendChild(row);
            table.appendChild(thead);

            var tbody = document.createElement('tbody');

            for (var i = 0; i < students.length; i++) {
                var row = document.createElement('tr');
                
                var student_id = document.createElement('td');
                var student_name = document.createElement('td');
                var sex = document.createElement('td');
                var birth_year = document.createElement('td');
                var province = document.createElement('td');
                var major_name = document.createElement('td');
                var credits = document.createElement('td');
                var number_of_courses = document.createElement('td');
                var average_grade = document.createElement('td');
                var detail = document.createElement('td');

                student_id.innerHTML = students[i].student_id;
                student_name.innerHTML = students[i].student_name;
                sex.innerHTML = students[i].sex;
                birth_year.innerHTML = students[i].birth_year;
                province.innerHTML = students[i].province;
                major_name.innerHTML = students[i].major_id + "/" + students[i].major_name;
                credits.innerHTML = students[i].credits;
                number_of_courses.innerHTML = students[i].number_of_courses;
                average_grade.innerHTML = students[i].average_grade;
                detail.innerHTML = "查看详情";
                detail.style = "cursor:pointer";
                
                detail.setAttribute('row',i.toString);
                detail.setAttribute("student_id",students[i].student_id);
                
                detail.onclick = function() {
                    localStorage.setItem("student_id", this.getAttribute("student_id"));
                    localStorage.setItem("current_type", "change_student");
                    window.location.href = "Admin_Detail.html";
                }

                row.appendChild(student_id);
                row.appendChild(student_name);
                row.appendChild(sex);
                row.appendChild(birth_year);
                row.appendChild(province);
                row.appendChild(major_name);
                row.appendChild(credits);
                row.appendChild(number_of_courses);
                row.appendChild(average_grade);
                row.appendChild(detail);
                tbody.appendChild(row);
            }
            table.appendChild(tbody);
            tablecontainer.appendChild(table); 
        }
        else if(ajaxObj.readyState == 4 && ajaxObj.status == 404) {
            var last=ajaxObj.responseText; //将JSON对象转化为JSON字符
            var obj = JSON.parse(last);
            alert(obj.error);
        }
    }
}

function process_teacher_info() {
    var ajaxObj = new XMLHttpRequest();
    ajaxObj.open('get', 'http://localhost:6060/admin/teacher/select');
    ajaxObj.send();
    ajaxObj.onreadystatechange = function () {
        if (ajaxObj.readyState == 4 && ajaxObj.status == 200) {
            console.log('数据返回成功');
            console.log(ajaxObj.responseText);
            var last=ajaxObj.responseText; //将JSON对象转化为JSON字符
            var obj = JSON.parse(last);
            var teachers = obj.teachers;

            var tablecontainer = document.getElementById("tablecontainer");
            while(tablecontainer.hasChildNodes()) {
                tablecontainer.removeChild(tablecontainer.firstChild);
            }

            var table=document.createElement("table");
            table.style.width = "790px";
            table.style.borderCollapse = "collapse";
            table.border = 1;
            table.className = "table table-striped table-bordered table-hover";

            var thead=document.createElement("thead");

            var row = document.createElement('tr');
            var teacher_id = document.createElement('td');
            var teacher_name = document.createElement('td');
            var sex = document.createElement('td');
            var birth_year = document.createElement('td');
            var number_of_courses = document.createElement('td');
            var detail = document.createElement("td");

            teacher_id.innerHTML = "教师编号";
            teacher_name.innerHTML = "姓名";
            sex.innerHTML = "性别";
            birth_year.innerHTML = "出生年份";
            number_of_courses.innerHTML = "课程数量";
            detail.innerHTML = "查看详情";

            row.appendChild(teacher_id);
            row.appendChild(teacher_name);
            row.appendChild(sex);
            row.appendChild(birth_year);
            row.appendChild(number_of_courses);
            row.appendChild(detail);

            thead.appendChild(row);
            table.appendChild(thead);

            var tbody = document.createElement('tbody');

            for (var i = 0; i < teachers.length; i++) {
                var row = document.createElement('tr');
                var teacher_id = document.createElement('td');
                var teacher_name = document.createElement('td');
                var sex = document.createElement('td');
                var birth_year = document.createElement('td');
                var number_of_courses = document.createElement('td');
                var detail = document.createElement("td");

                teacher_id.innerHTML = teachers[i].teacher_id;
                teacher_name.innerHTML = teachers[i].teacher_name;
                sex.innerHTML = teachers[i].sex;
                birth_year.innerHTML = teachers[i].birth_year;
                number_of_courses.innerHTML = teachers[i].number_of_courses;
                detail.innerHTML = "查看详情";
                detail.style = "cursor:pointer";
                
                detail.setAttribute('row',i.toString);
                detail.setAttribute("teacher_id",teachers[i].teacher_id);
                
                detail.onclick = function() {
                    localStorage.setItem("teacher_id", this.getAttribute("teacher_id"));
                    localStorage.setItem("current_type", "change_teacher");
                    window.location.href = "Admin_Detail.html";
                }

                row.appendChild(teacher_id);
                row.appendChild(teacher_name);
                row.appendChild(sex);
                row.appendChild(birth_year);
                row.appendChild(number_of_courses);
                row.appendChild(detail);
                tbody.appendChild(row);
            }
            table.appendChild(tbody);
            tablecontainer.appendChild(table); 
        }
        else if(ajaxObj.readyState == 4 && ajaxObj.status == 404) {
            var last=ajaxObj.responseText; //将JSON对象转化为JSON字符
            var obj = JSON.parse(last);
            alert(obj.error);
        }
    }
}

function process_course_info() {
    var ajaxObj = new XMLHttpRequest();
    ajaxObj.open('get', 'http://localhost:6060/admin/course/select');
    ajaxObj.send();
    ajaxObj.onreadystatechange = function () {
        if (ajaxObj.readyState == 4 && ajaxObj.status == 200) {
            console.log('数据返回成功');
            console.log(ajaxObj.responseText);
            var last=ajaxObj.responseText; //将JSON对象转化为JSON字符
            var obj = JSON.parse(last);
            var courses = obj.courses;

            var tablecontainer = document.getElementById("tablecontainer");
            while(tablecontainer.hasChildNodes()) {
                tablecontainer.removeChild(tablecontainer.firstChild);
            }

            var table=document.createElement("table");
            table.style.width = "790px";
            table.style.borderCollapse = "collapse";
            table.border = 1;
            table.className = "table table-striped table-bordered table-hover";

            var thead=document.createElement("thead");

            var row = document.createElement('tr');
            var course_id = document.createElement('td');
            var course_name = document.createElement('td');
            var year = document.createElement('td');
            var semester = document.createElement('td');
            var teacher_id = document.createElement('td');
            var credit = document.createElement('td');
            var number_of_students = document.createElement('td');
            var average_grade = document.createElement('td');
            var detail = document.createElement("td");

            course_id.innerHTML = "课程编号";
            course_name.innerHTML = "名称";
            year.innerHTML = "年份";
            semester.innerHTML = "学期";
            teacher_id.innerHTML = "教师编号/姓名";
            credit.innerHTML = "学分";
            number_of_students.innerHTML = "学生数量";
            average_grade.innerHTML = "平均成绩";
            detail.innerHTML = "查看详情";

            row.appendChild(course_id);
            row.appendChild(course_name);
            row.appendChild(year);
            row.appendChild(semester);
            row.appendChild(teacher_id);
            row.appendChild(credit);
            row.appendChild(number_of_students);
            row.appendChild(average_grade);
            row.appendChild(detail);

            thead.appendChild(row);
            table.appendChild(thead);

            var tbody = document.createElement('tbody');

            for (var i = 0; i < courses.length; i++) {
                var row = document.createElement('tr');
                var course_id = document.createElement('td');
                var course_name = document.createElement('td');
                var year = document.createElement('td');
                var semester = document.createElement('td');
                var teacher_id = document.createElement('td');
                var credit = document.createElement('td');
                var number_of_students = document.createElement('td');
                var average_grade = document.createElement('td');
                var detail = document.createElement("td");

                course_id.innerHTML = courses[i].course_id;
                course_name.innerHTML = courses[i].course_name;
                year.innerHTML = courses[i].year;
                semester.innerHTML = courses[i].semester;
                teacher_id.innerHTML = courses[i].teacher_id + "/" + courses[i].teacher_name;
                credit.innerHTML = courses[i].credit;
                number_of_students.innerHTML = courses[i].number_of_students;
                average_grade.innerHTML = courses[i].average_grade;
                detail.innerHTML = "查看详情";
                detail.style = "cursor:pointer";
                
                detail.setAttribute('row',i.toString);
                detail.setAttribute("course_id",courses[i].course_id);
                
                detail.onclick = function() {
                    localStorage.setItem("course_id", this.getAttribute("course_id"));
                    localStorage.setItem("current_type", "change_course");
                    window.location.href = "Admin_Detail.html";
                }
                
                row.appendChild(course_id);
                row.appendChild(course_name);
                row.appendChild(year);
                row.appendChild(semester);
                row.appendChild(teacher_id);
                row.appendChild(credit);
                row.appendChild(number_of_students);
                row.appendChild(average_grade);
                row.appendChild(detail);
                tbody.appendChild(row);
            }
            table.appendChild(tbody);
            tablecontainer.appendChild(table); 
        }
        else if(ajaxObj.readyState == 4 && ajaxObj.status == 404) {
            var last=ajaxObj.responseText; //将JSON对象转化为JSON字符
            var obj = JSON.parse(last);
            alert(obj.error);
        }
    }
}

function process_major_info() {
    var ajaxObj = new XMLHttpRequest();
    ajaxObj.open('get', 'http://localhost:6060/admin/major/select');
    ajaxObj.send();
    ajaxObj.onreadystatechange = function () {
        if (ajaxObj.readyState == 4 && ajaxObj.status == 200) {
            console.log('数据返回成功');
            console.log(ajaxObj.responseText);
            var last=ajaxObj.responseText; //将JSON对象转化为JSON字符
            var obj = JSON.parse(last);
            var majors = obj.majors;

            var tablecontainer = document.getElementById("tablecontainer");
            while(tablecontainer.hasChildNodes()) {
                tablecontainer.removeChild(tablecontainer.firstChild);
            }

            var table=document.createElement("table");
            table.style.width = "790px";
            table.style.borderCollapse = "collapse";
            table.border = 1;
            table.className = "table table-striped table-bordered table-hover";

            var thead=document.createElement("thead");

            var row = document.createElement('tr');
            var major_id = document.createElement('td');
            var major_name = document.createElement('td');
            var number_of_students = document.createElement('td');
            var detail = document.createElement("td");

            major_id.innerHTML = "专业编号";
            major_name.innerHTML = "专业名称";
            number_of_students.innerHTML = "学生数量";
            detail.innerHTML = "查看详情";

            row.appendChild(major_id);
            row.appendChild(major_name);
            row.appendChild(number_of_students);
            row.appendChild(detail);

            thead.appendChild(row);
            table.appendChild(thead);

            var tbody = document.createElement('tbody');

            for (var i = 0; i < majors.length; i++) {
                var row = document.createElement('tr');
                
                var major_id = document.createElement('td');
                var major_name = document.createElement('td');
                var number_of_students = document.createElement('td');
                var detail = document.createElement('td');

                major_id.innerHTML = majors[i].major_id;
                major_name.innerHTML = majors[i].major_name;
                number_of_students.innerHTML = majors[i].number_of_students;
                detail.innerHTML = "查看详情";
                detail.style = "cursor:pointer";
                
                detail.setAttribute('row',i.toString);
                detail.setAttribute("major_id",majors[i].major_id);
                
                detail.onclick = function() {
                    localStorage.setItem("major_id", this.getAttribute("major_id"));
                    localStorage.setItem("current_type", "change_major");
                    window.location.href = "Admin_Detail.html";
                }

                row.appendChild(major_id);
                row.appendChild(major_name);
                row.appendChild(number_of_students);
                row.appendChild(detail);
                tbody.appendChild(row);
            }
            table.appendChild(tbody);
            tablecontainer.appendChild(table); 
        }
        else if(ajaxObj.readyState == 4 && ajaxObj.status == 404) {
            var last=ajaxObj.responseText; //将JSON对象转化为JSON字符
            var obj = JSON.parse(last);
            alert(obj.error);
        }
    }
}

function process_major_course_info() {
    var ajaxObj = new XMLHttpRequest();
    ajaxObj.open('get', 'http://localhost:6060/admin/major_course/select');
    ajaxObj.send();
    ajaxObj.onreadystatechange = function () {
        if (ajaxObj.readyState == 4 && ajaxObj.status == 200) {
            console.log('数据返回成功');
            console.log(ajaxObj.responseText);
            var last=ajaxObj.responseText; //将JSON对象转化为JSON字符
            var obj = JSON.parse(last);
            var major_courses = obj.major_courses;

            var tablecontainer = document.getElementById("tablecontainer");
            while(tablecontainer.hasChildNodes()) {
                tablecontainer.removeChild(tablecontainer.firstChild);
            }

            var table=document.createElement("table");
            table.style.width = "790px";
            table.style.borderCollapse = "collapse";
            table.border = 1;
            table.className = "table table-striped table-bordered table-hover";

            var thead=document.createElement("thead");

            var row = document.createElement('tr');
            var major_id = document.createElement('td');
            var major_name = document.createElement('td');
            var course_id = document.createElement('td');
            var course_name = document.createElement('td');
            var detail = document.createElement("td");

            major_id.innerHTML = "专业编号";
            major_name.innerHTML = "专业名称";
            course_id.innerHTML = "课程编号";
            course_name.innerHTML = "课程名称"
            detail.innerHTML = "查看详情";

            row.appendChild(major_id);
            row.appendChild(major_name);
            row.appendChild(course_id);
            row.appendChild(course_name);
            row.appendChild(detail);

            thead.appendChild(row);
            table.appendChild(thead);

            var tbody = document.createElement('tbody');

            for (var i = 0; i < major_courses.length; i++) {
                var row = document.createElement('tr');
                
                var major_id = document.createElement('td');
                var major_name = document.createElement('td');
                var course_id = document.createElement('td');
                var course_name = document.createElement('td');
                var detail = document.createElement("td");

                major_id.innerHTML = major_courses[i].major_id;
                major_name.innerHTML = major_courses[i].major_name;
                course_id.innerHTML = major_courses[i].course_id;
                course_name.innerHTML = major_courses[i].course_name;
                detail.innerHTML = "查看详情";
                detail.style = "cursor:pointer";
                
                detail.setAttribute('row',i.toString);
                detail.setAttribute("major_id", major_courses[i].major_id);
                detail.setAttribute("course_id", major_courses[i].course_id);
                detail.onclick = function() {
                    localStorage.setItem("major_id", this.getAttribute("major_id"));
                    localStorage.setItem("course_id", this.getAttribute("course_id"));
                    localStorage.setItem("current_type", "change_major_course");
                    window.location.href = "Admin_Detail.html";
                }

                row.appendChild(major_id);
                row.appendChild(major_name);
                row.appendChild(course_id);
                row.appendChild(course_name);
                row.appendChild(detail);
                tbody.appendChild(row);
            }
            table.appendChild(tbody);
            tablecontainer.appendChild(table); 
        }
        else if(ajaxObj.readyState == 4 && ajaxObj.status == 404) {
            var last=ajaxObj.responseText; //将JSON对象转化为JSON字符
            var obj = JSON.parse(last);
            alert(obj.error);
        }
    }
}