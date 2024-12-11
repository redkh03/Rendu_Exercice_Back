1. ##Ajout de la gestion des erreurs personnalisées:
   Fichier modifié : core/exceptions.py Une fonction custom_exception_handler a été créée pour personnaliser les réponses d'erreur. Elle permet d'ajouter des informations supplémentaires, comme un message d'erreur détaillé
   ##2. Gestion de l'upload d'images
Nous avons ajouté la fonctionnalité permettant aux utilisateurs de télécharger une image (comme le logo de la société) avec une taille maximale définie.
Contrôles supplémentaires pour les fichiers téléchargés : La taille des fichiers téléchargés est limitée à 2 Mo pour éviter des fichiers trop volumineux.
##3. Améliorations Swagger pour la documentation de l'API
Nous avons intégré la documentation Swagger pour mieux documenter nos points de terminaison d'API et faciliter l'utilisation des différentes méthodes disponibles pour les utilisateurs et les administrateurs.
