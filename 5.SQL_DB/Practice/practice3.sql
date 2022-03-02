show Databases;
use mydata;
show tables;
desc my_table_new;


CREATE TABLE mytable(
	ID INT unsigned NOT NULL auto_increment,
    name varchar(20) not null,
    model_num varchar(10) not null,
    model_type varchar(10) not null,
    primary key(ID)
);
show tables;
desc mytable;


-- 생성된 테이블에 값 추가
INSERT INTO mytable VALUES(1, 'i7', '7700', 'Kaby Lake');
SELECT * FROM mytable;

-- 특정 field에 추가 ( ID는 auto_increment 이기때문에 안넣어줘도 위의 1번에서 순차적으로 인덱스값 하나씩 더해짐 )
INSERT INTO mytable (name, model_num, model_type) VALUES('i7', '7700K', 'Kaby Lake');
SELECT * FROM mytable;

ALTER TABLE mytable MODIFY COLUMN model_type VARCHAR(30) NOT NULL;
desc mytable;

INSERT INTO mytable (name, model_num, model_type) VALUES('i5', '9600K', 'Coffee Lake Refresh');
INSERT INTO mytable (name, model_num, model_type) VALUES('i5', '9400F', 'Coffee Lake Refresh');
INSERT INTO mytable (name, model_num, model_type) VALUES('i7', '9700K', 'Coffee Lake Refresh');
INSERT INTO mytable (name, model_num, model_type) VALUES('i7', '8700', 'Coffee Lake');
INSERT INTO mytable (name, model_num, model_type) VALUES('i5', '8500', 'Coffee Lake');

SELECT * FROM mytable;