from waitress import serve
import web_server

port_ = process.env.PORT || 5000
serve(web_server.app, host='0.0.0.0', port=port_)
