DROP TABLE IF EXISTS dealer;
DROP TABLE IF EXISTS sale;

CREATE TABLE dealer (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  fullname VARCHAR(255) NOT NULL,
  cpf VARCHAR(255) UNIQUE NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE sale (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  cod INTEGER UNIQUE NOT NULL,
  value FLOAT(2) NOT NULL,
  date TEXT NOT NULL,
  cpf VARCHAR(255) NOT NULL,
  status VARCHAR(30) NOT NULL DEFAULT 'EM VALIDACAO',
  FOREIGN KEY (cpf) REFERENCES dealer (cpf)
);