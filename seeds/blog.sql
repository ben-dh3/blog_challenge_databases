DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS comments;

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    content text
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    content text,
    author text,
    post_id int,
    constraint fk_posts foreign key(post_id) references posts(id) on delete cascade
);