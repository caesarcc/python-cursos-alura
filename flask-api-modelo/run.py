from api import api
from api.library import dotenv

if __name__ == "__main__":
    api.run(
        debug=dotenv.getBoolean("DEBUG"),
        host=dotenv.getString("SERVER_HOST"),
        port=dotenv.getString("SERVER_PORT")
    )
