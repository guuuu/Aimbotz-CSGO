-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 02, 2020 at 02:23 AM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.3.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `aimbotz`
--

-- --------------------------------------------------------

--
-- Table structure for table `times`
--

CREATE TABLE `times` (
  `id` int(11) NOT NULL,
  `d` date NOT NULL,
  `t` varchar(500) COLLATE utf8_bin NOT NULL,
  `a` varchar(5) COLLATE utf8_bin NOT NULL,
  `bt` varchar(5) COLLATE utf8_bin NOT NULL,
  `wt` varchar(5) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `times`
--

INSERT INTO `times` (`id`, `d`, `t`, `a`, `bt`, `wt`) VALUES
(8, '2020-06-25', '82/73/67/65/70/69/61/65/69/71', '69.0', '61', '82'),
(9, '2020-06-26', '71/61/61', '64.0', '61', '71'),
(10, '2020-06-27', '68/61/63/62/70/63/64/61/63/57', '62.0', '57', '70'),
(11, '2020-06-28', '63/60/58/61/59/62/60/55/60/58', '60.0', '55', '63'),
(12, '2020-06-29', '61/64/61/60/59/56/61/57/61/61', '60.0', '56', '64'),
(13, '2020-06-30', '65/62/61/59/62/57/61/57/59/62', '60.0', '57', '65'),
(14, '2020-07-01', '63/60/64/62/58/59/57/57/60/56', '60.0', '56', '64'),
(15, '2020-07-02', '57/61/57/59/58/60/61/61/59/55', '59.0', '55', '61'),
(16, '2020-07-03', '58/55/54/58/59/56/55/59/59/58', '57.0', '54', '59'),
(17, '2020-07-04', '60/59/55/61/61/57/52/57/55/58', '58.0', '52', '61'),
(18, '2020-07-05', '57/58/55/60/59/63/57/58/60/58', '58.0', '55', '63'),
(19, '2020-07-07', '66/58/58/64/63/59/60', '61.0', '58', '66'),
(20, '2020-07-08', '56/60/61/62/57/55/51/52/55/53', '56.0', '51', '62'),
(21, '2020-08-01', '58/57/45', '53.0', '45', '58'),
(23, '2020-08-02', '45/56/67', '56.0', '45', '67');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `times`
--
ALTER TABLE `times`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `times`
--
ALTER TABLE `times`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
