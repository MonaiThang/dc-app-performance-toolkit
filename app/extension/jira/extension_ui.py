import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.jira.pages.pages import Login
from util.conf import JIRA_SETTINGS


def app_specific_action(webdriver, datasets):
    page = BasePage(webdriver)
    plugin_key = 'com.atlassian.app.usage.app-usage-it-backdoor'
    sudo_confirm_button = (By.ID, 'login-form-submit')
    sudo_password_field = (By.ID, 'login-form-authenticatePassword')

    # To run action as specific user uncomment code bellow.
    # NOTE: If app_specific_action is running as specific user, make sure that app_specific_action is running
    # just before test_2_selenium_z_log_out action

    @print_timing("selenium_app_specific_user_login")
    def measure():
        def app_specific_user_login(username=JIRA_SETTINGS.admin_login, password=JIRA_SETTINGS.admin_password):
            login_page = Login(webdriver)
            login_page.delete_all_cookies()
            login_page.go_to()
            login_page.set_credentials(username=username, password=password)
            if login_page.is_first_login():
                login_page.first_login_setup()
            if login_page.is_first_login_second_page():
                login_page.first_login_second_page_setup()
            login_page.wait_for_page_loaded()
        app_specific_user_login(username=JIRA_SETTINGS.admin_login, password=JIRA_SETTINGS.admin_password)
    measure()

    def measure():
        def is_sudo():
            return True if '/secure/admin/WebSudoAuthenticate' in page.driver.current_url else False

        def sudo_admin(password=JIRA_SETTINGS.admin_password):
            page.get_element(sudo_password_field).send_keys(password)
            page.get_element(sudo_confirm_button).click()

        @print_timing("selenium_app_custom_action:app_list")
        def app_list_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/plugins/servlet/app-usage")
            if is_sudo():
                sudo_admin(password=JIRA_SETTINGS.admin_password)
            # Wait for content section visible
            page.wait_until_visible((By.ID, "content"))
            # Wait for app usage list element by CSS selector
            page.wait_until_visible((By.CSS_SELECTOR, "h2[data-testid='app-list-page-header']"))

        @print_timing("selenium_app_custom_action:app_details")
        def app_details_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/plugins/servlet/app-usage/plugin/{plugin_key}")
            if is_sudo():
                sudo_admin(password=JIRA_SETTINGS.admin_password)
            # Wait for content section visible
            page.wait_until_visible((By.ID, "content"))
            # Wait for app usage details element by CSS selector
            page.wait_until_visible((By.CSS_SELECTOR, "h2[data-testid='app-usage-app-details-header']"))

        @print_timing("selenium_app_custom_action:tab_common_usage_data")
        def common_usage_data_measure():
            page.go_to_url(
                f"{JIRA_SETTINGS.server_url}/plugins/servlet/app-usage/plugin/{plugin_key}/common-usage-data")
            if is_sudo():
                sudo_admin(password=JIRA_SETTINGS.admin_password)
            # Wait for content section visible
            page.wait_until_visible((By.ID, "content"))
            # Wait for app usage common usage data elements by CSS selector
            page.wait_until_visible(
                (By.CSS_SELECTOR, "button[data-testid='app-usage-expand-dropdown-api-usages-tables']"))
            page.wait_until_visible(
                (By.CSS_SELECTOR, "button[data-testid='app-usage-expand-dropdown-database-tables']"))
            page.wait_until_visible((By.CSS_SELECTOR, "button[data-testid='app-usage-expand-dropdown-jql-functions']"))

        @print_timing("selenium_app_custom_action:tab_user_interactions")
        def user_interactions_measure():
            page.go_to_url(
                f"{JIRA_SETTINGS.server_url}/plugins/servlet/app-usage/plugin/{plugin_key}/user-interactions")
            if is_sudo():
                sudo_admin(password=JIRA_SETTINGS.admin_password)
            # Wait for content section visible
            page.wait_until_visible((By.ID, "content"))
            # Wait for app usage user interactions element by CSS selector
            page.wait_until_visible((By.CSS_SELECTOR, "button[data-testid='app-usage-expand-dropdown-page-view-tables']"))
            # TODO user interactions web panels

        @print_timing("selenium_app_custom_action:tab_custom_fields")
        def custom_fields_measure():
            page.go_to_url(
                f"{JIRA_SETTINGS.server_url}/plugins/servlet/app-usage/plugin/{plugin_key}/custom-fields")
            if is_sudo():
                sudo_admin(password=JIRA_SETTINGS.admin_password)
            # Wait for content section visible
            page.wait_until_visible((By.ID, "content"))
            # Wait for app usage custom fields element by CSS selector
            page.wait_until_visible((By.CSS_SELECTOR, "table[data-testid='customfields-table--table']"))

        @print_timing("selenium_app_custom_action:tab_workflows")
        def workflows_measure():
            page.go_to_url(
                f"{JIRA_SETTINGS.server_url}/plugins/servlet/app-usage/plugin/{plugin_key}/workflows")
            if is_sudo():
                sudo_admin(password=JIRA_SETTINGS.admin_password)
            # Wait for content section visible
            page.wait_until_visible((By.ID, "content"))
            # Wait for app usage workflows element by CSS selector
            page.wait_until_visible((By.CSS_SELECTOR, "table[data-testid='workflows-table--table']"))

        @print_timing("selenium_app_custom_action:tab_dashboards")
        def dashboards_measure():
            page.go_to_url(
                f"{JIRA_SETTINGS.server_url}/plugins/servlet/app-usage/plugin/{plugin_key}/dashboards")
            if is_sudo():
                sudo_admin(password=JIRA_SETTINGS.admin_password)
            # Wait for content section visible
            page.wait_until_visible((By.ID, "content"))
            # Wait for app usage dashboards element by CSS selector
            page.wait_until_visible((By.CSS_SELECTOR, "table[data-testid='dashboards-table--table']"))

        app_list_measure()
        app_details_measure()
        common_usage_data_measure()
        user_interactions_measure()
        custom_fields_measure()
        workflows_measure()
        dashboards_measure()
    measure()

