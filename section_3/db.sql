-- phpMyAdmin SQL Dump
-- version 4.4.9
-- http://www.phpmyadmin.net
--
-- Host: localhost:8889
-- Generation Time: Nov 24, 2015 at 05:52 PM
-- Server version: 5.5.42
-- PHP Version: 5.6.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `addressbook`
--

-- --------------------------------------------------------

--
-- Table structure for table `Address`
--

CREATE TABLE `Address` (
  `ID` int(11) NOT NULL,
  `Address` text COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `Address`
--

INSERT INTO `Address` (`ID`, `Address`) VALUES
(1, 'Some street, 555'),
(2, 'Some street, 554');

-- --------------------------------------------------------

--
-- Table structure for table `People`
--

CREATE TABLE `People` (
  `ID` int(11) NOT NULL,
  `Firstname` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `Lastname` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `People`
--

INSERT INTO `People` (`ID`, `Firstname`, `Lastname`) VALUES
(1, 'John', 'Doe'),
(2, 'Jane', 'Doe');

-- --------------------------------------------------------

--
-- Table structure for table `PersonAddress`
--

CREATE TABLE `PersonAddress` (
  `PersonID` int(11) NOT NULL,
  `AddressID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `PersonAddress`
--

INSERT INTO `PersonAddress` (`PersonID`, `AddressID`) VALUES
(1, 2),
(2, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `People`
--
ALTER TABLE `People`
  ADD PRIMARY KEY (`ID`);
