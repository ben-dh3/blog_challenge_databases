DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email text,
    username text
);


CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    content text,
    views int,
    user_id int,
    constraint fk_users foreign key(user_id)
    references users(id)
    on delete cascade
);

INSERT INTO users (email, username) VALUES ('Test Email', 'Test Username');
INSERT INTO posts (title, content, views, user_id) VALUES ('Test Title', 'Test Content', 10, 1);