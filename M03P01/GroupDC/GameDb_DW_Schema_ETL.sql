/******************************************
# Class: CST-363
# Module 04, Project 01
# Authors: 
#   Victor Ramirez
#   Juan Sebastian Delgado
# File: GameDb_DW_Schema_ETL.sql
#   Gamedb Data Warehouse star schema table
******************************************/

DROP SCHEMA IF EXISTS gamedbdw;
CREATE SCHEMA gamedbdw;
USE gamedbdw;

CREATE TABLE timeline(
	timeid      INT         NOT NULL AUTO_INCREMENT PRIMARY KEY,
	date        DATETIME    NOT NULL,
    dayyear     INT         NOT NULL,
	monthid     INT		    NOT NULL,
	monthtext   CHAR(15)    NOT NULL,
	quarterid   INT		    NOT NULL,
	quartertext CHAR(10)    NOT NULL,
	year        CHAR(10)    NOT NULL
);

CREATE TABLE characters (
	characterid INT             NOT NULL PRIMARY KEY,
    `name`      VARCHAR(75)     NOT NULL,
	`level`     VARCHAR(100)    NOT NULL,
	experience  INT             NOT NULL,
	gold        INT             NOT NULL,
    assets      INT             default 0
);

CREATE TABLE quests (
	questid     INT         NOT NULL    PRIMARY KEY,
	type	    CHAR(25)    NOT NULL,
	experience  VARCHAR(75) NOT NULL,
    gold        INT         NOT NULL
);

CREATE TABLE bi_quest_log (
    characterid	INT         NOT NULL,
    questid	    INT         NOT NULL,
    in_timeid   INT         NOT NULL,
    done_timeid INT,
    duration    INT,

	CONSTRAINT bi_quest_log_pk PRIMARY KEY (characterid, questid, in_timeid),
	CONSTRAINT created_timeline_fk FOREIGN KEY (in_timeid) REFERENCES timeline(timeid),
    CONSTRAINT completed_timeline_fk FOREIGN KEY (done_timeid) REFERENCES timeline(timeid),
    CONSTRAINT characterid_characters_fk FOREIGN KEY (characterid) REFERENCES characters(characterid)
        on delete no action on update no action,
    CONSTRAINT questid_quests_fk FOREIGN KEY (questid) REFERENCES quests(questid)
        on delete no action	on update no action
);

CREATE TABLE items (
	itemid      CHAR(35)    NOT NULL    PRIMARY KEY,
	type	    CHAR(25)    NOT NULL,
	cost        INT         NOT NULL
);

CREATE TABLE bi_inventory (
    characterid	int         NOT NULL,
    itemid	    INT         NOT NULL,
    quantity    INT         NOT NULL,
    total       INT         NOT NULL,

	CONSTRAINT bi_inventory_pk PRIMARY KEY (characterid, itemid)
);

/*  months table used when loading timeline table */

CREATE TABLE months (
	monthid     INT         NOT NULL,
	monthtext   CHAR(15)    NOT NULL,
	quarterid   INT         NOT NULL,
	quartertext CHAR(10)    NOT NULL
);


INSERT INTO months VALUES
(1, 'January', 1, 'Qtr1'),
(2, 'February', 1, 'Qtr1'),
(3, 'March', 1, 'Qtr1'),
(4, 'April', 2, 'Qtr2'),
(5, 'May', 2, 'Qtr2'),
(6, 'June', 2, 'Qtr2'),
(7, 'July', 3, 'Qtr3'),
(8, 'August', 3, 'Qtr3'),
(9, 'September', 3, 'Qtr3'),
(10, 'October', 4, 'Qtr4'),
(11, 'November', 4,'Qtr4'),
(12, 'December', 4, 'Qtr4');

/*  load the timeline table from invoice data */
INSERT INTO gamedbdw.timeline (date, dayyear, monthid, monthtext, quarterid, quartertext, year) 
    SELECT DISTINCT date(a.created), dayofyear(a.created), month(a.created), b.monthtext, b.quarterid, b.quartertext, year(a.created)
    FROM gamedb.quest_log a, gamedbdw.months b WHERE month(a.created) = b.monthid
    UNION
    SELECT DISTINCT date(a.completed), dayofyear(a.completed), month(a.completed), b.monthtext, b.quarterid, b.quartertext, year(a.completed)
    FROM gamedb.quest_log a, gamedbdw.months b WHERE month(a.completed) = b.monthid AND completed IS NOT NULL;
    
	
/* load the gamedbdw character table from gamedb customer */
INSERT INTO gamedbdw.characters (characterid, name, level, experience, gold, assets)
    SELECT c.character_id, c.name, level, c.experience, gold, item_total + quest_total
    FROM gamedb.characters c
    LEFT JOIN (
        SELECT character_id, sum(cost * quantity) as item_total FROM gamedb.inventory JOIN gamedb.items USING (item_id) GROUP BY character_id
    ) it USING (character_id)
    LEFT JOIN (
        SELECT character_id, sum(reward) as quest_total FROM gamedb.quest_log JOIN gamedb.quests USING (quest_id) GROUP BY character_id
    ) qt USING (character_id);

/* load gamedbdw item table from gamedb */
INSERT INTO gamedbdw.items 
    SELECT item_id, t.name, cost
    FROM gamedb.items
    JOIN gamedb.item_types t USING (type_id);

/* load gamedbdw inventory table from gamedb */
INSERT INTO gamedbdw.bi_inventory (characterid, itemid, quantity, total)
    SELECT inv.character_id, inv.item_id, inv.quantity, inv.quantity * i.cost
    FROM gamedb.inventory inv
    JOIN gamedb.items i USING (item_id)
    WHERE inv.quantity > 0;

/* load gamedbdw quests table from gamedb */
INSERT INTO gamedbdw.quests (questid, type, experience, gold)
    SELECT quest_id, t.name, xp, reward
    FROM gamedb.quests
    JOIN gamedb.quest_types t using (type_id);

/* load gamedbdw quests logs table from gamedb */
INSERT INTO gamedbdw.bi_quest_log (characterid, questid, in_timeid, done_timeid, duration)
    SELECT ql.character_id, ql.quest_id, tin.timeid, tout.timeid, (tout.dayyear - tin.dayyear)
    FROM gamedb.quest_log ql
    JOIN (SELECT timeid, dayyear, date FROM gamedbdw.timeline) tin ON tin.date = date(ql.created)
    LEFT JOIN (SELECT timeid, dayyear, date FROM timeline) tout ON tout.date = date(ql.completed);
