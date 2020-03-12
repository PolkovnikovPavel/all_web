import flask
from data import db_session
from data.users import User
from data.Jobs import Jobs
from flask import jsonify

blueprint = flask.Blueprint('news_api', __name__, template_folder='templates')
list_of_parameters_jobs = ['job', 'creator', 'team_leader',
                                    'work_size', 'start_date', 'end_date',
                                    'collaborators', 'is_finished']


@blueprint.route('/api/jobs')
def get_jobs():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=(list_of_parameters_jobs))
                 for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:job_id>')
def get_jobs_one(job_id):
    job_id = job_id - 1
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return jsonify(
        {
            'job': jobs[job_id].to_dict(only=(list_of_parameters_jobs))
        }
    )
