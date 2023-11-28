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


# social network program

As a social network user,
So I can have my information registered,
I'd like to have a user account with my email address.

As a social network user,
So I can have my information registered,
I'd like to have a user account with my username.

As a social network user,
So I can write on my timeline,
I'd like to create posts associated with my user account.

As a social network user,
So I can write on my timeline,
I'd like each of my posts to have a title and a content.

As a social network user,
So I can know who reads my posts,
I'd like each of my posts to have a number of views.

# extract nouns

users, email, username, posts, user_id, title, content, views

| Record                | Properties                     |
| --------------------- | -----------------------------  |
| users                 | email, username                |
| posts                 | title, content, views, user_id |

# column types

Table: users
id: SERIAL
email: text
username: text

Table: posts
id: SERIAL
title: text
content: text
views: int
user_id: int