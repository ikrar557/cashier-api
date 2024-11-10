# Deploy the project

## Deploy to your machine

1. Download source code for project, and make sure you have python installed
2. Run below code inside the project folder to install dependencies
```bash
pip3 install -r requirements.txt
```  

3. Copy file ```.env.example``` to ```.env``` and change your configuration database to match your environment
4. Migrate your tables with 
```bash
alembic upgrade head
```
5. Populate your database with
```bash
python3 database/supplier_seeder.py
python3 database/barang_seeder.py
```
6. Run your project with
```bash
uvicorn src.main:app --host 0.0.0.0 --port 8080
```

## Docker deployment
build your image with
```bash
docker-compose build
```
and start your project with
```bash
docker-compose up
```

## How to access?
Navigate to your browser and access ```localhost:8080``` for entrypoint, or you can navigate to ```localhost:8080/docs``` to see lists of endpoints.