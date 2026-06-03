FROM python:3.11-slim

# System dependencies

RUN apt-get update && apt-get install -y 
wget 
curl 
git 
build-essential 
gcc 
g++ 
make 
libffi-dev 
libssl-dev 
&& rm -rf /var/lib/apt/lists/*

# Install Miniforge

RUN wget -q https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh && 
bash Miniforge3-Linux-x86_64.sh -b -p /opt/conda && 
rm Miniforge3-Linux-x86_64.sh

ENV PATH="/opt/conda/bin:${PATH}"

# Configure conda channels

RUN conda config --add channels conda-forge && 
conda config --add channels bioconda

# Install scientific software

RUN conda install -n base -y 
python=3.11 
openbabel 
mdanalysis 
numpy 
pandas 
scipy 
matplotlib 
biopython

# Clean cache

RUN conda clean -afy

# Install Python packages

RUN pip install --no-cache-dir 
flask 
flask-cors 
plotly 
requests 
gunicorn

# Working directory

WORKDIR /NeuroDynamicsFlow

# Copy project

COPY . .

# Create folders

RUN mkdir -p 
/NeuroDynamicsFlow/proteins 
/NeuroDynamicsFlow/ligands 
/NeuroDynamicsFlow/trajectories 
/NeuroDynamicsFlow/results 
/NeuroDynamicsFlow/images

# Permissions

RUN chmod -R 755 /NeuroDynamicsFlow

# Python path

ENV PYTHONPATH="/NeuroDynamicsFlow"

# Application port

EXPOSE 8502

# Launch application

CMD ["python", "server.py"]
