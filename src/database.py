from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://postgres:Battun2902*@localhost:5432/institutional_engine"

def get_engine():
    engine = create_engine(DATABASE_URL)
    return engine

def test_connection():
    engine = get_engine()
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))
        version = result.fetchone()
        print(f"Connected successfully!")
        print(f"PostgreSQL version: {version[0]}")

if __name__ == "__main__":
    test_connection()