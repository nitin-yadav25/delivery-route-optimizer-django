Delivery Route Optimizer (Django)

A Django web app that calculates the shortest delivery route using the Nearest Neighbor algorithm.  
Users can input warehouse coordinates and delivery locations to get an optimized route and total travel distance.

---

## Features

- Dynamic warehouse coordinate input
- Multiple delivery locations support
- Nearest Neighbor based optimization
- Total distance calculation (Euclidean)
- Clean minimal UI
- Basic input error handling

---

## Algorithm Used

**Nearest Neighbor Algorithm**

Steps:
1. Start at the warehouse location
2. Pick the nearest unvisited delivery point
3. Move to that point and repeat
4. Continue until all locations are visited

---

## Tech Stack

- Python 3.x  
- Django 6  
- HTML + CSS  
- Math (Euclidean distance via Python)

---

## Project Structure

delivery_project/
├── optimizer/ # App logic
├── templates/ # UI HTML
├── manage.py
└── README.md


---

## How to Run Locally

1. Clone repository  
   ```bash
   git clone https://github.com/nitin-yadav25/delivery-route-optimizer-django.git
Move into project

cd delivery-route-optimizer-django/delivery_project
Create virtual environment

python -m venv venv
Activate environment
Windows:

venv\Scripts\activate
Install dependencies

pip install django
Run server
python manage.py runserver

Open in browser:
http://127.0.0.1:8000/

Example Input
Warehouse:
0,0
Locations:

1,2;3,4;5,1
Output Example
Warehouse:
(0.0, 0.0)
Optimized Route:
(0.0, 0.0) → (1.0, 2.0) → (3.0, 4.0) → (5.0, 1.0)

Total Distance:
8.67
Purpose
Built as part of an internship assignment to showcase file handling, user input, web views, and simple algorithm implementation using Django.

Author
Nitin Yadav
