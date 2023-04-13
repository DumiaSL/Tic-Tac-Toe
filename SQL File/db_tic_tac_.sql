-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Aug 19, 2021 at 03:34 PM
-- Server version: 5.7.26
-- PHP Version: 7.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_tic_tac`
--
CREATE DATABASE IF NOT EXISTS `db_tic_tac` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `db_tic_tac`;

-- --------------------------------------------------------

--
-- Table structure for table `mytable`
--

DROP TABLE IF EXISTS `mytable`;
CREATE TABLE IF NOT EXISTS `mytable` (
  `rec_num` int(10) NOT NULL,
  `date_and_time` varchar(25) DEFAULT NULL,
  `player_1` varchar(10) DEFAULT NULL,
  `player_2` varchar(10) DEFAULT NULL,
  `winner` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`rec_num`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mytable`
--

INSERT INTO `mytable` (`rec_num`, `date_and_time`, `player_1`, `player_2`, `winner`) VALUES
(18, '08/19/2021	20:18:54', 'Kaveen', 'Tharuka', 'Match tied'),
(17, '08/19/2021	18:47:26', 'Sanjula', 'Dulaj', 'Dulaj'),
(16, '08/19/2021	18:23:28', 'Kaveesha', 'Dumindu', 'Match tied'),
(15, '08/19/2021	18:05:35', 'Dumindu', 'Ravindu', 'Dumindu'),
(14, '08/19/2021	18:00:22', 'Shehara', 'Amindu', 'Shehara'),
(13, '08/19/2021	17:47:49', 'Shalith', 'Kavindu', 'Match tied'),
(12, '08/19/2021	17:38:45', 'Tharindu', 'Maneesha', 'Tharindu'),
(11, '08/19/2021	17:38:01', 'Shakila', 'Dilshan', 'Match tied'),
(10, '08/19/2021	17:34:07', 'Maneesha', 'Janith', 'Maneesha'),
(9, '08/19/2021	17:23:26', 'Janith', 'Dinesh', 'Janith'),
(8, '08/19/2021	17:14:02', 'Tharindu', 'Janith', 'Match tied'),
(7, '08/19/2021	16:56:20', 'Maneesha', 'Dinesh', 'Maneesha'),
(6, '08/19/2021	16:45:16', 'Dinesh', 'Thirul', 'Thirul'),
(5, '08/19/2021	16:32:00', 'Tharindu', 'Heshan', 'Heshan'),
(4, '08/19/2021	16:20:14', 'Thirul', 'Mindiya', 'Mindiya'),
(3, '08/19/2021	15:49:58', 'Heshan', 'Kavindu', 'Heshan'),
(2, '08/19/2021	15:31:19', 'Maneesha', 'Shehara', 'Maneesha'),
(1, '08/19/2021	15:03:53', 'Tharindu', 'Dulaj', 'Tharindu');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
