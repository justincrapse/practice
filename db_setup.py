SQL_SETUP = """
DROP TABLE IF EXISTS flights;
CREATE TABLE flights(
    flight_id INT,
    plane_id INT,
    PRIMARY KEY (flight_id));

DROP TABLE IF EXISTS planes;
CREATE TABLE planes(
    plane_id INT,
    number_of_seats INT,
    PRIMARY KEY (plane_id));

INSERT INTO planes
    (plane_id, number_of_seats)
    VALUES
    (128, 5),
    (23, 7),
    (157, 4),
    (239, 2);

DROP TABLE IF EXISTS purchases;
CREATE TABLE purchases(
    purchase_id INT AUTO_INCREMENT,
    flight_id INT,
    seat_no INT,
    PRIMARY KEY (purchase_Id));

INSERT INTO purchases
    (flight_id, seat_no)
    VALUES
    (111, 1),
    (87, 1),
    (87, 7),
    (100, 5);

DROP TABLE IF EXISTS shwang;
create table shwang(
    shwang_id int(4) auto_increment,
    shwang_name varchar(50),
    primary key (shwang_id));

show tables;
"""