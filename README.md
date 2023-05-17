# Closest Points API

Closest Points API is a Django application that receives a set of points on a grid as semicolon separated values and finds the points that are closest to each other. The application stores the received set of points and their closest points in a database.

## Features
>- Receives a set of points as semicolon separated values through an API.
>- Calculates the closest points among the given set.
>- Stores the received set of points and their closest points in a database.
>- Provides an admin interface to view and manage the stored points.
>- Includes unit tests to ensure the functionality of the API view and data model

## Installation

1. Clone the repository:

    ```
       git clone <repository_url>
    ```
2. Install the dependencies:

    ```
     pip install -r requirements.txt
    ```

3. Apply the database migrations:

    ```
    python manage.py migrate
    ```
4. Create a superuser to access the admin interface:

    ```
    python manage.py createsuperuser
    ```
5. Start the development server:

    ```
    python manage.py runserver
    ```
6. Access the application at 'http://localhost:8000/'.

## API Usage

To find the closest points among a set of points, make a POST request to the following endpoint:

    POST /api/closest_points/

## Parameters:

>- points: A semicolon separated values of points on a grid. Example: 2,2;-1,30;20,11;4,5.

The API will respond with a JSON object containing the closest points.

## Admin Interface

To access the admin interface, follow these steps:

1. Start the development server:

    ```
    python manage.py runserver
    ```
2. Open your web browser and navigate to http://localhost:8000/admin.

3. Log in using the superuser credentials created during installation.

In the admin interface, you can view and manage the stored points.

## Running Tests
To run the unit tests, execute the following command:

    python manage.py test closest_points
    
The tests ensure the functionality of the API view and data model.
