if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/sachin9742s/PrabhasBotV3 /PrabhasBotV3
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /PrabhasBotV3
fi
cd /PrabhasBotV3
pip3 install -U -r requirements.txt
echo "Starting ...."
python3 bot.py
