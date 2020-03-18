from flask_restful import abort, Resource, reqparse
from flask import jsonify
from data import db_session
from data.users import User
from data.Jobs import Jobs
from data.parsers import *
import datetime


list_of_parameters_jobs = ['job', 'work_size', 'team_leader',
                                    'id', 'collaborators', 'start_date',
                                    'end_date', 'is_finished', 'creator']


class JobsResource(Resource):
    def get(self, job_id):
        abort_if_job_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        return jsonify({'job': job.to_dict(only=(list_of_parameters_jobs))})

    def put(self, job_id):
        abort_if_job_not_found(job_id)
        args = parser_change.parse_args()

        abort_if_user_not_found(args['team_leader'])

        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)

        job.job = args['job']
        job.work_size = args['work_size']
        job.team_leader = args['team_leader']
        job.collaborators = args['collaborators']
        job.is_finished = args['is_finished']

        session.commit()
        return jsonify({'success': 'OK'})

    def delete(self, job_id):
        abort_if_job_not_found(job_id)
        session = db_session.create_session()

        job = session.query(Jobs).get(job_id)
        session.delete(job)
        session.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'jobs': [job.to_dict(
            only=(list_of_parameters_jobs)) for job in jobs]})

    def post(self):
        args = parser_add_job.parse_args()
        abort_if_user_not_found(args['team_leader'])

        start_date = datetime.datetime.now()
        end_date = datetime.datetime.now() + datetime.timedelta(
            hours=args['work_size'])

        session = db_session.create_session()
        job = Jobs(
            job=args['job'],
            team_leader=args['team_leader'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            start_date=start_date,
            end_date=end_date,
            is_finished=args['is_finished'],
            creator=args['team_leader']
                   )
        session.add(job)
        session.commit()
        return jsonify({'success': 'OK'})


def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    users = session.query(User).get(user_id)
    if not users:
        abort(404, message=f"User {user_id} not found")


def abort_if_job_not_found(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        abort(404, message=f"Job {job_id} not found")
