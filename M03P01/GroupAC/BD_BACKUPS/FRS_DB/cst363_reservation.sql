-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: localhost    Database: cst363
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `reservation`
--

DROP TABLE IF EXISTS `reservation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `reservation` (
  `reservation_ID` int(10) NOT NULL AUTO_INCREMENT,
  `acc_number` int(11) NOT NULL,
  `flight_ID` int(11) NOT NULL,
  `passenger_ID` int(11) NOT NULL,
  PRIMARY KEY (`reservation_ID`),
  KEY `acc_number` (`acc_number`),
  KEY `flight_ID` (`flight_ID`),
  KEY `passenger_ID` (`passenger_ID`),
  CONSTRAINT `reservation_ibfk_1` FOREIGN KEY (`acc_number`) REFERENCES `login` (`acc_number`),
  CONSTRAINT `reservation_ibfk_2` FOREIGN KEY (`flight_ID`) REFERENCES `flight` (`flight_id`),
  CONSTRAINT `reservation_ibfk_3` FOREIGN KEY (`passenger_ID`) REFERENCES `passenger` (`passenger_id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservation`
--

LOCK TABLES `reservation` WRITE;
/*!40000 ALTER TABLE `reservation` DISABLE KEYS */;
INSERT INTO `reservation` VALUES (1,1,1,5),(2,1,2,6),(3,1,3,7),(4,1,4,8),(5,1,4,8),(6,2,5,8),(7,2,2,5),(8,2,6,7),(9,2,3,6),(10,2,3,6),(11,2,3,6),(12,2,6,7),(13,2,2,5),(14,2,5,8),(15,1,4,8),(16,1,3,7),(17,1,7,9),(18,3,5,10),(19,3,5,10),(20,3,4,11),(21,3,4,12),(22,3,7,13),(23,1,1,14),(24,2,1,15),(25,1,9,12),(26,3,3,16),(27,1,3,17),(28,2,6,18),(29,3,4,12),(30,3,5,12),(31,1,7,12),(32,3,8,12),(33,1,1,17),(34,1,1,17),(35,3,10,18),(36,2,10,16),(37,3,10,12),(38,3,10,12),(39,2,6,12);
/*!40000 ALTER TABLE `reservation` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-02-06  6:25:16
