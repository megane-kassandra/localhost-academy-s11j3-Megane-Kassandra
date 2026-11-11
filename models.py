import datetime
import sqlite3


def lister_chambres(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM chambres ORDER BY numero")
    rows = cursor.fetchall()
    
    if not rows:
        return []
    else:
        return rows
    

def lister_reservations(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT r.id, cl.nom as nom_client, ch.numero as numero_chambre, r.date_debut, r.date_fin FROM reservations r LEFT JOIN chambres ch ON ch.id = r.chambre_id LEFT JOIN clients cl ON cl.id = r.client_id ORDER BY r.id")
    rows = cursor.fetchall()
    
    if not rows:
        return []
    else:
        return rows
    
    
def creer_reservation(conn, client_id, chambre_id, date_debut, date_fin):
    
    if date_debut >= date_fin:
        raise ValueError("La date de début doit être antérieure à la date de fin.")
    if  not datetime.date.fromisoformat(date_debut) or not datetime.date.fromisoformat(date_fin):
        raise ValueError("Les dates doivent être au format AAAA-MM-JJ.")
        
    
    try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO reservations (client_id, chambre_id, date_debut, date_fin) VALUES (?, ?, ?, ?)", (client_id, chambre_id, date_debut, date_fin))
        
    except sqlite3.IntegrityError as e:
        conn.rollback()
        raise ValueError("Erreur lors de la création de la réservation : " + str(e))
    
    else:
        conn.commit()
        return cursor.lastrowid
    
def modifier_reservation(conn, reservation_id, date_debut, date_fin):
    
    if date_debut >= date_fin:
        raise ValueError("La date de début doit être antérieure à la date de fin.")
    if  not datetime.date.fromisoformat(date_debut) or not datetime.date.fromisoformat(date_fin):
        raise ValueError("Les dates doivent être au format AAAA-MM-JJ.")
    
    try:
        cursor = conn.cursor()
        cursor.execute("update reservations set date_debut = ?, date_fin = ? where id = ?", (date_debut, date_fin, reservation_id))
    except sqlite3.Error as e:
        conn.rollback()
        raise ValueError("Erreur lors de la vérification de l'existence de la réservation : " + str(e))
    
    else:
        if reservation_id not in [row[0] for row in cursor.execute("SELECT id FROM reservations")]:
            return 0  # Aucun enregistrement trouvé avec l'ID spécifié           
        else:
            conn.commit()
            return f"Reservation modifie avec succes"

def supprimer_reservation(conn, reservation_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reservations WHERE id = ?", (reservation_id,))
    conn.commit()
    return f"Reservation supprime avec success"