from sqlalchemy import text

from . import *

sql = """
CREATE USER mc_manager WITH PASSWORD 'os2M03ohC0Gd7QREAkWLEw44XFu1ju';
GRANT CONNECT ON DATABASE mc3 TO mc_manager;

GRANT SELECT ON ALL TABLES IN SCHEMA public TO mc_manager;
GRANT INSERT ON TABLE "custom_col_size", "custom_row_size", "customer", "door", "door_fragment", "material", "order",
"color" 
    TO mc_manager;
GRANT UPDATE ON TABLE "custom_col_size", "custom_row_size", "customer", "door", "door_fragment", "material", "order" 
    TO mc_manager;
GRANT USAGE ON ALL SEQUENCES IN SCHEMA public TO mc_manager;

"""
Database.init_superuser()
Database.Base.metadata.drop_all(Database.engine)
Database.Base.metadata.create_all(Database.engine)

