import os
from dotenv import load_dotenv
from pathlib import Path 

env_path = Path('.') / '.env'
dotenv = load_dotenv(dotenv_path=env_path, verbose=True)


