from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class DojoSurvey:
    DB = 'dojo_survey_schema'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_survey(survey):
        #We set this to True from the beginning, so that if this remains True to the end, data is valid
        is_valid = True
        if len (survey['name']) < 3:
            flash('Name must be at least 3 characters.')
            is_valid = False
        if len(survey['location']) < 1:
            flash('Must choose a dojo location.')
            is_valid = False
        if len(survey['language']) < 1:
            flash('Must choose a dojo location.')
            is_valid = False
        if len(survey['comment']) < 3:
            flash ('Comments must be at least 3 characters.')
            is_valid = False
        return is_valid
    
    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO dojos (name, location, language, comment)
        VALUES (%(name)s, %(location)s, %(language)s, %(comment)s)
        """

        return connectToMySQL(cls.DB).query_db(query, data)
        # return results
    
    # @classmethod
    # def get_one(cls, data):
    #     query = """
    #     SELECT * FROM dojos
    #     WHERE id = %(id)s;
    #     """

    #     results = connectToMySQL(cls.DB).query_db(query, data)
    #     return results
    
    @classmethod
    def get_last(cls):
        query = """
        SELECT * FROM dojos
        ORDER BY dojos.id
        DESC LIMIT 1;
        """
        results = connectToMySQL(cls.DB).query_db(query)
        return DojoSurvey(results[0])