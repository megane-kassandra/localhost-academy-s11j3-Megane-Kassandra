import sqlite3

from models import lister_chambres, lister_reservations, creer_reservation, modifier_reservation, supprimer_reservation
from db import get_connection


def show_menu():
    print("\n==== GESTION DE L'HOTEL ====\n")
    print("1. Lister les chambres")
    print("2. Lister les reservations")
    print("3. Ajouter une reservation")
    print("4. Modifier les dates d'une reservation")
    print("5. Supprimer une reservation")
    print("0. Quitter")

def main():
    
    while True:

        try:
        
        
    
            conn = get_connection()
    
            show_menu()
            
            choice = int(input("Entrez votre choix : "))
        
            if choice == 1:
                print("\n++++ LISTE DES CHAMBRES ++++\n")
                rows = lister_chambres(conn)
                for row in rows:
                    print(f"ID: {row[0]}, Numero: {row[1]}, Prix_unitaire: {row[2]}")
            
            elif choice == 2:
                print("\n++++ LISTE DES RESERVATIONS ++++\n")
                rows = lister_reservations(conn)
                for row in rows:
                    print(f"ID: {row[0]}, Nom_client: {row[1]}, Numero_chambre: {row[2]}, Début: {row[3]}, Fin: {row[4]}")
            
            elif choice == 3:
                id_client = int(input("Entrer l'identifiant du client : "))
                id_chambre = int(input("Entrer l'identifiant de la chambre : "))
                date_debut = input("Entrer la date de debut au format(AAAA-MM-JJ)")
                date_fin = input("Entrer la date de fin au format(AAAA-MM-JJ)")
                
                if id_client <= 0 or id_chambre <= 0:
                    raise ValueError("L'identifiant du client et de la chambre doit être un entier positif.")
                
                id_res = creer_reservation(conn, id_client, id_chambre, date_debut, date_fin)
                print(f"Lidentifiant de la nouvelle reservation est {id_res} ")
            
            elif choice == 4:
                id_res = int(input("Entrer l'identifiant de la reservation : "))
                date_debut = input("Entrer la nouvelle date de debut au format(AAAA-MM-JJ) : ")
                date_fin = input("Entrer la nouvelle date de fin au format(AAAA-MM-JJ) :5")
                
                if id_res <= 0:
                    raise ValueError("L'identifiant de la reservation doit être un entier positif.")
                
                result = modifier_reservation(conn, id_res, date_debut, date_fin)
                if isinstance(result, str):
                    print(result)
                else:
                    print(f"La reservation {id_res} est introuvable")

            elif choice == 5:
                id_res = int(input("Entrer l'identifiant de la reservation a supprimer : "))
                
                if id_res <= 0:
                    raise ValueError("L'identifiant de la reservation doit être un entier positif.")
                
                while True:
                    response = input(f"\nvoulez-vous vraiment supprimer la reservation {id_res} ? (Y/N) : ").upper()
                    if response == "Y":
                        supprimer_reservation(conn, id_res)
                        print("\nReservation supprimee avec succes!")
                        break
                    elif response == "N":
                        # show_menu()
                        break
                    else:
                        print("\nReponse invalide choisir ente Y ou N")
                    
            else:
                print("Reponse invalide, veuillez ressayer.")
            
        except sqlite3.IntegrityError as e:
            print("Erreur d'intégrité de la base de données :", e)
        except ValueError as e:
            print("Erreur de valeur :", e)
            
        finally:
            conn.close()
        
if __name__ == "__main__":
    main()
    