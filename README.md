# Multimedia-Systems-Projects

### Prerequisites
```sh
sudo su
apt update
apt install libcairo2-dev libpango1.0-dev ffmpeg texlive-fonts-extra texlive-formats-extra texlive-lang-german texlive-latex-extra texlive-metapost texlive-publishers texlive-science sox
pip3 install virtualenv
virtualenv -p python3 env
source env/bin/activate
pip3 install -r requirements.txt
```

### Executing program

```sh
git clone https://github.com/smmir-cent/Multimedia-Systems-Projects.git
manimgl src/VectorTrain.py VectorTrain -w
sox sound/sound.ogg sound/looped_sound.ogg repeat 2 # adjust count as necessary
ffmpeg -i videos/VectorTrain.mp4 -i sound/looped_sound.ogg -shortest videos/output.mp4
```
