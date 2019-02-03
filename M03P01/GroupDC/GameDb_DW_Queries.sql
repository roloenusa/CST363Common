/******************************************
# Class: CST-363
# Module 04, Project 01
# Authors: 
#   Victor Ramirez
#   Juan Sebastian Delgado
# File: GameDb_DW_Queries.sql
#   Entry point for character specific information.
#   This script Looks to answer questions
#   about the state of the game db, and players
#   that would provide insight into the business oportunities
#   and analytics.
******************************************/

USE gamedbdw;

/**
 * Question 1:
 * What are the are the quests that are most often completed.
 */
SELECT questid, count(*) timescompleted, experience, gold 
    FROM bi_quest_log
    JOIN quests USING (questid)
    WHERE duration IS NOT NULL GROUP BY questid
    ORDER BY count(*) DESC;

/**
 * Question 2:
 * What are the most popular types of quests for characters that have at least 1000 gold
 */
 SELECT q.type, q.questid, count(*) timescompleted
 FROM bi_quest_log ql
 JOIN quests q USING (questid)
 JOIN characters c USING (characterid) WHERE c.gold > 1000
 GROUP BY q.type, q.questid WITH ROLLUP;
 