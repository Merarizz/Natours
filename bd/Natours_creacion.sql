-- MySQL dump 10.13  Distrib 8.3.0, for Win64 (x86_64)
--
-- Host: localhost    Database: Natours
-- ------------------------------------------------------
-- Server version	8.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;



-- Creacion de la base de datos
DROP Database IF EXISTS Natours;
CREATE Database Natours;

-- Creacion del usuario
DROP user IF EXISTS 'natours_user'@'localhost';
create user 'natours_user'@'localhost' identified by '2411';
grant all on Natours.* to 'natours_user'@'localhost';
use Natours;
--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `id_cliente` int NOT NULL auto_increment,
  `nombre` varchar(30) NOT NULL,
  `ap_pat` varchar(30) NOT NULL,
  `ap_mat` varchar(30) NOT NULL,
  `curp` varchar(20) NOT NULL,
  `telefono` varchar(15) NOT NULL,
  `nom_empresa` varchar(20) NOT NULL,
  `id_direccion` int NOT NULL,
  `correo` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id_cliente`),
  KEY `id_direccion` (`id_direccion`),
  CONSTRAINT `clientes_ibfk_1` FOREIGN KEY (`id_direccion`) REFERENCES `direcciones` (`id_direccion`) on delete cascade on update cascade
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cp`
--

DROP TABLE IF EXISTS `cp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cp` (
  `id_cp` int NOT NULL auto_increment,
  `cp` int NOT NULL,
  `colonia` varchar(100) NOT NULL,
  `ciudad` varchar(50) NOT NULL,
  `estado` varchar(50) NOT NULL,
  `id_pais` int NOT NULL,
  PRIMARY KEY (`id_cp`),
  KEY `id_pais` (`id_pais`),
  CONSTRAINT `cp_ibfk_1` FOREIGN KEY (`id_pais`) REFERENCES `paises` (`id_pais`) on delete cascade on update cascade
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cp`
--

LOCK TABLES `cp` WRITE;
/*!40000 ALTER TABLE `cp` DISABLE KEYS */;
/*!40000 ALTER TABLE `cp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `direcciones`
--

DROP TABLE IF EXISTS `direcciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `direcciones` (
  `id_direccion` int NOT NULL auto_increment,
  `calle` varchar(30) NOT NULL,
  `no_exterior` int NOT NULL,
  `no_interior` varchar(10) NOT NULL,
  `id_cp` int NOT NULL,
  PRIMARY KEY (`id_direccion`),
  KEY `id_cp` (`id_cp`),
  CONSTRAINT `direcciones_ibfk_1` FOREIGN KEY (`id_cp`) REFERENCES `cp` (`id_cp`) on delete cascade on update cascade
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direcciones`
--

LOCK TABLES `direcciones` WRITE;
/*!40000 ALTER TABLE `direcciones` DISABLE KEYS */;
/*!40000 ALTER TABLE `direcciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empleados`
--

DROP TABLE IF EXISTS `empleados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empleados` (
  `id_empleado` int NOT NULL auto_increment,
  `nombre` varchar(30) NOT NULL,
  `ap_pat` varchar(30) NOT NULL,
  `ap_mat` varchar(30) NOT NULL,
  `curp` varchar(20) NOT NULL,
  `NSS` int NOT NULL,
  `telefono` varchar(15) NOT NULL,
  `id_direccion` int NOT NULL,
  `puesto` varchar(20) NOT NULL,
  `acceso` int NOT NULL,
  `correo` varchar(30) NOT NULL,
  `contraseña` varchar(10) NOT NULL,
  `sueldo` decimal(8,2) NOT NULL,
  `comision` decimal(4,2) NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_final` date,
  `estatus` varchar(20) NOT NULL DEFAULT (_cp850'activo'),
  PRIMARY KEY (`id_empleado`),
  KEY `id_direccion` (`id_direccion`),
  CONSTRAINT `empleados_ibfk_1` FOREIGN KEY (`id_direccion`) REFERENCES `direcciones` (`id_direccion`) on delete cascade on update cascade
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empleados`
--

LOCK TABLES `empleados` WRITE;
/*!40000 ALTER TABLE `empleados` DISABLE KEYS */;
/*!40000 ALTER TABLE `empleados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `facturas`
--

DROP TABLE IF EXISTS `facturas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `facturas` (
  `id_factura` int NOT NULL auto_increment,
  `id_empleado` int NOT NULL,
  `id_cliente` int NOT NULL,
  `fecha` date NOT NULL,
  `total` decimal(10,2) NOT NULL,
  `status` varchar(30) NOT NULL,
  PRIMARY KEY (`id_factura`),
  KEY `id_empleado` (`id_empleado`),
  KEY `id_cliente` (`id_cliente`),
  CONSTRAINT `facturas_ibfk_1` FOREIGN KEY (`id_empleado`) REFERENCES `empleados` (`id_empleado`) on delete cascade on update cascade,
  CONSTRAINT `facturas_ibfk_2` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id_cliente`) on delete cascade on update cascade
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `facturas`
--

LOCK TABLES `facturas` WRITE;
/*!40000 ALTER TABLE `facturas` DISABLE KEYS */;
/*!40000 ALTER TABLE `facturas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paises`
--

DROP TABLE IF EXISTS `paises`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paises` (
  `id_pais` int NOT NULL auto_increment,
  `nombre` varchar(50) NOT NULL,
  `prefijo` int NOT NULL DEFAULT (52),
  PRIMARY KEY (`id_pais`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paises`
--

LOCK TABLES `paises` WRITE;
/*!40000 ALTER TABLE `paises` DISABLE KEYS */;
/*!40000 ALTER TABLE `paises` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prospecto_servicio`
--

DROP TABLE IF EXISTS `prospecto_servicio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prospecto_servicio` (
  `id_prospecto_servicio` int NOT NULL auto_increment,
  `id_prospecto` int NOT NULL,
  `id_servicio` int NOT NULL,
  PRIMARY KEY (`id_prospecto_servicio`),
  KEY `id_prospecto` (`id_prospecto`),
  KEY `id_servicio` (`id_servicio`),
  CONSTRAINT `prospecto_servicio_ibfk_1` FOREIGN KEY (`id_prospecto`) REFERENCES `prospectos` (`id_prospecto`) on delete cascade on update cascade,
  CONSTRAINT `prospecto_servicio_ibfk_2` FOREIGN KEY (`id_servicio`) REFERENCES `servicios` (`id_servicio`) on delete cascade on update cascade
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prospecto_servicio`
--

LOCK TABLES `prospecto_servicio` WRITE;
/*!40000 ALTER TABLE `prospecto_servicio` DISABLE KEYS */;
/*!40000 ALTER TABLE `prospecto_servicio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prospectos`
--

DROP TABLE IF EXISTS `prospectos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prospectos` (
  `id_prospecto` int NOT NULL auto_increment,
  `empresa` varchar(20) NOT NULL,
  `telefono` varchar(15) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(100) DEFAULT NULL,
  `id_direccion` int NOT NULL,
  `correo` varchar(30) DEFAULT NULL,
  `ap_pat` varchar(30) DEFAULT NULL,
  `ap_mat` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id_prospecto`),
  KEY `id_direccion` (`id_direccion`),
  CONSTRAINT `prospectos_ibfk_1` FOREIGN KEY (`id_direccion`) REFERENCES `direcciones` (`id_direccion`) on delete cascade on update cascade
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prospectos`
--

LOCK TABLES `prospectos` WRITE;
/*!40000 ALTER TABLE `prospectos` DISABLE KEYS */;
/*!40000 ALTER TABLE `prospectos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servicios`
--

DROP TABLE IF EXISTS `servicios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `servicios` (
  `id_servicio` int NOT NULL auto_increment,
  `tipo_servicio` varchar(30) NOT NULL,
  `costo` decimal(10,2) NOT NULL,
  `detalles` varchar(200) DEFAULT NULL,
  `titulo` varchar(50) NOT NULL,
  `comision` decimal(4,2) NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_final` date NOT NULL,
  `restricciones` varchar(100) DEFAULT NULL,
  `subtipo` varchar(50) DEFAULT NULL,
  `ciudad` varchar(50) DEFAULT NULL,
  `estado` varchar(50) DEFAULT NULL,
  `pais` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_servicio`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servicios`
--

LOCK TABLES `servicios` WRITE;
/*!40000 ALTER TABLE `servicios` DISABLE KEYS */;
/*!40000 ALTER TABLE `servicios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ventas`
--

DROP TABLE IF EXISTS `ventas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ventas` (
  `id_venta` int NOT NULL auto_increment,
  `id_servicio` int NOT NULL,
  `id_factura` int NOT NULL,
  PRIMARY KEY (`id_venta`),
  KEY `id_servicio` (`id_servicio`),
  KEY `id_factura` (`id_factura`),
  CONSTRAINT `ventas_ibfk_1` FOREIGN KEY (`id_servicio`) REFERENCES `servicios` (`id_servicio`) on delete cascade on update cascade,
  CONSTRAINT `ventas_ibfk_2` FOREIGN KEY (`id_factura`) REFERENCES `facturas` (`id_factura`) on delete cascade on update cascade
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ventas`
--

LOCK TABLES `ventas` WRITE;
/*!40000 ALTER TABLE `ventas` DISABLE KEYS */;
/*!40000 ALTER TABLE `ventas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-02 11:31:15
