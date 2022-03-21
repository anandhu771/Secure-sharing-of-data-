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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `allocate_minister` */

insert  into `allocate_minister`(`allocate_id`,`dept_id`,`minister_id`,`year`) values 
(1,1,2,'2022-03-03');

/*Table structure for table `allocate_officer` */

DROP TABLE IF EXISTS `allocate_officer`;

CREATE TABLE `allocate_officer` (
  `allocate_officer_id` int(11) NOT NULL AUTO_INCREMENT,
  `officer_id` int(11) DEFAULT NULL,
  `department_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`allocate_officer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `allocate_officer` */

insert  into `allocate_officer`(`allocate_officer_id`,`officer_id`,`department_id`) values 
(1,3,1);

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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`sender_id`,`complaint`,`complaint_date`,`complaint_reply`,`reply_date`) values 
(1,3,'bad','2022-03-15','okko','2022-03-15'),
(2,2,'network issue','2022-03-30','okkkk','2022-03-15'),
(3,3,'tototo','2022-03-21','pending','2022-03-21');

/*Table structure for table `department` */

DROP TABLE IF EXISTS `department`;

CREATE TABLE `department` (
  `dept_id` int(11) NOT NULL AUTO_INCREMENT,
  `dept_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`dept_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `department` */

insert  into `department`(`dept_id`,`dept_name`) values 
(1,'mech');

/*Table structure for table `document` */

DROP TABLE IF EXISTS `document`;

CREATE TABLE `document` (
  `document_id` int(11) NOT NULL AUTO_INCREMENT,
  `allocate_officer_id` int(11) DEFAULT NULL,
  `document` varchar(500) DEFAULT NULL,
  `document_type` varchar(500) DEFAULT NULL,
  `document_date` date DEFAULT NULL,
  PRIMARY KEY (`document_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `document` */

insert  into `document`(`document_id`,`allocate_officer_id`,`document`,`document_type`,`document_date`) values 
(1,1,'shhe','pdf','2022-03-24');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(50) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `user_type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`user_type`) values 
(1,'admin','admin','admin'),
(2,'anjsaj@gmail.com','11781','minister'),
(3,'anjsaj@gmail.com','66245','officer'),
(4,NULL,NULL,NULL);

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
(2,'chandler','/static/minister/220310-100156.jpg','malappuram','anjsaj@gmail.com','/static/photo/220310-100156.jpg',918156911566,'Kasargod','male');

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
(3,'joy','anjsaj@gmail.com',918156911566,'/static/officer/220310-100310.jpg','/static/photo/220310-100310.jpg','Kasargod','malappuram','radio');

/*Table structure for table `suggestions` */

DROP TABLE IF EXISTS `suggestions`;

CREATE TABLE `suggestions` (
  `suggestion_id` int(11) NOT NULL AUTO_INCREMENT,
  `minister_id` int(11) DEFAULT NULL,
  `suggestion_date` date DEFAULT NULL,
  `suggestion_content` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`suggestion_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `suggestions` */

insert  into `suggestions`(`suggestion_id`,`minister_id`,`suggestion_date`,`suggestion_content`) values 
(1,2,'2022-03-10','good'),
(2,2,'2022-03-18','aah'),
(3,2,'2022-03-18','GVVDUS\r\n');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
