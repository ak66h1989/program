def setup_routes(app, handler, project_root):
    add_route = app.router.add_route
    add_route('*', '/', index)
    add_route('*', '/handler', handler)
    add_route('*', '/test', test)
    add_route('*', '/test1', test1)
    add_route('*', '/test2', test2)

app.router.add_route('*', '/', index)
app.router.add_route('*', '/test', test)
app.router.add_route('*', '/test1', test1)
app.router.add_route('*', '/test2', handle_request)
app.router.add_route('*', '/handler', handler)

