import os
from dotenv import load_dotenv

load_dotenv()

db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
path="/home/larex/Programming/Data Science/DE Project #1/copy_df_data.py"
table_name = 'all_countries'

os.chmod(path=path, mode=777)

os.system(f'''psql -U {db_user} -d {db_name} -c "\\copy {table_name} FROM '/home/larex/Programming/Data Science/DE Project #1/countries_of_the_world.csv' WITH CSV HEADER DELIMITER ','"''')
