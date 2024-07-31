<h1 align="center">
    <image src="imgs/image.png" height=500px>
    <br>
</h1>

###

This Python script aims to explore and identify functions in a GraphQL API where introspection is disabled, but the “did you mean…” suggestion feature is enabled. The “did you mean…” feature is a common characteristic in GraphQL APIs that suggests possible function names when a query with an incorrect name is submitted.

#### Key Features:
1.	Test Query Submission: Sends GraphQL queries with slightly modified or incorrect function names to the API.
2.	Response Analysis: Analyzes API responses to detect suggestions provided by the “did you mean…” feature.
3.	Valid Function Logging: Stores the correct function names discovered based on the API suggestions.
4.	Automation and Efficiency: Utilizes brute force techniques to cover a large number of possible variations in a reasonable time, maximizing the chance of discovering valid functions in the API.

#### Benefits:
•	Hidden Function Discovery: Useful for pentesters and security researchers aiming to uncover undocumented or protected functions in GraphQL APIs.
•	Automation: Reduces manual effort needed to test and validate function names.
•	Versatility: Can be adapted for different GraphQL APIs with minor configuration adjustments.

### Install

- via pipx:

```sh
pipx install git+https://github.com/phor3nsic/graphqlBrute
```
- via pip:

```sh
pip install git+https://github.com/phor3nsic/graphqlBrute
```

### Run

```sh
graphqlBrute -u http://target/graphql
```

### Security Considerations:

•	Ethical Use: This script should only be used for ethical security testing with proper authorization from the API owners.
•	Performance: Adjust the query submission rate to avoid overloading the target server.