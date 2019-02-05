/******************************************
# Class: CST-363
# Module 04, Project 01
# Authors: 
#   Victor Ramirez
#   Juan Sebastian Delgado
# File: GameDb_DW_Queries.sql
#   This script Looks to answer questions
#   about the state of the game db, and players
#   that would provide insight into the business oportunities
#   and analytics.
******************************************/

USE gamedbdw;

/**
 * View Table
 * This master view allows the OLAP user to get a full view of characters,
 * and their interactions with quests and items, as well as get a financial assesment of the player.
 */
 DROP VIEW IF EXISTS character_dashboard;
 CREATE VIEW character_dashboard AS
 SELECT c.characterid, c.name, c.level, c.gold, c.assets, c.experience, 
    pbiql.totalgold as pending_gold, pbiql.totalexperience as pending_experience, pbiql.questCount as pending_quests,
    pbiinv.totalassets as assets_count, pbiinv.totalgold as assets_value,
    compbiql.totalgold as gold_from_quests, compbiql.totalexperience as experience_from_quests, compbiql.questCount as completed_quests,
    (c.gold + ifnull(pbiinv.totalgold, 0) - ifnull(compbiql.totalgold, 0)) as starting_gold,
    (c.experience - ifnull(pbiql.totalexperience, 0)) as starting_experience
 FROM characters c
 LEFT JOIN (
    SELECT characterid, sum(experience) as totalexperience, count(*) questCount, sum(gold) as totalgold
    FROM bi_quest_log biql
    JOIN quests USING (questid)
    WHERE biql.duration IS NULL
    GROUP BY characterid
) pbiql USING(characterid)
LEFT JOIN (
    SELECT characterid, sum(cost) as totalgold, sum(quantity) as totalassets
    FROM bi_inventory biinv
    JOIN items USING (itemid)
    GROUP BY characterid
) pbiinv USING (characterid)
LEFT JOIN (
    SELECT characterid, sum(experience) as totalexperience, count(*) questCount, sum(gold) as totalgold
    FROM bi_quest_log biql
    JOIN quests USING (questid)
    WHERE biql.duration IS NOT NULL
    GROUP BY characterid
) compbiql USING (characterid);

/**
 * Display the view with the character statistics.
 */
SELECT * FROM character_dashboard;

/**
 * Question 1:
 * What are the are the quests that are most often completed and by how many distinct characters?
 * Order by the times it's been completed, the disctinct character count, and the type of quest.
 */
SELECT questid, type, count(*) timescompleted, experience, gold, characterCount
    FROM bi_quest_log biql
    JOIN quests USING (questid)
    JOIN (
        SELECT questid, count(distinct characterid) as characterCount
        FROM bi_quest_log
        WHERE duration IS NOT NULL GROUP BY questid
    ) cc USING (questid)
    WHERE duration IS NOT NULL GROUP BY questid
    ORDER BY timescompleted DESC, charactercount DESC, type ASC;

/**
 * Question 2:
 * What are the most popular types of quests for characters that have at least 1000 gold?
 */
SELECT q.type, q.questid, count(*) timescompleted
FROM bi_quest_log ql
JOIN quests q USING (questid)
JOIN characters c USING (characterid) WHERE c.gold > 1000
GROUP BY q.type, q.questid WITH ROLLUP;
 
 /**
  * Question 3:
  * What time of the year are users more likely to play the game?
  */
 SELECT tl1.quartertext as acquired, tl1.monthtext as month_acquired, tl2.quartertext as completed, count(*) as questcount, questid
 FROM bi_quest_log biql
 JOIN timeline tl1 ON biql.in_timeid = tl1.timeid
 JOIN timeline tl2 ON biql.done_timeid = tl2.timeid
 WHERE biql.duration IS NOT NULL
 GROUP BY tl1.quartertext, tl1.monthtext, tl2.quartertext WITH ROLLUP;
 
/**
 * Question 4:
 * What are the quests that have paid the most amount of gold?
 */
 SELECT questid, gold FROM gamedbdw.quests ORDER BY gold DESC;
 
 
 /**
  * Question 5:
  * What are the most popular items broken by total quantity sold, and gold value per unit and total?
  * What is the average level of the characters purchasing those items?
  */