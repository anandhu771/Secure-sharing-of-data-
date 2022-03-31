/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 5.6.12-log : Database - secure sharing of data
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`secure sharing of data` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `secure sharing of data`;

/*Table structure for table `allocate_minister` */

DROP TABLE IF EXISTS `allocate_minister`;

CREATE TABLE `allocate_minister` (
  `allocate_id` int(11) NOT NULL AUTO_INCREMENT,
  `dept_id` int(11) DEFAULT NULL,
  `minister_id` int(11) DEFAULT NULL,
  `year` date DEFAULT NULL,
  PRIMARY KEY (`allocate_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `allocate_minister` */

/*Table structure for table `allocate_officer` */

DROP TABLE IF EXISTS `allocate_officer`;

CREATE TABLE `allocate_officer` (
  `allocate_officer_id` int(11) NOT NULL AUTO_INCREMENT,
  `officer_id` int(11) DEFAULT NULL,
  `department_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`allocate_officer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `allocate_officer` */

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `from_id` int(11) DEFAULT NULL,
  `to_id` int(11) DEFAULT NULL,
  `message` varchar(50000) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

insert  into `chat`(`chat_id`,`from_id`,`to_id`,`message`,`date`) values 
(1,3,2,'hiiii','2022-03-31'),
(2,3,0,'hi','2022-03-31'),
(3,3,3,'heyyy','2022-03-31'),
(4,3,3,'','2022-03-31'),
(5,3,3,'hey','2022-03-31'),
(6,3,3,'jooo','2022-03-31');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) DEFAULT NULL,
  `complaint` varchar(500) DEFAULT NULL,
  `complaint_date` date DEFAULT NULL,
  `complaint_reply` varchar(500) DEFAULT NULL,
  `reply_date` date DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

/*Table structure for table `department` */

DROP TABLE IF EXISTS `department`;

CREATE TABLE `department` (
  `dept_id` int(11) NOT NULL AUTO_INCREMENT,
  `dept_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`dept_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `department` */

/*Table structure for table `document` */

DROP TABLE IF EXISTS `document`;

CREATE TABLE `document` (
  `document_id` int(11) NOT NULL AUTO_INCREMENT,
  `allocate_officer_id` int(11) DEFAULT NULL,
  `document` varchar(500) DEFAULT NULL,
  `document_type` varchar(500) DEFAULT NULL,
  `document_date` date DEFAULT NULL,
  PRIMARY KEY (`document_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `document` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(50) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `user_type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`user_type`) values 
(1,'admin','admin','admin'),
(2,'joy@gmail.com','67594','minister'),
(3,'ross@gmail.com','36715','officer');

/*Table structure for table `minister` */

DROP TABLE IF EXISTS `minister`;

CREATE TABLE `minister` (
  `minister_id` int(11) DEFAULT NULL,
  `miniter_name` varchar(50) DEFAULT NULL,
  `minister_proof` varchar(100) DEFAULT NULL,
  `minister_place` varchar(50) DEFAULT NULL,
  `minister_email` varchar(50) DEFAULT NULL,
  `minister_photo` varchar(100) DEFAULT NULL,
  `minister_contactnumber` bigint(50) DEFAULT NULL,
  `minister_district` varchar(50) DEFAULT NULL,
  `m_gender` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `minister` */

insert  into `minister`(`minister_id`,`miniter_name`,`minister_proof`,`minister_place`,`minister_email`,`minister_photo`,`minister_contactnumber`,`minister_district`,`m_gender`) values 
(2,'joy','/static/minister/220331-100817.jpg','mala','joy@gmail.com','/static/photo/220331-100817.jpg',8156911566,'Kasargod','radio');

/*Table structure for table `minister_group` */

DROP TABLE IF EXISTS `minister_group`;

CREATE TABLE `minister_group` (
  `group_id` int(11) NOT NULL AUTO_INCREMENT,
  `minister_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `minister_group` */

/*Table structure for table `officer` */

DROP TABLE IF EXISTS `officer`;

CREATE TABLE `officer` (
  `officer_id` int(11) DEFAULT NULL,
  `officer_name` varchar(50) DEFAULT NULL,
  `officer_email` varchar(50) DEFAULT NULL,
  `officer_contactnumber` bigint(20) DEFAULT NULL,
  `officer_proof` varchar(100) DEFAULT NULL,
  `officer_photo` varchar(100) DEFAULT NULL,
  `officer_district` varchar(100) DEFAULT NULL,
  `officer_place` varchar(100) DEFAULT NULL,
  `o_gender` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `officer` */

insert  into `officer`(`officer_id`,`officer_name`,`officer_email`,`officer_contactnumber`,`officer_proof`,`officer_photo`,`officer_district`,`officer_place`,`o_gender`) values 
(3,'ross','ross@gmail.com',9586587421,'/static/officer/220331-101139.jpg','/static/photo/220331-101139.jpg','kannur','vkkd','radio');

/*Table structure for table `suggestions` */

DROP TABLE IF EXISTS `suggestions`;

CREATE TABLE `suggestions` (
  `suggestion_id` int(11) NOT NULL AUTO_INCREMENT,
  `minister_id` int(11) DEFAULT NULL,
  `suggestion_date` date DEFAULT NULL,
  `suggestion_content` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`suggestion_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `suggestions` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
