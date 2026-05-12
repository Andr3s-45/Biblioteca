-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 13-05-2026 a las 01:04:35
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `biblioteca_2`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `autores`
--

CREATE TABLE `autores` (
  `idAutor` varchar(10) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `idPais` varchar(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `editoriales`
--

CREATE TABLE `editoriales` (
  `idEditorial` varchar(5) NOT NULL,
  `nombre` varchar(40) NOT NULL,
  `idPais` varchar(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `lectores`
--

CREATE TABLE `lectores` (
  `idLector` varchar(10) NOT NULL,
  `nombre` varchar(40) DEFAULT NULL,
  `cupoLibros` int(11) DEFAULT NULL,
  `cupoPrestados` int(11) DEFAULT NULL,
  `enMora` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libros`
--

CREATE TABLE `libros` (
  `idLibro` varchar(12) NOT NULL,
  `titulo` varchar(50) NOT NULL,
  `idioma` varchar(10) NOT NULL,
  `idAutor` varchar(10) NOT NULL,
  `idEditorial` varchar(5) NOT NULL,
  `numeroEjemplares` int(11) DEFAULT NULL,
  `ejemplaresPrestados` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `paises`
--

CREATE TABLE `paises` (
  `idPais` varchar(2) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `continente` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prestamos`
--

CREATE TABLE `prestamos` (
  `idPrestamo` int(11) NOT NULL,
  `idLibro` varchar(12) DEFAULT NULL,
  `IdLector` varchar(10) DEFAULT NULL,
  `fechaPrestamo` date DEFAULT NULL,
  `fechaPresupuestadev` date DEFAULT NULL,
  `fechaRealdev` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `idUsuario` varchar(15) NOT NULL,
  `nombre` varchar(40) DEFAULT NULL,
  `contrasena` varchar(128) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`idUsuario`, `nombre`, `contrasena`) VALUES
('afv', 'Juan C Posada', '0549ab26aefcba2df2f37dc4a2820597b0142f86ac8984214951c44621b63d1696f03cc3093ba1c7c88a7259d5cc83e7396e1614d1a5f3c3c0ad96e70cdfd0d7'),
('frank', 'Frank', '1234'),
('hernando', 'Hernando', '4321');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `autores`
--
ALTER TABLE `autores`
  ADD PRIMARY KEY (`idAutor`),
  ADD KEY `idPais` (`idPais`);

--
-- Indices de la tabla `editoriales`
--
ALTER TABLE `editoriales`
  ADD PRIMARY KEY (`idEditorial`),
  ADD KEY `idPais` (`idPais`);

--
-- Indices de la tabla `lectores`
--
ALTER TABLE `lectores`
  ADD PRIMARY KEY (`idLector`);

--
-- Indices de la tabla `libros`
--
ALTER TABLE `libros`
  ADD PRIMARY KEY (`idLibro`),
  ADD KEY `idAutor` (`idAutor`),
  ADD KEY `idEditorial` (`idEditorial`);

--
-- Indices de la tabla `paises`
--
ALTER TABLE `paises`
  ADD PRIMARY KEY (`idPais`);

--
-- Indices de la tabla `prestamos`
--
ALTER TABLE `prestamos`
  ADD PRIMARY KEY (`idPrestamo`),
  ADD KEY `fkprestamoslibros` (`idLibro`),
  ADD KEY `fkprestamoslectores` (`IdLector`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`idUsuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `prestamos`
--
ALTER TABLE `prestamos`
  MODIFY `idPrestamo` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `autores`
--
ALTER TABLE `autores`
  ADD CONSTRAINT `autores_ibfk_1` FOREIGN KEY (`idPais`) REFERENCES `paises` (`idPais`);

--
-- Filtros para la tabla `editoriales`
--
ALTER TABLE `editoriales`
  ADD CONSTRAINT `editoriales_ibfk_1` FOREIGN KEY (`idPais`) REFERENCES `paises` (`idPais`);

--
-- Filtros para la tabla `libros`
--
ALTER TABLE `libros`
  ADD CONSTRAINT `libros_ibfk_1` FOREIGN KEY (`idAutor`) REFERENCES `autores` (`idAutor`),
  ADD CONSTRAINT `libros_ibfk_2` FOREIGN KEY (`idEditorial`) REFERENCES `editoriales` (`idEditorial`);

--
-- Filtros para la tabla `prestamos`
--
ALTER TABLE `prestamos`
  ADD CONSTRAINT `fkprestamoslectores` FOREIGN KEY (`IdLector`) REFERENCES `lectores` (`idLector`),
  ADD CONSTRAINT `fkprestamoslibros` FOREIGN KEY (`idLibro`) REFERENCES `libros` (`idLibro`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
