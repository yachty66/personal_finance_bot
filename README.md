# personal_finance_bot

Goal is to have a finance bot that retrieves my daily transaction data from N26 and then sends me a daily summary of it. For example, every day at 23:59 synced with local time, I want to receive a WhatsApp message listing all my transactions.

## steps

- [x] get all transactions from the last 24 hours
    - [x] find out which timezone the api is using and than based on that schedule the script --> probablay UTC cause metadata and balances show this format too "2024-05-18T01:16:34.203493Z"
    - [x]| write functions so that they return a format which i can paste into the chat
- [x] create a structured format for the transactions (a nice sentence) which also contains the sum of all transactions
- [x] send this as message with an whatsapp bot (in the case whats app is getting to difficult i change to telegram or something similar) (set a beauty profile pic for the bot)
    - if the bot fails than i should send a link to an part in my readme where i am explaining how to get a new requisition_id
- [ ] deal with issue in the case the token expired
- [ ] setup a serverless function which is running every day 23:59 based on 
- [ ] in the same move generate a bot for sf2 for trash reminder
- [ ] launch in SF2 chat and on twitter