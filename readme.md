# Description

Web tool for searching similar code objects by AST tree

# Step-by-step guide

## Run smother

```
$ py.test --smother=registration registration
$ smother --semantic csv ../reg_smother.csv
```

## Upload code items

```
./manage.py load_code_items
```

## Visit AST for create characteristic of code

```
./manage.py visit_ast_for_items
```

## Calculate frequency of edges in code block

```
./manage.py calc_freq_code
```

## Set depth of code objects

```
./manage.py set_depth
```

## Set body length of code objects

```
./manage.py set_body_length
```

## Validate results

```
./manage.py validate
```

## Run django server and search code and tests

```
./manage.py runserver
```