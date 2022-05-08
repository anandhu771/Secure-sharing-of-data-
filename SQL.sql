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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `allocate_minister` */

insert  into `allocate_minister`(`allocate_id`,`dept_id`,`minister_id`,`year`) values 
(1,1,2,'2022-04-13'),
(3,2,3,'2022-04-06');

/*Table structure for table `allocate_officer` */

DROP TABLE IF EXISTS `allocate_officer`;

CREATE TABLE `allocate_officer` (
  `allocate_officer_id` int(11) NOT NULL AUTO_INCREMENT,
  `officer_id` int(11) DEFAULT NULL,
  `department_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`allocate_officer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `allocate_officer` */

insert  into `allocate_officer`(`allocate_officer_id`,`officer_id`,`department_id`) values 
(1,4,1),
(2,5,2);

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `from_id` int(11) DEFAULT NULL,
  `to_id` int(11) DEFAULT NULL,
  `message` varchar(50000) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

insert  into `chat`(`chat_id`,`from_id`,`to_id`,`message`,`date`) values 
(1,2,0,'hi adhish','2022-04-11'),
(2,2,5,'hi fasil','2022-04-11'),
(3,2,4,'hi adhish','2022-04-11'),
(4,4,0,'hai anandhu','2022-04-11'),
(5,4,2,'hi anandhu','2022-04-11');

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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`sender_id`,`complaint`,`complaint_date`,`complaint_reply`,`reply_date`) values 
(1,4,'not good ','2022-04-11','working on it ','2022-04-11'),
(2,4,'chat no working\r\n','2022-04-11','okay','2022-04-11'),
(3,4,'what','2022-04-12','pending','0000-00-00'),
(4,4,'yoo','2022-04-12','pending','0000-00-00');

/*Table structure for table `department` */

DROP TABLE IF EXISTS `department`;

CREATE TABLE `department` (
  `dept_id` int(11) NOT NULL AUTO_INCREMENT,
  `dept_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`dept_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `department` */

insert  into `department`(`dept_id`,`dept_name`) values 
(1,'civil'),
(2,'mca');

/*Table structure for table `document` */

DROP TABLE IF EXISTS `document`;

CREATE TABLE `document` (
  `document_id` int(11) NOT NULL AUTO_INCREMENT,
  `path` varchar(200) DEFAULT NULL,
  `algthm` varchar(500) DEFAULT NULL,
  `allocate_officer_id` varchar(500) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `key_1` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`document_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `document` */

insert  into `document`(`document_id`,`path`,`algthm`,`allocate_officer_id`,`date`,`key_1`) values 
(1,'1','/static/documents/220411-103603.pdf','expence details','2022-04-11 00:00:00',NULL),
(2,'2','/static/documents/220412-105528.pdf','final report','2022-04-12 00:00:00',NULL),
(3,'New Text Document.txt.aes','AES','4','2022-05-06 00:00:00','2765'),
(4,'New Text Document.txt.aes','AES','4','2022-05-06 00:00:00','4994');

/*Table structure for table `file` */

DROP TABLE IF EXISTS `file`;

CREATE TABLE `file` (
  `file_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `file_type` varchar(25) DEFAULT NULL,
  `catagory` varchar(25) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `key` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`file_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `file` */

/*Table structure for table `group1` */

DROP TABLE IF EXISTS `group1`;

CREATE TABLE `group1` (
  `group_id` int(11) NOT NULL AUTO_INCREMENT,
  `group_name` varchar(50) DEFAULT NULL,
  `group_password` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`group_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `group1` */

insert  into `group1`(`group_id`,`group_name`,`group_password`) values 
(1,'CSA','99667'),
(2,'EC','22428');

/*Table structure for table `group_members` */

DROP TABLE IF EXISTS `group_members`;

CREATE TABLE `group_members` (
  `member_id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`member_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `group_members` */

insert  into `group_members`(`member_id`,`group_id`,`user_id`) values 
(1,1,5),
(2,1,4),
(3,2,1),
(4,2,4),
(5,3,2);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(50) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `user_type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`user_type`) values 
(1,'admin','admin','admin'),
(2,'anandhu@gmail.com','92622','minister'),
(3,'nibil@gmail.com','62783','minister'),
(4,'adhish@gmail.com','81248','officer'),
(5,'fasil@gmail.com','80114','officer');

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
(2,'anandhu','/static/minister/220411-100040.jpg','matttu','anandhu@gmail.com','/static/photo/220411-100040.jpg',9875641258,'Kasargod','radio'),
(3,'nibil','/static/minister/220411-100136.jpg','vadamukku','nibil@gmail.com','/static/photo/220411-100136.jpg',9856325678,'kozhikode','radio');

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
  `o_gender` varchar(50) DEFAULT NULL,
  `imei` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `officer` */

insert  into `officer`(`officer_id`,`officer_name`,`officer_email`,`officer_contactnumber`,`officer_proof`,`officer_photo`,`officer_district`,`officer_place`,`o_gender`,`imei`) values 
(4,'adhish','adhish@gmail.com',9785632156,'/static/officer/220411-100232.jpg','/static/photo/220411-100232.jpg','malappuram','maranchry','radio','356786103846261'),
(5,'fasil','fasil@gmail.com',9756841258,'/static/officer/220411-100329.jpg','/static/photo/220411-100329.jpg','thriuvanathpuram','mukkala','radio','356787103846269');

/*Table structure for table `suggestions` */

DROP TABLE IF EXISTS `suggestions`;

CREATE TABLE `suggestions` (
  `suggestion_id` int(11) NOT NULL AUTO_INCREMENT,
  `minister_id` int(11) DEFAULT NULL,
  `suggestion_date` date DEFAULT NULL,
  `suggestion_content` varchar(500) DEFAULT NULL,
  `reply` varchar(500) DEFAULT NULL,
  `reply_date` date DEFAULT NULL,
  PRIMARY KEY (`suggestion_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `suggestions` */

insert  into `suggestions`(`suggestion_id`,`minister_id`,`suggestion_date`,`suggestion_content`,`reply`,`reply_date`) values 
(1,2,'2022-04-11','error ','pkkk','2022-04-12'),
(2,2,'2022-04-11','nothing\r\n','oooh','2022-04-12'),
(3,2,'2022-04-12','chat isnt working\r\n','okkk','2022-04-12'),
(4,2,'2022-04-12','error','ohhhh','2022-04-12'),
(5,2,'2022-04-12','ohhhhhhooh','pending','0000-00-00'),
(6,3,'2022-04-12','complaint session missing','pending','0000-00-00');

/*Table structure for table `xor_key` */

DROP TABLE IF EXISTS `xor_key`;

CREATE TABLE `xor_key` (
  `xor_id` int(11) NOT NULL AUTO_INCREMENT,
  `document_id` int(11) DEFAULT NULL,
  `key_1` bigint(20) DEFAULT NULL,
  `key_2` bigint(20) DEFAULT NULL,
  `key_3` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`xor_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `xor_key` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
