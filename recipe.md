As a blogger
So I can write interesting stuff
I want to write posts having a title.

As a blogger
So I can write interesting stuff
I want to write posts having a content.

As a blogger
So I can let people comment on interesting stuff
I want to allow comments on my posts.

As a blogger
So I can let people comment on interesting stuff
I want the comments to have a content.

As a blogger
So I can let people comment on interesting stuff
I want the author to include their name in comments.

# extract nouns

posts, title, content, comment, comment_content, comment_author

| Record                | Properties               |
| --------------------- | ------------------------ |
| posts                 | title, content           |
| comments              | content, author, post_id |


# column types

Table: posts
id: SERIAL
title: text
content: text

Table: comments
id: SERIAL
content: text
author: text
post_id: int