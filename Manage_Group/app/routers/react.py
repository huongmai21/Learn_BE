from fastapi import status, HTTPException, Depends, APIRouter
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/react",
    tags=["Reacts"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def react(react: schemas.ReactCreate, 
               db: Session = Depends(database.get_db), 
               current_user: int = Depends(oauth2.get_current_user)):
    
    react_query = db.query(models.React).filter(models.React.post_id == react.post_id, models.React.user_id == current_user.id)
    react_found = react_query.first()

    if react.dir == 1:
        if react_found:
            react_query.delete(synchronize_session=False)
            db.commit()
            return {"message": "Unliked"}
        else:
            new_react = models.React(post_id = react.post_id, user_id = current_user.id)
            db.add(new_react)
            db.commit()
            return {"message": "Liked"}
    else:
        if react_found:
            react_query.delete(synchronize_session=False)
            db.commit()
            return {"message": "Unliked"}
        
