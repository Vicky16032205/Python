So in FastAPI, 
```
@app is called as path operation decorators
```

```
('/') etc, are for specifying paths what will happen or open on ehat particular path.
```

```
get or put or update  etc, are for specifying the operation that will occur behind the scenes.
```

```
the function you wrote down the FastAPI is called path operation function.
```

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## FastAPI reads code line by line
so for this to read line by line, we need to make sure that no dynamic routes are provided.

```
For example there are two routes with same routes but one is dynamic and other is static:
        
        @app.get('/blog/{id}') and other one @app.get('/blog/unpublished')
        these both will work same, if we use dynamic one firstly then the url would never reach unpublished one route.
        
        @app.get('/blog/{id}')
        def show(id: int):
            return {"data" : id}
            
        @app.get('/blog/unpublished')
        def show():
            return {"data" : "all unpublished blogs"}
            
        In both of these functions, the first one is taking the inputs as --int and other one is just parameter named --unpublished
        So if we called unpublished in url then it will always give error as the fastapi searches code line by line,
        it will reach the dynamic parameter code firstand since it is taking parameter as int only so error will come for sure. 
```

To solve this error, write these upside down, and the error will never occur.
```
        @app.get('/blog/unpublished')
        def show():
            return {"data" : "all unpublished blogs"}
        
        @app.get('/blog/{id}')
        def show(id: int):
            return {"data" : id}
            
In this manner the error will never occur.
```