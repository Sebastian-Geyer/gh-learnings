# gh-learnings

this repo show high level learning from mit github ci/cd projects with examples. These are intended to give ideas and technologies how to implement new requirements.

## issue template forms

In github you can define issue templates so users can create standadized issues. Multiple possibilities can be seen in https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository. A special case is creating a form and triggering a workflow with this form. This can be seen in the template 1-sample-issue-form.yaml and the workflow 1-sample-issue-workflow.yaml.

## dispatch workflow
We can use https://github.com/Codex-/return-dispatch to trigger Workflows in other Repositories. A sample is done in this Repository with 2-workflow-triggered-manual.yaml as a sender and 3-workflow-triggered-dispatch.yaml as a receiver. These 2 files could be different Repositories by changing the destination Repository in the disptching workflow.

## run workflows locally

Sometimes it is necessary to run workflows locally for testing and debugging if we don´t want to produce errornous workflow runs in github.
Needed:
- Docker Environment
- act https://github.com/nektos/act

A Workflow run can be triggered via Visual Studion Code launch.json and payload.json in this repo or similar. We can copy payload for payload.json from the debug info, when running a workflow in github. We can use "View raw logs" and copy the JSON Object of the element "event" of the "github payload". This can be processed to a JSON Obejct with some search an replaces
- "\[0m\r" -> "\r" to use simple line breaks
- "^.*1m" -> "" to remove timestamps

## gh cli

One way to interact with an github repository is the github cli https://cli.github.com/. We can use the cli for different use case in wortkflow. The example workflow 4-gh-cli.yaml creates a new branch with git commands and opens a pull request for this branch with the github cli. The second workflow 5-gh-cli-graphql.yaml adds a comment to a pull request with the github cli using the github graphql api https://docs.github.com/en/graphql. For the cli to work properly in workflows some setting regarding permissions must be done. These aree found in repository setting under settings/actions.