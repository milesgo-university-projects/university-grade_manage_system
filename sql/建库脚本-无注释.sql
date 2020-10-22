delimiter //

create database grade_manage_system;//
use grade_manage_system


create table major(major_id char(3) primary key, major_name varchar(20) not null unique);//


create table student(student_id char(10) primary key, student_name varchar(20) not null, sex char(2), 
                     birth_year char(4), province varchar(20), enter_year char(4) not null, 
                     major_id char(3) not null, password varchar(128) not null);//
alter table student add foreign key (major_id) references major (major_id) on delete cascade;//


create table teacher(teacher_id char(5) primary key, teacher_name varchar(20) not null, sex char(2), 
                     birth_year char(4), password varchar(128) not null);//


create table course(course_id char(5) primary key, course_name varchar(20) not null, 
                    year char(4) not null, semester char(2) not null, teacher_id char(5) not null, 
                    credit tinyint unsigned not null);//
alter table course add foreign key (teacher_id) references teacher (teacher_id) on delete cascade;//


create table major_course(major_id char(3), course_id char(5));//
alter table major_course add primary key (major_id, course_id);//
alter table major_course add foreign key (major_id) references major (major_id) on delete cascade;//
alter table major_course add foreign key (course_id) references course (course_id) on delete cascade;//


create table student_course(student_id char(10), course_id char(5), grade tinyint unsigned);//
alter table student_course add primary key (student_id, course_id);//


create trigger trigger_insert_1 after insert on major_course for each row
begin
    insert into student_course (
        select student_id, new.course_id, null
        from student
        where major_id = new.major_id
    );
end//

create trigger trigger_delete_1 after delete on major_course for each row
begin
    delete from student_course
    where student_id in (
        select student_id
        from student
        where major_id = old.major_id
    ) and course_id = old.course_id;
end//

create trigger trigger_insert_2 after insert on student for each row
begin
    insert into student_course (
        select new.student_id, course_id, null
        from major_course
        where major_id = new.major_id
    );
end//

create trigger tigger_delete_2 after delete on student for each row
begin
    delete from student_course
    where course_id in (
        select course_id
        from major_course
        where major_id = old.major_id
    ) and student_id = old.student_id;
end//

delimiter ;
