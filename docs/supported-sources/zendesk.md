# Zendesk

[Zendesk](https://www.zendesk.com/) is a cloud-based customer service and support platform. It offers a range of features including ticket management, self-service options, knowledgebase management, live chat, customer analytics, and conversations.

ingestr supports Zendesk as a source.

The Zendesk supports two authentication methods:

- OAuth Token
- API Token

All resources supports API Token except "chats resources" i.e Zendesk Chat API. For more information, you can find additional details [here.](https://dlthub.com/docs/dlt-ecosystem/verified-sources/zendesk#grab-credentials)

## URI Format

The URI format for Zendesk is as follows:

```plaintext
zendesk://:<oauth_token>@<sub-domain>
```

```plaintext
zendesk://<email>:<api_token>@<sub-domain>
```

URI parameters:

- `subdomain`: Unique zendesk subdomain that can be found in account url. For example, if your account url is https://My_Company.zendesk.com/, then `My_Company` is your subdomain
- `email`: Email address of the user
- `api_token`: API token used for authentication with zendesk
- `oauth_token`: OAuth token used for authentication with zendesk

## Setting up a Zendesk Integration

Zendesk requires a few steps to set up an integration, please follow the guide dltHub [has built here](https://dlthub.com/docs/dlt-ecosystem/verified-sources/zendesk#setup-guide).

Once you complete the guide, if you decide to use an OAuth Token, you should have a subdomain and an OAuth token. Let’s say your subdomain is `mycompany` and your OAuth token is `qVsbdiasVt`.

```sh
ingestr ingest --source-uri "zendesk://:qVsbdiasVt@mycompany" \
--source-table 'tickets' \
--dest-uri 'duckdb:///zendesk.duckdb' \
--dest-table 'zendesk.tickets' \
--interval-start '2024-01-01'
```

If you decide to use an API Token, you should have a subdomain, email, and API token. Let’s say your subdomain is `mycompany`, your email is `john@get.com`, and your API token is `nbs123`.

```sh
ingestr ingest --source-uri "zendesk://john@get.com:nbs123@mycompany" \
--source-table 'tickets' \
--dest-uri 'duckdb:///zendesk.duckdb' \
--dest-table 'zendesk.tickets' \
--interval-start '2024-01-01'
```

The result of this command will be a table in the `zendesk.duckdb` database.

## Available Tables

Zendesk source allows ingesting the following sources into separate tables:

- [activities](https://developer.zendesk.com/api-reference/ticketing/tickets/activity_stream/): Retrieves ticket activities affecting the agent
- [addresses](https://developer.zendesk.com/api-reference/voice/talk-api/addresses/): Retrieves addresses information
- [agents_activity](https://developer.zendesk.com/api-reference/voice/talk-api/stats/#list-agents-activity): Retrieves activity information for agents
- [automations](https://developer.zendesk.com/api-reference/ticketing/business-rules/automations/): Retrives automations for the current account
- [brands](https://developer.zendesk.com/api-reference/ticketing/account-configuration/brands/): Retrieves all brands for your account
- [calls](https://developer.zendesk.com/api-reference/voice/talk-api/incremental_exports/#incremental-calls-export): Retrieves all calls specific to channels
- [chats](https://developer.zendesk.com/api-reference/live-chat/chat-api/incremental_export/): Retrieves available chats
- [greetings](https://developer.zendesk.com/api-reference/voice/talk-api/greetings/): Retrieves all default or customs greetings
- [groups](https://developer.zendesk.com/api-reference/ticketing/groups/groups/): Retrieves groups of support agents
- [legs_incremental](https://developer.zendesk.com/api-reference/voice/talk-api/incremental_exports/#incremental-call-legs-export): Retrieves detailed information about each agent involved in a call
- [lines](https://developer.zendesk.com/api-reference/voice/talk-api/lines/): Retrieves all available lines (phone numbers and digital lines) in your Zendesk voice account
- [organizations](https://developer.zendesk.com/api-reference/ticketing/organizations/organizations/) : Retrieves organizations (your customers can be grouped into organizations by their email domain)
- [phone_numbers](https://developer.zendesk.com/api-reference/voice/talk-api/phone_numbers/): Retrieves all available phone numbers
- [settings](https://developer.zendesk.com/api-reference/voice/talk-api/voice_settings/): Retrieves account settings related to Zendesk voice accounts
- [sla_policies](https://developer.zendesk.com/api-reference/ticketing/business-rules/sla_policies/): Retrives different sla policies.
- [targets](https://developer.zendesk.com/api-reference/ticketing/targets/targets/): Retrieves targets where as targets are data from Zendesk to external applications like Slack when a ticket is updated or created.
- [tickets](https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/): Retrieves all tickets, which are the means through which customers communicate with agents
- [ticket_forms](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_forms/): Retrieves all ticket forms
- [ticket_metrics](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_metrics/): Retrieves various metrics about one or more tickets.
- [ticket_metric_events](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_metric_events/): Retrieves ticket metric events that occurred on or after the start time
- [users](https://developer.zendesk.com/api-reference/ticketing/users/users/): Retrieves all users

Use these as `--source-table` parameter in the `ingestr ingest` command.