CREATE DATABASE  IF NOT EXISTS `banking` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `banking`;
-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: localhost    Database: banking
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
-- Table structure for table `Account`
--

DROP TABLE IF EXISTS `Account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Account` (
  `acct_nbr` int(11) NOT NULL,
  `acct_type` varchar(50) DEFAULT NULL,
  `balance` float DEFAULT NULL,
  `branch_id` int(11) DEFAULT NULL,
  `ssn` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`acct_nbr`),
  KEY `branch_id` (`branch_id`),
  KEY `ssn` (`ssn`),
  CONSTRAINT `account_ibfk_1` FOREIGN KEY (`branch_id`) REFERENCES `Branch` (`branch_id`),
  CONSTRAINT `account_ibfk_2` FOREIGN KEY (`ssn`) REFERENCES `Customer` (`ssn`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Account`
--

LOCK TABLES `Account` WRITE;
/*!40000 ALTER TABLE `Account` DISABLE KEYS */;
INSERT INTO `Account` VALUES (12134,'checking',-234,5,'172863542'),(12434,'checking',1500,2,'128765434'),(18727,'saving',20000,4,'128765434'),(33456,'saving',900000000,1,'128765434'),(222211,'checking',123451,7,'172863542'),(9872123,'checking',-12,1,'128765434');
/*!40000 ALTER TABLE `Account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Address`
--

DROP TABLE IF EXISTS `Address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Address` (
  `postal_code` varchar(50) NOT NULL,
  `city` varchar(50) DEFAULT NULL,
  `country` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`postal_code`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Address`
--

LOCK TABLES `Address` WRITE;
/*!40000 ALTER TABLE `Address` DISABLE KEYS */;
INSERT INTO `Address` VALUES ('12234','fifth_city','country_4'),('1234','first_city','country_1'),('12342','third_city','country_2'),('27648','third_city','country_2'),('3245','sixth_city','country_3'),('4321','second_city','country_1'),('90871','fourth_city','country_5');
/*!40000 ALTER TABLE `Address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Bank`
--

DROP TABLE IF EXISTS `Bank`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Bank` (
  `code_bank` int(11) NOT NULL,
  `name_bank` varchar(50) DEFAULT NULL,
  `street_number` int(11) DEFAULT NULL,
  `street_name` varchar(100) DEFAULT NULL,
  `postal_code` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`code_bank`),
  UNIQUE KEY `name_bank` (`name_bank`),
  KEY `postal_code` (`postal_code`),
  CONSTRAINT `bank_ibfk_1` FOREIGN KEY (`postal_code`) REFERENCES `Address` (`postal_code`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Bank`
--

LOCK TABLES `Bank` WRITE;
/*!40000 ALTER TABLE `Bank` DISABLE KEYS */;
INSERT INTO `Bank` VALUES (1,'First Bank',2,'first street','12234'),(2,'Second Bank',1,'second street','12342'),(3,'Third Bank',34,'third street','4321'),(4,'Fourth Bank',21,'fourth street','90871');
/*!40000 ALTER TABLE `Bank` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Branch`
--

DROP TABLE IF EXISTS `Branch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Branch` (
  `branch_id` int(11) NOT NULL,
  `street_number` int(11) DEFAULT NULL,
  `street_name` varchar(50) DEFAULT NULL,
  `postal_code` varchar(50) DEFAULT NULL,
  `code_bank` int(11) DEFAULT NULL,
  PRIMARY KEY (`branch_id`),
  KEY `code_bank` (`code_bank`),
  KEY `postal_code` (`postal_code`),
  CONSTRAINT `branch_ibfk_1` FOREIGN KEY (`code_bank`) REFERENCES `Bank` (`code_bank`),
  CONSTRAINT `branch_ibfk_2` FOREIGN KEY (`postal_code`) REFERENCES `Address` (`postal_code`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Branch`
--

LOCK TABLES `Branch` WRITE;
/*!40000 ALTER TABLE `Branch` DISABLE KEYS */;
INSERT INTO `Branch` VALUES (1,223,'White Wall Street','1234',1),(2,221,'Black Wall Street','90871',1),(3,234,'Brown Wall Street','4321',1),(4,435,'Yellow Wall Street','1234',2),(5,123,'Cyan Wall Street','12342',2),(6,345,'White House Street','27648',3),(7,234,'Red Carpet Street','4321',3),(8,111,'Whatever Color Street','4321',3);
/*!40000 ALTER TABLE `Branch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customer`
--

DROP TABLE IF EXISTS `Customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Customer` (
  `ssn` varchar(50) NOT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `telephone` varchar(50) DEFAULT NULL,
  `street_number` int(11) DEFAULT NULL,
  `street_name` varchar(50) DEFAULT NULL,
  `postal_code` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ssn`),
  KEY `postal_code` (`postal_code`),
  CONSTRAINT `customer_ibfk_1` FOREIGN KEY (`postal_code`) REFERENCES `Address` (`postal_code`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer`
--

LOCK TABLES `Customer` WRITE;
/*!40000 ALTER TABLE `Customer` DISABLE KEYS */;
INSERT INTO `Customer` VALUES ('128765434','John','Smith','98763252',12,'SEC Street','1234'),('128787673','First','Customer','987654312',3,'FC Street','12234'),('129876532','Third','Entity','254165283',23,'TC Street','4321'),('172863542','Fourth','Member','109876352',12,'FC Street','90871'),('192827392','Fifth','Whatever','98765243',11,'SC Street','27648'),('219086468','Second','Person','276543511',34,'SC Street','27648');
/*!40000 ALTER TABLE `Customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Loan`
--

DROP TABLE IF EXISTS `Loan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Loan` (
  `loan_nbr` int(11) NOT NULL,
  `loan_type` varchar(50) DEFAULT NULL,
  `amount` float DEFAULT NULL,
  `branch_id` int(11) DEFAULT NULL,
  `ssn` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`loan_nbr`),
  KEY `branch_id` (`branch_id`),
  KEY `ssn` (`ssn`),
  CONSTRAINT `loan_ibfk_1` FOREIGN KEY (`branch_id`) REFERENCES `Branch` (`branch_id`),
  CONSTRAINT `loan_ibfk_2` FOREIGN KEY (`ssn`) REFERENCES `Customer` (`ssn`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Loan`
--

LOCK TABLES `Loan` WRITE;
/*!40000 ALTER TABLE `Loan` DISABLE KEYS */;
INSERT INTO `Loan` VALUES (1,'mortgage',22000,4,'128765434'),(2,'mortgage',1120000,5,'128765434'),(3,'car',5000,1,'172863542'),(4,'car',2000,3,'192827392'),(5,'renovation',10000,8,'219086468');
/*!40000 ALTER TABLE `Loan` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-09-24 14:34:32
