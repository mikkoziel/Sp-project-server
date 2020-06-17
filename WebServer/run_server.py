from waitress import serve
import web_server
import os

# Bind to PORT if defined, otherwise default to 5000.
port_ = int(os.environ.get('PORT', 5000))
serve(web_server.app, host='0.0.0.0', port=port_)
