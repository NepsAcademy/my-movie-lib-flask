import csv
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)


@app.get("/")
def index():
    movies = []
    with open("movies.csv", mode="r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            movies.append(row)

    return render_template("index.html", movies=movies)


@app.get("/movie/<int:movie_id>")
def movie_details(movie_id):
    found_movie = None

    with open("movies.csv", mode="r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for movie in csv_reader:
            # Compara o ID da linha (convertido para int) com o ID da URL
            if int(movie["id"]) == movie_id:
                found_movie = movie
                break  # Encontramos o filme, podemos parar o loop

    # Se um filme foi encontrado, renderiza a página de detalhes com seus dados
    if found_movie:
        return render_template("review-details.html", movie=found_movie)

    # Se não, retorna uma página de erro 404
    else:
        return "Movie not found!", 404


@app.get("/add-review")
def show_add_form():
    return render_template("add-review.html")


@app.post("/add-review")
def add_review():

    # 1. Busca o último ID adicionado (código que vimos acima)
    with open("movies.csv", mode="r", encoding="utf-8") as csv_file:
        reader = list(csv.reader(csv_file))
        last_id = 0

        if len(reader) > 1:
            last_row = reader[-1]
            if last_row:
                last_id = int(last_row[0])

        next_id = last_id + 1

    # 2. Converte a data para o formato esperado
    watched_date_raw = request.form.get("watched_date")
    date_object = datetime.strptime(watched_date_raw, "%Y-%m-%d")

    formatted_date = date_object.strftime("%m/%d/%Y")

    # 3. Coleta os dados do formulário usando o atributo 'name' de cada campo
    new_movie_data = [
        next_id,
        request.form.get("title"),
        request.form.get("poster_url"),
        request.form.get("rating"),
        formatted_date,
        request.form.get("review"),
    ]

    # 3. Anexa os novos dados ao arquivo CSV
    with open("movies.csv", mode="a", encoding="utf-8", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(new_movie_data)

    # 4. Redireciona para a página principal
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
