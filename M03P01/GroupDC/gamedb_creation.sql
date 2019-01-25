DROP DATABASE IF EXISTS gamedb;
CREATE DATABASE gamedb;

USE gamedb;

CREATE TABLE `classes` (
    class_id        INT                         PRIMARY KEY AUTO_INCREMENT,
    name            VARCHAR(30)    NOT NULL                 UNIQUE
);

CREATE TABLE `item_types` (
    type_id        INT                          PRIMARY KEY AUTO_INCREMENT,
    name           VARCHAR(30)     NOT NULL
);

CREATE TABLE `items` (
    item_id        INT                          PRIMARY KEY AUTO_INCREMENT,
    type_id        INT             NOT NULL     REFERENCES item_types(type_id),
    `name`         VARCHAR(30)     NOT NULL,
    `description`  VARCHAR(200), 
    cost           INT             NOT NULL     DEFAULT 0
);

CREATE TABLE `characters` (
    character_id    INT                         PRIMARY KEY AUTO_INCREMENT,
    player_id       INT         NOT NULL        REFERENCES player(player_id),
    class_id        INT         NOT NULL        REFERENCES classes(class_id),
    `name`          VARCHAR(30) NOT NULL,
    `level`         INT         NOT NULL        DEFAULT 0,
    `experience`    INT         NOT NULL        DEFAULT 0,
    gold            INT         NOT NULL        DEFAULT 0
);

CREATE TABLE `inventory` (
    item_id         INT         NOT NULL        REFERENCES items(item_id),
    character_id    INT         NOT NULL        REFERENCES characters(character_id),
    quantity        INT                         DEFAULT 0,
    CONSTRAINT item_character_uq UNIQUE (item_id, character_id)
);

INSERT INTO classes VALUES 
    (DEFAULT, 'druid'),
    (DEFAULT, 'hunter'),
    (DEFAULT, 'mage'),
    (DEFAULT, 'priest'),
    (DEFAULT, 'rogue'),
    (DEFAULT, 'warrior');
    
INSERT INTO item_types VALUES 
    (DEFAULT, 'armor'),
    (DEFAULT, 'bow'),
    (DEFAULT, 'sword'),
    (DEFAULT, 'shield'),
    (DEFAULT, 'staff'),
    (DEFAULT, 'food');

INSERT INTO items (type_id, `name`, `description`, cost) VALUES 
    (1, 'helm', 'An iron helm to protect your head', 200),
    (1, 'shoulders', 'Spoulders of might', 532),
    (1, 'boots', 'The boots of switfness were merged by the gods', 335),
    (2, 'arcanite reaper', 'The sword of giants', 1400),
    (2, 'scaleshard', 'Here is whence true strength comes. From deep places... within the world, and within oneself.', 193),
    (2, 'ice', 'Winter is Coming.', 345),
    (2, 'oathkeeper', 'A red and blue short sword.', 1764),
    (3, 'truthguard', 'A single ray of sunlight pierced the storm clouds and whispered over Truthguard\'s surface.', 650),
    (4, 'gada', 'Avatar of shiva', 450),
    (4, 'atiesh', 'Greater staff of the guardian', 566),
    (5, 'cake', 'Delicious chocolate cake!', 142),
    (5, 'roasted boar', 'Slow roasted boar over a fire spit.', 557),
    (5, 'fried calamari', 'Did you check the expiration date before eating it?', 862),
    (5, 'water', 'Fresh water.', 490);
