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
    
### Tiles
    Several layers are pulling pre-cut tiles (not served by tilestache or similar). These only work in OL3 for Firefox and IE if served locally. Grab the layers you need from apps.ecotrust.org/tiles/juniper, zip them, scp them to /tmp/, then:
    
    sudo tar zxf /tmp/your_file.tar.gz -C /usr/local/apps/wja/wja/static/ui/tiles/juniper/
    
