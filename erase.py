import os
import shutil
import stat

def changer_permissions(dossier):
    for racine, dossiers, fichiers in os.walk(dossier, topdown=False):
        for fichier in fichiers:
            chemin_fichier = os.path.join(racine, fichier)
            try:
                os.chmod(chemin_fichier, stat.S_IWUSR | stat.S_IREAD)
                print(f"Permissions modifiées pour le fichier: {chemin_fichier}")
            except Exception as e:
                print(f"Erreur lors de la modification des permissions du fichier {chemin_fichier}: {e}")
        for dossier in dossiers:
            chemin_dossier = os.path.join(racine, dossier)
            try:
                os.chmod(chemin_dossier, stat.S_IWUSR | stat.S_IREAD | stat.S_IXUSR)
                print(f"Permissions modifiées pour le dossier: {chemin_dossier}")
            except Exception as e:
                print(f"Erreur lors de la modification des permissions du dossier {chemin_dossier}: {e}")

def supprimer_contenu(dossier):
    print(f"Suppression du contenu du dossier: {dossier}")
    if not os.path.exists(dossier):
        print(f"Le dossier {dossier} n'existe pas.")
        return

    changer_permissions(dossier)

    for racine, dossiers, fichiers in os.walk(dossier, topdown=False):
        print(f"Parcourir le dossier: {racine}")
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
    dossier_a_supprimer = os.path.expanduser("~/Desktop/testerase")
    supprimer_contenu(dossier_a_supprimer)
