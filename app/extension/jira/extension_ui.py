import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.jira.pages.pages import Login
from util.conf import JIRA_SETTINGS


def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)
    plugin_key = 'com.atlassian.app.usage.app-usage-it-backdoor'

    # To run action as specific user uncomment code bellow.
    # NOTE: If app_specific_action is running as specific user, make sure that app_specific_action is running
    # just before test_2_selenium_z_log_out action
    #
    # @print_timing("selenium_app_specific_user_login")
    # def measure():
    #     def app_specific_user_login(username='admin', password='admin'):
    #         login_page = Login(webdriver)
    #         login_page.delete_all_cookies()
    #         login_page.go_to()
    #         login_page.set_credentials(username=username, password=password)
    #         if login_page.is_first_login():
    #             login_page.first_login_setup()
    #         if login_page.is_first_login_second_page():
    #             login_page.first_login_second_page_setup()
    #         login_page.wait_for_page_loaded()
    #     app_specific_user_login(username='admin', password='admin')
    # measure()

    @print_timing("selenium_app_custom_action")
    def measure():
        @print_timing("selenium_app_custom_action:app_list")
        def app_list_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/plugins/servlet/app-usage")
            page.wait_until_visible((By.ID, "content"))  # Wait for content section visible
            page.wait_until_visible((By.ID, "app-usage-root"))  # Wait for app usage UI element by ID selector

        @print_timing("selenium_app_custom_action:app_details")
        def app_details_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/plugins/servlet/app-usage/plugin/{plugin_key}")
            page.wait_until_visible((By.ID, "content"))  # Wait for summary field visible
            page.wait_until_visible((By.ID, "app-usage-root"))  # Wait for app usage UI element by ID selector

        @print_timing("selenium_app_custom_action:tab_common_usage_data")
        def common_usage_data_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/plugins/servlet/app-usage/plugin/{plugin_key}/common-usage-data")
            page.wait_until_visible((By.ID, "content"))  # Wait for summary field visible
            page.wait_until_visible((By.ID, "app-usage-root"))  # Wait for app usage UI element by ID selector

        # TODO user interactions
        @print_timing("selenium_app_custom_action:tab_user_interactions")
        def user_interactions_measure():
            page.go_to_url(
                f"{JIRA_SETTINGS.server_url}/plugins/servlet/app-usage/plugin/{plugin_key}/user-interactions")
            page.wait_until_visible((By.ID, "content"))  # Wait for summary field visible
            page.wait_until_visible((By.ID, "app-usage-root"))  # Wait for app usage UI element by ID selector

        @print_timing("selenium_app_custom_action:tab_custom_fields")
        def custom_fields_measure():
            page.go_to_url(
                f"{JIRA_SETTINGS.server_url}/plugins/servlet/app-usage/plugin/{plugin_key}/custom-fields")
            page.wait_until_visible((By.ID, "content"))  # Wait for summary field visible
            page.wait_until_visible((By.ID, "app-usage-root"))  # Wait for app usage UI element by ID selector

        @print_timing("selenium_app_custom_action:tab_workflows")
        def workflows_measure():
            page.go_to_url(
                f"{JIRA_SETTINGS.server_url}/plugins/servlet/app-usage/plugin/{plugin_key}/workflows")
            page.wait_until_visible((By.ID, "content"))  # Wait for summary field visible
            page.wait_until_visible((By.ID, "app-usage-root"))  # Wait for app usage UI element by ID selector

        @print_timing("selenium_app_custom_action:tab_dashboards")
        def dashboards_measure():
            page.go_to_url(
                f"{JIRA_SETTINGS.server_url}/plugins/servlet/app-usage/plugin/{plugin_key}/dashboards")
            page.wait_until_visible((By.ID, "content"))  # Wait for summary field visible
            page.wait_until_visible((By.ID, "app-usage-root"))  # Wait for app usage UI element by ID selector

        app_list_measure()
        app_details_measure()
        common_usage_data_measure()
        # user_interactions_measure()
        custom_fields_measure()
        workflows_measure()
        dashboards_measure()

    measure()

