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
    `begin` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `end` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM("not started", "in progress", "done") DEFAULT "not started"
);

CREATE TABLE user_has_task
(
    id INT AUTO_INCREMENT PRIMARY KEY,
    fk_user_id INT(50) NOT NULL,
    fk_task_id INT(50) NOT NULL
);

ALTER TABLE `user_has_task`
  ADD CONSTRAINT fk_task_id FOREIGN KEY (fk_task_id) REFERENCES task (task_id),
  ADD CONSTRAINT fk_user_id FOREIGN KEY (fk_user_id) REFERENCES user (user_id);
COMMIT;