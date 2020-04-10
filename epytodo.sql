DROP DATABASE IF EXISTS epytodo;
CREATE DATABASE epytodo;

USE epytodo;
CREATE TABLE user
(
    user_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL
);

CREATE TABLE task
(
    task_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    title VARCHAR(10) NOT NULL,
    `begin` TIMESTAMP DEFAULT UTC_TIMESTAMP(),
    `end` TIMESTAMP,
    status ENUM("not started", "in progress", "done") DEFAULT "not started"
);

CREATE TABLE user_has_task
(
    fk_user_id VARCHAR(50) NOT NULL,
    fk_task_id VARCHAR(50) NOT NULL
);