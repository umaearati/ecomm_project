import importlib.metadata
packages = [
    "langchain_core",
    "langchain",
    "python-dotenv",
    "streamlit",
    "beautifulsoup4",
    "fastapi",
    "html5lib",
"jinja2",
"langchain",
"langchain-astradb",
"langchain_core",
"langchain-google-genai",
"langchain-groq",
"lxml",
"python-multipart",
"selenium",
"treamlit",
"undetected-chromedriver",
"uvicorn",
"structlog",
]
for pkg in packages:
    try:
        version = importlib.metadata.version(pkg)
        print(f"{pkg}=={version}")
    except importlib.metadata.PackageNotFoundError:
        print(f"{pkg} (not installed)")