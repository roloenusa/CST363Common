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
-- Table structure for table `flight`
--

DROP TABLE IF EXISTS `flight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `flight` (
  `flight_ID` int(10) NOT NULL AUTO_INCREMENT,
  `departure_time` time DEFAULT NULL,
  `departure_date` date DEFAULT NULL,
  `arrival_time` time DEFAULT NULL,
  `arrival_date` date DEFAULT NULL,
  `flight_seat` int(10) NOT NULL,
  `ticket_type` varchar(10) NOT NULL,
  `src_airport_code` varchar(10) NOT NULL,
  `dest_airport_code` varchar(10) NOT NULL,
  PRIMARY KEY (`flight_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flight`
--

LOCK TABLES `flight` WRITE;
/*!40000 ALTER TABLE `flight` DISABLE KEYS */;
INSERT INTO `flight` VALUES (1,'12:22:00','2019-02-01','19:45:11','2019-02-01',30,'economy','SFO','PHL'),(2,'14:22:00','2019-02-01','19:45:11','2019-02-02',30,'economy','SFO','CKY'),(3,'17:22:00','2019-02-01','19:45:11','2019-02-02',30,'business','JFK','CKY'),(4,'18:22:00','2019-03-05','23:45:11','2019-03-06',30,'business','PEK','CKY'),(5,'19:22:00','2019-02-01','00:45:11','2019-02-02',30,'business','MIA','ATL'),(6,'20:22:00','2019-03-14','13:00:11','2019-03-15',30,'business','JFK','HND'),(7,'21:22:00','2019-02-01','09:45:11','2019-02-02',30,'business','JFK','DEL'),(8,'22:22:00','2019-02-22','10:45:11','2019-02-23',30,'business','DEL','PEK'),(9,'23:22:00','2019-03-30','15:40:11','2019-03-31',30,'business','MIA','CKY'),(10,'24:22:00','2019-05-01','17:45:11','2019-05-02',30,'business','ATL','CKY');
/*!40000 ALTER TABLE `flight` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-02-06  6:25:17
