from smartphone.bot import main
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.environ.get('TOKEN')

main(TOKEN)
