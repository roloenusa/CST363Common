DROP DATABASE IF EXISTS gamedb;
CREATE DATABASE gamedb;

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
