CREATE TABLE User (
    username        VARCHAR(255),
    id              INTEGER NOT NULL,
    departmentCode  INTEGER,
    PRIMARY KEY (id)
);

CREATE TABLE Post (
    url             VARCHAR(255),
    title           VARCHAR(255),
    createdAt       TIMESTAMP,
    id              INTEGER NOT NULL,
    userId          INTEGER NOT NULL,
    titleId         INTEGER,
    courseId        INTEGER,
    PRIMARY KEY (id)
);

CREATE TABLE Department (
    departmentTitle VARCHAR(255),
    departmentCode  INTEGER NOT NULL,
    PRIMARY KEY (departmentCode)
);

CREATE TABLE Course (
    courseTitle     VARCHAR(255),
    courseCode      VARCHAR(50),
    courseId        INTEGER NOT NULL,
    departmentCode  INTEGER NOT NULL,
    PRIMARY KEY (courseId)
);

CREATE TABLE Student (
    id              INTEGER NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE Admin (
    id              INTEGER NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE Developer (
    id              INTEGER NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE Category (
    title           VARCHAR(255) NOT NULL,
    courseId        INTEGER NOT NULL,
    PRIMARY KEY (title, courseId)
);

CREATE TABLE Reactions (
    title           VARCHAR(255),
    userId          INTEGER NOT NULL,
    postId          INTEGER NOT NULL,
    PRIMARY KEY (userId, postId)
);

CREATE TABLE Fullname (
    firstName       VARCHAR(255) NOT NULL,
    lastName        VARCHAR(255) NOT NULL,
    userId          INTEGER NOT NULL,
    PRIMARY KEY (firstName, lastName, userId)
);

ALTER TABLE User ADD FOREIGN KEY (departmentCode) REFERENCES Department (departmentCode) ON DELETE SET NULL ON UPDATE CASCADE;
ALTER TABLE Post ADD FOREIGN KEY (userId) REFERENCES User (id) ON DELETE SET NULL ON UPDATE CASCADE;
ALTER TABLE Post ADD FOREIGN KEY (titleId, courseId) REFERENCES Category (title, courseId) ON DELETE SET NULL ON UPDATE CASCADE;
ALTER TABLE Course ADD FOREIGN KEY (departmentCode) REFERENCES Department (departmentCode) ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE Student ADD FOREIGN KEY (id) REFERENCES User (id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE Admin ADD FOREIGN KEY (id) REFERENCES User (id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE Developer ADD FOREIGN KEY (id) REFERENCES User (id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE Category ADD FOREIGN KEY (courseId) REFERENCES Course (courseId) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE Reactions ADD FOREIGN KEY (userId) REFERENCES User (id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE Reactions ADD FOREIGN KEY (postId) REFERENCES Post (id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE Fullname ADD FOREIGN KEY (userId) REFERENCES User (id) ON DELETE CASCADE ON UPDATE CASCADE;
