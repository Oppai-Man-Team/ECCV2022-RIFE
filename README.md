Instalação

python -m pip install -f https://download.pytorch.org/whl/cu110/torch_stable.html torch==1.7.1+cu110 torchvision==0.8.2

python -m pip install --upgrade pip setuptools wheel

python -m pip install -r requirements.txt

build

pithon -m pyinstaller inference_video.spec

