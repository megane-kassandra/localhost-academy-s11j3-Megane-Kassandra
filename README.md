# Projet Hôtel modulaire

**LocalHost Academy — Programme Python Full-Stack**  
**Semaine 11, Jour 3**

**Nom et prénom :** MATSINKOU TAKOUDJOU MEGANE KASSANDRA

## 1. Présentation du projet

Ce projet consiste à développer une application console en Python pour la gestion d'un petit hôtel. Elle permet de consulter les chambres et les réservations, puis d'ajouter, de modifier et de supprimer des réservations.

L'application utilise une base de données SQLite créée à partir du fichier `hotel.sql` fourni par l'enseignant.

## 2. Modèle de données

La base de données contient trois tables liées :

- **`clients`** : `id`, `nom`, `email`. Cette table contient les informations des clients.
- **`chambres`** : `id`, `numero`, `prix_nuit`. Cette table contient les informations des chambres.
- **`reservations`** : `id`, `client_id`, `chambre_id`, `date_debut`, `date_fin`. Cette table enregistre les réservations. Chaque réservation concerne un seul client et une seule chambre.

Un client et une chambre peuvent apparaître dans plusieurs réservations à des dates différentes.

## 3. Organisation des fichiers

| Fichier | Rôle |
|---|---|
| `hotel.sql` | Script SQL fourni par l'enseignant. Il contient la création des tables, les contraintes et les données initiales. Il permet de reconstruire la base. |
| `db.py` | Définit le chemin de la base et la fonction `get_connection()`, qui ouvre une connexion SQLite et active les clés étrangères avec `PRAGMA foreign_keys = ON`. |
| `models.py` | Contient les fonctions de consultation des chambres et des réservations ainsi que les opérations de création, modification et suppression des réservations. La logique SQL reste dans ce module. |
| `main.py` | Point d'entrée de l'application. Il affiche le menu, recueille les saisies et appelle les fonctions de `models.py`. |
| `verification_models.py` | Contient les tests manuels des fonctions définies dans `models.py`. |
| `recette.md` | Présente les scénarios de vérification de l'application et les résultats observés. |
| `.gitignore` | Indique les fichiers qui ne doivent pas être suivis par Git, notamment la base locale et les fichiers temporaires Python. |

## 4. Version de Python

Le projet est développé en **Python 3**.  

## 5. Création de la base de données

La base `hotel.db` doit être créée à partir du fichier `hotel.sql` avec **DB Browser for SQLite**.

1. Ouvrir DB Browser for SQLite.
2. Choisir **Fichier → Importer → Base de données depuis un fichier SQL** (le libellé peut varier selon la version).
3. Sélectionner le fichier `hotel.sql`.
4. Importer le script dans une nouvelle base SQLite.
5. Enregistrer la base sous le nom `hotel.db` dans le dossier du projet.

Le fichier `hotel.sql` contient déjà les instructions de création des tables, les contraintes et les données de départ. Il ne faut donc pas réécrire le schéma ni les insertions initiales. Il faut également éviter de réexécuter le script sur une base qui contient déjà les tables.

### Pourquoi utiliser `Path(__file__)` ?

Dans `db.py`, le chemin de la base est construit à partir de l'emplacement du fichier Python :

```python
DB_PATH = Path(__file__).resolve().parent / "hotel.db"
```

`__file__` désigne le fichier Python courant. `resolve()` donne son chemin absolu et `parent` désigne le dossier qui le contient. Ainsi, le programme retrouve `hotel.db` dans le dossier du projet, même si la commande est lancée depuis un autre dossier. Le chemin ne dépend donc pas du répertoire courant du terminal.

## 6. Lancement de l'application

Après avoir créé `hotel.db` et placé les fichiers dans le dossier du projet, ouvrir un terminal dans ce dossier et exécuter :

```bash
python main.py
```

Selon l'installation, la commande peut être :

```bash
python3 main.py
```

Le menu permet de :

1. Lister les chambres.
2. Lister les réservations.
3. Ajouter une réservation.
4. Modifier les dates d'une réservation.
5. Supprimer une réservation après confirmation.
0. Quitter l'application.

## 7. Fichier `.gitignore`

Le fichier `.gitignore` doit contenir au minimum :

```gitignore
__pycache__/
*.pyc
*.db
*.db-journal
*.db-wal
*.db-shm
.env
.venv/
```

**Important :** `hotel.db` reste local et ne doit pas être publié sur GitHub. Le dépôt doit contenir `hotel.sql`, qui permet à toute personne de reconstruire la base avec DB Browser for SQLite.

## 8. Remarque sur le périmètre

Conformément au sujet, cette version du projet ne vérifie pas encore les chevauchements de réservations pour une même chambre. Le modèle ne définit donc pas de statut permanent « libre » ou « occupée » pour une chambre.