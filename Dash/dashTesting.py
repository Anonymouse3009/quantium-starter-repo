from Data_Visual import app

def header(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#header",timeout = 5)

def test_region(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#pick_region", timeout=5)

def graph_test (dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#graph", timeout=5)