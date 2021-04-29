# Microservices
* Built a photo uploading application that's based on **Microservices Architecture**.
* The app has two (micro)services:
    1. Admin App: This service deals with photo uploads by owner of the photo and is built using **Python/Django**.
    2. Main App: This service deals with allowing random users to view and like uploaded Images and is built using **Python/Flask**.

### Features
1. For the database, I used seperate **MySQL** database for each (micro)service. 
2. I deployed each (micro)service in seperate **docker** environments.
3. I built the frontend using **TypeScript React**.
4. I implemented two types of communication for the (micro)services to communicate with each other:
    - **Synchronous Call**: I implemented this to use **Http REST call**.
    - **Asynchronous Call**. I implemented this to use **RabbitMQ** as the message broker.