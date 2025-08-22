Feature: Order Transaction
    Tests related to Order Transactions

    Scenario Outline: Verify order details are shown on the Details Page
        Given I place the item order with <username> and <Password>
        And the user is on the landing page
        When I login to the Portal with <username> and <Password>
        And navigate to the order page
        Then the order id is successfully displayed
        Examples:
        | username            | Password  |
        | rahulsingh@test.com | Test@123  |