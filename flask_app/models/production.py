from flask_app.config.mysqlconnection import connectToMySQL
from flask import Flask, flash

class Product():
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.desc = data["desc"]
        self.language = data["language"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def save(cls,data):
        query = "INSERT INTO project(name, desc, language, created_at, updated_at) VALUE %(img_data)s, %(name)s, %(desc)s, %(language)s, NOW(), NOW()"
        new_proj = connectToMySQL('projects').query_db( query, data )
        return new_proj
    
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM project WHERE id = %(id)s"

        remove = connectToMySQL('projects').query_db( query, data )
        return remove
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM projects"
        result = connectToMySQL('projects').query_db( query, data )

        prod = []    
        for result in results:
            one_instance = cls(result)
            prod.append(one_instance)
            
        return results