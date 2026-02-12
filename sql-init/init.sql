CREATE DATABASE IF NOT EXISTS test17;

USE test17;

CREATE TABLE IF NOT EXISTS orders (
        orderNumber int,
        orderDate varchar(50),
        requiredDate varchar(50),
        shippedDate varchar(50),
        status varchar(50),
        comments varchar(50),
        customerNumber int
    ) ;

CREATE TABLE IF NOT EXISTS customers (
        customerNumber int,
        customerName varchar(50),
        contactLastName varchar(50),
        contactFirstName  varchar(50),
        phone varchar(50),
        addressLine1 varchar(50),
        addressLine2 varchar(50),
        city varchar(50),
        state varchar(50),
        postalCode int,
        country varchar(50),
        salesRepEmployeeNumber int,
        creditLimit float
    );

