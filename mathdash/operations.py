import json

from webapp2_extras import i18n

def add_to_model(model):
            # get the games
    script = []
    operations = dict()
    #q = model.Game.all()
    operations['two_factor_multiplication_upto_9'] = {
            'id': 'two_factor_multiplication_upto_9',
            'title' : i18n.gettext('Multiply'),
            'defaultDisplay': '? x ?',
        } 
    operations['additions_substractions'] = {
        'id' : 'additions_substractions',
        'title' : i18n.gettext('Add & Substract'),
        'defaultDisplay' : '? + ?'
    }
    
    model['operations'] = operations;
    model['operations_json'] = json.dumps(operations)
    #modl['gamecode'] = ''.join(script)
