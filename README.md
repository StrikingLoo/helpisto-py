# Helpisto-py
A simple Telegram bot to help me with stuff. So far it only allows a couple of commands.
- `/log`: Log a note.
- `/weight`: Log a weight.

### Installation
To install in an instance:

```
sudo apt update
sudo apt-get -y install python-dev build-essential
sudo apt -y install python3-pip
python3 -m pip install -U pip
export PATH="$HOME/.local/bin:$PATH"
pip3 install --upgrade setuptools
git clone https://github.com/StrikingLoo/helpisto-py.git
cd helpisto-py
sudo apt install python3-pip
pip3 install -r requirements.txt
```

### Running

To make instance:

```
gcloud compute instances create test-bot --machine-type f1-micro --zone us-west1-a --image-family ubuntu-1804-lts --image-project ubuntu-os-cloud --project helpisto-py
```

To run:

```nohup python3 main.py &```
