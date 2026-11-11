from models import lister_chambres, lister_reservations, creer_reservation, modifier_reservation ,supprimer_reservation
from db import get_connection

def tester():
    conn = get_connection()
    
    print("Test de lister_chambres :")
    print(lister_chambres(conn))
    
    print("\nTest de lister_reservations :")
    print(lister_reservations(conn))
    
    id_res = creer_reservation(conn, 3, 3, "2024-11-11", "2024-12-05")
    print("\nTest de creer_reservation :")
    print(lister_reservations(conn))
    
    modifier_reservation(conn, id_res, "2024-11-15", "2024-12-10")
    print("\nTest de modifier_reservation :")
    print(lister_reservations(conn))
    
    supprimer_reservation(conn, id_res)
    print("\nTest de supprimer_reservation :")
    print(lister_reservations(conn))
    
    print(modifier_reservation(conn, 999, "2024-11-15", "2024-12-10"))

    
    id_res = creer_reservation(conn, 999, 3, "2024-11-11", "2024-11-05")
    
    
if __name__ == "__main__":
    tester()