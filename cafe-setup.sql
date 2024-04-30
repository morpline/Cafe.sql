CREATE SCHEMA IF NOT EXISTS cafe;

CREATE TABLE IF NOT EXISTS cafe.menu (
    name text,
    ingredients text[],
    price numeric,
    _id integer UNIQUE NOT NULL
);
CREATE TABLE IF NOT EXISTS cafe.orders (
    _id integer UNIQUE NOT NULL,
    name text,
    customerid integer,
    products integer[],
    discounts text[],
    cost numeric
);
CREATE TABLE IF NOT EXISTS cafe.customers (
    _id integer UNIQUE NOT NULL,
    fullname text,
    email text,
    phone text,
    rewardpoints integer
);
CREATE TABLE IF NOT EXISTS cafe.discounts (
    _id integer UNIQUE NOT NULL,
    name text,
    type float,
    expires date,
    items integer[]
);