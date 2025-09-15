## Generate Blog Title and Content based on a given "Topic"

This functionality is exposed as an API endpoint.

### Sample Request in 

#### Blog content generation in english
```
POST http://127.0.0.1:8004/blogs
{
  "topic": "Agentic AI"
}
```

#### Blog content generation with language translation (french or hindi)
```
POST http://127.0.0.1:8004/blogs
{
  "topic": "Agentic AI",
  "language": "french"
}
```
