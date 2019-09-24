CREATE DATABASE  IF NOT EXISTS `sn_platform` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `sn_platform`;
-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: localhost    Database: sn_platform
-- ------------------------------------------------------
-- Server version	5.7.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `EmailAddress`
--

DROP TABLE IF EXISTS `EmailAddress`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `EmailAddress` (
  `email_address` varchar(100) NOT NULL,
  `nickname` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`email_address`),
  KEY `nickname` (`nickname`),
  CONSTRAINT `emailaddress_ibfk_1` FOREIGN KEY (`nickname`) REFERENCES `UserAccount` (`nickname`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EmailAddress`
--

LOCK TABLES `EmailAddress` WRITE;
/*!40000 ALTER TABLE `EmailAddress` DISABLE KEYS */;
INSERT INTO `EmailAddress` VALUES ('nick_ANIS@email.me','nick_ANIS'),('nick_BIANCHI@email.me','nick_BIANCHI'),('nick_BLANCO@email.me','nick_BLANCO'),('nick_CAMERON@email.me','nick_CAMERON'),('nick_CHOISNE@email.me','nick_CHOISNE'),('nick_COEFFARD@email.me','nick_COEFFARD'),('nick_COUILLAUD@email.me','nick_COUILLAUD'),('nick_FERRON@email.me','nick_FERRON'),('nick_GUEFFIER@email.me','nick_GUEFFIER'),('nick_HUGHES@email.me','nick_HUGHES'),('nick_MORENO@email.me','nick_MORENO'),('nick_RELION@email.me','nick_RELION'),('nick_REVERDY@email.me','nick_REVERDY'),('nick_ROSSI@email.me','nick_ROSSI'),('nick_ROUSSIERE@email.me','nick_ROUSSIERE'),('nick_SCHEIDER@email.me','nick_SCHEIDER'),('nick_SCHMIDT@email.me','nick_SCHMIDT'),('nick_SMITH@email.me','nick_SMITH'),('nick_WEBER@email.me','nick_WEBER');
/*!40000 ALTER TABLE `EmailAddress` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Post`
--

DROP TABLE IF EXISTS `Post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Post` (
  `post_id` int(11) NOT NULL,
  `content` text,
  `date` varchar(50) DEFAULT NULL,
  `time` varchar(50) DEFAULT NULL,
  `latitude` float DEFAULT NULL,
  `longitude` float DEFAULT NULL,
  `nickname` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`post_id`),
  KEY `nickname` (`nickname`),
  CONSTRAINT `post_ibfk_1` FOREIGN KEY (`nickname`) REFERENCES `UserAccount` (`nickname`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Post`
--

LOCK TABLES `Post` WRITE;
/*!40000 ALTER TABLE `Post` DISABLE KEYS */;
INSERT INTO `Post` VALUES (1,'first post','2012-05-06','08:00:00',0,0,'nick_CAMERON'),(2,'second post','2015-07-09','09:00:00',0,0,'nick_BLANCO');
/*!40000 ALTER TABLE `Post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Relationship`
--

DROP TABLE IF EXISTS `Relationship`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Relationship` (
  `nickname_src` varchar(100) NOT NULL,
  `nickname_dst` varchar(100) NOT NULL,
  `type` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`nickname_src`,`nickname_dst`),
  KEY `nickname_dst` (`nickname_dst`),
  CONSTRAINT `relationship_ibfk_1` FOREIGN KEY (`nickname_src`) REFERENCES `UserAccount` (`nickname`),
  CONSTRAINT `relationship_ibfk_2` FOREIGN KEY (`nickname_dst`) REFERENCES `UserAccount` (`nickname`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Relationship`
--

LOCK TABLES `Relationship` WRITE;
/*!40000 ALTER TABLE `Relationship` DISABLE KEYS */;
INSERT INTO `Relationship` VALUES ('nick_ANIS','nick_BIANCHI','friendship','2009-04-03'),('nick_ANIS','nick_BLANCO','friendship','2009-04-03'),('nick_ANIS','nick_CAMERON','friendship','2009-04-03'),('nick_ANIS','nick_CHOISNE','friendship','2009-04-03'),('nick_ANIS','nick_COEFFARD','friendship','2009-04-03'),('nick_ANIS','nick_COUILLAUD','friendship','2009-04-03'),('nick_ANIS','nick_HUGHES','follower','2009-04-03'),('nick_ANIS','nick_MORENO','friendship','2009-04-03'),('nick_ANIS','nick_REVERDY','friendship','2009-04-03'),('nick_ANIS','nick_ROSSI','follower','2009-04-03'),('nick_ANIS','nick_ROUSSIERE','friendship','2009-04-03'),('nick_ANIS','nick_SCHEIDER','follower','2009-04-03'),('nick_BIANCHI','nick_ANIS','friendship','2009-04-03'),('nick_BIANCHI','nick_BLANCO','follower','2009-04-03'),('nick_BIANCHI','nick_CHOISNE','friendship','2009-04-03'),('nick_BIANCHI','nick_COEFFARD','friendship','2009-04-03'),('nick_BIANCHI','nick_COUILLAUD','friendship','2009-04-03'),('nick_BIANCHI','nick_FERRON','friendship','2009-04-03'),('nick_BIANCHI','nick_GUEFFIER','friendship','2009-04-03'),('nick_BIANCHI','nick_HUGHES','friendship','2009-04-03'),('nick_BIANCHI','nick_MORENO','friendship','2009-04-03'),('nick_BIANCHI','nick_RELION','follower','2009-04-03'),('nick_BIANCHI','nick_REVERDY','follower','2009-04-03'),('nick_BIANCHI','nick_ROSSI','friendship','2009-04-03'),('nick_BIANCHI','nick_ROUSSIERE','friendship','2009-04-03'),('nick_BIANCHI','nick_SCHEIDER','follower','2009-04-03'),('nick_BIANCHI','nick_SMITH','friendship','2009-04-03'),('nick_BIANCHI','nick_WEBER','follower','2009-04-03'),('nick_BLANCO','nick_ANIS','friendship','2009-04-03'),('nick_BLANCO','nick_CAMERON','follower','2009-04-03'),('nick_BLANCO','nick_CHOISNE','friendship','2009-04-03'),('nick_BLANCO','nick_COEFFARD','friendship','2009-04-03'),('nick_BLANCO','nick_COUILLAUD','friendship','2009-04-03'),('nick_BLANCO','nick_FERRON','friendship','2009-04-03'),('nick_BLANCO','nick_GUEFFIER','friendship','2009-04-03'),('nick_BLANCO','nick_MORENO','friendship','2009-04-03'),('nick_BLANCO','nick_RELION','follower','2009-04-03'),('nick_BLANCO','nick_REVERDY','follower','2009-04-03'),('nick_BLANCO','nick_ROUSSIERE','friendship','2009-04-03'),('nick_BLANCO','nick_SCHEIDER','friendship','2009-04-03'),('nick_BLANCO','nick_SCHMIDT','friendship','2009-04-03'),('nick_BLANCO','nick_SMITH','follower','2009-04-03'),('nick_BLANCO','nick_WEBER','follower','2009-04-03'),('nick_CAMERON','nick_ANIS','friendship','2009-04-03'),('nick_CAMERON','nick_BIANCHI','follower','2009-04-03'),('nick_CAMERON','nick_BLANCO','follower','2009-04-03'),('nick_CAMERON','nick_COEFFARD','friendship','2009-04-03'),('nick_CAMERON','nick_FERRON','follower','2009-04-03'),('nick_CAMERON','nick_GUEFFIER','friendship','2009-04-03'),('nick_CAMERON','nick_MORENO','friendship','2009-04-03'),('nick_CAMERON','nick_RELION','friendship','2009-04-03'),('nick_CAMERON','nick_REVERDY','follower','2009-04-03'),('nick_CAMERON','nick_ROSSI','friendship','2009-04-03'),('nick_CAMERON','nick_ROUSSIERE','friendship','2009-04-03'),('nick_CAMERON','nick_SCHEIDER','friendship','2009-04-03'),('nick_CAMERON','nick_SCHMIDT','friendship','2009-04-03'),('nick_CAMERON','nick_SMITH','friendship','2009-04-03'),('nick_CAMERON','nick_WEBER','follower','2009-04-03'),('nick_CHOISNE','nick_ANIS','friendship','2009-04-03'),('nick_CHOISNE','nick_BIANCHI','friendship','2009-04-03'),('nick_CHOISNE','nick_BLANCO','friendship','2009-04-03'),('nick_CHOISNE','nick_COEFFARD','friendship','2009-04-03'),('nick_CHOISNE','nick_COUILLAUD','friendship','2009-04-03'),('nick_CHOISNE','nick_FERRON','friendship','2009-04-03'),('nick_CHOISNE','nick_GUEFFIER','follower','2009-04-03'),('nick_CHOISNE','nick_HUGHES','friendship','2009-04-03'),('nick_CHOISNE','nick_REVERDY','friendship','2009-04-03'),('nick_CHOISNE','nick_ROSSI','friendship','2009-04-03'),('nick_CHOISNE','nick_SCHEIDER','friendship','2009-04-03'),('nick_CHOISNE','nick_SCHMIDT','friendship','2009-04-03'),('nick_COEFFARD','nick_ANIS','friendship','2009-04-03'),('nick_COEFFARD','nick_BIANCHI','friendship','2009-04-03'),('nick_COEFFARD','nick_BLANCO','friendship','2009-04-03'),('nick_COEFFARD','nick_CAMERON','friendship','2009-04-03'),('nick_COEFFARD','nick_CHOISNE','friendship','2009-04-03'),('nick_COEFFARD','nick_FERRON','friendship','2009-04-03'),('nick_COEFFARD','nick_HUGHES','follower','2009-04-03'),('nick_COEFFARD','nick_RELION','friendship','2009-04-03'),('nick_COEFFARD','nick_ROUSSIERE','follower','2009-04-03'),('nick_COEFFARD','nick_SCHEIDER','friendship','2009-04-03'),('nick_COEFFARD','nick_SMITH','friendship','2009-04-03'),('nick_COEFFARD','nick_WEBER','friendship','2009-04-03'),('nick_COUILLAUD','nick_ANIS','friendship','2009-04-03'),('nick_COUILLAUD','nick_BIANCHI','friendship','2009-04-03'),('nick_COUILLAUD','nick_BLANCO','friendship','2009-04-03'),('nick_COUILLAUD','nick_CAMERON','follower','2009-04-03'),('nick_COUILLAUD','nick_CHOISNE','friendship','2009-04-03'),('nick_COUILLAUD','nick_RELION','friendship','2009-04-03'),('nick_COUILLAUD','nick_REVERDY','friendship','2009-04-03'),('nick_COUILLAUD','nick_ROSSI','friendship','2009-04-03'),('nick_COUILLAUD','nick_SCHEIDER','friendship','2009-04-03'),('nick_COUILLAUD','nick_SCHMIDT','friendship','2009-04-03'),('nick_COUILLAUD','nick_SMITH','friendship','2009-04-03'),('nick_FERRON','nick_ANIS','follower','2009-04-03'),('nick_FERRON','nick_BIANCHI','friendship','2009-04-03'),('nick_FERRON','nick_BLANCO','friendship','2009-04-03'),('nick_FERRON','nick_CAMERON','follower','2009-04-03'),('nick_FERRON','nick_CHOISNE','friendship','2009-04-03'),('nick_FERRON','nick_COEFFARD','friendship','2009-04-03'),('nick_FERRON','nick_GUEFFIER','friendship','2009-04-03'),('nick_FERRON','nick_HUGHES','friendship','2009-04-03'),('nick_FERRON','nick_MORENO','friendship','2009-04-03'),('nick_FERRON','nick_RELION','follower','2009-04-03'),('nick_FERRON','nick_ROSSI','follower','2009-04-03'),('nick_FERRON','nick_ROUSSIERE','friendship','2009-04-03'),('nick_FERRON','nick_SCHMIDT','follower','2009-04-03'),('nick_FERRON','nick_WEBER','friendship','2009-04-03'),('nick_GUEFFIER','nick_BIANCHI','friendship','2009-04-03'),('nick_GUEFFIER','nick_BLANCO','friendship','2009-04-03'),('nick_GUEFFIER','nick_CAMERON','friendship','2009-04-03'),('nick_GUEFFIER','nick_FERRON','friendship','2009-04-03'),('nick_GUEFFIER','nick_MORENO','friendship','2009-04-03'),('nick_GUEFFIER','nick_ROSSI','friendship','2009-04-03'),('nick_GUEFFIER','nick_ROUSSIERE','friendship','2009-04-03'),('nick_GUEFFIER','nick_SCHEIDER','follower','2009-04-03'),('nick_GUEFFIER','nick_SCHMIDT','friendship','2009-04-03'),('nick_GUEFFIER','nick_SMITH','friendship','2009-04-03'),('nick_HUGHES','nick_BIANCHI','friendship','2009-04-03'),('nick_HUGHES','nick_BLANCO','follower','2009-04-03'),('nick_HUGHES','nick_CAMERON','follower','2009-04-03'),('nick_HUGHES','nick_CHOISNE','friendship','2009-04-03'),('nick_HUGHES','nick_COEFFARD','follower','2009-04-03'),('nick_HUGHES','nick_FERRON','friendship','2009-04-03'),('nick_HUGHES','nick_MORENO','friendship','2009-04-03'),('nick_HUGHES','nick_RELION','follower','2009-04-03'),('nick_HUGHES','nick_ROSSI','friendship','2009-04-03'),('nick_HUGHES','nick_ROUSSIERE','friendship','2009-04-03'),('nick_HUGHES','nick_SCHMIDT','follower','2009-04-03'),('nick_HUGHES','nick_SMITH','follower','2009-04-03'),('nick_HUGHES','nick_WEBER','friendship','2009-04-03'),('nick_MORENO','nick_ANIS','friendship','2009-04-03'),('nick_MORENO','nick_BIANCHI','friendship','2009-04-03'),('nick_MORENO','nick_BLANCO','friendship','2009-04-03'),('nick_MORENO','nick_CAMERON','friendship','2009-04-03'),('nick_MORENO','nick_FERRON','friendship','2009-04-03'),('nick_MORENO','nick_GUEFFIER','friendship','2009-04-03'),('nick_MORENO','nick_HUGHES','friendship','2009-04-03'),('nick_MORENO','nick_RELION','follower','2009-04-03'),('nick_MORENO','nick_REVERDY','friendship','2009-04-03'),('nick_MORENO','nick_ROSSI','friendship','2009-04-03'),('nick_MORENO','nick_ROUSSIERE','friendship','2009-04-03'),('nick_MORENO','nick_SCHEIDER','friendship','2009-04-03'),('nick_MORENO','nick_SCHMIDT','follower','2009-04-03'),('nick_MORENO','nick_SMITH','friendship','2009-04-03'),('nick_RELION','nick_BIANCHI','follower','2009-04-03'),('nick_RELION','nick_CAMERON','friendship','2009-04-03'),('nick_RELION','nick_CHOISNE','follower','2009-04-03'),('nick_RELION','nick_COEFFARD','friendship','2009-04-03'),('nick_RELION','nick_COUILLAUD','friendship','2009-04-03'),('nick_RELION','nick_GUEFFIER','follower','2009-04-03'),('nick_RELION','nick_ROUSSIERE','friendship','2009-04-03'),('nick_RELION','nick_SCHMIDT','follower','2009-04-03'),('nick_REVERDY','nick_ANIS','friendship','2009-04-03'),('nick_REVERDY','nick_CHOISNE','friendship','2009-04-03'),('nick_REVERDY','nick_COEFFARD','follower','2009-04-03'),('nick_REVERDY','nick_COUILLAUD','friendship','2009-04-03'),('nick_REVERDY','nick_MORENO','friendship','2009-04-03'),('nick_REVERDY','nick_RELION','follower','2009-04-03'),('nick_REVERDY','nick_ROSSI','follower','2009-04-03'),('nick_REVERDY','nick_ROUSSIERE','friendship','2009-04-03'),('nick_REVERDY','nick_SCHMIDT','follower','2009-04-03'),('nick_REVERDY','nick_WEBER','follower','2009-04-03'),('nick_ROSSI','nick_BIANCHI','friendship','2009-04-03'),('nick_ROSSI','nick_BLANCO','follower','2009-04-03'),('nick_ROSSI','nick_CAMERON','friendship','2009-04-03'),('nick_ROSSI','nick_CHOISNE','friendship','2009-04-03'),('nick_ROSSI','nick_COUILLAUD','friendship','2009-04-03'),('nick_ROSSI','nick_GUEFFIER','friendship','2009-04-03'),('nick_ROSSI','nick_HUGHES','friendship','2009-04-03'),('nick_ROSSI','nick_MORENO','friendship','2009-04-03'),('nick_ROSSI','nick_REVERDY','follower','2009-04-03'),('nick_ROSSI','nick_ROUSSIERE','friendship','2009-04-03'),('nick_ROSSI','nick_SCHEIDER','follower','2009-04-03'),('nick_ROSSI','nick_SCHMIDT','follower','2009-04-03'),('nick_ROUSSIERE','nick_ANIS','friendship','2009-04-03'),('nick_ROUSSIERE','nick_BIANCHI','friendship','2009-04-03'),('nick_ROUSSIERE','nick_BLANCO','friendship','2009-04-03'),('nick_ROUSSIERE','nick_CAMERON','friendship','2009-04-03'),('nick_ROUSSIERE','nick_CHOISNE','follower','2009-04-03'),('nick_ROUSSIERE','nick_COUILLAUD','follower','2009-04-03'),('nick_ROUSSIERE','nick_FERRON','friendship','2009-04-03'),('nick_ROUSSIERE','nick_GUEFFIER','friendship','2009-04-03'),('nick_ROUSSIERE','nick_HUGHES','friendship','2009-04-03'),('nick_ROUSSIERE','nick_MORENO','friendship','2009-04-03'),('nick_ROUSSIERE','nick_RELION','friendship','2009-04-03'),('nick_ROUSSIERE','nick_REVERDY','friendship','2009-04-03'),('nick_ROUSSIERE','nick_ROSSI','friendship','2009-04-03'),('nick_ROUSSIERE','nick_SCHEIDER','friendship','2009-04-03'),('nick_ROUSSIERE','nick_SCHMIDT','follower','2009-04-03'),('nick_ROUSSIERE','nick_SMITH','friendship','2009-04-03'),('nick_ROUSSIERE','nick_WEBER','friendship','2009-04-03'),('nick_SCHEIDER','nick_BIANCHI','follower','2009-04-03'),('nick_SCHEIDER','nick_BLANCO','friendship','2009-04-03'),('nick_SCHEIDER','nick_CAMERON','friendship','2009-04-03'),('nick_SCHEIDER','nick_CHOISNE','friendship','2009-04-03'),('nick_SCHEIDER','nick_COEFFARD','friendship','2009-04-03'),('nick_SCHEIDER','nick_COUILLAUD','friendship','2009-04-03'),('nick_SCHEIDER','nick_MORENO','friendship','2009-04-03'),('nick_SCHEIDER','nick_RELION','follower','2009-04-03'),('nick_SCHEIDER','nick_ROUSSIERE','friendship','2009-04-03'),('nick_SCHEIDER','nick_SCHMIDT','follower','2009-04-03'),('nick_SCHMIDT','nick_ANIS','follower','2009-04-03'),('nick_SCHMIDT','nick_BLANCO','friendship','2009-04-03'),('nick_SCHMIDT','nick_CAMERON','friendship','2009-04-03'),('nick_SCHMIDT','nick_CHOISNE','friendship','2009-04-03'),('nick_SCHMIDT','nick_COEFFARD','follower','2009-04-03'),('nick_SCHMIDT','nick_COUILLAUD','friendship','2009-04-03'),('nick_SCHMIDT','nick_GUEFFIER','friendship','2009-04-03'),('nick_SCHMIDT','nick_ROUSSIERE','follower','2009-04-03'),('nick_SCHMIDT','nick_SMITH','friendship','2009-04-03'),('nick_SMITH','nick_BIANCHI','friendship','2009-04-03'),('nick_SMITH','nick_CAMERON','friendship','2009-04-03'),('nick_SMITH','nick_COEFFARD','friendship','2009-04-03'),('nick_SMITH','nick_COUILLAUD','friendship','2009-04-03'),('nick_SMITH','nick_GUEFFIER','friendship','2009-04-03'),('nick_SMITH','nick_MORENO','friendship','2009-04-03'),('nick_SMITH','nick_REVERDY','follower','2009-04-03'),('nick_SMITH','nick_ROUSSIERE','friendship','2009-04-03'),('nick_SMITH','nick_SCHMIDT','friendship','2009-04-03'),('nick_WEBER','nick_COEFFARD','friendship','2009-04-03'),('nick_WEBER','nick_FERRON','friendship','2009-04-03'),('nick_WEBER','nick_GUEFFIER','follower','2009-04-03'),('nick_WEBER','nick_HUGHES','friendship','2009-04-03'),('nick_WEBER','nick_ROUSSIERE','friendship','2009-04-03'),('nick_WEBER','nick_SCHEIDER','follower','2009-04-03');
/*!40000 ALTER TABLE `Relationship` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Tag`
--

DROP TABLE IF EXISTS `Tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Tag` (
  `post_id` int(11) NOT NULL,
  `nickname` varchar(100) NOT NULL,
  PRIMARY KEY (`post_id`,`nickname`),
  KEY `nickname` (`nickname`),
  CONSTRAINT `tag_ibfk_1` FOREIGN KEY (`post_id`) REFERENCES `Post` (`post_id`),
  CONSTRAINT `tag_ibfk_2` FOREIGN KEY (`nickname`) REFERENCES `UserAccount` (`nickname`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Tag`
--

LOCK TABLES `Tag` WRITE;
/*!40000 ALTER TABLE `Tag` DISABLE KEYS */;
INSERT INTO `Tag` VALUES (2,'nick_ANIS'),(1,'nick_BIANCHI'),(1,'nick_COEFFARD');
/*!40000 ALTER TABLE `Tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `UserAccount`
--

DROP TABLE IF EXISTS `UserAccount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `UserAccount` (
  `nickname` varchar(100) NOT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `country` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`nickname`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `UserAccount`
--

LOCK TABLES `UserAccount` WRITE;
/*!40000 ALTER TABLE `UserAccount` DISABLE KEYS */;
INSERT INTO `UserAccount` VALUES ('nick_ANIS','Karl','ANIS','Freiburg','Germany'),('nick_BIANCHI','Matteo','BIANCHI','Milan','Italy'),('nick_BLANCO','Francisco','BLANCO','Madrir','Spain'),('nick_CAMERON','Andrew','CAMERON','London','UK'),('nick_CHOISNE','Eliane','CHOISNE','Nice','France'),('nick_COEFFARD','Florian','COEFFARD','Montpellier','France'),('nick_COUILLAUD','Timothée','COUILLAUD','Paris','France'),('nick_FERRON','Prosper','FERRON','Lisbon','Portugal'),('nick_GUEFFIER','Hortense','GUEFFIER','Lille','France'),('nick_HUGHES','Lara ','HUGHES','Manchester','UK'),('nick_MORENO','Franco','MORENO','Barcelona','Spain'),('nick_RELION','Léonie','RELION','Montpellier','France'),('nick_REVERDY','Frantz','REVERDY','Miami','USA'),('nick_ROSSI','Gina','ROSSI','Rome','Italy'),('nick_ROUSSIERE','Jacob','ROUSSIERE','Bordeaux','France'),('nick_SCHEIDER','Paul','SCHEIDER','Stuttgart','Germany'),('nick_SCHMIDT','Gerda','SCHMIDT','Freiburg','Germany'),('nick_SMITH','John','SMITH','New York City','USA'),('nick_WEBER','Bertha','WEBER','Munich','Germany');
/*!40000 ALTER TABLE `UserAccount` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-09-24 14:31:50
