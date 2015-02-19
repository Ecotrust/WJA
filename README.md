WJA
===

Western Juniper Alliance Juniper Treatment Mapper

Viewer for tracking and utilizing available treated juniper.

# Quickstart

### Setup
    virtualenv --python /usr/bin/python3.4 ~/env/wja
    source ~/env/wja/bin/activate

    sudo apt-get install build-essential 
    sudo apt-get install python3-dev python3-pip python3-psycopg2 python-psycopg2
    sudo apt-get install gdal-bin libgeos-dev libgdal1-dev 
    sudo apt-get install spatialite-bin
    sudo apt-get install zlib1g-dev 
    pip install -r requirements.txt

    cd wja  # just a container
    ./test

### Initialize

    spatialite dst/db.sqlite3 "SELECT InitSpatialMetaData();"
    python manage.py migrate
    python manage.py createsuperuser
    # python manage.py systemcheck