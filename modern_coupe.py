from app.controller import AppLauncher
from app.model.orm import Database

Database.init_superuser()
Database.Base.metadata.create_all(Database.engine)
AppLauncher().start()
