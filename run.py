from costpro import create_app

if __name__ == '__main__':
    costpro_app = create_app()
    costpro_app.run(host='10.0.2.15', port=8001, debug=True, use_reloader=True)