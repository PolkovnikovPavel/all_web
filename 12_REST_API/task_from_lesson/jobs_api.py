import flask
import datetime
from data import db_session
from data.users import User
from data.Jobs import Jobs
from flask import jsonify, request

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
    session = db_session.create_session()
    jobs = session.query(Jobs).get(job_id)
    if not jobs:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'job': jobs.to_dict(only=(list_of_parameters_jobs))
        }
    )


@blueprint.route('/api/jobs', methods=['POST'])
def create_news():
    if not request.json:
        return jsonify({'error': 'Empty request'})

    elif not all(key in request.json for key in
                    ['job', 'team_leader', 'work_size', 'collaborators', 'id',
                     'is_finished']):
        return jsonify({'error': 'Bad request'})

    elif (not str(request.json['id']).isdigit() or
          not str(request.json['team_leader']).isdigit() or
          not str(request.json['work_size']).isdigit() or
          not isinstance(request.json['is_finished'], bool)):
        return jsonify({'error': 'Wrong data'})

    session = db_session.create_session()

    if not session.query(User).filter(User.id == int(request.json['team_leader'])).first():
        return jsonify({'error': 'Wrong data'})
    elif session.query(Jobs).filter(Jobs.id == int(request.json['id'])).first():
        return jsonify({'error': 'Id already exists'})

    creator = request.json['team_leader']
    start_date = datetime.datetime.now()
    end_date = datetime.datetime.now() + datetime.timedelta(
        hours=int(request.json['work_size']))

    jobs = Jobs(
        id=request.json['id'],
        job=request.json['job'],
        creator=creator,
        team_leader=request.json['team_leader'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        is_finished=request.json['is_finished'],
        start_date=start_date,
        end_date=end_date
    )
    session.add(jobs)
    session.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:job_id>', methods=['DELETE'])
def delete_jobs(job_id):
    session = db_session.create_session()
    jobs = session.query(Jobs).filter(Jobs.id == job_id).first()
    if jobs:
        session.delete(jobs)
        session.commit()
    else:
        return jsonify({'error': 'there was no job with such id'})
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:job_id>', methods=['PUT'])
def change_jobs(job_id):
    if not request.json:
        return jsonify({'error': 'Empty request'})

    elif not all(key in request.json for key in
                    ['job', 'team_leader', 'work_size', 'collaborators', 'is_finished']):
        return jsonify({'error': 'Bad request'})

    elif (not str(request.json['team_leader']).isdigit() or
          not str(request.json['work_size']).isdigit() or
          not isinstance(request.json['is_finished'], bool)):
        return jsonify({'error': 'Wrong data'})

    session = db_session.create_session()

    if not session.query(User).filter(
            User.id == int(request.json['team_leader'])).first():
        return jsonify({'error': 'Wrong data, team_leader not found'})

    job = session.query(Jobs).filter(Jobs.id == job_id).first()
    if job:
        job.job = request.json['job']
        job.team_leader = int(request.json['team_leader'])
        job.work_size = int(request.json['work_size'])
        job.collaborators = request.json['collaborators']
        job.is_finished = request.json['is_finished']

        session.commit()
    else:
        return jsonify({'error': 'there was no job with such id'})

    return jsonify({'success': 'OK'})
