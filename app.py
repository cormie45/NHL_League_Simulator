from flask import Flask, render_template

import repositories.team_repository as team_repository
from controllers.teams_controller import teams_blueprint
from controllers.players_controller import players_blueprint
from controllers.matches_controller import matches_blueprint


app = Flask(__name__)

app.register_blueprint(teams_blueprint)
app.register_blueprint(players_blueprint)
app.register_blueprint(matches_blueprint)

@app.route('/')
def home():
    teams = team_repository.select_all()
    return render_template('index.html', teams=teams)

if __name__ == '__main__':
    app.run(debug=True)