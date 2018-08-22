from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import time

app = Flask(__name__)

CORS(app)

date_4 = 3600*4
date_24 = 3600*24

@app.route('/')
def all():

    with open('query_specs.json') as fil:
        data = json.load(fil)


    return jsonify(data)

#routes for traffic and cisco traffic
@app.route('/traffic/')
def traffic():

    args = []

    for arg in request.args:
        if arg == 'data_models' or arg == 'date_filters':
            args.append(arg)

    if len(args) != 2:
        return "This is a bad request.", 404

    if request.args['data_models'] is not None:
        data_models = request.args['data_models']
    else:
        return "This was an incorrectly formatted request.", 404
    
    if request.args['date_filters'] is not None:
        date_filters = request.args['date_filters']
    else:
        return "This was an incorrectly formatted request.", 404

    if request.args['sourcetypes'] is not None:
        source_type = request.args['sourcetypes']
    else:
        return "No sourcetype specified.", 404

    try:
        query_time = int(time.mktime(time.strptime(date_filters, "%m/%d/%Y %H:%M:%S")))
    except:
        return jsonify({'errors': {'time': date_filters}})

    with open('query_specs.json') as spec:
        data = json.load(spec)

        current = int(time.time())

        values = current-query_time

        errors = {'errors': {}}

        if values > date_4 or values < 0:
            errors['errors']['date_filter'] = date_filters

        data = data['traffic']

        check = False
        verified_dm = ''

        for model in data['datamodels']:
            if data_models in model:
                check = True
                verified_dm = data_models
        
        if check == False:
            errors['errors']['data_models'] = data_models
        
        if len(errors['errors']) > 0:
            return jsonify(errors)

        traffic_data = {}

        traffic_data['data_models'] = verified_dm

        traffic_data['date_filter'] = date_filters

        #This is optional
        if request.args['sourcetypes'] == 'cisco':
            with open('query_specs.json') as sp:
                cisco = json.load(sp)
                cisco = cisco['cisco traffic']
                traffic_data['sourcetypes_filter'] = cisco['sourcetypes_filter']
            sp.close()

        traffic_data['valid'] = True

        spec.close()

    return jsonify(traffic_data)

#route for logins to infected machines
@app.route('/logins')
def logins():

    args = []

    for arg in request.args:
        if arg == 'data_models' or arg == 'date_filters' or arg == 'filters':
            args.append(arg)

    if len(args) != 3:
        return "This is a bad request.", 404

    if request.args['data_models'] is not None:
        data_models = request.args['data_models']
    else:
        return "This was an incorrectly formatted request.", 404
    
    if request.args['date_filters'] is not None:
        date_filters = request.args['date_filters']
    else:
        return "This was an incorrectly formatted request.", 404

    if request.args['filters'] is not None:
        filters = request.args['filters']
    else:
        return "This was an incorrectly formatted request.", 404

    try:
        query_time = int(time.mktime(time.strptime(date_filters, "%m/%d/%Y %H:%M:%S")))
    except:
        return jsonify({'errors': {'time': date_filters}})

    with open('query_specs.json') as spec:
        data = json.load(spec)

        current = int(time.time())

        values = current-query_time
        
        errors = {'errors': {}}

        if values > date_24 or values < 0:
            errors['errors']['date_filter'] = date_filters

        data = data['logins to infected machines']

        check = False
        verified_dm = ''

        for model in data['datamodels']:
            if data_models in model:
                check = True
                verified_dm = data_models
        
        verified_filters = {}
        
        if check == False:
            errors['errors']['data_models'] = data_models
        
        if len(errors['errors']) > 0:
            return jsonify(errors)
        
        #This is optional
        filt_arr = filters.split(" ")
        for filt in filt_arr:
            if filt.lower() == 'other':
                filter_values = data['filters']['other']['values']
                other_values = request.args['other_values'].split(" ")
                for val in filter_values:
                    if val in other_values:
                        verified_filters[val] = True
            if filt.lower() == 'location' or filt.lower() == 'src':
                ver_check = True
                quer = filt.lower()
                filter_values = data['filters'][quer]
                quer_value = request.args[quer]
                if quer == 'location':
                    for val in filter_values:
                        check_val = val[1]
                        if quer_value in check_val:
                            ver_check = False
                else:
                    src_check = filter_values['values']
                    for val in src_check:
                        if quer_value in val:
                            ver_check = False
                if ver_check == True:
                    verified_filters[quer_value] = True
                else:
                    verified_filters[quer_value] = False

        login_data = {}

        login_data['data_models'] = verified_dm

        login_data['date_filter'] = date_filters

        login_data['filters'] = verified_filters

        login_data['valid'] = True
    
    return jsonify(login_data)

#route for intrusion attacks from outside the United States
@app.route('/outside')
def outside():

    args = []

    for arg in request.args:
        if arg == 'data_models' or arg == 'date_filters' or arg == 'filters':
            args.append(arg)

    if len(args) != 3:
        return "This is a bad request.", 404

    if request.args['data_models'] is not None:
        data_models = request.args['data_models']
    else:
        return "This was an incorrectly formatted request.", 404
    
    if request.args['date_filters'] is not None:
        date_filters = request.args['date_filters']
    else:
        return "This was an incorrectly formatted request.", 404

    if request.args['filters'] is not None:
        filters = request.args['filters']
    else:
        return "This was an incorrectly formatted request.", 404

    try:
        query_time = int(time.mktime(time.strptime(date_filters, "%m/%d/%Y %H:%M:%S")))
    except:
        return jsonify({'errors': {'time': date_filters}})

    with open('query_specs.json') as spec:
        data = json.load(spec)

        current = int(time.time())

        values = current-query_time

        errors = {'errors': {}}

        if values > date_24 or values < 0:
            errors['errors']['date_filter']: date_filters

        data = data['intrusion attacks from outside the US']

        check = False
        verified_dm = ''

        for model in data['datamodels']:
            if data_models in model:
                check = True
                verified_dm = data_models
        
        if check == False:
            errors['errors']['data_models'] = data_models
        
        if len(errors['errors']) > 0:
            return jsonify(errors)

        verified_filters = {}

        #This is optional
        filt_arr = filters.split(" ")
        for filt in filt_arr:
            if filt.lower() == 'other':
                filter_values = data['filters']['other']['values']
                other_values = request.args['other_values'].split(" ")
                for val in filter_values:
                    if val in other_values:
                        verified_filters[val] = True
            if filt.lower() == 'location' or filt.lower() == 'src':
                ver_check = True
                quer = filt.lower()
                filter_values = data['filters'][quer]
                quer_value = request.args[quer]
                if quer == 'location':
                    for val in filter_values:
                        check_val = val[1]
                        if quer_value in check_val:
                            ver_check = False
                else:
                    src_check = filter_values['values']
                    for val in src_check:
                        if quer_value in val:
                            ver_check = False
                if ver_check == True:
                    verified_filters[quer_value] = True
                else:
                    verified_filters[quer_value] = False

        intrusion_data = {}

        intrusion_data['data_models'] = verified_dm

        intrusion_data['date_filter'] = date_filters

        intrusion_data['filters'] = verified_filters

        intrusion_data['valid'] = True
    
    return jsonify(intrusion_data)

#route for searches based on avg cpu load last week vs. normal
@app.route('/cpu')
def cpu():

    args = []

    for arg in request.args:
        if arg == 'data_models' or arg == 'date_filters':
            args.append(arg)

    if len(args) != 2:
        return "This is a bad request.", 404

    if request.args['data_models'] is not None:
        data_models = request.args['data_models']
    else:
        return "This was an incorrectly formatted request.", 404
    
    if request.args['date_filters'] is not None:
        date_filters = request.args['date_filters']
    else:
        return "This was an incorrectly formatted request.", 404
    
    try:
        query_time = int(time.mktime(time.strptime(date_filters, "%m/%d/%Y:%H:%M:%S")))
    except:
        return jsonify({'errors': {'time': date_filters}})

    print(query_time)
    
    with open('query_specs.json') as spec:
        data = json.load(spec)

        time_check = False

        data = data['avg cpu load last week vs normal']

        for tm in data['date_filters']:
            print(tm)
            start = int(time.mktime(time.strptime(tm[0], "%m/%d/%Y:%H:%M:%S")))
            finish = int(time.mktime(time.strptime(tm[1], "%m/%d/%Y:%H:%M:%S")))

            if query_time >= start and query_time <= finish:
                time_check = True

        errors = {'errors': {}}

        if time_check == False:
            errors['errors']['date_filter'] = date_filters

        check = False
        verified_dm = ''

        for model in data['datamodels']:
            if data_models in model:
                check = True
                verified_dm = data_models
        
        if check == False:
            errors['errors']['data_models'] = data_models
        
        if len(errors['errors']) > 0:
            return jsonify(errors)
        
        invalid_models = data['field_errors']['datamodels'][0]['invalid']
        print(invalid_models)

        invalid = ''

        for model in invalid_models:
            if model == verified_dm:
                invalid = model

        cpu_data = {}

        cpu_data['data_models'] = verified_dm

        cpu_data['date_filter'] = date_filters

        if invalid != '':
            cpu_data['field_error'] = invalid

        cpu_data['valid'] = True
    
    return jsonify(cpu_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3134)

