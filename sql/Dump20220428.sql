CREATE DATABASE  IF NOT EXISTS `MedicineManagementSystem` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `MedicineManagementSystem`;
-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: tars-knock.cn    Database: MedicineManagementSystem
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tb_customer`
--

DROP TABLE IF EXISTS `tb_customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_customer` (
  `Customer_id` char(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `Customer_name` char(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `Customer_phone` char(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `Customer_addr` char(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `isdelete` tinyint DEFAULT '0',
  PRIMARY KEY (`Customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_customer`
--

LOCK TABLES `tb_customer` WRITE;
/*!40000 ALTER TABLE `tb_customer` DISABLE KEYS */;
INSERT INTO `tb_customer` VALUES ('C0001','卫闰朴','15600000000','北京市昌平区沙河镇南丰路一号北京邮电大学沙河校区',0);
/*!40000 ALTER TABLE `tb_customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_dispatch`
--

DROP TABLE IF EXISTS `tb_dispatch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_dispatch` (
  `disp_id` char(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `account` char(20) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `out_id` char(20) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `disp_date` date NOT NULL,
  PRIMARY KEY (`disp_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_dispatch`
--

LOCK TABLES `tb_dispatch` WRITE;
/*!40000 ALTER TABLE `tb_dispatch` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_dispatch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_draftorder`
--

DROP TABLE IF EXISTS `tb_draftorder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_draftorder` (
  `draftorder_id` char(20) NOT NULL,
  `sale_id` char(20) NOT NULL,
  `goods_id` char(20) NOT NULL,
  `order_num` int NOT NULL,
  `supplier_id` char(20) NOT NULL,
  `account_id` char(20) NOT NULL,
  `date` date NOT NULL,
  `isfinish` tinyint NOT NULL DEFAULT '0',
  `isdelete` tinyint NOT NULL DEFAULT '0',
  PRIMARY KEY (`draftorder_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_draftorder`
--

LOCK TABLES `tb_draftorder` WRITE;
/*!40000 ALTER TABLE `tb_draftorder` DISABLE KEYS */;
INSERT INTO `tb_draftorder` VALUES ('DB2022040002','S2022040001','P0002',601,'G0002','4','2022-04-28',1,0);
/*!40000 ALTER TABLE `tb_draftorder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_goods`
--

DROP TABLE IF EXISTS `tb_goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_goods` (
  `goods_id` char(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `goods_name` char(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `goods_number` int NOT NULL,
  `price_cost` char(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `price_sell` char(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `goods_unit` char(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `supplier_id` char(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `isdelete` tinyint DEFAULT '0',
  PRIMARY KEY (`goods_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_goods`
--

LOCK TABLES `tb_goods` WRITE;
/*!40000 ALTER TABLE `tb_goods` DISABLE KEYS */;
INSERT INTO `tb_goods` VALUES ('P0001','阿莫西林软胶囊',10,'10','20','盒','G0001',0),('P0002','ラブ',649,'500','1000','个','G0002',0),('P0003','曼珠沙华',100,'20','40','盆','G0002',0);
/*!40000 ALTER TABLE `tb_goods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_inbound`
--

DROP TABLE IF EXISTS `tb_inbound`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_inbound` (
  `in_id` char(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `order_id` char(20) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `goods_id` char(20) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `account` char(20) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `in_date` date NOT NULL,
  `in_num` int DEFAULT NULL,
  PRIMARY KEY (`in_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_inbound`
--

LOCK TABLES `tb_inbound` WRITE;
/*!40000 ALTER TABLE `tb_inbound` DISABLE KEYS */;
INSERT INTO `tb_inbound` VALUES ('I2022040001','B2022040002','P0002','4','2022-04-27',400),('I2022040002','B2022040003','P0002','4','2022-04-28',250);
/*!40000 ALTER TABLE `tb_inbound` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_manager`
--

DROP TABLE IF EXISTS `tb_manager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_manager` (
  `account` char(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `password` char(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `manager_name` char(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `partment` char(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`account`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_manager`
--

LOCK TABLES `tb_manager` WRITE;
/*!40000 ALTER TABLE `tb_manager` DISABLE KEYS */;
INSERT INTO `tb_manager` VALUES ('1','1','销售员','销售部门'),('2','2','仓库管理员','仓库部门'),('3','3','采购员','采购部门'),('4','4','总管理员','超级管理员');
/*!40000 ALTER TABLE `tb_manager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_order`
--

DROP TABLE IF EXISTS `tb_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_order` (
  `order_id` char(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `account` char(20) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `Supplier_id` char(20) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `order_left` int DEFAULT NULL,
  `order_date` date NOT NULL,
  `goods_id` char(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `order_flag` char(20) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `order_number` int DEFAULT NULL,
  PRIMARY KEY (`order_id`,`goods_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_order`
--

LOCK TABLES `tb_order` WRITE;
/*!40000 ALTER TABLE `tb_order` DISABLE KEYS */;
INSERT INTO `tb_order` VALUES ('B2022040001','4','G0001',1,'2022-04-27','P0001','未入库',1),('B2022040002','4','G0002',100,'2022-04-27','P0002','未入库数量：100',500),('B2022040003','4','G0002',0,'2022-04-28','P0002','已入库',250),('B2022040003','4','G0002',50,'2022-04-28','P0003','未入库数量：50',100);
/*!40000 ALTER TABLE `tb_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_outbound`
--

DROP TABLE IF EXISTS `tb_outbound`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_outbound` (
  `out_id` char(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `sale_id` char(20) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `goods_id` char(20) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `account` char(20) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `out_date` date NOT NULL,
  `out_num` int DEFAULT NULL,
  `out_flag` char(20) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`out_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_outbound`
--

LOCK TABLES `tb_outbound` WRITE;
/*!40000 ALTER TABLE `tb_outbound` DISABLE KEYS */;
INSERT INTO `tb_outbound` VALUES ('O2022040001','S2022040001','P0002','4','2022-04-28',1000,'未发货');
/*!40000 ALTER TABLE `tb_outbound` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_return`
--

DROP TABLE IF EXISTS `tb_return`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_return` (
  `re_id` char(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `account` char(20) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `order_id` char(20) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `goods_id` char(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `re_date` date NOT NULL,
  PRIMARY KEY (`re_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_return`
--

LOCK TABLES `tb_return` WRITE;
/*!40000 ALTER TABLE `tb_return` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_return` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_sale`
--

DROP TABLE IF EXISTS `tb_sale`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_sale` (
  `sale_id` char(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `account_id` char(20) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `Customer_id` char(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `goods_id` char(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `sale_date` date DEFAULT NULL,
  `sale_number` int NOT NULL,
  `sale_left` int NOT NULL,
  `sale_flag` char(20) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`sale_id`,`goods_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_sale`
--

LOCK TABLES `tb_sale` WRITE;
/*!40000 ALTER TABLE `tb_sale` DISABLE KEYS */;
INSERT INTO `tb_sale` VALUES ('S2022040001','4','C0001','P0002','2022-04-28',2000,1000,'未出库数量：1000');
/*!40000 ALTER TABLE `tb_sale` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_supplier`
--

DROP TABLE IF EXISTS `tb_supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_supplier` (
  `Supplier_id` char(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `Supplier_name` char(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `Supplier_contactor` char(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `Supplier_phone` char(20) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `Supplier_addr` char(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `isdelete` tinyint DEFAULT '0',
  PRIMARY KEY (`Supplier_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_supplier`
--

LOCK TABLES `tb_supplier` WRITE;
/*!40000 ALTER TABLE `tb_supplier` DISABLE KEYS */;
INSERT INTO `tb_supplier` VALUES ('G0001','测试供应商','Domiko','123456789','北京市昌平区沙河镇',0),('G0002','私たちの小屋','卫闰朴','15555555555','河北省保定市望都县赵庄乡赵庄村151号',0);
/*!40000 ALTER TABLE `tb_supplier` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-28 18:07:43
