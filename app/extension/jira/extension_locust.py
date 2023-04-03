from locustio.common_utils import init_logger, jira_measure, run_as_specific_user  # noqa F401
from util.conf import JIRA_SETTINGS

logger = init_logger(app_type='jira')


@jira_measure("locust_app_specific_action")
@run_as_specific_user(username=JIRA_SETTINGS.admin_login, password=JIRA_SETTINGS.admin_password)  # run as specific user
def app_specific_action(locust):
    plugin_key = 'com.atlassian.app.usage.app-usage-it-backdoor'
    app_usage_app_list_endpoint = '/rest/app-usage/latest/apps'
    app_usage_app_details_endpoint = f'/rest/app-usage/latest/apps/{plugin_key}'

    @jira_measure("locust_app_common_usage_data_database_table")
    def app_common_usage_database_table():
        locust.get(app_usage_app_list_endpoint, catch_response=True)
        locust.get(app_usage_app_details_endpoint, catch_response=True)
        # common usage data - database tables
        locust.get(f'/rest/app-usage/latest/common-usage-data/database-tables?pluginKey={plugin_key}', catch_response=True)

    @jira_measure("locust_app_user_interactions")
    def app_user_interactions():
        locust.get(app_usage_app_list_endpoint, catch_response=True)
        locust.get(app_usage_app_details_endpoint, catch_response=True)
        # TODO user interactions
        locust.get(f'/rest/app-usage/latest/user-interactions?pluginKey={plugin_key}', catch_response=True)

    @jira_measure("locust_app_custom_fields")
    def app_custom_fields():
        locust.get(app_usage_app_list_endpoint, catch_response=True)
        locust.get(app_usage_app_details_endpoint, catch_response=True)
        # custom fields - list of custom fields
        locust.get(f'/rest/app-usage/latest/custom-fields?pluginKey={plugin_key}', catch_response=True)
        # custom fields - total projects and issues count
        locust.get('/rest/app-usage/latest/counts', catch_response=True)

    @jira_measure("locust_app_workflows")
    def app_workflows():
        locust.get(app_usage_app_list_endpoint, catch_response=True)
        locust.get(app_usage_app_details_endpoint, catch_response=True)
        # workflows
        locust.get(f'/rest/app-usage/latest/workflows?pluginKey={plugin_key}', catch_response=True)

    @jira_measure("locust_app_dashboards")
    def app_dashboards():
        locust.get(app_usage_app_list_endpoint, catch_response=True)
        locust.get(app_usage_app_details_endpoint, catch_response=True)
        # dashboards
        locust.get(f'/rest/app-usage/latest/dashboards?pluginKey={plugin_key}', catch_response=True)

    app_common_usage_database_table()
    # app_user_interactions()
    app_custom_fields()
    app_workflows()
    app_dashboards()
