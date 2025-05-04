# 📖 **Blog API Documentation**

This API provides endpoints to fetch article data, section data, explore mixed sections, and search blog articles from a MongoDB-backed system.

---

## **1️⃣ Get Article Data**

**Endpoint:**

```
GET mongo/blog/section/<category>/article/<article_name>
```

**Description:**

Fetch detailed data of a specific article from a given category.

**Path Parameters:**

| Name           | Type   | Description                          |
| -------------- | ------ | ------------------------------------ |
| `category`     | string | The category the article belongs to. |
| `article_name` | string | The specific name of the article.    |

**Response:**

* **200 OK**

  ```json
  {
      "status": "success",
      "data": { ...article_data... }
  }
  ```

* **404 Not Found**

  ```json
  {
      "status": "fail",
      "message": "Article '<article_name>' in category '<category>' not found."
  }
  ```

* **500 Internal Server Error**

  ```json
  {
      "status": "error",
      "message": "A database error occurred.",
      "details": "<error_details>"
  }
  ```

---

## **2️⃣ Get Section Data (Cards)**

**Endpoint:**

```
GET mongo/blog/section/<category>
```

**Description:**

Retrieve card-style previews for articles in a specific section/category.

**Path Parameters:**

| Name       | Type   | Description                   |
| ---------- | ------ | ----------------------------- |
| `category` | string | The section or category name. |

**Query Parameters:**

| Name  | Type | Description                           | Default  |
| ----- | ---- | ------------------------------------- | -------- |
| limit | int  | Number of items to fetch (minimum 3). | No limit |

**Response:**

* **200 OK**

  ```json
  {
      "status": "success",
      "data": [ ...list_of_cards... ]
  }
  ```

* **404 Not Found**

  ```json
  {
      "status": "fail",
      "message": "No data found for category '<category>'."
  }
  ```

* **500 Internal Server Error**

  ```json
  {
      "status": "error",
      "message": "A database error occurred.",
      "details": "<error_details>"
  }
  ```

---

## **3️⃣ Get Explore Data (Mixed Sections)**

**Endpoint:**

```
GET mongo/blog/section/explore
```

**Description:**

Fetches mixed cards from multiple sections, with optional limit.

**Query Parameters:**

| Name  | Type | Description                                    | Default |
| ----- | ---- | ---------------------------------------------- | ------- |
| limit | int  | Number of items to fetch per section (min: 3). | 15      |

**Response:**

* **200 OK**

  ```json
  {
      "status": "success",
      "data": [ ...combined_card_data... ]
  }
  ```

* **500 Internal Server Error**

  ```json
  {
      "status": "error",
      "message": "A database error occurred while fetching the explore data.",
      "details": "<error_details>"
  }
  ```

---

## **4️⃣ Search Articles**

**Endpoint:**

```
GET mongo/blog/search
```

**Description:**

Search for blog articles that match a specific keyword.

**Query Parameters:**

| Name    | Type   | Description                 |
| ------- | ------ | --------------------------- |
| keyword | string | The search term (required). |

**Response:**

* **200 OK**

  ```json
  {
      "status": "success",
      "data": [ ...search_results... ]
  }
  ```

* **400 Bad Request**

  ```json
  {
      "status": "fail",
      "message": "The 'keyword' query parameter is required."
  }
  ```

* **404 Not Found**

  ```json
  {
      "status": "fail",
      "message": "No results found for keyword '<keyword>'."
  }
  ```

* **500 Internal Server Error**

  ```json
  {
      "status": "error",
      "message": "A database error occurred while performing the search.",
      "details": "<error_details>"
  }
  ```

---

## 🛡️ **Error Handling**

* **Database Errors:** Return a 500 error with details.
* **Unexpected Errors:** Return a 500 error with exception details.
* **Validation Errors:** Return a 400 error when required query parameters are missing.

---

## 💡 **Examples**

### Fetch a Single Article

```
GET mongo/blog/section/tech/article/python-tips
```

### Get Section Data (with Limit)

```
GET mongo/blog/section/tech?limit=5
```

### Explore Mixed Sections

```
GET mongo/blog/section/explore?limit=10
```

### Search Articles

```
GET mongo/blog/search?keyword=flask
```

---


## 🔒 **Error Handling**

All endpoints return a structured JSON response with:

* `status`: success, fail, or error
* `message`: description of what happened
* `data`: (if applicable) the data payload returned

Example:

```json
{
    "status": "success",
    "data": [
        {
            "_id": "653af7f8b1e88d5e9f7c12d3",
            "article_name": "test1",
            "content": "This is a sample blog post.",
            "author": "John Doe"
        }
    ]
}
```


