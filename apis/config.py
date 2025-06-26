# config.py

# MongoDB configurations for dev and production environments.
# This file contains the MongoDB connection details and collection names.
# This file is used to configure the MongoDB connection settings for the application.
MONGO_DB_NAME = "test-main-database"
MONGO_COLLECTION_NAME = "test-article-collections"
MONGO_HOST_NAME = "localhost"
MONGO_SECTION_NAME = ["tech", "project", "life"]
API_KEY = "test_key"


ARTICLE_SCHEMA = {
    "name": "articles",
    "enable_nested_fields": True,
    "fields": [
        {"name": "id", "type": "string"},  # Required primary key
        {"name": "article_name", "type": "string"},
        {"name": "slug", "type": "string"},
        {"name": "article_image", "type": "string"},
        {"name": "article_para", "type": "string"},
        {"name": "section_name", "type": "string", "facet": True},
        {"name": "id_number", "type": "int32"},

        # Flattened nested fields
        {"name": "article_data.title", "type": "string[]"},
        {"name": "article_data.article_para", "type": "string[]"},
        {"name": "article_data.markdown_data", "type": "string[]"},

        # Links
        {"name": "github_url", "type": "string"},
        {"name": "linkedin_url", "type": "string"},
        {"name": "twitter_url", "type": "string"},
        {"name": "leetcode_url", "type": "string"},
        {"name": "gitlab_url", "type": "string"},
        {"name": "kaggle_url", "type": "string"},
        {"name": "medium_url", "type": "string"},
        {"name": "demo_link", "type": "string"},
        {"name": "article_link", "type": "string"},
        {"name": "more_link", "type": "string"}
    ],
    "default_sorting_field": "id_number"
}

