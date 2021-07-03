/*
Navicat MySQL Data Transfer

Source Server         : 本地数据库
Source Server Version : 50729
Source Host           : localhost:3306
Source Database       : testproject

Target Server Type    : MYSQL
Target Server Version : 50729
File Encoding         : 65001

Date: 2020-09-23 17:28:00
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for order_info
-- ----------------------------
DROP TABLE IF EXISTS `order_info`;
CREATE TABLE `order_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `type` varchar(11) NOT NULL,
  `dep` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `system` varchar(255) DEFAULT NULL,
  `desc` varchar(255) NOT NULL,
  `status` char(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=287 DEFAULT CHARSET=utf8;
