CREATE TABLE "Customer" (
  "Cusomter_id" varchar PRIMARY KEY,
  "Country" varchar
);

CREATE TABLE "Invoice" (
  "InvoiceNo" int PRIMARY KEY,
  "Cusomter_id" varchar,
  "InvoiceDate" timestamp
);

CREATE TABLE "stock_code" (
  "Id_stock" int PRIMARY KEY,
  "StockCode" varchar,
  "UnitPrice" double,
  "Description" varchar,
  "Quantity" int
);

CREATE TABLE "invoice_stock" (
  "Id_invoice_stock" int PRIMARY KEY,
  "InvoiceNo" int,
  "Id_stock" int
);

ALTER TABLE "Invoice" ADD FOREIGN KEY ("Cusomter_id") REFERENCES "Customer" ("Cusomter_id");

ALTER TABLE "invoice_stock" ADD FOREIGN KEY ("InvoiceNo") REFERENCES "Invoice" ("InvoiceNo");

ALTER TABLE "invoice_stock" ADD FOREIGN KEY ("Id_stock") REFERENCES "stock_code" ("Id_stock");
