from apiflask import HTTPBasicAuth
from werkzeug.security import check_password_hash

from bluehealth.models import User

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username: str, password: str) -> bool:
    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return False
    return True
