# django_backend_food_order

This repository is currently incomplete



The initial sql query generated within cmd via the model:

BEGIN;
--
-- Create model Customer
--
CREATE TABLE "restaurants_customer" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "customer_name" varchar(100) NOT NULL, "customer_email" varchar(254) NOT NULL);
--
-- Create model Item
--
CREATE TABLE "restaurants_item" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "item_name" varchar(100) NOT NULL, "item_description" varchar(400) NOT NULL, "item_price" integer NOT NULL);
--
-- Create model Order
--
CREATE TABLE "restaurants_order" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "order_customerId" integer NOT NULL, "order_restaurantId" integer NOT NULL, "order_status" smallint NOT NULL, "order_items" text NOT NULL CHECK ((JSON_VALID("order_items") OR "order_items" IS NULL)));
--
-- Create model Restaurant
--
CREATE TABLE "restaurants_restaurant" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "restaurant_name" varchar(100) NOT NULL);
COMMIT;

The second sql query:

BEGIN;
--
-- Add field item_seller to item
--
CREATE TABLE "new__restaurants_item" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "item_seller" integer unsigned NOT NULL CHECK ("item_seller" >= 0), "item_name" varchar(100) NOT NULL, "item_description" varchar(400) NOT NULL, "item_price" integer NOT NULL);
INSERT INTO "new__restaurants_item" ("id", "item_name", "item_description", "item_price", "item_seller") SELECT "id", "item_name", "item_description", "item_price", 1 FROM "restaurants_item";
DROP TABLE "restaurants_item";
ALTER TABLE "new__restaurants_item" RENAME TO "restaurants_item";
COMMIT;
