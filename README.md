WJA
===

Western Juniper Alliance Juniper Treatment Mapper

Viewer for tracking and utilizing available treated juniper.

# Quickstart

### Setup (assuming ubuntu with ubuntugis-unstable ppa)

    sudo apt-get install build-essential 
    sudo apt-get install python3-dev python3-pip 
    sudo apt-get install binutils gdal-bin libgeos-dev libgdal1-dev 
    sudo apt-get install libproj0=4.8.0-2ubuntu2 libproj-dev    #libproj0 version req'd by libproj-dev
    sudo apt-get install zlib1g-dev 

    #if postgres
    sudo apt-get install python3-psycopg2 python-psycopg2   
    
    #if spatialite
    sudo apt-get install libfreexl-dev libreadosm-dev       
    sudo apt-get install spatialite-bin libspatialite5

    virtualenv --python /usr/bin/python3.4 ~/env/wja
    source ~/env/wja/bin/activate
    pip install -r requirements.txt

    See if you have SQLite installed correctly:
    https://docs.djangoproject.com/en/1.7/ref/contrib/gis/install/spatialite/#sqlite

### Initialize

    cd wja
    ./init_db.sh
    python manage.py createsuperuser
    # python manage.py systemcheck