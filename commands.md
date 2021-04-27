<!-- Creating a new django app using docker -->
cd ./admin
    <!-- Execute a command in a running container (backend). -->
    docker-compose exec backend sh 
        <!-- OR docker-compose exec backend bash -->
        python manage.py startapp products

<!-- Migrations -->
docker-compose exec backend bash
    python manage.py makemigrations
    python manage.py migrate


<!-- FLASK APP -->
<!-- Migrations -->
docker-compose exec backend bash
    $ python manage.py db init
    $ python manage.py db migrate
    $ python manage.py db upgrade
    $ python manage.py db --help

<!-- https://flask-migrate.readthedocs.io/en/latest/ -->

<!-- RabbitMQ -->
    <!-- Create account -->
        <!-- https://www.cloudamqp.com/ -->

<!-- After RabbitMQ setup in admin app -->
    docker-compose exec backend sh
    python consumer.py
