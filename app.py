from ariadne import graphql_sync, make_executable_schema, load_schema_from_path, ObjectType, QueryType
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify
import resolver as r

app = Flask(__name__)

type_defs = load_schema_from_path('schema.graphql')

query = QueryType()
students = ObjectType('Students')
classes = ObjectType('Classes')
mutation = ObjectType('Mutation')

query.set_field('student_with_id', r.student_with_id)
query.set_field('class_with_id', r.class_with_id)
query.set_field('all_students', r.all_students)
query.set_field('all_classes', r.all_classes)
mutation.set_field('add_student', r.add_student)
mutation.set_field('add_class', r.add_class)
mutation.set_field('add_student_to_class', r.add_student_to_class)


schema = make_executable_schema(type_defs, [students, classes, query, mutation])


@app.route('/graphql', methods=['GET'])
def playground():
    return PLAYGROUND_HTML, 200


@app.route('/graphql', methods=['POST'])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=None,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code
