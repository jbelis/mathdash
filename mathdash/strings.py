
from webapp2_extras import i18n


def add_to_model(model):
    model['r_login_justification'] = i18n.gettext('... so you can track your progress')
    model['r_signin_with_google'] = i18n.gettext('Sign in with <b>Google</b>')    
    model['r_title'] = i18n.gettext('Math Dash - timed math practice')
    model['r_points'] = i18n.gettext('points')
    model['r_seconds_remaining'] = i18n.gettext('seconds remaining')
    model['r_count_faster'] = i18n.gettext('count faster')
    model['r_how_am_i_doing'] = i18n.gettext('How am I doing?')
