rm wja/db.sqlite3
spatialite wja/db.sqlite3 "SELECT InitSpatialMetaData();"
~/env/wja/bin/python manage.py migrate
