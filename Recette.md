# Recette de test — Projet de gestion d'hôtel

**Projet :** Gestion d'un hôtel modulaire — LocalHost Academy, Semaine 11, Jour 3  
**Langage :** Python  
**Base de données :** SQLite

## Objectif

Ce document présente les vérifications à effectuer sur l'application de gestion d'hôtel. Les tests portent sur l'affichage des chambres et des réservations, la création, la modification et la suppression d'une réservation, la gestion des erreurs ainsi que la conservation des données.

## Préparation

Avant de commencer les tests :

1. Vérifier que les fichiers `hotel.sql`, `db.py`, `models.py`, `main.py` et `verification_models.py` sont présents dans le projet.
2. Importer le fichier `hotel.sql` dans DB Browser for SQLite.
3. Enregistrer la base créée sous le nom `hotel.db` dans le dossier du projet.
4. Vérifier que `DB_PATH` dans `db.py` pointe vers ce fichier.
5. Ouvrir un terminal dans le dossier du projet et lancer `python main.py`.

## Scénario 1 — Afficher les chambres et les réservations

**Étapes :**
1. Lancer l'application.
2. Choisir l'option `1 - Lister les chambres`.
3. Revenir au menu et choisir `2 - Lister les réservations`.

**Résultat attendu :**
- Les chambres présentes dans la base sont affichées avec leur numéro et leur prix par nuit.
- Les réservations sont affichées avec leur identifiant, le nom du client, le numéro de chambre et les dates.
- Les résultats sont présentés dans l'ordre prévu par les requêtes.

**Résultat obtenu :** pareils que les resultats attendus.

## Scénario 2 — Ajouter, modifier et annuler une suppression

**Étapes :**
1. Choisir `3 - Ajouter une réservation`.
2. Saisir un identifiant de client existant, un identifiant de chambre existant, puis les dates au format `AAAA-MM-JJ`.
3. Noter l'identifiant de la réservation créée.
4. Choisir `4 - Modifier les dates d'une réservation` et saisir cet identifiant ainsi que les nouvelles dates.
5. Choisir `5 - Supprimer une réservation`, saisir le même identifiant puis répondre autre chose que `oui` à la demande de confirmation.

**Résultat attendu :**
- La réservation est créée et son identifiant est affiché.
- Les nouvelles dates sont enregistrées.
- La réservation n'est pas supprimée lorsque la confirmation exacte `oui` n'est pas donnée.

**Résultat obtenu :** pareils que les resultats attendus.

## Scénario 3 — Vérifier la conservation des données

**Étapes :**
1. Après avoir créé ou modifié une réservation, quitter l'application avec l'option `0`.
2. Relancer `python main.py`.
3. Afficher la liste des réservations avec l'option `2`.

**Résultat attendu :**
- La réservation créée est toujours présente.
- Les dates modifiées sont conservées après la fermeture et le redémarrage de l'application.

**Résultat obtenu :** pareils que les resultats attendus.

## Scénario 4 — Confirmer une suppression et tester un identifiant inexistant

**Étapes :**
1. Choisir l'option de suppression.
2. Saisir l'identifiant d'une réservation existante et répondre exactement `oui`.
3. Afficher de nouveau les réservations.
4. Tenter ensuite de modifier la réservation portant l'identifiant `999`.

**Résultat attendu :**
- La réservation confirmée est supprimée.
- Elle n'apparaît plus dans la liste.
- La modification de la réservation `999` indique qu'aucune réservation correspondante n'a été trouvée. L'application continue de fonctionner.

**Résultat obtenu :** pareils que les resultats attendus.

## Scénario 5 — Tester les saisies incorrectes et les erreurs

Effectuer les essais suivants séparément :

| Saisie ou action | Résultat attendu |
|---|---|
| Saisir `abc` à la place d'un identifiant numérique | Un message d'erreur est affiché et le menu reste utilisable. |
| Saisir `-1` comme identifiant | La valeur est refusée. |
| Saisir une date qui n'existe pas ou qui ne respecte pas le format attendu | Une erreur de date est signalée. |
| Saisir une date de fin antérieure ou égale à la date de début | La réservation est refusée avec une erreur de validation. |
| Créer une réservation avec un identifiant de client inexistant, par exemple `999` | La contrainte de clé étrangère déclenche une erreur traitée par le menu. |
| Saisir un choix qui n'existe pas dans le menu | Un message indique que le choix est invalide et le menu est réaffiché. |

**Résultat obtenu :** pareils que les resultats attendus.

## Scénario 6 — Lancer le programme depuis le dossier parent

**Étapes :**
1. Ouvrir un terminal dans le dossier qui contient le dossier du projet.
2. Exécuter `python NOM_DU_PROJET/main.py`, en remplaçant `NOM_DU_PROJET` par le nom réel du dossier.
3. Afficher les chambres ou les réservations.

**Résultat attendu :**
- L'application utilise la même base `hotel.db` située dans le dossier du projet.
- Le fonctionnement ne dépend pas du dossier courant du terminal, grâce au chemin construit avec `Path(__file__).resolve().parent`.

**Résultat obtenu :** pareils que les resultats attendus.

## Question de compréhension

**Pourquoi le menu ne doit-il pas se lancer automatiquement lorsqu'on importe `main.py` dans un autre fichier ?**

La condition :

```python
if __name__ == "__main__":
    main()
```

permet de lancer le menu uniquement lorsque `main.py` est exécuté directement. Si le fichier est importé par un autre module, le menu ne démarre pas automatiquement. Cela permet de réutiliser ses fonctions sans déclencher l'application.

## Bilan

Les tests doivent permettre de vérifier que les opérations sur les réservations fonctionnent, que les saisies incorrectes sont prises en charge et que les données enregistrées restent disponibles après le redémarrage.

**Conclusion des tests :** À compléter après avoir exécuté les scénarios et noté les résultats réellement observés.