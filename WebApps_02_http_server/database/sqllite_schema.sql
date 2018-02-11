drop table if exists meetings;
create table meetings (
  id integer primary key uid,
  title text not null,
  date text not null
);