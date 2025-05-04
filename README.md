## Mongo Access Service


# 📰 **Blog API**

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
```

The API will be available at `http://127.0.0.1:5000/`.

---

## ⚙️ **API Endpoints**

### 1️⃣ Get Article Data

`GET /blog/section/<category>/article/<article_name>`

### 2️⃣ Get Section Data

`GET /blog/section/<category>?limit=<number>`

### 3️⃣ Get Explore Data

`GET /blog/section/explore?limit=<number>`

### 4️⃣ Search Articles

`GET /blog/search?keyword=<your_search_term>`

Full API details ➡️ [See API Documentation](#)

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

