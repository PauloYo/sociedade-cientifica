import uvicorn

api_root_path = "src.backend.api.app"
port = 8000
config = uvicorn.Config(api_root_path + ":app",host="0.0.0.0", port=port, log_level="info", reload=True)
server = uvicorn.Server(config)
server.run()