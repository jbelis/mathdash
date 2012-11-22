
import json

from webapp2_extras import i18n


def add_to_model(model):
    model['strings'] = dict();
    model['strings']['login_justification'] = i18n.gettext('... so you can track your progress')
    model['strings']['signin_with_google'] = i18n.gettext('Sign in with <b>Google</b>')    
    model['strings']['title'] = i18n.gettext('Math Dash - timed math practice')
    model['strings']['points'] = i18n.gettext('points')
    model['strings']['seconds_remaining'] = i18n.gettext('seconds remaining')
    model['strings']['count_faster'] = i18n.gettext('count faster')
    model['strings']['how_am_i_doing'] = i18n.gettext('How am I doing?')
    model['strings']['challenges'] = i18n.gettext('Challenges')
    model['strings']['not_signed_in'] = i18n.gettext('You\'re not signed-in.  Math Dash will not record your points')
    model['strings']['just_practice'] = i18n.gettext('Just practice')
    model['strings']['sign_out'] = i18n.gettext('Sign Out')
    model['strings']['sign_me_in'] = i18n.gettext('Sign-in now and record my points')
    model['strings']['well_done'] = i18n.gettext('Well done!')
    model['strings']['giving_up_already'] = i18n.gettext('Giving up already?')
    model['strings']['result_stats'] = i18n.gettext('You answered <span id="questions_total"></span> questions in <span id="time_spent"></span> seconds and got <span id="questions_correct"></span> right.')
    model['strings']['main_page'] = i18n.gettext('Main Page')
    
    model['strings_json'] = json.dumps(model['strings'])
