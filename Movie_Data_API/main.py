from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

app = FastAPI()


class Movie(BaseModel):
    title: str
    genre: str
    language: str
    release_year: int
    rating: float
    duration_minutes: int
    platform: str
    budget_crore: float
    box_office_crore: float

def load_data():
    with open("movies.json", "r") as file:
        data = json.load(file)
        return data

def save_data(data):
    with open("movies.json", "w") as file:
        json.dump(data, file, indent=4)


@app.post("/movies")
def add_movie(movie:Movie):
    movie_data = load_data()

    movie_id = len(movie_data) + 1
    movie_dict = movie.model_dump()
    movie_dict["movie_id"] = movie_id

    # movie_data.append(movie.model_dump())
    movie_data.append(movie_dict)

    save_data(movie_data)
    return {
        "message": "Movie added successfully",
        "movie": movie_data
    }

@app.get("/movies")
def get_movie():
    return load_data()

@app.put("/movies/{movie_id}")
def update_movie(movie_id:int, updated_movie:Movie):
    data = load_data()

    for movie in data:
        if movie["movie_id"] == movie_id:

            movie["title"] = updated_movie.title
            movie["genre"] = updated_movie.genre
            movie["language"] = updated_movie.language
            movie["release_year"] = updated_movie.release_year
            movie["rating"] = updated_movie.rating
            movie["duration_minutes"] = updated_movie.duration_minutes
            movie["platform"] = updated_movie.platform
            movie["budget_crore"] = updated_movie.budget_crore
            movie["box_office_crore"] = updated_movie.box_office_crore

            save_data(data)

            return{
                "message" : "Movie updated successfully",
                "movie" : movie
            }
    raise HTTPException(status_code=404, detail="Movie not found")

@app.delete("/movies/{movie_id}")
def delete_movie(movie_id:int):
    movies = load_data()

    for movie in movies:
        if movie["movie_id"] == movie_id:
            movies.remove(movie)
            save_data(movies)

            return {
                "message": "Movie deleted successfully"
            }
    raise HTTPException(status_code=404, detail="Movie not found")
