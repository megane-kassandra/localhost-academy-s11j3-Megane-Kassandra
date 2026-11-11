-- LOCALHOST ACADEMY | Semaine 11 - Jour 3
-- Mini-projet : Gestion d'un hotel
-- Importer ce script dans DB Browser for SQLite pour creer hotel.db.
-- Donnees fictives destinees aux exercices CRUD Python.
-- ATTENTION : ce script est concu pour une base SQLite neuve.

PRAGMA foreign_keys = ON;
BEGIN TRANSACTION;

-- 1. Clients
CREATE TABLE clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);

-- 2. Chambres
CREATE TABLE chambres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero TEXT NOT NULL UNIQUE,
    prix_nuit REAL NOT NULL CHECK (prix_nuit > 0)
);

-- 3. Reservations : chaque reservation relie un client et une chambre.
-- Les dates sont stockees au format ISO AAAA-MM-JJ.
CREATE TABLE reservations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    chambre_id INTEGER NOT NULL,
    date_debut TEXT NOT NULL,
    date_fin TEXT NOT NULL,
    FOREIGN KEY (client_id) REFERENCES clients(id),
    FOREIGN KEY (chambre_id) REFERENCES chambres(id),
    CHECK (date_fin > date_debut)
);

-- Jeu de depart : 3 clients
INSERT INTO clients (id, nom, email) VALUES
    (1, 'Amina', 'amina@example.com'),
    (2, 'Paul', 'paul@example.com'),
    (3, 'Sara', 'sara@example.com');

-- Jeu de depart : 3 chambres (prix en euros par nuit)
INSERT INTO chambres (id, numero, prix_nuit) VALUES
    (1, '101', 45.00),
    (2, '102', 60.00),
    (3, '201', 85.00);

-- Jeu de depart : 2 reservations
INSERT INTO reservations (id, client_id, chambre_id, date_debut, date_fin) VALUES
    (1, 1, 1, '2026-11-10', '2026-11-12'),
    (2, 2, 2, '2026-11-13', '2026-11-15');

COMMIT;

-- Requetes de verification (resultats visibles dans « Executer le SQL »)
SELECT 'clients' AS table_nom, COUNT(*) AS nombre FROM clients
UNION ALL
SELECT 'chambres', COUNT(*) FROM chambres
UNION ALL
SELECT 'reservations', COUNT(*) FROM reservations;

SELECT r.id, c.nom AS client, ch.numero AS chambre,
       r.date_debut, r.date_fin
FROM reservations AS r
JOIN clients AS c ON c.id = r.client_id
JOIN chambres AS ch ON ch.id = r.chambre_id
ORDER BY r.id;
