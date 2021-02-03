➡ Set up un SQL container avec la base de donnée bdd.sql ici(https://
drive.google.com/file/d/19E1pMuH6EcdovUDACTJTPVl3a1HJTFSz/view?
usp=sharing) ( on going )
➡ Créer un utilisateur pour votre base et afficher ses autorisations ( done , https://severalnines.com/database-blog/mysql-docker-containers-understanding-basics )
➡ Écrire un script python afin de se connecter au container MySQL et
vérifier les opérations CRUD standard.

    - First of all Build an image and then a container : two different things.
        -- " docker build -t mysql_image . " 
        -- " docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root_password --name=mysql_container mysql_image " [ if i have root password in docker , remove -e MYSQL_ROOT_PASSWORD=root_password ]
        -- " sudo docker exec -it mysql_container mysql -u root -p " ( password to put in with : root_password )
         to login with user mohamed write this : " sudo docker exec -it mysql_container mysql -u mohamed -p " and then password is: mohamed
            --- container mysql terminal : " show databases; use classicmodels; show tables;"
    - Créer un user en dockerfile pour communiquer du dehors

➡ Effectuer les requêtes suivantes (voir page suivante) via le sdk
python ou le CLI MySQL
➡ Vous ferez un push de votre travail dans un repo git dédié avec les
fichiers queries.sql (dans le cas ou vous passer par le CLI) ou un
fichier scripts.py (si vous passez par le SDK)