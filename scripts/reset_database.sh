#!/bin/bash

# This script deletes all the data and the tables, and then recreates the tables.

function drop_recreate_public_schema(){
    SQL_STATEMENTS=( 
        "DROP SCHEMA public CASCADE;" 
        "CREATE SCHEMA public;" 
        "GRANT ALL ON SCHEMA public TO ${POSTGRES_USER};"
        "GRANT ALL ON SCHEMA public TO public;"
    )
    for SQL in "${SQL_STATEMENTS[@]}" ; do 
        PGPASSWORD="${POSTGRES_PASSWORD}" ${PSQL_CMD} -c "${SQL}"
    done
    echo "Deleting existing tables..."
}

function remigrate(){
    python3 manage.py migrate &> /dev/null
    if [ "$?" != "0" ]; then
        echo "Migration error!" && exit 1
    else
        echo "Recreating tables..."
    fi
}

function insert_seed_data(){
    PGPASSWORD="${POSTGRES_PASSWORD}" ${PSQL_CMD} -f load_onboarding_data.sql
}

# Ask the user for postgres details
[[ -z ${POSTGRES_PASSWORD} ]] && read -sp 'Your superuser password: ' POSTGRES_PASSWORD
[[ -z ${POSTGRES_USER} ]] && read -p 'Your superuser (typically postgres): ' POSTGRES_USER
[[ -z ${POSTGRES_HOST} ]] && read -p 'Host url: ' POSTGRES_HOST
[[ -z ${POSTGRES_PORT} ]] && read -p 'Port: ' POSTGRES_PORT
[[ -z ${POSTGRES_NAME} ]] && read -p 'Database name: ' POSTGRES_NAME

# is psql installed? 
if [ -z $( which psql ) ] ; then
    echo "installing psql..."
    apt-get install postgresql -y &> /dev/null
fi

PSQL_CMD="psql -U $POSTGRES_USER -h $POSTGRES_HOST -p $POSTGRES_PORT -d $POSTGRES_NAME"

PGPASSWORD="${POSTGRES_PASSWORD}" ${PSQL_CMD} -c "SELECT 1;" &> /dev/null
if [ "$?" != "0" ]; then
    echo "Please verify dbname, user and password and try again!" 1>&2
    exit 1
fi
#cd ..

drop_recreate_public_schema
remigrate
#insert_seed_data

echo "Database reset!"#!/bin/bash

# This script deletes all the data and the tables, and then recreates the tables.

function drop_recreate_public_schema(){
    SQL_STATEMENTS=( 
        "DROP SCHEMA public CASCADE;" 
        "CREATE SCHEMA public;" 
        "GRANT ALL ON SCHEMA public TO ${POSTGRES_USER};"
        "GRANT ALL ON SCHEMA public TO public;"
    )
    for SQL in "${SQL_STATEMENTS[@]}" ; do 
        PGPASSWORD="${POSTGRES_PASSWORD}" ${PSQL_CMD} -c "${SQL}"
    done
    echo "Deleting existing tables..."
}

function remigrate(){
    python3 manage.py migrate &> /dev/null
    if [ "$?" != "0" ]; then
        echo "Migration error!" && exit 1
    else
        echo "Recreating tables..."
    fi
}

function insert_seed_data(){
    PGPASSWORD="${POSTGRES_PASSWORD}" ${PSQL_CMD} -f load_onboarding_data.sql
}

# Ask the user for postgres details
[[ -z ${POSTGRES_PASSWORD} ]] && read -sp 'Your superuser password: ' POSTGRES_PASSWORD
[[ -z ${POSTGRES_USER} ]] && read -p 'Your superuser (typically postgres): ' POSTGRES_USER
[[ -z ${POSTGRES_HOST} ]] && read -p 'Host url: ' POSTGRES_HOST
[[ -z ${POSTGRES_PORT} ]] && read -p 'Port: ' POSTGRES_PORT
[[ -z ${POSTGRES_NAME} ]] && read -p 'Database name: ' POSTGRES_NAME

# is psql installed? 
if [ -z $( which psql ) ] ; then
    echo "installing psql..."
    apt-get install postgresql -y &> /dev/null
fi

PSQL_CMD="psql -U $POSTGRES_USER -h $POSTGRES_HOST -p $POSTGRES_PORT -d $POSTGRES_NAME"

PGPASSWORD="${POSTGRES_PASSWORD}" ${PSQL_CMD} -c "SELECT 1;" &> /dev/null
if [ "$?" != "0" ]; then
    echo "Please verify dbname, user and password and try again!" 1>&2
    exit 1
fi
#cd ..

drop_recreate_public_schema
remigrate
#insert_seed_data

echo "Database reset!"
