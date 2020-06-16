sudo apt update || exit 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 10 || exit 1
sudo apt-get install -y python3-pip || exit 1
sudo update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1 || exit 1
pip install flask || exit 1