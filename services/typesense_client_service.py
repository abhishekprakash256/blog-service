"""
The file to make the typesense client
"""

import typesense

from apis.config import API_KEY



#make the typesense client 
typesense_client = typesense.Client({
  'api_key': API_KEY,
  'nodes': [{
    'host': 'localhost',
    'port': '8108',
    'protocol': 'http'
  }],
  'connection_timeout_seconds': 2
})

