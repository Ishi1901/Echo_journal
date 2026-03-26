from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from datetime import datetime
from textblob import TextBlob
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

# --- DATABASE SETUP ---
DATABASE_URL = "sqlite:///./echo_journal.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class JournalEntry(Base):
    __tablename__ = "entries"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    sentiment_score = Column(Float)  # -1.0 to 1.0
    vibe_label = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

# --- APP INITIALIZATION ---
app = FastAPI(title="EchoJournal AI")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- INNOVATIVE LOGIC: SENTIMENT ANALYSIS ---
def get_vibe(text: str):
    analysis = TextBlob(text)
    score = analysis.sentiment.polarity
    if score > 0.3:
        return score, "Elevated 🚀"
    elif score < -0.3:
        return score, "Heavy ⛈️"
    elif 0.3 >= score >= 0.1:
        return score, "Chilling 🌊"
    else:
        return score, "Neutral ☁️"

# --- ROUTES ---

@app.post("/entries/")
def create_entry(content: str, db: Session = Depends(get_db)):
    if not content:
        raise HTTPException(status_code=400, detail="Entry cannot be empty")
    
    score, label = get_vibe(content)
    
    new_entry = JournalEntry(
        content=content,
        sentiment_score=score,
        vibe_label=label
    )
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

@app.get("/entries/")
def get_all_entries(db: Session = Depends(get_db)):
    return db.query(JournalEntry).order_by(JournalEntry.timestamp.desc()).all()

@app.get("/stats/")
def get_stats(db: Session = Depends(get_db)):
    entries = db.query(JournalEntry).all()
    if not entries:
        return {"msg": "No data yet"}
    
    avg_vibe = sum(e.sentiment_score for e in entries) / len(entries)
    return {
        "total_entries": len(entries),
        "average_sentiment": round(avg_vibe, 2),
        "overall_outlook": "Positive" if avg_vibe > 0 else "Reflective"
    }
@app.get("/")
async def read_index():
    return FileResponse('static/index.html')

app.mount("/static", StaticFiles(directory="static"), name="static")
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)