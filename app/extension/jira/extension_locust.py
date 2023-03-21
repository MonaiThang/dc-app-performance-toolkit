from locustio.common_utils import init_logger, jira_measure, run_as_specific_user  # noqa F401

logger = init_logger(app_type='jira')


@jira_measure("locust_app_specific_action")
@run_as_specific_user(username='admin', password='admin')  # run as specific user
def app_specific_action(locust):
    plugin_key = 'com.atlassian.app.usage.app-usage-it-backdoor'

    # common usage data - database tables
    locust.get(f'/rest/app-usage/latest/common-usage-data/database-tables?pluginKey={plugin_key}',
                   catch_response=True)

    # TODO user interactions

    # custom fields - list of custom fields
    locust.get(f'/rest/app-usage/latest/custom-fields?pluginKey={plugin_key}',
                   catch_response=True)

    # custom fields - total projects and issues count
    locust.get('/rest/app-usage/latest/counts',
                   catch_response=True)

    # workflows
    locust.get(f'/rest/app-usage/latest/workflows?pluginKey={plugin_key}',
                   catch_response=True)

    # TODO dashboards
    locust.get(f'/rest/app-usage/latest/dashboards?pluginKey={plugin_key}',
               catch_response=True)