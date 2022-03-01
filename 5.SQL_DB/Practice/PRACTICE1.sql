-- 데이터베이스 생성
create  database mydata;

-- 데이터베이스 보는법
show databases;

-- 해당 데이터베이스 사용
USE mydata;

-- 테이블 생성
CREATE TABLE myproduct(
	-- INT UNSINGED 사용하면 0~255 정수를 사용, 안쓰고 INT쓰면 -128 ~ 127
    -- NOT NULL 사용하면 해당 컬럼 데이터 값이 할당되지 않는 경우에 에러뜨게만듬
    -- AUTO_INCREMENT 사용하면, 지금저장되어있는 KEY값에서 인덱스 1씩 증가해서 들어감(UNIQUE 데이터에서 UNIQUE값을 가지게하려고 사용함)

    MYKEY INT UNSIGNED NOT NULL AUTO_INCREMENT,
    PRODUCTID TEXT,
    TITLE TEXT,
    ORI_PRICE INT,
    DISCOUNT_PRICE INT,
    DISCOUNT_PERCENT INT,
    DELEVERY TEXT,
    PRIMARY KEY(MYKEY)
);

-- 테이블 보기
SHOW TABLES;

-- 해당 테이블 구조 보기
DESC myproduct;

/* 연습 DB 생성 customer_db */
CREATE DATABASE customer_db;
SHOW DATABASES;
USE customer_db;

CREATE TABLE practice1(
	NO INT UNSIGNED NOT NULL AUTO_INCREMENT,
    NAME CHAR(20),
    AGE TINYINT,
    PHONE VARCHAR(20),
    EMAIL VARCHAR(30),
    ADDRESS VARCHAR(50),
    PRIMARY KEY(NO)
);

SHOW TABLES;
DESC practice1;

-- 3.2.3 테이블 구조 수정
SHOW DATABASES;
USE MYDATA;
SHOW TABLES;
DESC MYPRODUCT;
CREATE TABLE customer_db(
	NO INT UNSIGNED NOT NULL AUTO_INCREMENT,
    NAME CHAR(20),
    AGE TINYINT,
    PHONE VARCHAR(20),
    EMAIL VARCHAR(30),
    ADDRESS VARCHAR(50),
    PRIMARY KEY(NO)
);
SHOW TABLES;
DESC customer_db;

/*
1. 테이블에 새로운 컬럼 추가 ALTER TABLE PRACTICE1 ADD COLUMN model_type varchar(10) NOT NULL;
2. 테이블 컬럼 타입 변경
3. 테이블 컬럼 이름 변경
4. 테이블 컬럼 삭제
*/
-- 1. 테이블에 새로운 컬럼 추가
ALTER TABLE customer_db ADD COLUMN model_type VARCHAR(10) NOT NULL;
DESC customer_db;

-- 2. 테이블 컬럼 타입 변경
ALTER TABLE customer_db MODIFY COLUMN NAME VARCHAR(20) NOT NULL;
DESC customer_db;

-- 3. 테이블 컬럼 이름 변경
ALTER TABLE customer_db CHANGE COLUMN NAME MODEL_NAME VARCHAR(10) NOT NULL;
DESC customer_db;

-- 4. 테이블 컬럼 삭제
ALTER TABLE customer_db DROP COLUMN AGE;
DESC customer_db;














