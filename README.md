## Mongo Access Service

A Flask-based REST API for retrieving blog articles and sections stored in MongoDB. This API allows you to fetch full articles, preview cards by section, explore mixed sections, and perform keyword-based searches.

---

## 🚀 **Features**

* 📄 Fetch detailed article data by category and name.
* 🗂️ Get card-style article previews from any section.
* 🌐 Explore mixed articles across sections.
* 🔍 Search blog articles using keywords.
* ⚙️ MongoDB-backed storage for scalability.

---

## 🛠️ **Tech Stack**

* **Backend:** Flask (Python)
* **Database:** MongoDB
* **Dependencies:** Flask, PyMongo

---

## 📦 **Installation**

1️⃣ **Clone the repository:**

```bash
git clone git@github.com:abhishekprakash256/mongo-access-service.git
cd mongo-access-service
```

2️⃣ **Create a virtual environment & activate:**

```bash
python3 -m venv venv
source venv/bin/activate
```

3️⃣ **Install dependencies:**

## **1. Requirements**
To set up and run this project, ensure you meet the following requirements:

- **MongoDB Installation**  
  - Install MongoDB **bare-metal** or run it using Docker:  
    ```bash
    # Run MongoDB in Docker (recommended)
    docker run -d --name mongo-db -p 27017:27017 mongo
    ```
  - Ensure the MongoDB server is running before testing or development.

- **MongoDB Connection Setup**
  - Configure the **MongoDB client** in `Helper_Fun` class:
    - Use `"localhost"` if running MongoDB **locally**.
    - Use `"mongo"` if running **inside Docker**.

- **Install Required Dependencies**
  ```bash
  pip install -r requirements.txt
  ```

4️⃣ **Set environment variables (optional):**

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
```

5️⃣ **Run the API:**

```bash
flask run

flask run --port=5000  #on specifc port

```

The API will be available at `http://127.0.0.1:5000/`.

the localhost and 127.0.0.1 is resolved in mac and linux diffrently

## For the production env

- use gununicorn
- run the app with command 

```bash
gunicorn -w 4 -b 0.0.0.0:5000 "app:create_app()"

```
runs in port 5000 for production 


### Run the module files

Use commands in python to run module file in examples dir from root dir 

python3 -m folder_name.file_name

```bash
python3 -m examples.basic_usage
```

### Run the test locally 

```bash
pytest

```
Run the command pytest in root directory

## Configuration

- Clients 
    - "mongo" is passed when using insiede the docker conatienr to acces the mongo
    - "localhost" is passed when using outside the docker container to access the mongo for bulk data insertion


## Note

The client name passed in the helper fucntion is imp as using from outside use - "localhost"
The client name passed in the helper fucntion is imp as using from docker container use - "mongo"


---

## ⚙️ **API Endpoints**

### 1️⃣ Get Article Data

`GET /mogno/blog/section/<category>/article/<article_name>`

### 2️⃣ Get Section Data

`GET /mogno/blog/section/<category>?limit=<number>`

### 3️⃣ Get Explore Data

`GET /mongo/blog/section/explore?limit=<number>`

### 4️⃣ Search Articles

`GET /mongo/blog/search?keyword=<your_search_term>`

Full API details ➡️ [See API Documentation](https://github.com/abhishekprakash256/mongo-access-service/blob/main/DEVDOC.md)

---

## 🖥️ **MongoDB Setup**

* Make sure you have a running MongoDB instance.


---

## 🚨 **Error Handling**

* 400: Bad request (e.g., missing query parameters)
* 404: Not found (e.g., no articles matching query)
* 500: Internal server errors (e.g., DB connection issues)


---

## 🤝 **Contributing**

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

