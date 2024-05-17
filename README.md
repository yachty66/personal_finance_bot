# personal_finance_bot

Goal is to have a finance bot that retrieves my daily transaction data from N26 and then sends me a daily summary of it. For example, every day at 23:59 synced with local time, I want to receive a WhatsApp message listing all my transactions.

## steps

- [ ] get all transactions from the last 24 hours
- [ ] create a structured format for the transactions (a nice sentence) which also contains the sum of all transactions
- [ ] send this as message with an whatsapp bot (in the case whats app is getting to difficult i change to telegram or something similar) (set a beauty profile pic for the bot)
- [ ] setup a serverless function which is running every day 23:59 based on 
- [ ] launch in SF2 chat and on twitter