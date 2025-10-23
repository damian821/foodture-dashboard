from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Overview
from datetime import date
from sqlalchemy import func

router = APIRouter(prefix="/api", tags=["overview"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/overview")
def get_overview(
    start: date = Query(...),
    end: date = Query(...),
    db: Session = Depends(get_db)
):
    q = (
        db.query(
            func.sum(Overview.revenue).label("revenue"),
            func.sum(Overview.cost).label("cost"),
            func.sum(Overview.gross).label("gross"),
            func.sum(Overview.comm).label("comm"),
            func.sum(Overview.net).label("net"),
            func.avg(Overview.net_pct).label("net_pct"),
            func.sum(Overview.visits).label("visits")
        )
        .filter(Overview.date >= start)
        .filter(Overview.date <= end)
    )
    row = q.one_or_none()
    return {
        "period": {"start": str(start), "end": str(end)},
        "totals": {k: getattr(row, k) for k in row._fields} if row else None
    }
