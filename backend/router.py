from fastapi import APIRouter, Depends, HTTPException 
from sqlalchemy.orm import Session 
from database import SessionLocal, get_db 
from schema import RegisterTrain
from typing import List
from crud import get_data 