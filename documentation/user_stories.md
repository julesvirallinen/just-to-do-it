As a user I can create an account 

```
params: username, password

INSERT INTO account (date_created, date_modified, username, password) 
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, PARAM:username, PARAM:password)
```
As a user I can login


```
params: username, password

SELECT account.id
FROM account 
WHERE account.username = PARAM:username AND account.password = PARAM:password 
LIMIT 1
```


As a user I can add new tasks 

```
params: name, description, deadline, possible_after, current_user_id, category_id

INSERT INTO task (date_created, date_modified, name, description, deadline, possible_after, done, account_id, category_id)
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMT, PARAM:name, PARAM:description, PARAM:deadline, PARAM:possible_after, FALSE, PARAM:current user, PARAM:category id)
```

As a user I can set tasks as done

```
params: task_id

UPDATE task
SET done = TRUE
WHERE id = PARAM:task_id
```

As a user I can edit a task

```
params: name, description, deadline, possible_after, done, current_user_id, category_id, task_id

UPDATE task
SET date_modified=CURRENT_TIMESTAMP, name=PARAM:name, description=PARAM:description, deadline=PARAM:deadline, possible_after=PARAM:possible_after, done=PARAM:done, PARAM:current user, PARAM:category id
WHERE id = PARAM:task_id

```

As a user I can delete a task
```
params: task_id

DELETE FROM task
WHERE task.id = PARAM:task_id
```

As a user I can set prerequisite tasks for tasks. 
`not in app`

As a user I can see all tasks 
```
params: current_user_id

SELECT task.id, task.name, task.description, task.deadline, task.possible_after, task.done, task.account_id, task.category_id
FROM task 
WHERE task.account_id = PARAM:current_user_id 
ORDER BY task.done, task.deadline ASC
```
As a user I can add a category

```
params: name, current_user_id

INSERT INTO category (date_created, date_modified, name, account_id) 
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, PARAM: name, PARAM: current_user_id)
```

As a user I can delete a category
```
params: category_id

DELETE FROM category
WHERE category.id = PARAM:category_id

UPDATE task
SET category_id = NULL
WHERE task.category_id = PARAM:category_id
```


As a user I can filter tasks by category. 
```
params: current_user_id, category_id

SELECT task.id, task.name, task.description, task.deadline, task.possible_after, task.done, task.account_id, task.category_id
FROM task 
WHERE task.account_id = PARAM:current_user_id, task.category_id = PARAM:category_id
ORDER BY task.done, task.deadline ASC
```

As a user I can list categories and amount of undone tasks in them
```
SELECT c.name, COUNT(t.category_id), c.id FROM Category c
LEFT JOIN Account a ON c.account_id = a.id
LEFT JOIN Task t ON c.id = t.category_id
AND (t.done = FALSE)
AND (t.possible_after IS NULL OR t.possible_after < to_date(cast(:today as TEXT),'YYYY-MM-DD'))
GROUP BY c.name, c.id
ORDER BY c.id

And get amount of undone tasks for NULL category, because it's not trivial to add above.

SELECT COUNT(t.id) FROM Task t
LEFT JOIN Account a ON t.account_id = a.id
WHERE (t.category_id IS NULL AND t.done = FALSE)
AND (t.possible_after IS NULL OR t.possible_after < to_date(cast(:today as TEXT),'YYYY-MM-DD'))
```