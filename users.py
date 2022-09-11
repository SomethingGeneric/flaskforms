import os, yaml
from passlib.hash import pbkdf2_sha256


class usermgr:
    def __init__(self):
        if not os.path.exists("db"):
            os.makedirs("db")
        self.srcdir = "db"

    def write_user(self, uid, obj):
        with open(self.srcdir + os.sep + uid, "w") as f:
            f.write(yaml.dump(obj))

    def get_user(self, uid):
        if self.check_user_exists(uid):
            with open(self.srcdir + os.sep + uid) as f:
                obj = yaml.safe_load(f)
            return obj
        else:
            return {"message": "not found"}

    def check_user_exists(self, uid):
        if uid == "" or uid is None:
            return False
        if os.path.exists(self.srcdir + os.sep + uid):
            return True
        return False

    def auth_user(self, uid, attempt):
        if self.check_user_exists(uid):
            phash = self.get_user(uid)["passw"]
            if pbkdf2_sha256.verify(attempt, phash):
                return True
        return False

    def make_user(self, uid, passw):
        obj = {"passw": pbkdf2_sha256.hash(passw)}
        self.write_user(uid, obj)

    def set_user_password(self, uid, newpass):
        if self.check_user_exists(uid):
            obj = self.get_user(uid)
            hashed_pw = pbkdf2_sha256.hash(newpass)
            obj["passw"] = hashed_pw
            self.write_user(uid, obj)
            return {"message": "done."}
        else:
            return {"message": f"error: no such user {uid}"}
