Feature: Passanger fare check

    Scenario: Fare check
        
        Given Get "input" dataset from "titanic"
        And Get "memory" dataset from "titanic"
        And Get "output" dataset from "titanic"

        When Filter "Fare" column from "input"
        And Filter "Fare" column from "memory"
        And Filter "Fare" column from "output"

        Then Verify "Fare" + "10" pecentage for "input" == "Fare" for "memory" == "Fare" for "output"