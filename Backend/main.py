from typing import Union, List, Dict
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

projects = [
    {
        "id": 1,
        "image": "p2Pic.png",
        "title": "Education Platform",
        "description": "Developed Education Platform, a TypeScript and React-based website designed to help young people choose an education, as part of my second-semester Computer Science project.",
        "details": "Developed Education Platform as part of my second-semester Computer Science project. The platform is a web application built with TypeScript and React, designed to help young people explore and choose suitable educational paths. It features a user-friendly interface for browsing various educational programs, providing detailed information and resources to guide decision-making. My main responsibilities included API integration with multiple services such as OpenAI and Cortical.IO, as well as developing a web scraper to collect the necessary text data. Additionally, I implemented a calculation system to score subjects based on their connection to mathematics, using a mix of TypeScript and Python. The project aims to make the process of selecting an education more accessible and informed for users.",
        "link": ["https://github.com/P2-API/Education-Platform"]
    },
    {
        "id": 2,
        "image": "Tutorly.svg",
        "title": "Tutorly",
        "description": "Developed Tutorly as my third-semester Computer Science project, a platform created in collaboration with Hasseris Gymnasium to support tutor-tutee relationships, featuring a Java backend and a TypeScript React frontend.",
        "details": "Contributed as part of a team in the development of Tutorly during my third semester, a platform created in collaboration with Hasseris Gymnasium to support tutor-tutee relationships. My primary responsibility was working on the backend, where I helped develop core functionalities using object-oriented programming principles with Spring Java and a MySQL database. I also handled pull requests for both the backend and frontend, ensuring smooth integration. The frontend utilized TypeScript with React, providing an efficient and user-friendly platform for managing tutor-tutee interactions.",
        "link": ["https://github.com/P3-HasserisGymnasium/Tutor-Administration-Platform"]
    },
    {
        "id": 3,
        "image": "foodDonations.jpg",
        "title": "P2P Food Donation",
        "description": "Developed P2P Food Donations, a C-based program enabling peer-to-peer food donation coordination, as part of my first-year Computer Science semester project.",
        "details": "Developed P2P Food Donations as my first university project, a terminal-based program enabling peer-to-peer food donation coordination. My main responsibility was implementing the login flow, ensuring secure access for users. This project provided an introduction to programming concepts and terminal-based interfaces in a real-world application.",
        "link": ["https://github.com/P1-P2P-Food-donation/P2P-Food-Donation"]
    },
    {
        "id": 4,
        "image": "Mywebsite.jpg",
        "title": "My Website",
        "description": "Created a personal hobby project: a website about myself, featuring a Python backend and a Vue.js frontend written in TypeScript.",
        "details": "Developed a personal website to promote the projects I’ve worked on and showcase my capabilities. The website is built using Vue.js with TypeScript for the frontend, while the backend is powered by Python and the FastAPI framework, ensuring a fast and scalable experience for users.",
        "link": ["https://github.com/EmilVorre/AboutMeWebsite",
                 "https://github.com/EmilVorre/BackendForWebsites"
                ]
    },
    {
        "id": 5,
        "image": "Twitch.png",
        "title": "Twitch View Prediction",
        "description": "Currently developing a hobby project combining web scraping and machine learning to create a program that predicts Twitch viewer counts for specific categories.",
        "details": "Currently developing a hobby project to predict Twitch viewer counts for specific categories, built to challenge myself in web scraping, integrating multiple languages into one program, and exploring machine learning. The data processing is written in Rust, the web scraper in Go, the website frontend in Vue.js with TypeScript, and the backend in Python. The program scrapes relevant data and uses machine learning algorithms to analyze trends and make predictions, helping users anticipate viewer engagement for different streams. This project is still under development and aims to improve predictions with more refined models over time.",
        "link": ["https://github.com/EmilVorre/TwitchViewerPredictionApp",
                 "https://github.com/EmilVorre/BackendForWebsites"
                ]
    },
    {
        "id": 6,
        "image": "dart.jpg",
        "title": "Dart Tournament Organizer",
        "description": "Created a Dart Tournament Organizer for a dart club, which are Python-based application with a random matchmaking system and a simple user interface to streamline tournament management.",
        "details": "Developed a Dart Tournament Organizer for a dart club in Denmark, a Python-based application designed to streamline the management of dart tournaments. The program includes a random matchmaking system and a simple user interface, making it easy to organize and track tournament progress. This project aimed at providing a more efficient and automated way to handle dart competitions.",
        "link": ["https://github.com/EmilVorre/DartTournamentOrganizer"]
    },
]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/projects", response_model=List[Dict])
def get_projects():
    return projects

@app.get("/project/{project_id}", response_model=Dict)
def get_project(project_id: int):
    project = next((project for project in projects if project["id"] == project_id), None)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}