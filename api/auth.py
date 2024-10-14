#!/usr/bin/python3
"""authentication class"""
from models.admin import Admin
from models.parent import Parent
from models.teacher import Teacher
from models.student import Student
from api.models.course import Course
from models import storage
import bcrypt, uuid


def hashpassword(password) -> bytes:
    """hashes the password"""
    pass_word = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(salt, pass_word)

def _generate_uuid() -> str:
    """generates uuid"""
    return uuid.uuid4()

class Auth:
    """authentication
    class"""

    user_model = {'admin': Admin, 'student': Student,
              'parent': Parent, 'teacher': Teacher}

    def register_user(self, **kwargs)-> None:
        """registers a user"""
        email = kwargs['email']
        obj = None
        user = None
        password = hashpassword(kwargs['password'])
        kwargs['password'] = password
        if kwargs['role'] == "student":
            user = storage.find_user(Student, email=email)
            if user:
                raise ValueError('email already registered')
            obj =  Student(**kwargs)
        elif kwargs['role'] == "teacher":
            user = storage.find_user(Teacher, email=email)
            if user:
                raise ValueError('email already registered')
            obj = Teacher(**kwargs)
        elif kwargs['role'] == "parent":
            user = storage.find_user(Parent, email=email)
            if user:
                raise ValueError('email already registered')
            obj = Parent(**kwargs)
        else:
            user = storage.find_user(Admin, email=email)
            if user:
                raise ValueError('email already registered')
            obj = Admin(**kwargs)
        obj.new()
        return obj.id
    
    def register_course(self, admin_id, teacher_id):
        """registers a course"""
        course = storage.find_user(Course, admin_id )
        if course:
            raise ValueError('course already registered')
        new_course = Course(admin_id=admin_id, teacher_id=teacher_id)
        new_course.new()
        return new_course.id
    
    def enroll_student_course(self, course_id, student_id):
        """enroll a student in a course"""
        student = storage.find_user(Student, id=student_id)
        course = storage.find_user(Course, id=course_id)
        if not student or not course:
            raise ValueError('course or student not registered')
        student.course.append(course)
        storage.save()
        return student.firstname


    def validate_login(self, email, password):
        """validate user credential"""
        state = False
        for v in self.user_model.values():
             user = storage.find_user(
                 v, email=email)
             if user:
                 state = bcrypt.checkpw(password, user.hashed_password)
                 break
        return state

    def create_session(self, email):
        """create session"""
        user = None
        session_id = _generate_uuid()
        for v in self.user_model.values():
             user = storage.find_user(
                 v, email=email)
             if user:
                user.update_user_info(session_id=session_id)
                return session_id
    

    def get_usr_from_session_id(self, session_id):
        """ get user
        from session"""
        if not session_id:
            return None
        for v in self.user_model.values():
             user = storage.find_user(
                 v, session_id=session_id)
             if user:
                return user
        return None
    
    def destroy_session(self, user_id):
        """destroy user session"""
        for v in self.user_model.values():
             user = storage.find_user(
                 v, user_id=user_id)
             if user:
                 user.session_id = None
                 break
        return
    
    def reset_password_token(self, email):
        """reset user 
        password"""
        for v in self.user_model.values():
             user = storage.find_user(
                 v, email=email)
             if not user:
                 raise ValueError('No user found')
             else:
                 token = _generate_uuid()
                 user.update_user_info(
                     reset_token = token)
                 return token


    def update_password(self, token, password):
        """updates user password"""
        for v in self.user_model.values():
             user = storage.find_user(
                 v, reset_token=token)
             if user:
                 hashed_password = hashpassword(password)
                 user.update_user_info(
                     hashed_password=hashed_password,
                     reset_token=None)
        raise ValueError('No user found')
