-- 4.1.2 데이터 읽기(검색)
show databases;
use mydata;
show tables;

-- 전체 데이터 읽기
select * from mytable;


-- 필요한 컬럼명만 읽어오기
select name from mytable;
select name, model_num from mytable;

-- alias 사용
SELECT name as cup_name FROM mytable;
SELECT name as cup_name, model_num as CPU_NUM FROM mytable;

-- 데이터 row order by로 읽기
SELECT *
FROM mytable 
order by ID desc;

-- where 이용
SELECT *
FROM mytable
WHERE id <= 3;

-- LIKE 이용 일부분 찾기
-- LIKE '시작이%' , LIKE '%들어가는거전부%', LIKE '뒤에언더바갯수___'
SELECT *
FROM mytable
WHERE model_type LIKE '%by%';

SELECT *
FROM mytable
WHERE model_type LIKE 'Kaby_____';

SELECT *
FROM mytable
WHERE model_type LIKE 'Kaby%';

SELECT *
FROM mytable
WHERE model_type LIKE '_____Lake';


-- limit 이용 : 상위 N개만 보기
SELECT *
FROM mytable
limit 3;

SELECT *
FROM mytable
limit 3, 3; -- 3개 이후에 3개 보기

-- 조건 조합
SELECT id, name FROM mytable
where id < 4 AND name LIKE '%i%'
order by name desc
limit 2;

-- 실습
select * from mytable where model_num like '7700%';
select * from mytable where name = 'i7';
select * from mytable where model_type like '%Kaby Lake%' limit 1;

desc mytable;
select * from mytable;

-- 데이터 수정하기 UPDATE xxxx SET
UPDATE mytable SET name = 'i3' where id = 3;
select * from mytable;

UPDATE mytable SET name = 'i3', model_num = '5500K' where id = 3;
select * from mytable;

-- 특정 row 데이터 삭제하기 DELETE WHERE
DELETE FROM mytable WHERE id = 1;
select * from mytable;

-- 실습 - 테이블 수정, 데이터 수정, 검색
show databases;
use mydata;
show tables;

-- 테이블 변경
ALTER TABLE mytable ADD COLUMN lowest_price INT UNSIGNED;
DESC mytable;
SELECT * FROM mytable;
UPDATE mytable SET lowest_price = 176660 WHERE ID = 2;
UPDATE mytable SET lowest_price = 468090 WHERE ID = 3;
UPDATE mytable SET lowest_price = 357520 WHERE ID = 4;
UPDATE mytable SET lowest_price = 252130 WHERE ID = 5;
UPDATE mytable SET lowest_price = 369800 WHERE ID = 6;

SELECT name, model_num
FROM mytable
WHERE lowest_price <= 300000;

SELECT name, model_num
FROM mytable
WHERE lowest_price >= 400000;











