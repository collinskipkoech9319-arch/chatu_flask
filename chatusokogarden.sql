-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Feb 25, 2026 at 06:15 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `chatusokogarden`
--

-- --------------------------------------------------------

--
-- Table structure for table `product_details`
--

CREATE TABLE `product_details` (
  `product_id` int(11) NOT NULL,
  `product_name` varchar(255) NOT NULL,
  `product_description` text DEFAULT NULL,
  `product_cost` int(11) DEFAULT NULL,
  `product_photo` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product_details`
--

INSERT INTO `product_details` (`product_id`, `product_name`, `product_description`, `product_cost`, `product_photo`) VALUES
(1, 'Dalemere yoghurt', 'Strawberry flavor', 150, '<FileStorage: \'cdc-GDokEYnOfnE-unsplash.jpg\' (\'image/jpeg\')>'),
(2, 'Royal youghurt', 'apple flavor', 250, '<FileStorage: \'national-cancer-institute-N_aihp118p8-unsplash.jpg\' (\'image/jpeg\')>'),
(3, 'Daima Pure test', 'starwberry flavor', 200, 'andrew-ebrahim-zRwXf6PizEo-unsplash (copy).jpg'),
(4, 'DailyFresh Delight', 'Nature flavor', 180, 'thomas-park-6MePtA9EVDA-unsplash.jpg'),
(5, 'Delight Moments', 'Nature flavor', 190, 'budi-gustaman--Qe_hAGqYlA-unsplash.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `username`, `password`, `email`, `phone`) VALUES
(1, 'Harrison', '12345', 'harrison.com', '0712345678'),
(2, 'Ishmael', '23454', 'ishmael.com', '0798654321'),
(3, 'Evra', '34567', 'evra@.com', '0786543217'),
(4, 'Enock', '45678', 'enock@.com', '0112345672'),
(5, 'Francis', '32456', 'francis@.com', '0765432432'),
(6, 'Mery', '1234', 'mary@gmail.com', '0768321423'),
(7, 'Alan', '3245', 'alan@gmail.com', '0754321567'),
(9, 'Ezra', '4567', 'ezra@gmail.com', '0755678987'),
(10, 'Amos', '3267', 'amos@gmail.com', '0743215345'),
(11, 'Evans', '6574', 'evans@gmail.com', '07865432143'),
(12, 'Naomi', '5678', 'naomi@gmail.com', '0785432123'),
(13, 'Caleb', '4356', 'caleb@gmail.com', '0776890654'),
(14, 'Calos', '5675', 'calos@gmail.com', '0798675654'),
(15, 'Tabitha', '5674', 'tabitha@gmail.com', '0794567432'),
(16, 'Ruth', '9876', 'ruth@gmail.com', '0756432321'),
(17, 'Dorcas', '9987', 'dorcas@gmail.com', '078654321'),
(18, 'Brian', '9234', 'brian@gmail.com', '0765432876'),
(22, 'Harrison', '12345', 'harrison@gmail.com', '078654321');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `product_details`
--
ALTER TABLE `product_details`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `product_details`
--
ALTER TABLE `product_details`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
