from dotenv import load_dotenv
from pathlib import Path


# Specifing our .env file location
env_path = Path('.') / 'env' / '.env'

# Loads our python env file
load_dotenv(dotenv_path=env_path)
