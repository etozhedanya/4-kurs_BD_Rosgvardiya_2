/* SQL Manager for MySQL                              5.8.0.53936 */
/* -------------------------------------------------------------- */
/* Host     : localhost                                           */
/* Port     : 3306                                                */
/* Database : ShemetovRG                                          */


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES 'utf8mb4' */;

SET FOREIGN_KEY_CHECKS=0;

DROP DATABASE IF EXISTS `shemetovrg`;

CREATE DATABASE `ShemetovRG`
    CHARACTER SET 'utf8mb4'
    COLLATE 'utf8mb4_general_ci';

USE `shemetovrg`;

SET sql_mode = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION';

/* Удаление объектов БД */

DROP TABLE IF EXISTS `sotrudniki`;
DROP TABLE IF EXISTS `sosttr`;
DROP TABLE IF EXISTS `transport`;
DROP TABLE IF EXISTS `otryad`;

/* Структура для таблицы `otryad`:  */

CREATE TABLE `otryad` (
  `IDOtr` INTEGER DEFAULT NULL,
  `Naznach` VARCHAR(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  KEY `IDOtr` USING BTREE (`IDOtr`)
) ENGINE=InnoDB
ROW_FORMAT=DYNAMIC CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci'
;

/* Data for the `otryad` table  (LIMIT 0,500) */

INSERT INTO `otryad` (`IDOtr`, `Naznach`) VALUES
  (1,'Патруль'),
  (2,'Выездная'),
  (3,'Штурмовая'),
  (4,'Митинговая'),
  (5,'Охранная');
COMMIT;

/* Структура для таблицы `transport`:  */

CREATE TABLE `transport` (
  `IDTr` INTEGER DEFAULT NULL,
  `NameTr` VARCHAR(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  KEY `IDTr` USING BTREE (`IDTr`)
) ENGINE=InnoDB
ROW_FORMAT=DYNAMIC CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci'
;

/* Data for the `transport` table  (LIMIT 0,500) */

INSERT INTO `transport` (`IDTr`, `NameTr`) VALUES
  (1,'Лада Калина'),
  (2,'Автозак'),
  (3,'Маршрутка \"13\"'),
  (4,'Лада Гранта'),
  (5,'Надувной Вертолет');
COMMIT;

/* Структура для таблицы `sosttr`:  */

CREATE TABLE `sosttr` (
  `IDOtr` INTEGER DEFAULT NULL,
  `IDTr` INTEGER DEFAULT NULL,
  KEY `sosttr_fk1` USING BTREE (`IDOtr`),
  KEY `sosttr_fk2` USING BTREE (`IDTr`),
  CONSTRAINT `sosttr_fk1` FOREIGN KEY (`IDOtr`) REFERENCES `otryad` (`IDOtr`),
  CONSTRAINT `sosttr_fk2` FOREIGN KEY (`IDTr`) REFERENCES `transport` (`IDTr`)
) ENGINE=InnoDB
ROW_FORMAT=DYNAMIC CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci'
;

/* Data for the `sosttr` table  (LIMIT 0,500) */

INSERT INTO `sosttr` (`IDOtr`, `IDTr`) VALUES
  (1,3),
  (2,1),
  (3,4),
  (4,2),
  (5,5);
COMMIT;

/* Структура для таблицы `sotrudniki`:  */

CREATE TABLE `sotrudniki` (
  `ID` INT UNSIGNED NOT NULL,
  `FIO` VARCHAR(30) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Gender` TINYINT(1) DEFAULT NULL,
  `Old` INTEGER DEFAULT NULL,
  `Zvanie` VARCHAR(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `IDOtr` INTEGER DEFAULT NULL,
  PRIMARY KEY USING BTREE (`ID`),
  KEY `sotrudniki_fk1` USING BTREE (`IDOtr`),
  CONSTRAINT `sotrudniki_fk1` FOREIGN KEY (`IDOtr`) REFERENCES `otryad` (`IDOtr`)
) ENGINE=InnoDB
ROW_FORMAT=DYNAMIC CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci'
;

/* Data for the `sotrudniki` table  (LIMIT 0,500) */

INSERT INTO `sotrudniki` (`ID`, `FIO`, `Gender`, `Old`, `Zvanie`, `IDOtr`) VALUES
  (1,'Зубенко Михаил Петрович',1,40,'Вор в законе',1),
  (2,'Жмышенко Валерий Альбертович',1,54,'Полковник',2),
  (3,'Жабакова Джамиля Сержановна',0,18,'Генерал',3),
  (4,'Шеметов Даниил Александрович',1,18,'Рядовой',4),
  (5,'Моргенштерн Алишер Тагирович',1,22,'Майор',5),
  (6,'Паркер Питер Бэнович',1,21,'Сержант',1),
  (7,'Поклонская Наталья Владимировн',0,36,'Майор',2),
  (8,'Путин Владимир Владимирович',1,69,'Генерал',3),
  (9,'Навальный Алексей Анатольевич',1,45,'Сержант',4),
  (10,'Лавров Сергей Викторович',1,65,'Майор',5),
  (11,'Мединский Владимир Петрович',1,43,'Полковник',1),
  (12,'Деренченко Евгений Николаевич',1,20,'Рядовой',2),
  (13,'Тарасюк Данил Николаевич',1,19,'Рядовой',3),
  (14,'Дорошенко Марина Викторовна',0,20,'Сержант',4),
  (15,'Соловьев Владимир Какойтович',1,50,'Уборщик',5);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;