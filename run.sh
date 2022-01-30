BASEDIR=$(pwd)
echo "$BASEDIR"

docker build -t pda .
docker run -it -v "$BASEDIR/docs:/app/docs" pda
