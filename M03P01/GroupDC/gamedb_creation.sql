DROP DATABASE IF EXISTS gamedb;
CREATE DATABASE gamedb;

-- create a user and grant privileges to that user
CREATE USER IF NOT EXISTS 'gameadmin'@'localhost' IDENTIFIED BY 'sesame';
GRANT ALL PRIVILEGES ON gamedb.* TO 'gameadmin'@'localhost'
	WITH GRANT OPTION;

USE gamedb;

CREATE TABLE `classes` (
	class_id			INT			 			PRIMARY KEY	AUTO_INCREMENT,
	name				VARCHAR(30)	NOT NULL			UNIQUE
);

CREATE TABLE `item_types` (
	type_id	INT			 					PRIMARY KEY	AUTO_INCREMENT,
	name		VARCHAR(30)			NOT NULL			UNIQUE
);

CREATE TABLE `items` (
	item_id			INT			 			PRIMARY KEY 	AUTO_INCREMENT,
    type_id			INT						NOT NULL,
	`name`				VARCHAR(30)	NOT NULL			UNIQUE,
    `description`	VARCHAR(200), 
	cost					INT 						NOT NULL		DEFAULT 0,

    CONSTRAINT item_fk_item_types FOREIGN KEY (type_id) REFERENCES item_types(type_id)
);

CREATE TABLE `quest_types` (
	type_id	INT			 					PRIMARY KEY	AUTO_INCREMENT,
	name		VARCHAR(30)			NOT NULL			UNIQUE
);

CREATE TABLE `quests` (
	quest_id			INT			 			PRIMARY KEY 	AUTO_INCREMENT,
    type_id			INT						NOT NULL,
	`title`				VARCHAR(100)	NOT NULL			UNIQUE,
    `description`	VARCHAR(200), 
	reward				INT 						NOT NULL		DEFAULT 0,
    xp					INT 						NOT NULL		DEFAULT 0,

    CONSTRAINT quests_fk_quest_types FOREIGN KEY (type_id) REFERENCES quest_types(type_id)
);

CREATE TABLE `characters` (
	character_id	INT						PRIMARY KEY	AUTO_INCREMENT,
    class_id			INT						NOT NULL,
	`name`				VARCHAR(30)	NOT NULL			UNIQUE,
    `level`				INT 						NOT NULL			DEFAULT 0,
    `experience`	INT 						NOT NULL			DEFAULT 0,
	gold					INT						NOT NULL			DEFAULT 0,

    CONSTRAINT character_fk_classes FOREIGN KEY (class_id) REFERENCES classes(class_id)
);

CREATE TABLE `inventory` (
	item_id			INT						NOT NULL,
    character_id	INT						NOT NULL,
	quantity			int						DEFAULT 0,

	CONSTRAINT inventory_fk_items FOREIGN KEY (item_id) REFERENCES items(item_id),
    CONSTRAINT inventory_fk_characters FOREIGN KEY (character_id) REFERENCES characters(character_id),
    CONSTRAINT item_character_uq UNIQUE (item_id, character_id)
);

CREATE TABLE `quest_log` (
	quest_log_id  	int						PRIMARY KEY	AUTO_INCREMENT,
	quest_id			INT						NOT NULL			REFERENCES items(item_id),
    character_id	INT						NOT NULL			REFERENCES characters(character_id),
    created			DATETIME			NOT NULL			DEFAULT NOW(),
	completed		DATETIME,

    CONSTRAINT quest_log_fk_quests FOREIGN KEY (quest_id) REFERENCES quests(quest_id),
    CONSTRAINT quest_log_fk_characters FOREIGN KEY (character_id) REFERENCES characters(character_id)
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

INSERT INTO quest_types VALUES 
	(DEFAULT, 'kill'),
    (DEFAULT, 'gather'),
    (DEFAULT, 'escort'),
    (DEFAULT, 'talk'),
    (DEFAULT, 'destroy');

INSERT INTO quests (type_id, `title`, `description`, reward, xp) VALUES 
	(1, 'All orcs must die', 'The orcs are terrorizing the mountains!', 200, FLOOR(RAND()*1000)),
    (1, 'The threat of sleepy hollow', 'Slain the headless horseman', 20, FLOOR(RAND()*1000)),
	(1, 'Valhalla', 'Kill 20 vikings so they can reach valhalla', 1255, FLOOR(RAND()*1000)),
	(2, 'An tasty stew', 'Get 20 potatoes so Mrs Crabby Pants can make a stew', 323, FLOOR(RAND()*1000)),
    (2, 'Call to Arms', 'Gather 10 swords and 10 shields for the army', 530, FLOOR(RAND()*1000)),
    (2, 'Flowers for Amy', 'Amy is sick. Get her a bouquet of flowers', 670, FLOOR(RAND()*1000)),
    (3, 'The Following', 'Follow Master Kenobi to the training grounds', 577, FLOOR(RAND()*1000)),
    (3, 'Show Me the Grounds', 'The Master Chief wants to show you the ship.', 879, FLOOR(RAND()*1000)),
    (4, 'Make them Talk', 'The spy you captured must be made to talk!', 1355, FLOOR(RAND()*1000)),
    (4, 'You Wouldn\'t like me when I\'m angry!', 'It\'s time to release the hulk! Make bruce very upset', 886, FLOOR(RAND()*1000)),
    (5, 'Save the village', 'Throw water in every building that is on fire', 556, FLOOR(RAND()*1000)),
    (5, 'Break Their Lines', 'Use the calvary to overrun their troops. Break their defenses to win!', 432, FLOOR(RAND()*1000));

INSERT INTO characters (class_id, `name`, `level`, `experience`, gold) VALUES
	(3, 'Gandalf', 60, 9000, FLOOR(RAND()*1000)),
    (1, 'Sodastere', 10, 433, FLOOR(RAND()*1000)),
    (6, 'Master Chef', 17, 343, FLOOR(RAND()*1000)),
    (6, 'Edard Stark', 1, 1000, FLOOR(RAND()*1000)),
    (2, 'Robert Baratheon', 1, 100000, FLOOR(RAND()*100000)),
    (5, 'Sid Vicious', 4, 23, FLOOR(RAND()*100));

INSERT INTO quest_log (character_id, quest_id, created, completed) VALUES
	(1, 1, from_unixtime(unix_timestamp() - (60*60*24*6)), from_unixtime(unix_timestamp() - (57*60*24*1))),
    (1, 2, from_unixtime(unix_timestamp() - (60*60*24*2)), from_unixtime(unix_timestamp() - (12*60*24*1))),
    (1, 2, from_unixtime(unix_timestamp() - (60*60*24*5)), null),
    (1, 4, from_unixtime(unix_timestamp() - (60*60*24*10)), from_unixtime(unix_timestamp() - (22*60*24*1))),
    (1, 5, from_unixtime(unix_timestamp() - (60*60*24*13)), null),

    (2, 2, from_unixtime(unix_timestamp() - (290*60*24*2)), from_unixtime(unix_timestamp() - (59*60*24*1))),
    (2, 2, from_unixtime(unix_timestamp() - (540*60*24*4)), from_unixtime(unix_timestamp() - (37*60*24*1))),
    (2, 2, from_unixtime(unix_timestamp() - (23*60*24*13)), null),
    (2, 3, from_unixtime(unix_timestamp() - (40*60*24*4)), from_unixtime(unix_timestamp() - (33*60*24*1))),
    (2, 4, from_unixtime(unix_timestamp() - (55*60*24*15)), null),

    (3, 1, from_unixtime(unix_timestamp() - (21*60*24*2)), null),
    (3, 2, from_unixtime(unix_timestamp() - (42*60*24*15)), null),
    (3, 3, from_unixtime(unix_timestamp() - (55*60*24*4)), null),
    (3, 4, from_unixtime(unix_timestamp() - (23*60*24*4)), null),
    (3, 6, from_unixtime(unix_timestamp() - (20*60*24*13)), null),

    (4, 1, from_unixtime(unix_timestamp() - (60*60*24*2)), from_unixtime(unix_timestamp() - (50*60*24*1))),
    (4, 2, from_unixtime(unix_timestamp() - (2*60*24*15)), null),
    (4, 3, from_unixtime(unix_timestamp() - (53*20*24*4)), from_unixtime(unix_timestamp() - (9*60*24*1))),
    (4, 4, from_unixtime(unix_timestamp() - (60*60*24*4)), null),
    (4, 6, from_unixtime(unix_timestamp() - (60*50*24*13)), null),

    (5, 4, from_unixtime(unix_timestamp() - (60*40*24*15)), null),
    (5, 5, from_unixtime(unix_timestamp() - (60*10*24*2)), from_unixtime(unix_timestamp() - (47*60*24*1))),
    (5, 5, from_unixtime(unix_timestamp() - (60*30*24*4)), from_unixtime(unix_timestamp() - (12*60*24*1))),
    (5, 7, from_unixtime(unix_timestamp() - (60*10*24*4)), null),
    (5, 8, from_unixtime(unix_timestamp() - (60*60*24*2)), from_unixtime(unix_timestamp() - (23*60*24*1))),
    (5, 10, from_unixtime(unix_timestamp() - (60*44*24*13)), null),

    (6, 1, from_unixtime(unix_timestamp() - (60*50*24*15)), null),
    (6, 3, from_unixtime(unix_timestamp() - (34*63*24*4)), null),
    (6, 4, from_unixtime(unix_timestamp() - (30*23*24*4)), from_unixtime(unix_timestamp() - (23*60*24*1))),
    (6, 8, from_unixtime(unix_timestamp() - (60*60*24*2)), from_unixtime(unix_timestamp() - (23*60*24*1))),
    (6, 10, from_unixtime(unix_timestamp() - (60*40*24*13)), null);

INSERT INTO inventory (character_id, item_id, quantity) VALUES
	(1, 1, FLOOR(RAND()*14)),
    (1, 2, FLOOR(RAND()*14)),
    (1, 5, FLOOR(RAND()*14)),
    (1, 10, FLOOR(RAND()*14)),

    (2, 3, FLOOR(RAND()*14)),
    (2, 7, FLOOR(RAND()*14)),
    (2, 13, FLOOR(RAND()*14)),

    (3, 2, 0),
    (3, 3, FLOOR(RAND()*14)),
    (3, 6, FLOOR(RAND()*14)),
    (3, 11, 0),
    (3, 12, 0),
    (3, 14, FLOOR(RAND()*14)),

    (4, 1, FLOOR(RAND()*14)),
    (4, 5, FLOOR(RAND()*14)),
    (4, 6, 0),
    (4, 8, FLOOR(RAND()*14)),

    (6, 3, FLOOR(RAND()*14)),
    (6, 4, FLOOR(RAND()*14)),
    (6, 6, FLOOR(RAND()*14)),
    (6, 8, 0),
    (6, 9, FLOOR(RAND()*14)),
    (6, 12, FLOOR(RAND()*14)),
    (6, 13, 0);

