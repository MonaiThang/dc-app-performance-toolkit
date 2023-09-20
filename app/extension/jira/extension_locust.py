from locustio.common_utils import init_logger, jira_measure, run_as_specific_user, ADMIN_HEADERS  # noqa F401
from util.conf import JIRA_SETTINGS

logger = init_logger(app_type='jira')


@run_as_specific_user(username=JIRA_SETTINGS.admin_login, password=JIRA_SETTINGS.admin_password)  # run as specific user
def app_specific_action(locust):
    plugin_key = 'com.atlassian.app.usage.app-usage-it-backdoor'
    app_usage_app_list_endpoint = '/rest/app-usage/latest/apps'
    app_usage_app_details_endpoint = f'/rest/app-usage/latest/apps/{plugin_key}'

    @jira_measure("locust_app_common_app_list_and_details")
    def app_list_and_details():
        locust.get(app_usage_app_list_endpoint, catch_response=True)
        locust.get(app_usage_app_details_endpoint, catch_response=True)

    @jira_measure("locust_app_common_usage_data_database_table")
    def app_common_usage_database_table():
        locust.get(f'/rest/app-usage/latest/common-usage-data/database-tables?pluginKey={plugin_key}', catch_response=True)

    @jira_measure("locust_app_common_usage_data_jql_functions")
    def app_common_usage_jql_functions():
        locust.get(f'/rest/app-usage/latest/common-usage-data/jql-functions?pluginKey={plugin_key}', catch_response=True)

    @jira_measure("locust_app_common_usage_data_rest_api")
    def app_common_usage_rest_api():
        locust.get(f'/rest/app-usage/latest/common-usage-data/api-usage?pluginKey={plugin_key}', catch_response=True)

    @jira_measure("locust_app_user_interactions_page_views")
    def app_user_interactions_page_views():
        locust.get(f'/rest/app-usage/latest/user-interactions/page-views?pluginKey={plugin_key}', catch_response=True)

    @jira_measure("locust_app_user_interactions_web_panels")
    def app_user_interactions_web_panels():
        locust.get(f'/rest/app-usage/latest/user-interactions/web-panels?pluginKey={plugin_key}', catch_response=True)

    @jira_measure("locust_app_user_interactions_web_panels_click_api")
    def app_user_interactions_web_panels_click_api():
        body = {"pluginKey": "com.atlassian.app.usage.app-usage-it-backdoor", "resourceLocation": "templates/web-panel/sample-web-panel.vm"}  # include parsed variables to POST request body
        ADMIN_HEADERS['Content-Type'] = 'application/json'
        locust.post('/rest/app-usage/latest/user-interactions/web-panels/clicks', json=body, headers=ADMIN_HEADERS, catch_response=True)

    @jira_measure("locust_app_custom_fields")
    def app_custom_fields():
        # custom fields - list of custom fields
        locust.get(f'/rest/app-usage/latest/custom-fields?pluginKey={plugin_key}', catch_response=True)
        # custom fields - total projects and issues count
        locust.get('/rest/app-usage/latest/counts', catch_response=True)

    @jira_measure("locust_app_workflows")
    def app_workflows():
        locust.get(f'/rest/app-usage/latest/workflows?pluginKey={plugin_key}', catch_response=True)

    @jira_measure("locust_app_dashboards")
    def app_dashboards():
        locust.get(f'/rest/app-usage/latest/dashboards?pluginKey={plugin_key}', catch_response=True)

    app_list_and_details()
    app_common_usage_database_table()
    app_common_usage_jql_functions()
    app_common_usage_rest_api()
    app_user_interactions_page_views()
    app_user_interactions_web_panels()
    app_user_interactions_web_panels_click_api()
    app_custom_fields()
    app_workflows()
    app_dashboards()
