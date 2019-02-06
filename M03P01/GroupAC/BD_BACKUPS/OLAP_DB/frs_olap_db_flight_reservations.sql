-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: localhost    Database: frs_olap_db
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
-- Table structure for table `flight_reservations`
--

DROP TABLE IF EXISTS `flight_reservations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `flight_reservations` (
  `reservation_id` int(11) NOT NULL,
  `flight_ID` int(11) NOT NULL,
  `passenger_ID` int(11) NOT NULL,
  KEY `flight_ID` (`flight_ID`),
  KEY `passenger_ID` (`passenger_ID`),
  CONSTRAINT `flight_reservations_ibfk_1` FOREIGN KEY (`flight_ID`) REFERENCES `flight` (`flight_id`),
  CONSTRAINT `flight_reservations_ibfk_2` FOREIGN KEY (`passenger_ID`) REFERENCES `passenger` (`passenger_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flight_reservations`
--

LOCK TABLES `flight_reservations` WRITE;
/*!40000 ALTER TABLE `flight_reservations` DISABLE KEYS */;
INSERT INTO `flight_reservations` VALUES (1,1,5),(2,2,6),(3,3,7),(4,4,8),(5,4,8),(6,5,8),(7,2,5),(8,6,7),(9,3,6),(10,3,6),(11,3,6),(12,6,7),(13,2,5),(14,5,8),(15,4,8),(16,3,7),(17,7,9),(18,5,10),(19,5,10),(20,4,11),(21,4,12),(22,7,13),(23,1,14),(24,1,15),(25,9,12),(26,3,16),(27,3,17),(28,6,18),(29,4,12),(30,5,12),(31,7,12),(32,8,12),(33,1,17),(34,1,17),(35,10,18),(36,10,16),(37,10,12),(38,10,12),(39,6,12);
/*!40000 ALTER TABLE `flight_reservations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-02-06  6:24:12
