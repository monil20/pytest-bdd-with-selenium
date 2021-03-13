@web @login
Feature: Serenity Covid portal login
    The page from where you can login to the portal.

    Background:
        Given the Serenity Covid login page is displayed

    Scenario: Normal User Login
        When the user enters email "user@foo.com", password "user123"
        And clicks the login button

        Then it should redirect to the homepage
        And the user should have "user" rights

    Scenario: Admin User Login
        When the user enters email "admin@foo.com", password "admin123"
        And clicks the login button

        Then it should redirect to the homepage
        And the user should have "admin" rights
